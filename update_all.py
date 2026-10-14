# -*- coding: utf-8 -*-
import json
import re

# 1. READ FLASHCARDS
with open('flashcards.json', 'r', encoding='utf-8') as f:
    flashcards = json.load(f)

print(f"Loaded {len(flashcards)} flashcards from flashcards.json")

# 2. UPDATE GENERATE_APP.PY
with open('generate_app.py', 'r', encoding='utf-8') as f:
    gen_app_code = f.read()

# Replace or insert window.SOMMERVILLE_FLASHCARDS
flashcards_json_str = json.dumps(flashcards, indent=2, ensure_ascii=False)

if 'window.SOMMERVILLE_FLASHCARDS' not in gen_app_code:
    # Insert right after window.SOMMERVILLE_QUESTIONS
    pos = gen_app_code.find('window.SOMMERVILLE_QUESTIONS = """ + json.dumps(questions, indent=2, ensure_ascii=False) + """;')
    if pos != -1:
        end_pos = pos + len('window.SOMMERVILLE_QUESTIONS = """ + json.dumps(questions, indent=2, ensure_ascii=False) + """;')
        insert_code = '\n\n// Banco oficial de 100 Flashcards clave\nwindow.SOMMERVILLE_FLASHCARDS = """ + json.dumps(flashcards, indent=2, ensure_ascii=False) + """;\n'
        gen_app_code = gen_app_code[:end_pos] + insert_code + gen_app_code[end_pos:]
        print("Inserted window.SOMMERVILLE_FLASHCARDS into generate_app.py")

# Ensure renderFlashcards() is called on DOMContentLoaded
if 'renderFlashcards();' not in gen_app_code:
    gen_app_code = gen_app_code.replace(
        'updateGlobalQuizScore();',
        'updateGlobalQuizScore();\n    renderFlashcards();'
    )
    print("Added renderFlashcards() to DOMContentLoaded in generate_app.py")

# Replace Flashcards logic in section 7
old_flashcards_logic_pattern = r'/\* =+ *\n *7\. FLASHCARDS 3D *\n *=+ \*/.*?(?=/\* =+ *\n *8\. GLOSARIO)'
new_flashcards_logic = """/* ==========================================================================
   7. FLASHCARDS 3D (100 PUNTOS CLAVE DE INGENIERÍA DE SOFTWARE)
   ========================================================================== */

let activeFlashcardFilter = 'all';
let flashcardSearchQuery = '';
const knownCardsSet = new Set();

function renderFlashcards() {
    const container = document.getElementById('fcContainer');
    if (!container || !window.SOMMERVILLE_FLASHCARDS) return;

    const filtered = window.SOMMERVILLE_FLASHCARDS.filter(card => {
        const matchesCat = (activeFlashcardFilter === 'all' || card.cat === activeFlashcardFilter);
        const qLower = flashcardSearchQuery.toLowerCase();
        const matchesSearch = !qLower || card.question.toLowerCase().includes(qLower) || card.answer.toLowerCase().includes(qLower);
        return matchesCat && matchesSearch;
    });

    if (filtered.length === 0) {
        container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 3.5rem 1.5rem; background: var(--bg-card); border: 1px dashed var(--border); border-radius: var(--radius-lg); color: var(--text-dim);">
                <span style="font-size: 2.2rem; display: block; margin-bottom: 0.65rem;">🔍</span>
                <h4 style="color:var(--text-main); font-family:'Outfit',sans-serif; margin-bottom:0.35rem; font-size:1.15rem;">No se encontraron tarjetas</h4>
                <p style="font-size:0.88rem;">No hay tarjetas que coincidan con "${flashcardSearchQuery}". Intenta con otro término.</p>
            </div>
        `;
        return;
    }

    let html = '';
    filtered.forEach(card => {
        const isMastered = knownCardsSet.has(card.id);
        html += `
        <div class="flashcard ${isMastered ? 'mastered' : ''}" data-cat="${card.cat}" data-card-id="${card.id}" onclick="flipCard(this)">
            <div class="flashcard-inner">
                <div class="flashcard-front">
                    <div class="fc-top">
                        <span class="fc-tag">${card.catName}</span>
                        <span>#${card.id} de 100</span>
                    </div>
                    <div class="fc-question">${card.question}</div>
                    <div class="fc-hint">💡 Clic para voltear</div>
                </div>
                <div class="flashcard-back">
                    <div class="fc-top">
                        <span class="fc-tag">${card.catName}</span>
                        <span>Respuesta Oficial</span>
                    </div>
                    <div class="fc-answer">${card.answer}</div>
                    <div class="fc-actions" onclick="event.stopPropagation()">
                        <button class="fc-action-btn known ${isMastered ? 'active' : ''}" onclick="markCard(${card.id}, true, event)">✔️ Dominado</button>
                        <button class="fc-action-btn review" onclick="markCard(${card.id}, false, event)">🔄 Repasar</button>
                    </div>
                </div>
            </div>
        </div>
        `;
    });

    container.innerHTML = html;
}

function flipCard(el) {
    el.classList.toggle('flipped');
    playTone(330, 'sine', 0.05);
}

function markCard(cardId, isKnown, ev) {
    if (ev) ev.stopPropagation();

    if (isKnown) {
        knownCardsSet.add(cardId);
        playTone(659.25, 'triangle', 0.1);
        showToast('✔️ ¡Tarjeta #' + cardId + ' dominada!');
    } else {
        knownCardsSet.delete(cardId);
        playTone(392, 'sine', 0.1);
        showToast('🔄 Tarjeta #' + cardId + ' marcada para repaso');
    }

    const total = window.SOMMERVILLE_FLASHCARDS.length || 100;
    const count = knownCardsSet.size;

    const countEl = document.getElementById('knownCardsCount');
    const barEl = document.getElementById('fcProgressBar');

    if (countEl) countEl.textContent = count;
    if (barEl) barEl.style.width = `${(count / total) * 100}%`;

    const cardEl = document.querySelector(`.flashcard[data-card-id="${cardId}"]`);
    if (cardEl) {
        if (isKnown) {
            cardEl.classList.add('mastered');
            const inner = cardEl.querySelector('.flashcard-inner');
            if (inner) inner.style.boxShadow = '0 0 16px rgba(16, 185, 129, 0.45)';
        } else {
            cardEl.classList.remove('mastered');
            const inner = cardEl.querySelector('.flashcard-inner');
            if (inner) inner.style.boxShadow = '';
        }
    }
}

function filterFlashcards(cat, btn) {
    activeFlashcardFilter = cat;
    document.querySelectorAll('.flashcard-filter-btn').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    renderFlashcards();
}

function filterFlashcardsSearch(query) {
    flashcardSearchQuery = query.trim();
    renderFlashcards();
}

"""

