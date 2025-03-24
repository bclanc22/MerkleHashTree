import hashlib

def hash_file(filepath, algorithm="sha1"):
    """Computes the hash of a file using SHA1 or MD5."""
    hasher = hashlib.sha1() if algorithm == "sha1" else hashlib.md5()
    with open(filepath, "rb") as f:
        while chunk := f.read(4096):  # Read in chunks to handle large files
            hasher.update(chunk)
    return hasher.hexdigest()
