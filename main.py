import os
import argparse
from hash import hash_file
from merkle_tree import merkle_tree

def compute_top_hash(filepaths, algorithm="sha1"):
    """Computes the Top Hash of a set of files."""
    file_hashes = [hash_file(fp, algorithm) for fp in filepaths if os.path.isfile(fp)]
    return merkle_tree(file_hashes, algorithm)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute Merkle Tree Top Hash for file integrity checking.")
    parser.add_argument("files", nargs="+", help="List of file paths")
    parser.add_argument("--algorithm", choices=["sha1", "md5"], default="sha1", help="Hash algorithm to use (default: sha1)")
    
    args = parser.parse_args()

    top_hash_before = compute_top_hash(args.files, args.algorithm)
    print(f"Top Hash before modification: {top_hash_before}")

    input("\nModify a file and press Enter to check status.")

    top_hash_after = compute_top_hash(args.files, args.algorithm)
    print(f"Top Hash after modification: {top_hash_after}")

    if top_hash_before != top_hash_after:
        print("\n⚠️ Alert! Files have been modified!")
    else:
        print("\n All files are safe.")
