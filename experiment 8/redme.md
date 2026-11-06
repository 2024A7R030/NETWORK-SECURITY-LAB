Here is the complete content rewritten in clear, professional, and easy-to-understand language while maintaining the original meaning.
Experiment: Setting Up OpenPGP in Thunderbird for Secure Email Communication
Aim: To set up OpenPGP in Thunderbird to send, receive, and verify encrypted and digitally signed emails.
1. Theory
PGP (Pretty Good Privacy) uses a two-key system to secure email communication.
1. Public Key: Shared with others to encrypt messages sent to you.
2. Private Key: Kept secret and used to decrypt incoming messages and digitally sign outgoing messages.
3. Encryption and Digital Signatures: Ensure confidentiality, authenticity, and integrity of messages.
2. Methodology
Step 1: Generate Key Pair
- Go to Account Settings.
- Open End-to-End Encryption.
- Add a new key and select Create a New OpenPGP Key.
- Generate a new OpenPGP key pair.
Step 2: Exchange Keys
- Export your public key in .asc format.
- Share it with your communication partner.
- Import your partner's public key into Thunderbird's OpenPGP Key Manager.
- Mark the imported key as trusted after verifying its fingerprint.
Step 3: Send an Encrypted Email
- Compose a new email.
- Open Security settings.
- Enable Message Encryption and Digital Signature.
- Send the email securely.
Step 4: Receive an Encrypted Email
- Open the incoming email.
- Thunderbird automatically decrypts the message using your private key.
- Verify the sender's digital signature using their public key.
- A signature verification message is displayed.
3. Results
1. Key Format: Generated a 4096-bit RSA OpenPGP key pair with a unique fingerprint.
2. Email Format: The email was sent in multipart/encrypted format using the AES-256 encryption cipher.
3. Digital Signature: A "Good Signature" message and a green verification indicator were displayed after successful verification.
4. Discussion
Thunderbird's built-in OpenPGP support simplifies email encryption without requiring external tools. However, public key fingerprints must be verified directly with the recipient to prevent Man-in-the-Middle (MITM) attacks. Messages also remain unencrypted by default unless encryption is enabled.
5. Requirement
- Header Encryption: Enable Bcc/MIME header protection to hide email subject information.
6. Visualization
Secure Email Communication Process
Sender
Original Email Message

Two security operations

Encryption

Recipient's public key

Digital Signature

Sender's private key



Encrypted and Signed Email

Transmitted over SMTP


Recipient
- Decrypt using recipient's private key.
- Verify signature using sender's public key.
  
  Secure message successfully received and verified.
