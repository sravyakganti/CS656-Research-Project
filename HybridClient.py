import socket
import rsa
import time

# RSA Public Key Components
n = ...  # Replace with actual 'n' value
e = ...  # Replace with actual 'e' value
public_key = rsa.PublicKey(n, e)

# Set up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Read file to send
with open('path/to/your/file', 'rb') as file:
    file_data = file.read(245)  # Read only 245 bytes for RSA encryption

# Number of encryption cycles
encryption_cycles = 100000

start_time = time.time()
for _ in range(encryption_cycles):
    encrypted_file_data = rsa.encrypt(file_data, public_key)
end_time = time.time()

total_time = end_time - start_time
print(f"Total encryption time for {encryption_cycles} cycles: {total_time} seconds")

# Send the last encrypted file data
client.send(encrypted_file_data)
client.close()
