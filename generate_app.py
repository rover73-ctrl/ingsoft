# -*- coding: utf-8 -*-
import json
from test_questions import questions
flashcards = json.load(open('flashcards.json', encoding='utf-8'))

# 1. GENERATE APP.JS
js_code = """/**
 * GUÍA OFICIAL DE INGENIERÍA DE SOFTWARE (CLA035) - IAN SOMMERVILLE 9ª ED.
 * Lógica e Interactividad Completa (app.js)
 * Contiene 105 preguntas académicas (15 por unidad), simuladores, flashcards y modo docente
 */

// Banco oficial de 105 preguntas rigurosas (15 por unidad)
window.SOMMERVILLE_QUESTIONS = """ + json.dumps(questions, indent=2, ensure_ascii=False) + """;

// Banco oficial de 100 Flashcards clave
window.SOMMERVILLE_FLASHCARDS = """ + json.dumps(flashcards, indent=2, ensure_ascii=False) + """;


// Estado global de respuestas y puntuación
let userAnswers = {}; // { questionIndex: selectedOptionIndex }
let activeUnitFilter = 1; // 1 to 7, or 'all'
let professorModeActive = false;
let soundEnabled = true;

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initScrollSpy();
    initCalculators();
    renderQuestionnaire();
    updateGlobalQuizScore();
    renderFlashcards();
});

/* ==========================================================================
   1. GESTIÓN DEL TEMA (LIGHT / DARK MODE)
   ========================================================================== */

function initTheme() {
    const savedTheme = localStorage.getItem('cla035_theme') || 'dark';
    setTheme(savedTheme, false);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme, true);
}

function setTheme(theme, showToastMsg) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('cla035_theme', theme);

    const themeBtn = document.getElementById('themeToggleBtn');
    if (themeBtn) {
        themeBtn.innerHTML = theme === 'dark' ? '☀️' : '🌙';
        themeBtn.title = theme === 'dark' ? 'Cambiar a Modo Claro' : 'Cambiar a Modo Oscuro';
    }

    if (showToastMsg) {
        showToast(theme === 'dark' ? '🌙 Modo Oscuro activado' : '☀️ Modo Claro activado');
    }
}


/* ==========================================================================
   2. NAVEGACIÓN ENTRE VISTAS DEL DASHBOARD
   ========================================================================== */

function showView(viewId, param) {
    const views = document.querySelectorAll('.view-container');
    views.forEach(v => {
        v.classList.remove('active');
        v.style.display = 'none';
    });

    const target = document.getElementById(viewId + '-view');
    if (target) {
        target.classList.add('active');
        target.style.display = 'flex';
    }

    document.querySelectorAll('.sidebar-nav-item').forEach(item => {
        if (item.getAttribute('data-view') === viewId) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });

    if (viewId === 'cuestionario' && param !== undefined) {
        switchQuizUnit(param);
    }

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function openUnitReading(unitNum) {
    showView('lecturas');
    setTimeout(() => {
        const el = document.getElementById('unit-group-' + unitNum);
        if (el) {
            const yOffset = -90;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    }, 120);
    showToast('📖 Abriendo Lecturas de la Unidad ' + unitNum);
}

function openUnitQuiz(unitNum) {
    showView('cuestionario', unitNum);
    showToast('📝 Abriendo Cuestionario de la Unidad ' + unitNum + ' (15 Preguntas)');
}

function startExamSimulator() {
    showView('cuestionario', 'all');
    showToast('🚀 Simulador Global de Examen activado (105 Preguntas)');
}

// Retroalimentación de audio Web Audio API
function toggleAudioFeedback() {
    soundEnabled = !soundEnabled;
    const btn = document.getElementById('audioToggleBtn');
    if (btn) {
        btn.innerHTML = soundEnabled ? '🔊' : '🔇';
        btn.title = soundEnabled ? 'Silenciar Efectos de Audio' : 'Activar Efectos de Audio';
    }
    showToast(soundEnabled ? '🔊 Sonidos activados' : '🔇 Sonidos silenciados');
}

function playTone(freq = 440, type = 'sine', duration = 0.08) {
    if (!soundEnabled) return;
    try {
        const AudioContextClass = window.AudioContext || window.webkitAudioContext;
        if (!AudioContextClass) return;
        const ctx = new AudioContextClass();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, ctx.currentTime);
        gain.gain.setValueAtTime(0.08, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
    } catch (e) {}
}

/* ==========================================================================
   3. BÚSQUEDA GLOBAL Y FILTROS
   ========================================================================== */

function handleGlobalSearch(query) {
    const q = query.trim().toLowerCase();
    const items = document.querySelectorAll('.searchable-item');
    const banner = document.getElementById('filterBanner');
    const querySpan = document.getElementById('filterQuery');

    if (!q) {
        if (banner) banner.style.display = 'none';
        items.forEach(item => item.style.display = '');
        return;
    }

    if (banner && querySpan) {
        banner.style.display = 'flex';
        querySpan.textContent = query;
    }

    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(q)) {
            item.style.display = '';
        } else {
            item.style.display = 'none';
        }
    });
}

function clearFilter() {
    const searchInput = document.getElementById('globalSearchInput');
    if (searchInput) {
        searchInput.value = '';
        handleGlobalSearch('');
    }
}

function scrollToSection(secId) {
    const el = document.getElementById(secId);
    if (el) {
        const yOffset = -135;
        const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: 'smooth' });
    }
}

function selectUnitFromTopBar(unitNum) {
    switchQuizUnit(unitNum);
    scrollToSection('unit-group-' + unitNum);
    showToast('📌 Navegando a Unidad ' + unitNum);
}

/* ==========================================================================
   4. MODO PROFESOR (CLAVE DOCENTE)
   ========================================================================== */

function toggleProfessorMode() {
    professorModeActive = !professorModeActive;
    const btn = document.getElementById('toggleProfBtn');

    if (btn) {
        if (professorModeActive) {
            btn.innerHTML = `
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg>
                <span>Desactivar Clave del Profesor</span>
            `;
            btn.classList.add('active');
            showToast('🎓 Modo Docente Activado: Se muestran todas las claves y justificaciones');
        } else {
            btn.innerHTML = `
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1Z"/></svg>
                <span>Activar Clave del Profesor</span>
            `;
            btn.classList.remove('active');
            showToast('🔒 Modo Docente Desactivado');
        }
    }

    renderQuestionnaire();
}

/* ==========================================================================
   5. MOTOR DEL CUESTIONARIO ACADÉMICO (15 PREGUNTAS POR UNIDAD)
   ========================================================================== */

function switchQuizUnit(unitNum) {
    activeUnitFilter = unitNum;
    
    document.querySelectorAll('.quiz-unit-tab').forEach(tab => {
        const u = tab.getAttribute('data-quiz-unit');
        if (u === String(unitNum)) {
            tab.classList.add('active');
        } else {
            tab.classList.remove('active');
        }
    });

    const activeTitle = document.getElementById('activeUnitTitleText');
    if (activeTitle) {
        if (unitNum === 'all') {
            activeTitle.textContent = 'Banco Global: 105 Preguntas de Examen';
        } else {
            activeTitle.textContent = `Unidad ${unitNum}: 15 Preguntas Académicas`;
        }
    }

    renderQuestionnaire();
}

function renderQuestionnaire() {
    const container = document.getElementById('quizQuestionsContainer');
    if (!container) return;

    const filtered = (activeUnitFilter === 'all')
        ? window.SOMMERVILLE_QUESTIONS
        : window.SOMMERVILLE_QUESTIONS.filter(q => q.unit === activeUnitFilter);

    let html = '';

    filtered.forEach(item => {
        const globalIndex = window.SOMMERVILLE_QUESTIONS.indexOf(item);
        const answered = userAnswers.hasOwnProperty(globalIndex);
        const chosen = answered ? userAnswers[globalIndex] : null;
        const isCorrect = answered && chosen === item.correct;

        html += `
        <div class="quiz-card searchable-item" id="q-card-${globalIndex}">
            <div class="quiz-card-header">
                <div class="quiz-unit-badge">${item.unitName} • Pregunta ${item.num} de 15</div>
                <div class="quiz-card-status" id="q-status-${globalIndex}">
                    ${answered ? (isCorrect ? '<span style="color:var(--success-text); font-weight:700;">✔️ Correcto (+1 pt)</span>' : '<span style="color:var(--danger-text); font-weight:700;">❌ Incorrecto</span>') : '<span style="color:var(--text-dim);">⏳ Pendiente</span>'}
                </div>
            </div>

            <div class="quiz-card-question">${item.q}</div>

            <div class="quiz-card-options">
                ${item.options.map((opt, optIdx) => {
                    let optClass = 'quiz-opt-btn';
                    if (answered) {
                        if (optIdx === item.correct) {
                            optClass += ' opt-correct';
                        } else if (chosen === optIdx) {
                            optClass += ' opt-wrong';
                        }
                    } else if (professorModeActive && optIdx === item.correct) {
                        optClass += ' opt-teacher-key';
                    }

                    return `
                    <button class="${optClass}" onclick="answerQuestion(${globalIndex}, ${optIdx})">
                        <span class="opt-bullet">${['A', 'B', 'C', 'D'][optIdx]}</span>
                        <span class="opt-text">${opt.substring(3)}</span>
                    </button>
                    `;
                }).join('')}
            </div>

            <div class="quiz-card-explanation ${answered || professorModeActive ? 'show' : ''} ${isCorrect ? 'exp-correct' : 'exp-info'}">
                <strong>💡 Justificación Técnica (Sommerville 9ª Ed.):</strong><br>
                ${item.explanation}
            </div>
        </div>
        `;
    });

    container.innerHTML = html;
    updateGlobalQuizScore();
    renderFlashcards();
}

function answerQuestion(globalIndex, optionIndex) {
    userAnswers[globalIndex] = optionIndex;
    renderQuestionnaire();

    const item = window.SOMMERVILLE_QUESTIONS[globalIndex];
    if (optionIndex === item.correct) {
        playTone(587.33, 'triangle', 0.12);
        showToast('✔️ ¡Pregunta ' + item.num + ' acertada! (+1 pt)');
    } else {
        playTone(220, 'sawtooth', 0.15);
        showToast('❌ Pregunta ' + item.num + ': respuesta incorrecta');
    }
}

function resetQuizUnit() {
    if (activeUnitFilter === 'all') {
        userAnswers = {};
        showToast('🔄 Se han reiniciado todas las respuestas');
    } else {
        window.SOMMERVILLE_QUESTIONS.forEach((q, idx) => {
            if (q.unit === activeUnitFilter) {
                delete userAnswers[idx];
            }
        });
        showToast('🔄 Respuestas reiniciadas para Unidad ' + activeUnitFilter);
    }
    renderQuestionnaire();
}

function updateGlobalQuizScore() {
    let totalCorrect = 0;
    const unitScores = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 };
    const unitAttempted = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 };

    window.SOMMERVILLE_QUESTIONS.forEach((q, idx) => {
        if (userAnswers.hasOwnProperty(idx)) {
            unitAttempted[q.unit] = (unitAttempted[q.unit] || 0) + 1;
            if (userAnswers[idx] === q.correct) {
                totalCorrect++;
                unitScores[q.unit] = (unitScores[q.unit] || 0) + 1;
            }
        }
    });

    const totalQuestions = window.SOMMERVILLE_QUESTIONS.length || 105;
    const percentage = totalQuestions > 0 ? Math.round((totalCorrect / totalQuestions) * 100) : 0;

    // Actualizar badges en pestañas del cuestionario
    const scoreText = document.getElementById('quizScoreText');
    if (scoreText) scoreText.textContent = `${totalCorrect} / ${totalQuestions} pts`;

    for (let u = 1; u <= 7; u++) {
        const badge = document.getElementById('unit-score-badge-' + u);
        if (badge) badge.textContent = `${unitScores[u]}/15`;

        // Actualizar badges de módulos en el dashboard
        const modMetaStatus = document.getElementById('mod-status-' + u);
        if (modMetaStatus) {
            if (unitAttempted[u] === 0) {
                modMetaStatus.innerHTML = '⚪ No Intentado';
            } else if (unitScores[u] === 15) {
                modMetaStatus.innerHTML = '<span style="color:var(--success-text); font-weight:700;">🟢 15/15 Dominado (100%)</span>';
            } else {
                modMetaStatus.innerHTML = `<span style="color:#60a5fa; font-weight:700;">🟡 ${unitScores[u]}/15 (${unitAttempted[u]} resp.)</span>`;
            }
        }
    }

    if (activeUnitFilter !== 'all') {
        const activeScore = unitScores[activeUnitFilter] || 0;
        const activeScoreText = document.getElementById('activeUnitScoreText');
        const activeProgressBar = document.getElementById('activeUnitProgressBar');
        if (activeScoreText) activeScoreText.textContent = `${activeScore} / 15 correctas`;
        if (activeProgressBar) activeProgressBar.style.width = `${(activeScore / 15) * 100}%`;
    }

    // Actualizar métricas del Dashboard (Cards Superiores)
    const statApproved = document.getElementById('statApprovedQuestions');
    if (statApproved) statApproved.textContent = `${totalCorrect}/${totalQuestions}`;

    const statAverage = document.getElementById('statAverageScore');
    if (statAverage) statAverage.textContent = `${percentage}%`;

    // Actualizar pie del sidebar
    const footerPct = document.getElementById('footerPercentText');
    if (footerPct) footerPct.textContent = `${percentage}% Dominado`;

    const footerBar = document.getElementById('footerProgressBar');
    if (footerBar) footerBar.style.width = `${percentage}%`;

    updateStudyLevel(totalCorrect, totalQuestions);

    if (totalCorrect === totalQuestions && totalQuestions > 0) {
        triggerConfetti();
        showToast('🏆 ¡Felicidades! Has dominado las 105 preguntas con éxito');
    }
}

function updateStudyLevel(score, total) {
    const percentage = total > 0 ? Math.round((score / total) * 100) : 0;
    const fillBar = document.getElementById('studyProgressBar');
    const textStatus = document.getElementById('studyStatusText');

    if (fillBar) fillBar.style.width = `${percentage}%`;

    if (textStatus) {
        if (percentage < 20) {
            textStatus.textContent = '🌱 Estudiante Novel (' + percentage + '%)';
        } else if (percentage < 45) {
            textStatus.textContent = '📘 Analista de Requerimientos (' + percentage + '%)';
        } else if (percentage < 70) {
            textStatus.textContent = '⚙️ Diseñador de Software (' + percentage + '%)';
        } else if (percentage < 90) {
            textStatus.textContent = '🚀 Ingeniero de Software (' + percentage + '%)';
        } else {
            textStatus.textContent = '🏆 Arquitecto de Software Senior (' + percentage + '%)';
        }
    }
}

/* ==========================================================================
   6. CALCULADORAS INTERACTIVAS (COCOMO II & MCCABE)
   ========================================================================== */

function initCalculators() {
    calculateCocomo();
    calculateMcCabe();
}

function calculateCocomo() {
    const klocInput = document.getElementById('cocomoKloc');
    const modeSelect = document.getElementById('cocomoMode');
    if (!klocInput || !modeSelect) return;

    const kloc = Math.max(1, parseFloat(klocInput.value) || 25);
    const mode = modeSelect.value;

    let a, b, c, d;
    if (mode === 'organic') {
        a = 2.4; b = 1.05; c = 2.5; d = 0.38;
    } else if (mode === 'semidetached') {
        a = 3.0; b = 1.12; c = 2.5; d = 0.35;
    } else {
        a = 3.6; b = 1.20; c = 2.5; d = 0.32;
    }

    const effort = a * Math.pow(kloc, b);
    const time = c * Math.pow(effort, d);
    const staff = effort / time;

    const resEffort = document.getElementById('resCocomoEffort');
    const resTime = document.getElementById('resCocomoTime');
    const resStaff = document.getElementById('resCocomoStaff');

    if (resEffort) resEffort.textContent = effort.toFixed(1) + ' PM';
    if (resTime) resTime.textContent = time.toFixed(1) + ' meses';
    if (resStaff) resStaff.textContent = Math.ceil(staff) + ' personas';
}

function calculateMcCabe() {
    const eInput = document.getElementById('mccabeE');
    const nInput = document.getElementById('mccabeN');
    const pInput = document.getElementById('mccabeP');
    if (!eInput || !nInput || !pInput) return;

    const E = parseInt(eInput.value) || 14;
    const N = parseInt(nInput.value) || 10;
    const P = parseInt(pInput.value) || 1;

    const vg = E - N + (2 * P);

    const resVal = document.getElementById('resMcCabeVal');
    const resRisk = document.getElementById('resMcCabeRisk');

    if (resVal) resVal.textContent = `V(G) = ${vg}`;
    if (resRisk) {
        if (vg <= 10) {
            resRisk.textContent = '🟢 Módulo Simple (Bajo Riesgo)';
            resRisk.style.color = 'var(--success-text)';
        } else if (vg <= 20) {
            resRisk.textContent = '🟡 Complejidad Moderada (Riesgo Medio)';
            resRisk.style.color = 'var(--warning-text)';
        } else if (vg <= 50) {
            resRisk.textContent = '🟠 Alta Complejidad (Alto Riesgo)';
            resRisk.style.color = 'var(--warning-text)';
        } else {
            resRisk.textContent = '🔴 Código Inmanejable (Riesgo Crítico)';
            resRisk.style.color = 'var(--danger-text)';
        }
    }
}

/* ==========================================================================
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

/* ==========================================================================
   8. GLOSARIO DE TÉRMINOS
   ========================================================================== */

function filterGlossary(query) {
    const q = query.trim().toLowerCase();
    const cards = document.querySelectorAll('.glossary-card');

    cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(q)) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

/* ==========================================================================
   9. SCROLLSPY Y BOTÓN VOLVER ARRIBA
   ========================================================================== */

function initScrollSpy() {
    const backToTopBtn = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
        if (backToTopBtn) {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        }
    });
}

/* ==========================================================================
   10. NOTIFICACIONES TOAST & CONFETI
   ========================================================================== */

function showToast(message) {
    let container = document.getElementById('toastContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerHTML = message;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
    }, 3200);
}

function triggerConfetti() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '9999';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const particles = [];
    const colors = ['#2563eb', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#06b6d4'];

    for (let i = 0; i < 110; i++) {
        particles.push({
            x: canvas.width / 2,
            y: canvas.height / 2,
            vx: (Math.random() - 0.5) * 16,
            vy: (Math.random() - 0.5) * 16 - 4,
            size: Math.random() * 8 + 4,
            color: colors[Math.floor(Math.random() * colors.length)],
            alpha: 1
        });
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let alive = false;

        particles.forEach(p => {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.25;
            p.alpha -= 0.012;

            if (p.alpha > 0) {
                alive = true;
                ctx.globalAlpha = p.alpha;
                ctx.fillStyle = p.color;
                ctx.fillRect(p.x, p.y, p.size, p.size);
            }
        });

        if (alive) {
            requestAnimationFrame(animate);
        } else {
            canvas.remove();
        }
    }
    requestAnimationFrame(animate);
}
"""

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

print("Updated app.js written successfully!")
