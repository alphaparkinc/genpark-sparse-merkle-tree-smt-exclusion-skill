from client import SparseMerkleTreeSMT

def main():
    print("=== Testing Sparse Merkle Tree (SMT) Exclusion Proofs ===")
    smt = SparseMerkleTreeSMT(depth=8)
    smt.insert(10, 99999)

    root = smt.get_root()
    print("SMT Root Hash:", hex(root))

    assert smt.exclusion_proof(10) is False # exists
    assert smt.exclusion_proof(11) is True  # does not exist (exclusion verified)
    print("Key 11 verified absent (exclusion proof valid).")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
