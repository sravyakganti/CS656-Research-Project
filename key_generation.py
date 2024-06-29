import rsa

# Generate new RSA keys with a larger size (2048 bits)
public_key, private_key = rsa.newkeys(2048)

# Print the keys for use in your client and server scripts
print('Public key (n, e):', (public_key.n, public_key.e))
print('Private key (n, e, d, p, q):', (private_key.n, private_key.e, private_key.d, private_key.p, private_key.q))

#print('public key:', (public_key))