import logging
logging.basicConfig(level=logging.INFO)

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        ...
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
