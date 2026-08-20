from __future__ import annotations
import argparse
import json
from .core import compare_inventories, load_inventory

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog='directory-drift-checker', description='Compare sanitized inventory snapshots offline.')
    parser.add_argument('baseline')
    parser.add_argument('current')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    result = compare_inventories(load_inventory(args.baseline), load_inventory(args.current))
    print(json.dumps(result, indent=2))
    return 1 if result['added'] or result['removed'] or result['changed'] else 0

if __name__ == '__main__':
    raise SystemExit(main())
