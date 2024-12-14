// sendmessage.js
async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value;
    if (!message) return;

    // Add user message to chat and save history
    addMessage('user', message);
    saveChatHistory('user', message);
    userInput.value = '';

    // Show typing indicator
    showTypingIndicator();

    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_message: message }),
        });
        const data = await response.json();
        removeTypingIndicator();
        if (data.reply) {
            addMessage('bot', data.reply);
            saveChatHistory('bot', data.reply);
        } else {
            addMessage('bot', 'Error: Unable to get a response.');
        }
    } catch (error) {
        removeTypingIndicator();
        addMessage('bot', 'Error: ' + error.message);
    }
}
