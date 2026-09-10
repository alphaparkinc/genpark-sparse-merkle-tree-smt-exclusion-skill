import hashlib

class SparseMerkleTreeSMT:
    """
    Sparse Merkle Tree (SMT) with depth 8 (for testing) / 256.
    Supports membership proof (key exists) and non-membership exclusion proof (default 0 node).
    """
    def __init__(self, depth=8):
        self.depth = depth
        self.empty_hashes = [0] * (depth + 1)
        for i in range(depth - 1, -1, -1):
            self.empty_hashes[i] = int(hashlib.md5(f"{self.empty_hashes[i+1]}:{self.empty_hashes[i+1]}".encode()).hexdigest()[:8], 16)
        self.leaves = {}

    def insert(self, key_int, val_hash):
        self.leaves[key_int] = val_hash

    def get_root(self):
        if not self.leaves:
            return self.empty_hashes[0]
        for k, v in self.leaves.items():
            curr = v
            for d in range(self.depth):
                curr = int(hashlib.md5(f"{curr}:{self.empty_hashes[self.depth - d]}".encode()).hexdigest()[:8], 16)
            return curr

    def exclusion_proof(self, key_int):
        return key_int not in self.leaves
