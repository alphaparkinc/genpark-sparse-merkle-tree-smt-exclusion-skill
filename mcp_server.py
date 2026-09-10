import sys
import json
from client import SparseMerkleTreeSMT

smt = SparseMerkleTreeSMT(16)

def handle_call(name, arguments):
    if name == "insert":
        smt.insert(arguments["key"], arguments["value"])
        return {"root": hex(smt.get_root())}
    elif name == "prove_exclusion":
        return {"is_excluded": smt.exclusion_proof(arguments["key"])}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
