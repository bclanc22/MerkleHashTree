import hashlib

def merkle_tree(hashes, algorithm="sha1"):
    """Builds a Merkle Tree from a list of file hashes and returns the Top Hash."""
    hasher_func = hashlib.sha1 if algorithm == "sha1" else hashlib.md5

    while len(hashes) > 1:
        if len(hashes) % 2 == 1:  # If odd, duplicate the last one
            hashes.append(hashes[-1])

        new_level = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i+1]  # Concatenate two hashes
            hasher = hasher_func()
            hasher.update(combined.encode('utf-8'))
            new_level.append(hasher.hexdigest())
        
        hashes = new_level  # Move to the next level

    return hashes[0] if hashes else None  # Final Top Hash
