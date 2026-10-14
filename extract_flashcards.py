# -*- coding: utf-8 -*-
import re
import json

with open('Flashcards Ingeniería de Software -.txt', 'r', encoding='utf-8') as f:
    lines = [l.rstrip('\r\n') for l in f.readlines()]

categories = [
    ('cat-fundamentos', '📘 Fundamentos', 'FUNDAMENTOS'),
    ('cat-requisitos', '📋 Requisitos', 'REQUISITOS'),
    ('cat-metodologias', '🏗️ Metodologías', 'METODOLOGÍAS'),
    ('cat-diseno', '🎨 Diseño y Arq.', 'DISEÑO'),
    ('cat-pruebas', '💻 Pruebas', 'CODIFICACIÓN'),
    ('cat-gestion', '📊 Gestión & Métricas', 'GESTIÓN')
]

cards = []
current_cat = 'cat-fundamentos'
current_cat_name = '📘 Fundamentos'

i = 0
while i < len(lines):
    line = lines[i].strip()
    if not line or line.startswith('Flashcards:'):
        i += 1
        continue
    
    # Check if category header
    matched_cat = False
    for cat_id, cat_name, keyword in categories:
        if keyword in line:
            current_cat = cat_id
            current_cat_name = cat_name
            matched_cat = True
            break
    if matched_cat:
        i += 1
        continue

    # Check question number e.g. "1. ¿Qué es...?" or "17. Requisitos..."
    m = re.match(r'^(\d+)\.\s*(.*)', line)
    if m:
        num = int(m.group(1))
        q = m.group(2).strip()
        i += 1
        a_lines = []
        while i < len(lines):
            next_line = lines[i].strip()
            if not next_line:
                i += 1
                break
            if re.match(r'^\d+\.', next_line):
                break
            if any(keyword in next_line for _, _, keyword in categories):
                break
            a_lines.append(next_line)
            i += 1
        answer = ' '.join(a_lines).strip()
        cards.append({
            'id': num,
            'cat': current_cat,
            'catName': current_cat_name,
            'question': q,
            'answer': answer
        })
    else:
        i += 1

print(f"Total cards parsed: {len(cards)}")
with open('flashcards.json', 'w', encoding='utf-8') as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

print("Saved to flashcards.json successfully!")
