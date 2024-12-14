// bottyping.js
function showTypingIndicator() {
    const messagesDiv = document.getElementById('messages');
    const typingIndicator = document.createElement('div');
    typingIndicator.classList.add('message', 'bot');
    typingIndicator.innerText = 'Bot is typing...';
    typingIndicator.setAttribute('id', 'typingIndicator');
    messagesDiv.appendChild(typingIndicator);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}
