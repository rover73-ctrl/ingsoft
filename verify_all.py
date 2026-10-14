# -*- coding: utf-8 -*-
import re

with open('hola.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Extract IDs accessed via getElementById in app.js
js_ids = set(re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", js))

# Extract IDs present in hola.html
html_ids = set(re.findall(r'id=["\']([^"\']+)["\']', html))

print(f"Total IDs checked in app.js: {len(js_ids)}")
missing_ids = []
for j_id in sorted(js_ids):
    # Some IDs are dynamically rendered by renderQuestionnaire (like q-status-, q-card-)
    if j_id.startswith('q-card-') or j_id.startswith('q-status-'):
        continue
    if j_id not in html_ids:
        missing_ids.append(j_id)

if missing_ids:
    print(f"WARNING: The following IDs are called in app.js but not found statically in hola.html: {missing_ids}")
else:
    print("ALL app.js element IDs are successfully present in hola.html!")

# Verify 105 questions count
import json
start_idx = js.find('window.SOMMERVILLE_QUESTIONS = ') + len('window.SOMMERVILLE_QUESTIONS = ')
end_idx = js.find(';\n\n// Banco oficial de 100')
questions = json.loads(js[start_idx:end_idx])
print(f"Verified questions in app.js: {len(questions)}")


unit_counts = {}
for q in questions:
    u = q['unit']
    unit_counts[u] = unit_counts.get(u, 0) + 1
print("Questions per unit:", sorted(unit_counts.items()))
