// chathistory.js
function loadChatHistory() {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.forEach(({ role, text }) => {
        addMessage(role, text);
    });
}

function saveChatHistory(role, text) {
    const chatHistory = JSON.parse(localStorage.getItem('chatHistory')) || [];
    chatHistory.push({ role, text });
    localStorage.setItem('chatHistory', JSON.stringify(chatHistory));
}
