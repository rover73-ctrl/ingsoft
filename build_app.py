# -*- coding: utf-8 -*-
import json
from test_questions import questions

js_header = """/**
 * GUÍA OFICIAL DE INGENIERÍA DE SOFTWARE (CLA035) - IAN SOMMERVILLE 9ª ED.
 * Lógica e Interactividad Completa (app.js)
 * Contiene 105 preguntas académicas (15 por unidad), simuladores, flashcards y modo docente
 */

// Banco oficial de 105 preguntas rigurosas (15 por unidad)
window.SOMMERVILLE_QUESTIONS = """ + json.dumps(questions, indent=2, ensure_ascii=False) + """;

// Estado global de respuestas y puntuación
let userAnswers = {}; // { questionIndex: selectedOptionIndex }
let activeUnitFilter = 1; // 1 to 7, or 'all'
let professorModeActive = false;

document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initScrollSpy();
    initCalculators();
    renderQuestionnaire();
    updateGlobalQuizScore();
});

/* ==========================================================================
   1. GESTIÓN DEL TEMA (LIGHT / DARK MODE)
   ========================================================================== */

function initTheme() {
    const savedTheme = localStorage.getItem('cla035_theme') || 'light';
    setTheme(savedTheme, false);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    setTheme(newTheme, true);
}

function setTheme(theme, showToastMsg) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('cla035_theme', theme);

    const themeIcon = document.getElementById('themeIcon');
    const themeLabel = document.getElementById('themeLabel');

    if (theme === 'dark') {
        if (themeIcon) themeIcon.textContent = '☀️';
        if (themeLabel) themeLabel.textContent = 'Modo Claro';
        if (showToastMsg) showToast('🌙 Modo Oscuro activado');
    } else {
        if (themeIcon) themeIcon.textContent = '🌙';
        if (themeLabel) themeLabel.textContent = 'Modo Oscuro';
        if (showToastMsg) showToast('☀️ Modo Claro activado');
    }
}

/* ==========================================================================
   2. NAVEGACIÓN Y BÚSQUEDA GLOBAL
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
   3. MODO PROFESOR (CLAVE DOCENTE)
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
   4. MOTOR DEL CUESTIONARIO ACADÉMICO (15 PREGUNTAS POR UNIDAD)
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
                    ${answered ? (isCorrect ? '<span style="color:var(--success); font-weight:700;">✔️ Correcto (+1 pt)</span>' : '<span style="color:var(--danger); font-weight:700;">❌ Incorrecto</span>') : '<span style="color:var(--text-subtle);">⏳ Pendiente</span>'}
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
}

function answerQuestion(globalIndex, optionIndex) {
    userAnswers[globalIndex] = optionIndex;
    renderQuestionnaire();

    const item = window.SOMMERVILLE_QUESTIONS[globalIndex];
    if (optionIndex === item.correct) {
        showToast('✔️ ¡Pregunta ' + item.num + ' acertada! (+1 pt)');
    } else {
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

    window.SOMMERVILLE_QUESTIONS.forEach((q, idx) => {
        if (userAnswers.hasOwnProperty(idx) && userAnswers[idx] === q.correct) {
            totalCorrect++;
            unitScores[q.unit] = (unitScores[q.unit] || 0) + 1;
        }
    });

    const totalQuestions = window.SOMMERVILLE_QUESTIONS.length || 105;
    const scoreText = document.getElementById('quizScoreText');
    if (scoreText) scoreText.textContent = `${totalCorrect} / ${totalQuestions} pts`;

    for (let u = 1; u <= 7; u++) {
        const badge = document.getElementById('unit-score-badge-' + u);
        if (badge) badge.textContent = `${unitScores[u]}/15`;
    }

    if (activeUnitFilter !== 'all') {
        const activeScore = unitScores[activeUnitFilter] || 0;
        const activeScoreText = document.getElementById('activeUnitScoreText');
        const activeProgressBar = document.getElementById('activeUnitProgressBar');
        if (activeScoreText) activeScoreText.textContent = `${activeScore} / 15 correctas`;
        if (activeProgressBar) activeProgressBar.style.width = `${(activeScore / 15) * 100}%`;
    }

    updateStudyLevel(totalCorrect, totalQuestions);

    if (totalCorrect === totalQuestions && totalQuestions > 0) {
        triggerConfetti();
        showToast('🏆 ¡Felicidades! Has obtenido la máxima calificación en las 105 preguntas');
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
   5. CALCULADORAS INTERACTIVAS (COCOMO II & MCCABE)
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
   6. FLASHCARDS 3D
   ========================================================================== */

function flipCard(el) {
    el.classList.toggle('flipped');
}

const knownCardsSet = new Set();

function markCard(btn, isKnown) {
    const card = btn.closest('.flashcard');
    const allCards = Array.from(document.querySelectorAll('.flashcard'));
    const index = allCards.indexOf(card);

    if (isKnown) {
        knownCardsSet.add(index);
        card.style.borderColor = 'var(--success)';
        showToast('✔️ ¡Tarjeta dominada!');
    } else {
        knownCardsSet.delete(index);
        card.style.borderColor = '';
        showToast('🔄 Tarjeta para repaso');
    }

    const total = allCards.length || 12;
    const count = knownCardsSet.size;

    const countEl = document.getElementById('knownCardsCount');
    const barEl = document.getElementById('fcProgressBar');

    if (countEl) countEl.textContent = count;
    if (barEl) barEl.style.width = `${(count / total) * 100}%`;
}

function filterFlashcards(cat, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const cards = document.querySelectorAll('.flashcard');
    cards.forEach(card => {
        if (cat === 'all' || card.getAttribute('data-cat') === cat) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

/* ==========================================================================
   7. GLOSARIO DE TÉRMINOS
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
   8. SCROLLSPY Y BOTÓN VOLVER ARRIBA
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
   9. NOTIFICACIONES TOAST & CONFETI
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
    f.write(js_header)

print("app.js has been generated successfully!")