gen_app_code = re.sub(old_flashcards_logic_pattern, new_flashcards_logic, gen_app_code, flags=re.DOTALL)

with open('generate_app.py', 'w', encoding='utf-8') as f:
    f.write(gen_app_code)

print("Updated generate_app.py successfully!")

# 3. UPDATE BUILD_HTML.PY
with open('build_html.py', 'r', encoding='utf-8') as f:
    build_html_code = f.read()

# Update sidebar item: "12 Tarjetas" -> "100 Tarjetas"
build_html_code = build_html_code.replace(
    '<span class="nav-item-badge badge-purple">12 Tarjetas</span>',
    '<span class="nav-item-badge badge-purple">100 Tarjetas</span>'
)

# Update Flashcards View section
old_fc_view_pattern = r'<!-- =+ *\n *VISTA 5: FLASHCARDS DE MEMORIZACIÓN 3D *\n *=+ -->.*?(?=<!-- =+ *\n *VISTA 6: GLOSARIO)'

new_fc_view = """<!-- ==============================================================
                 VISTA 5: FLASHCARDS DE MEMORIZACIÓN 3D (100 PUNTOS CLAVE)
                 ============================================================== -->
            <div id="flashcards-view" class="view-container">

                <div class="view-back-bar">
                    <button class="view-back-btn" onclick="showView('dashboard')">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                        <span>Volver al Tablero de Estudio</span>
                    </button>
                    <div style="font-family:'Outfit',sans-serif; font-weight:700; color:var(--text-dim); font-size:0.9rem;">
                        100 Puntos Clave de Ingeniería de Software
                    </div>
                </div>

                <div class="section-header">
                    <div class="section-title-wrap">
                        <h2>Flashcards de Memorización Activa 3D (100 Puntos Clave)</h2>
                        <div class="section-subtitle">Compendio oficial de 100 reactivos y conceptos esenciales organizados por áreas de conocimiento</div>
                    </div>
                    <div class="sommerville-pill">100 Tarjetas Oficiales</div>
                </div>

                <!-- Controles y Filtros de Categorías -->
                <div class="flashcard-controls">
                    <div class="filter-buttons">
                        <button class="filter-btn flashcard-filter-btn active" onclick="filterFlashcards('all', this)">Todas (100)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-fundamentos', this)">📘 Fundamentos (15)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-requisitos', this)">📋 Requisitos (15)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-metodologias', this)">🏗️ Metodologías (20)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-diseno', this)">🎨 Diseño &amp; Arq. (20)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-pruebas', this)">💻 Pruebas (15)</button>
                        <button class="filter-btn flashcard-filter-btn" onclick="filterFlashcards('cat-gestion', this)">📊 Gestión &amp; Métricas (15)</button>
                    </div>
                    <div class="progress-box">
                        <span>Dominadas: <strong id="knownCardsCount">0</strong> / 100</span>
                        <div class="progress-bar-bg" style="width: 140px;">
                            <div id="fcProgressBar" class="progress-bar-fill"></div>
                        </div>
                    </div>
                </div>

                <!-- Buscador Específico de Tarjetas de Memoria -->
                <div class="glossary-search-box" style="margin-top: 1.25rem; margin-bottom: 0.5rem;">
                    <span class="search-icon-pos">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
                    </span>
                    <input type="text" id="flashcardSearchInput" class="glossary-input" placeholder="Buscar en las 100 tarjetas (ej: Scrum, SOLID, COCOMO, Brooks, TDD, cascada, acoplamiento, deuda técnica...)" oninput="filterFlashcardsSearch(this.value)">
                </div>

                <!-- Contenedor Dinámico donde app.js Renderiza las 100 Tarjetas 3D -->
                <div class="flashcard-container" id="fcContainer">
                    <!-- Se puebla automáticamente con las 100 tarjetas interactivas 3D -->
                </div>

            </div>

            """

build_html_code = re.sub(old_fc_view_pattern, new_fc_view, build_html_code, flags=re.DOTALL)

with open('build_html.py', 'w', encoding='utf-8') as f:
    f.write(build_html_code)

print("Updated build_html.py successfully!")
