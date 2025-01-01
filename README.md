# Codex Chatbot

## Overview
Codex Chatbot is an AI-powered chatbot designed to provide intelligent and human-like interactions on your website. Built using FastAPI for the backend and OpenAI's GPT-4 model, this chatbot can handle a wide range of queries, offering insightful, concise, and user-centric responses. The project demonstrates an integration of modern web technologies for creating a seamless user experience.

---

## Features
- **AI-Powered:** Utilizes OpenAI's GPT-4 for human-like conversational abilities.
- **FastAPI Backend:** Lightweight, fast, and scalable backend framework.
- **Frontend Integration:** Built with HTML, CSS, and JavaScript for a responsive UI.
- **Customizable System Prompts:** Fine-tune the chatbot's behavior to suit your needs.
- **Message History:** Retains chat history for a more human and coherent conversation.
- **Cross-Origin Support:** CORS enabled for seamless frontend-backend communication.

---

## Requirements
To run this project, ensure you have the following installed:
- Python 3.8+
- Node.js (for frontend testing, optional)
- pip (Python package installer)

---

## Installation

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/CodexClub567/Edit_My_Coda.git
   cd Edit_My_Coda
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-dotenv openai
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Run the backend:
   ```bash
   uvicorn backend:app --reload
   ```
   The backend will be available at `http://127.0.0.1:8000`.

### Frontend Setup
1. Open the `index.html` file in any browser to test the chatbot UI.

2. Update the fetch URL in the `sendMessage` function if you deploy the backend on a different server.
   ```javascript
   const response = await fetch('http://your-backend-url/chat', {
   ```

---

## File Structure
```
.
├── .github/                # GitHub configuration files (optional)
├── .vscode/                # VSCode settings (optional)
├── node_modules/           # Node.js dependencies (optional)
├── .env                    # Environment variables
├── backend.py              # Backend code (FastAPI + GPT-4 integration)
├── index.html              # Frontend user interface
├── package.json            # Node.js package configuration (optional)
├── package-lock.json       # Dependency lock file (optional)
├── README.md               # Documentation (this file)
```

---

## Usage
1. Launch the backend server by running `uvicorn`.
2. Open the `index.html` file in a browser.
3. Type a message in the input box and click "Send" to interact with the chatbot.

---

## Customization
### Modify Chatbot Behavior
You can edit the `system` prompt in `backend.py` to adjust the chatbot's behavior:
```python
{"role": "system", "content": "You are an extremely helpful and articulate chatbot specialized in providing insightful, concise, and audience-tailored responses to any queries. Focus on clarity, creativity, and user satisfaction."}
```

### Enhance UI
Edit the styles in the `<style>` section of `index.html` to match your design preferences.

---

## Deployment
### Backend Deployment
You can deploy the backend using platforms like:
- **Heroku**
- **AWS Elastic Beanstalk**
- **Render**

Example for deploying on Heroku:
1. Create a `Procfile`:
   ```
   web: uvicorn backend:app --host=0.0.0.0 --port=${PORT}
   ```

2. Push the code to Heroku:
   ```bash
   git init
   heroku create
   git add .
   git commit -m "Deploy chatbot"
   git push heroku master
   ```

### Frontend Deployment
You can deploy the frontend using:
- **GitHub Pages**
- **Vercel**
- **Netlify**

---

## Debugging Tips
- Check the browser console (`F12`) for any JavaScript errors.
- Use `Postman` or `curl` to test the backend API independently.
- Ensure the `.env` file is correctly configured with your OpenAI API key.
- Check CORS settings if you face cross-origin issues.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- OpenAI for their GPT-4 API.
- FastAPI for the robust backend framework.
- The developers and community members who contributed to this project.
