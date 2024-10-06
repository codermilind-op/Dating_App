const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/messaging/chat/' + roomName + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    document.querySelector('#chat-log').value += (data.sender_id === senderId ? 'Me: ' : 'Other: ') + data.message + '\n';
};

function sendMessage() {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'sender_id': senderId,
        'receiver_id': receiverId // Ensure this variable is defined
    }));
    messageInputDom.value = '';
}

document.querySelector('#chat-message-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
        event.preventDefault();
    }
});

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

header nav ul {
    list-style: none;
    padding: 0;
}

header nav ul li {
    display: inline;
    margin-right: 20px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

main {
    padding: 20px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: absolute;
    bottom: 0;
    width: 100%;
}

