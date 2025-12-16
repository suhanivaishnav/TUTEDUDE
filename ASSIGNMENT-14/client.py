import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
host = socket.gethostname()
port = 12345
client_socket.connect((host, port))
print("Connected to server.")

while True:
    # Send message to server
    message = input("You: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

    # Receive reply from server
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()
