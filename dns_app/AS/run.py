from socket import socket, AF_INET, SOCK_DGRAM

def main():
    server_port = 53533
    mappings = {}

    # Create and bind the socket
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('', server_port))
    print('Server is ready to receive messages...')

    while True:
        # Receive a message
        message, client_address = server_socket.recvfrom(2048)
        decoded_message = message.decode()
        print(f"Received message: {decoded_message}")

        if 'VALUE' in decoded_message:  # Registration request
            print("Processing registration request")
            lines = decoded_message.split('\n')
            name = lines[1].split('=')[1]
            value = lines[2].split('=')[1]
            mappings[name] = value
            print(f"Name: {name}, Value: {value}")
            server_socket.sendto("success".encode(), client_address)
        else:  # Query request
            print("Processing query request")
            lines = decoded_message.split('\n')
            name = lines[1].split('=')[1]
            print(f"Name: {name}")
            if name in mappings:
                response = f"TYPE=A\nNAME={name}\nVALUE={mappings[name]}\nTTL=10"
                server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    main()
