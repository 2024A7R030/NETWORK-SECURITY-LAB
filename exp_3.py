import hashlib
import secrets

# Secret shared between the client and server
shared_secret = "mysecret"

# Server creates a random challenge
server_challenge = secrets.token_hex(8)
print("Challenge sent by server:", server_challenge)

# Client creates a hashed response
client_response = hashlib.sha256(
    f"{server_challenge}:{shared_secret}".encode()
).hexdigest()

print("Response received from client:", client_response)

# Server calculates the response it expects
verification_hash = hashlib.sha256(
    f"{server_challenge}:{shared_secret}".encode()
).hexdigest()

# Compare the client response with the expected response
if secrets.compare_digest(client_response, verification_hash):
    print("Authentication Successful")
else:
    print("Authentication Failed")


# Replay attack demonstration
print("\n--- Replay Attack Simulation ---")

# Store the challenge after it has been used
used_challenges = {server_challenge}

# An attacker tries to reuse the same challenge
reused_challenge = server_challenge

if reused_challenge in used_challenges:
    print("Replay Attack Detected")
else:
    print("Challenge is valid")
