from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from utils.language import translate_message, detect_language  # Language utilities
import logging
import openai
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    logging.error("OPENAI_API_KEY is not set. Please add it to your environment variables.")
openai.api_key = OPENAI_API_KEY

# Initialize templates for HTML rendering
templates = Jinja2Templates(directory="templates")

# Initialize conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant ready to answer questions."}
]

# HTTP endpoint to serve the main chat page
@app.get("/", response_class=HTMLResponse)
async def get_chat_page(request: Request):
    """
    Renders the main chat interface using templates.
    """
    return templates.TemplateResponse("chat.html", {"request": request, "title": "Codex Chatbot", "heading": "Welcome!"})


# HTTP endpoint to serve the dark mode page
@app.get("/darkmode", response_class=HTMLResponse)
async def get_darkmode_page(request: Request):
    """
    Renders the dark mode page using templates.
    """
    return templates.TemplateResponse("darkmode.html", {"request": request})


# Define a Pydantic model for the chat POST endpoint
class ChatRequest(BaseModel):
    user_message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Handles chatbot communication via HTTP POST.
    """
    try:
        # Detect language and translate if necessary
        user_language = detect_language(request.user_message)
        translated_message = translate_message(request.user_message, target_language="en")

        # Append translated user message to conversation history
        conversation_history.append({"role": "user", "content": translated_message})

        # Get response from OpenAI GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation_history
        )

        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content']

        # Translate the reply back to the user's language
        translated_reply = translate_message(reply, target_language=user_language)

        # Add translated reply to conversation history
        conversation_history.append({"role": "assistant", "content": reply})

        return {"reply": translated_reply}

    except Exception as e:
        logging.error(f"Error during chat: {e}")
        return JSONResponse(content={"error": "An error occurred while processing your request."}, status_code=500)


@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    """
    Handles chatbot communication via WebSocket for real-time responses.
    """
    await websocket.accept()
    logging.info("WebSocket connection accepted")

    while True:
        try:
            # Receive user message
            data = await websocket.receive_text()

            # Detect language and translate if necessary
            user_language = detect_language(data)
            translated_message = translate_message(data, target_language="en")

            # Append translated user message to conversation history
            conversation_history.append({"role": "user", "content": translated_message})

            # Get response from OpenAI GPT-4
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversation_history
            )

            # Extract the assistant's reply
            reply = response['choices'][0]['message']['content']

            # Translate the reply back to the user's language
            translated_reply = translate_message(reply, target_language=user_language)

            # Add translated reply to conversation history
            conversation_history.append({"role": "assistant", "content": reply})

            # Send translated reply back to WebSocket client
            await websocket.send_text(translated_reply)

        except Exception as e:
            logging.error(f"WebSocket Error: {e}")
            await websocket.send_text("Error: Unable to process your message.")
            break


# Entry point for the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
