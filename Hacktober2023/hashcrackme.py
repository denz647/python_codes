import hashlib

def hash_cracker(target_hash, charset='abcdefghijklmnopqrstuvwxyz'):
    for c in charset:
        for d in charset:
            for e in charset:
                for f in charset:
                    candidate = f"{c}{d}{e}{f}"
                    hashed_candidate = hashlib.md5(candidate.encode()).hexdigest()
                    if hashed_candidate == target_hash:
                        return candidate
    return None

if __name__ == "__main__":
    target_hash = input("Enter the target MD5 hash: ")
    charset = input("Enter the character set (default is lowercase letters): ") or 'abcdefghijklmnopqrstuvwxyz'
    
    result = hash_cracker(target_hash, charset)
    if result:
        print(f"Found: {result}")
    else:
        print("Hash not cracked.")
