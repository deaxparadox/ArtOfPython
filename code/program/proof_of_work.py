import hashlib
import time


def proof_of_work(data, difficulty):
    nonce = 0
    prefix = '0' * difficulty
    
    start_time = time.time()
    
    while True:
        text = f"{data}{nonce}".encode()
        hash_result = hashlib.sha256(text).hexdigest()
        print(hash_result)
        if hash_result.startswith(prefix):
            end_time = time.time()
            print(f"Valid nonce found: {nonce}")
            print(f"Hash: {hash_result}")
            print(f"Time taken: {end_time-start_time:.2f} seconds")
            return nonce, hash_result
        nonce+=1

def main():
    difficulty = 6
    proof_of_work("Hello world", difficulty=difficulty)
    
if __name__ == "__main__":
    main()