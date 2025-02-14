import hashlib
import time

def proof_of_work(prev_hash, difficulty=4):
    nonce = 0
    prefix = '0' * difficulty  # Require hash to start with N zeros
    while True:
        data = f"{prev_hash}{nonce}".encode()
        hash_result = hashlib.sha256(data).hexdigest()
        if hash_result.startswith(prefix):
            return nonce, hash_result
        nonce += 1

prev_hash = "0000a7f5b"
start_time = time.time()
nonce, final_hash = proof_of_work(prev_hash, difficulty=4)
end_time = time.time()

print(f"Nonce: {nonce}")
print(f"Hash: {final_hash}")
print(f"Time Taken: {end_time - start_time:.2f} seconds")
