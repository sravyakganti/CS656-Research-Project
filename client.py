import socket
import rsa
import time
import os

# RSA Public Key Components
n=16392362778256780220954276216546242254283082059831755731579401885794615283058219194385117331167932338939934809926325344824272192435155520791240827118866751725451188130227783725386919016357212747309448444286821026436919609641860419335129545738225312480018195593328936241320448758153962633252574639254433999108833960961102349202779669773155325870156635925761560139637302661811797932859047350600091239313544006776913160750088183132068656619332430225794363409684374938395692704525996724092129007165328531309237676346707052272668702382542488378374969810765214796973666394162198599703279169493550965785926632442580800799579
e = 65537  
public_key = rsa.PublicKey(n, e)

# Set up the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Read file to send
file_path = r'C:\Users\cardo\OneDrive\Desktop\Code\This is a test message for RSA encr.txt'
with open(file_path, 'rb') as file:
    file_data = file.read(245)  # Read only 245 bytes for RSA encryption

# Single encryption time measurement
print(f"Encrypting data from: {file_path}")
start_time = time.perf_counter_ns()
encrypted_file_data = rsa.encrypt(file_data, public_key)
end_time = time.perf_counter_ns()
single_encryption_time = (end_time - start_time) / 1e6  # Convert to milliseconds
print(f"Time for a single encryption: {single_encryption_time:.2f} milliseconds")

# Number of encryption cycles
encryption_cycles = 100000

# Multiple encryption cycles time measurement
print(f"Encrypting the data for 1 cycle...")
start_time = time.perf_counter_ns()
for _ in range(encryption_cycles):
    encrypted_file_data = rsa.encrypt(file_data, public_key)
end_time = time.perf_counter_ns()

total_time = (end_time - start_time) / 1e6  # Convert to milliseconds
print(f"Total encryption time for 1 cycle: {total_time:.2f} milliseconds")


book_size = 4 * 1024 * 1024 * 1024  #  in bytes
chunks = book_size // 245 + (1 if book_size % 245 else 0)
estimated_book_encryption_time = chunks * single_encryption_time
print(f"Estimated time to encrypt a book: {estimated_book_encryption_time:.2f} milliseconds")

# Send the last encrypted file data
client.send(encrypted_file_data)
print("Encrypted data sent to the server.")
client.close()