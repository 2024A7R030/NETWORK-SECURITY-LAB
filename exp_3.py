import hashlib
import secrets


shared_secret = "mysecret"


server_challenge = secrets.token_hex(8)
print("Challenge sent by server:", server_challenge)


client_response = hashlib.sha256(
    f"{server_challenge}:{shared_secret}".encode()
).hexdigest()

print("Response received from client:", client_response)


verification_hash = hashlib.sha256(
    f"{server_challenge}:{shared_secret}".encode()
).hexdigest()


if secrets.compare_digest(client_response, verification_hash):
    print("Authentication Successful")
else:
    print("Authentication Failed")


print("\n--- Replay Attack Simulation ---")

used_challenges = {server_challenge}


reused_challenge = server_challenge

if reused_challenge in used_challenges:
    print("Replay Attack Detected")
else:
    print("Challenge is valid")
