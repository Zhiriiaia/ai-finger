import socket

# Define the host and port
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 8080       # Port to listen on

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Bind to the specified host and port
    server_socket.listen(5)           # Listen for incoming connections
    print(f"Server is listening on port {PORT}...")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connection established with {client_address}")
            client_socket.sendall(b"Hello! You've connected to the server.\n")
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")