import socket
import rsa
import time

# RSA Private Key Components
n = ...  # Replace with actual 'n' value
e = ...  # Replace with actual 'e' value
d = ...  # Replace with actual 'd' value
private_key = rsa.PrivateKey(n, e, d, ...)

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server is listening for connections...")

conn, addr = server.accept()
print(f"Connected to {addr}")

# Receive encrypted file data
encrypted_file_data = conn.recv(1024)
start_time = time.time()
decrypted_file_data = rsa.decrypt(encrypted_file_data, private_key)
end_time = time.time()

print(f"Decryption time: {end_time - start_time} seconds")

conn.close()
server.close()
