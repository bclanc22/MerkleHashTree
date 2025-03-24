import os
import unittest
from hash import hash_file
from merkle_tree import merkle_tree
from main import compute_top_hash

class TestMerkleTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create test files before running tests."""
        cls.test_dir = "test_files"
        os.makedirs(cls.test_dir, exist_ok=True)

        cls.files = {
            "L1.txt": "This is the first file",
            "L2.txt": "Merkle Trees are scary!",
            "L3.txt": "How are you?",
            "L4.txt": "Secret message incoming."
        }

        for filename, content in cls.files.items():
            with open(os.path.join(cls.test_dir, filename), "w") as f:
                f.write(content)

    def test_file_hashing(self):
        """Test if hashing works correctly."""
        hash1 = hash_file(os.path.join(self.test_dir, "L1.txt"), "sha1")
        hash2 = hash_file(os.path.join(self.test_dir, "L2.txt"), "sha1")
        self.assertNotEqual(hash1, hash2)  # Different files should have different hashes

    def test_merkle_tree_consistency(self):
        """Ensure Merkle Tree produces a deterministic hash."""
        filepaths = [os.path.join(self.test_dir, f) for f in self.files.keys()]
        top_hash1 = compute_top_hash(filepaths, "sha1")
        top_hash2 = compute_top_hash(filepaths, "sha1")
        self.assertEqual(top_hash1, top_hash2)  # Should be the same since files are unchanged

    def test_merkle_tree_detects_modification(self):
        """Check if the Merkle Tree detects file modifications."""
        filepaths = [os.path.join(self.test_dir, f) for f in self.files.keys()]
        original_top_hash = compute_top_hash(filepaths, "sha1")

        # Modify one file
        with open(os.path.join(self.test_dir, "L2.txt"), "a") as f:
            f.write("This is an edit!")

        modified_top_hash = compute_top_hash(filepaths, "sha1")
        self.assertNotEqual(original_top_hash, modified_top_hash)  # Hash should change

    @classmethod
    def tearDownClass(cls):
        """Cleanup test files after running tests."""
        for filename in cls.files.keys():
            os.remove(os.path.join(cls.test_dir, filename))
        os.rmdir(cls.test_dir)

if __name__ == "__main__":
    unittest.main()
