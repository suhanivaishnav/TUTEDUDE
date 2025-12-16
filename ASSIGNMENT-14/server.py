import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind IP and port
host = socket.gethostname()
port = 12345
server_socket.bind((host, port))

# Listen for connections
server_socket.listen(1)
print("Server is waiting for connection...")

# Accept client connection
conn, addr = server_socket.accept()
print("Connected to:", addr)

while True:
    # Receive message from client
    message = conn.recv(1024).decode()
    if message.lower() == "exit":
        print("Client disconnected.")
        break
    print("Client:", message)

    # Send reply to client
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()
