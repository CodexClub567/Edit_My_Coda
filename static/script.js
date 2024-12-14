const messagesDiv = document.getElementById('messages');

function addMessage(role, text) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', role);
    messageDiv.innerText = text;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value;
    if (!message) return;

    // Add user message to chat
    addMessage('user', message);
    userInput.value = '';

    // Show typing indicator
    addMessage('bot', 'Bot is typing...');
    const typingIndicator = document.querySelector('.message.bot:last-child');

    try {
        const response = await fetch('http://127.0.0.1:8000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_message: message })
        });
        const data = await response.json();
        if (typingIndicator) typingIndicator.remove();
        if (data.reply) {
            addMessage('bot', data.reply);
        } else {
            addMessage('bot', 'Error: Unable to get a response.');
        }
    } catch (error) {
        if (typingIndicator) typingIndicator.remove();
        addMessage('bot', 'Error: ' + error.message);
    }
}

// Initialize chat on page load
window.onload = function() {
    const userInput = document.getElementById('userInput');
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
};
