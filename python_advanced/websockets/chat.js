const statusElement = document.getElementById("status");
const messagesElement = document.getElementById("messages");
const formElement = document.getElementById("message-form");
const inputElement = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");

const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const socket = new WebSocket(`${protocol}//${window.location.host}/ws`);

function addMessage(text, type) {
    const messageElement = document.createElement("div");
    messageElement.className = `message ${type}`;
    messageElement.textContent = text;
    messagesElement.appendChild(messageElement);
    messagesElement.scrollTop = messagesElement.scrollHeight;
}

function setStatus(text, state) {
    statusElement.textContent = text;
    statusElement.className = `status ${state}`;
}

function setFormEnabled(enabled) {
    inputElement.disabled = !enabled;
    sendButton.disabled = !enabled;
}

setFormEnabled(false);

socket.addEventListener("open", () => {
    setStatus("Connected", "connected");
    setFormEnabled(true);
    inputElement.focus();
});

socket.addEventListener("message", (event) => {
    addMessage(event.data, "received");
});

socket.addEventListener("close", () => {
    setStatus("Disconnected", "disconnected");
    setFormEnabled(false);
    addMessage("Connection closed", "system");
});

socket.addEventListener("error", () => {
    setStatus("Connection error", "disconnected");
});

formElement.addEventListener("submit", (event) => {
    event.preventDefault();

    const message = inputElement.value;
    if (message.length === 0 || socket.readyState !== WebSocket.OPEN) {
        return;
    }

    socket.send(message);
    addMessage(message, "sent");
    inputElement.value = "";
    inputElement.focus();
});
