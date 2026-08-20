from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_inventory(path: str) -> dict[str, dict[str, Any]]:
    raw = json.loads(Path(path).read_text(encoding='utf-8'))
    items = raw.get('items', raw) if isinstance(raw, dict) else raw
    if not isinstance(items, list):
        raise ValueError('inventory must be a list or an object with an items list')
    result: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict) or not item.get('name'):
            continue
        result[str(item['name'])] = {k: v for k, v in item.items() if k != 'name'}
    return result


def compare_inventories(baseline: dict[str, dict[str, Any]], current: dict[str, dict[str, Any]]) -> dict[str, Any]:
    before = set(baseline)
    after = set(current)
    changed = []
    for name in sorted(before & after):
        if baseline[name] != current[name]:
            changed.append({'name': name, 'before': baseline[name], 'after': current[name]})
    return {
        'added': sorted(after - before),
        'removed': sorted(before - after),
        'changed': changed,
    }
