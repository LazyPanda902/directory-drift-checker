import json
from directory_drift_checker.core import compare_inventories, load_inventory

def test_added_item():
    result = compare_inventories({'pc1': {'os': '11'}}, {'pc1': {'os': '11'}, 'pc2': {'os': '11'}})
    assert result['added'] == ['pc2']

def test_removed_item():
    result = compare_inventories({'pc1': {}}, {})
    assert result['removed'] == ['pc1']

def test_changed_item():
    result = compare_inventories({'pc1': {'owner': 'A'}}, {'pc1': {'owner': 'B'}})
    assert result['changed'][0]['name'] == 'pc1'

def test_load_inventory(tmp_path):
    p = tmp_path / 'x.json'
    p.write_text(json.dumps({'items': [{'name': 'pc1', 'os': '11'}]}))
    assert load_inventory(str(p)) == {'pc1': {'os': '11'}}
