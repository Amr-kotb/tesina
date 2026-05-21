(function() {
    // --------------------------------------------------------
    // 0. PRELOADER (10 secondi)
    // --------------------------------------------------------
    const preloader = document.getElementById('preloader');
    const progressBar = document.getElementById('preloaderProgressBar');
    const counterEl = document.getElementById('preloaderCounter');
    const DURATION = 10000;
    const startTime = Date.now();

    function updatePreloader() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / DURATION * 100, 100);
        if (progressBar) progressBar.style.width = progress + '%';
        if (counterEl) counterEl.textContent = Math.round(progress) + '%';

        if (elapsed < DURATION) {
            requestAnimationFrame(updatePreloader);
        } else {
            if (progressBar) progressBar.style.width = '100%';
            if (counterEl) counterEl.textContent = '100%';
            setTimeout(hidePreloader, 300);
        }
    }

    function hidePreloader() {
        if (preloader) {
            preloader.classList.add('hidden');
            document.body.classList.remove('preloader-active');
            setTimeout(() => {
                if (preloader && preloader.parentNode) {
                    preloader.remove();
                }
            }, 700);
        }
    }

    requestAnimationFrame(updatePreloader);

    // --------------------------------------------------------
    // 1. DATI PER LE MODALI
    // --------------------------------------------------------
    const languageDetails = {
        c: {
            title: "Linguaggio C - Approfondimento",
            content: `
            <h4>Contesto Storico</h4>
            <p>Il linguaggio C fu sviluppato da Dennis Ritchie presso i Bell Labs tra il 1969 e il 1973. Nasce dall'esigenza di riscrivere il sistema operativo UNIX, inizialmente scritto in assembly.</p>
            <h4>Caratteristiche Tecniche</h4>
            <ul>
                <li><strong>Compilato</strong> - Il codice viene tradotto direttamente in linguaggio macchina</li>
                <li><strong>Gestione manuale della memoria</strong> - Utilizzo di malloc() e free()</li>
                <li><strong>Puntatori</strong> - Accesso diretto agli indirizzi di memoria</li>
            </ul>
            <h4>Esempio di Codice</h4>
            <pre class="code-example">#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

int main() {
    int *arr = (int*)malloc(5 * sizeof(int));
    if (arr == NULL) return 1;
    for(int i = 0; i < 5; i++) arr[i] = i * 10;
    free(arr);
    return 0;
}</pre>
            `
        },
        python: {
            title: "Linguaggio Python - Approfondimento",
            content: `
            <h4>Contesto Storico</h4>
            <p>Python fu creato da Guido van Rossum e rilasciato nel 1991. Il nome deriva dal gruppo comico "Monty Python".</p>
            <h4>Caratteristiche Tecniche</h4>
            <ul>
                <li><strong>Interpretato</strong> - Esecuzione tramite interprete</li>
                <li><strong>Tipizzazione dinamica</strong> - Le variabili non hanno tipo fisso</li>
                <li><strong>Multi-paradigma</strong> - Supporta OOP, funzionale e procedurale</li>
            </ul>
            <h4>Esempio di Codice</h4>
            <pre class="code-example">numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati_pari = [n**2 for n in numeri if n % 2 == 0]
print(f"Quadrati dei numeri pari: {quadrati_pari}")</pre>
            `
        },
        java: {
            title: "Linguaggio Java - Approfondimento",
            content: `
            <h4>Contesto Storico</h4>
            <p>Java fu sviluppato da James Gosling alla Sun Microsystems, rilasciato nel 1995. Il motto e' "Write Once, Run Anywhere".</p>
            <h4>Caratteristiche Tecniche</h4>
            <ul>
                <li><strong>JVM</strong> - Java Virtual Machine esegue il bytecode</li>
                <li><strong>OOP puro</strong> - Tutto e' un oggetto</li>
                <li><strong>Garbage Collection</strong> - Gestione automatica della memoria</li>
            </ul>
            <h4>Esempio di Codice</h4>
            <pre class="code-example">public class Studente {
    private String nome;
    private int eta;
    
    public Studente(String nome, int eta) {
        this.nome = nome;
        this.eta = eta;
    }
    
    public void presentati() {
        System.out.println("Ciao, sono " + nome);
    }
}</pre>
            `
        }
    };

    const projectDetails = {
        flutter: {
            title: "AKnote - App per la gestione delle attivita'",
            image: "/images/aknote-poster.jpg",
            content: `
            <h4>Descrizione del Progetto</h4>
            <p>AKnote e' un'applicazione mobile per la gestione delle note e delle attivita' quotidiane, sviluppata con Flutter e Dart. Funziona su iOS e Android con un'unica base di codice.</p>
            <h4>Tecnologie Utilizzate</h4>
            <ul><li>Flutter</li><li>Dart</li><li>Firebase</li><li>Provider</li></ul>
            <h4>Funzionalita'</h4>
            <ul><li>Registrazione e login</li><li>CRUD task</li><li>Sincronizzazione cloud</li></ul>
            `
        },
        recart: {
            title: "Task Gariboldi - Portale gestionale aziendale",
            image: "/images/taskG.png",
            content: `
            <h4>Descrizione del Progetto</h4>
            <p>Portale gestionale per azienda con dashboard interattiva, gestione task, clienti e dipendenti. Include reportistica personalizzata ed esportazione dati.</p>
            <h4>Tecnologie Utilizzate</h4>
            <ul><li>JavaScript</li><li>Recart</li><li>Node.js</li><li>Firebase</li><li>JSON/ENV</li></ul>
            <h4>Funzionalita'</h4>
            <ul><li>Dashboard per ruoli</li><li>Export report PDF/Excel</li><li>Autenticazione</li></ul>
            `
        },
        website: {
            title: "Portfolio Creativo - Sito Web Professionale",
            image: "/images/akstore.png",
            content: `
            <h4>Descrizione del Progetto</h4>
            <p>Sito web responsive con animazioni CSS avanzate per presentare progetti e competenze. Design moderno e ottimizzato per i motori di ricerca.</p>
            <h4>Tecnologie Utilizzate</h4>
            <ul><li>HTML5</li><li>CSS3</li></ul>
            <h4>Caratteristiche</h4>
            <ul><li>Design responsive</li><li>Animazioni CSS</li><li>SEO ottimizzato</li></ul>
            `
        }
    };

    // --------------------------------------------------------
    // 2. GESTIONE MODALE
    // --------------------------------------------------------
    let modalOverlay = null, modalContainer = null;
    let lastFocusedElement = null;

    function closeModal() {
        if (modalOverlay) modalOverlay.remove();
        if (modalContainer) modalContainer.remove();
        modalOverlay = null;
        modalContainer = null;
        document.body.classList.remove('modal-open');
        if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
            lastFocusedElement.focus();
        }
    }

    function openModal(title, content, imageUrl = null) {
        closeModal();
        lastFocusedElement = document.activeElement;
        modalOverlay = document.createElement('div');
        modalOverlay.className = 'modal-overlay';
        modalOverlay.setAttribute('role', 'dialog');
        modalOverlay.setAttribute('aria-modal', 'true');
        modalOverlay.setAttribute('aria-label', title);
        modalContainer = document.createElement('div');
        modalContainer.className = 'modal-container';
        let imageHtml = imageUrl ? `<img src="${imageUrl}" alt="Anteprima del progetto" class="modal-image" loading="lazy">` : '';
        modalContainer.innerHTML = `
            <div class="modal-header">
                <h3>${title}</h3>
                <button class="modal-close" aria-label="Chiudi modale">✕</button>
            </div>
            <div class="modal-body">
                ${imageHtml}
                ${content}
            </div>
        `;
        document.body.appendChild(modalOverlay);
        document.body.appendChild(modalContainer);
        document.body.classList.add('modal-open');

        const closeBtn = modalContainer.querySelector('.modal-close');
        closeBtn.addEventListener('click', closeModal);
        modalOverlay.addEventListener('click', closeModal);

        setTimeout(() => closeBtn.focus(), 100);

        function escHandler(e) {
            if (e.key === 'Escape') {
                closeModal();
                document.removeEventListener('keydown', escHandler);
            }
        }
        document.addEventListener('keydown', escHandler);
    }

    // Apertura modali dalle card dei linguaggi
    document.querySelectorAll('.lang-card').forEach(card => {
        const btn = card.querySelector('.lang-card-btn');
        if (btn) {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = card.getAttribute('data-lang');
                if (lang && languageDetails[lang]) {
                    openModal(languageDetails[lang].title, languageDetails[lang].content);
                }
            });
        }
        card.addEventListener('click', (e) => {
            if (e.target.closest('.lang-card-btn')) return;
            const lang = card.getAttribute('data-lang');
            if (lang && languageDetails[lang]) {
                openModal(languageDetails[lang].title, languageDetails[lang].content);
            }
        });
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                if (e.target.closest('.lang-card-btn')) return;
                e.preventDefault();
                card.click();
            }
        });
    });

    document.querySelectorAll('.progetto-reale-card').forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('a') || e.target.closest('button')) return;
            const project = card.getAttribute('data-project');
            if (project && projectDetails[project]) {
                const dettaglio = projectDetails[project];
                openModal(dettaglio.title, dettaglio.content, dettaglio.image);
            }
        });
        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                if (e.target.closest('a') || e.target.closest('button')) return;
                e.preventDefault();
                card.click();
            }
        });
    });

    // --------------------------------------------------------
    // 3. MENU HAMBURGER MOBILE
    // --------------------------------------------------------
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            const isActive = navMenu.classList.toggle('active');
            hamburger.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isActive);
        });

        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                hamburger.classList.remove('active');
                hamburger.setAttribute('aria-expanded', 'false');
            });
        });
    }

    // --------------------------------------------------------
    // 4. EFFETTO SCROLL SULLA NAVBAR E TORNA SU
    // --------------------------------------------------------
    const navbar = document.querySelector('.navbar');
    const backToTop = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        if (navbar) {
            if (scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        }
        if (backToTop) {
            if (scrollY > 400) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        }
    }, { passive: true });

    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // --------------------------------------------------------
    // 5. ANIMAZIONE CONTATORI STATISTICHE
    // --------------------------------------------------------
    const statNumbers = document.querySelectorAll('.stat-number');
    const countedStats = new Set();

    function animateNumbers() {
        statNumbers.forEach(stat => {
            if (countedStats.has(stat)) return;
            const target = parseInt(stat.getAttribute('data-target'));
            if (!target && target !== 0) return;
            const rect = stat.getBoundingClientRect();
            if (rect.top < window.innerHeight - 50 && rect.bottom > 0) {
                countedStats.add(stat);
                let current = 0;
                const duration = 1500;
                const steps = 60;
                const increment = target / steps;
                const interval = duration / steps;
                let step = 0;

                function stepCounter() {
                    step++;
                    current = Math.min(increment * step, target);
                    stat.textContent = Math.floor(current).toLocaleString();
                    if (step < steps) {
                        setTimeout(stepCounter, interval);
                    } else {
                        stat.textContent = target.toLocaleString();
                    }
                }
                stepCounter();
            }
        });
    }
    window.addEventListener('scroll', animateNumbers, { passive: true });
    setTimeout(animateNumbers, DURATION + 500);

    // --------------------------------------------------------
    // 6. INVIO FORM SUPPORTO (AJAX)
    // --------------------------------------------------------
    const form = document.getElementById('supportoForm');
    const successDiv = document.getElementById('formSuccess');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span>Invio in corso...</span>';
            submitBtn.disabled = true;
            try {
                const formData = new FormData(form);
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                });
                if (response.ok) {
                    if (successDiv) successDiv.style.display = 'block';
                    form.reset();
                    setTimeout(() => { if (successDiv) successDiv.style.display = 'none'; }, 5000);
                } else {
                    throw new Error('Errore nella risposta del server');
                }
            } catch (error) {
                alert('Errore durante l\'invio. Riprova più tardi.');
            } finally {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }
        });
    }

    // --------------------------------------------------------
    // 7. SMOOTH SCROLL PER ANCORE INTERNE
    // --------------------------------------------------------
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target && navbar) {
                e.preventDefault();
                const navHeight = navbar.offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 10;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                if (navMenu && navMenu.classList.contains('active')) {
                    navMenu.classList.remove('active');
                    if (hamburger) hamburger.classList.remove('active');
                    if (hamburger) hamburger.setAttribute('aria-expanded', 'false');
                }
            }
        });
    });

    // --------------------------------------------------------
    // 8. ANIMAZIONE BARRE STATISTICHE LINGUAGGI
    // --------------------------------------------------------
    const statBars = document.querySelectorAll('.stat-fill');
    const animatedBars = new Set();

    function animateStatBars() {
        statBars.forEach(bar => {
            if (animatedBars.has(bar)) return;
            const rect = bar.getBoundingClientRect();
            if (rect.top < window.innerHeight - 30 && rect.bottom > 0) {
                animatedBars.add(bar);
                const targetWidth = bar.style.width;
                bar.style.width = '0';
                bar.style.transition = 'width 1.2s cubic-bezier(0.4, 0, 0.2, 1)';
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        bar.style.width = targetWidth;
                    });
                });
            }
        });
    }
    window.addEventListener('scroll', animateStatBars, { passive: true });
    setTimeout(animateStatBars, DURATION + 300);

    // --------------------------------------------------------
    // 9. EVIDENZIA LINK ATTIVO NELLA NAV
    // --------------------------------------------------------
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    window.addEventListener('scroll', () => {
        let current = '';
        const scrollPosition = window.scrollY + 120;
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${current}`) {
                link.classList.add('active');
            } else if (current === '' && href === '#home') {
                link.classList.add('active');
            }
        });
    }, { passive: true });

    // --------------------------------------------------------
    // 10. CHATBOT AI - KNOWLEDGE BASE
    // --------------------------------------------------------
    (function() {
        const KNOWLEDGE_BASE = [
            { keywords: ["ciao", "salve", "buongiorno", "buonasera", "hey"], response: "👋 Ciao! Sono l'assistente per i linguaggi di programmazione. Digita `aiuto` per tutti gli argomenti!" },
            { keywords: ["aiuto", "help", "cosa sai fare", "argomenti"], response: "📚 **ARGOMENTI DISPONIBILI**\n\n**LINGUAGGI:** Python, Java, C, C++, JavaScript, Rust\n**CONCETTI:** OOP, compilato vs interpretato\n**STRUMENTI:** Framework, API, Git\n**WEB:** Frontend vs Backend\n**CONSIGLI:** quale linguaggio studiare" },
            { keywords: ["grazie", "thank", "grazie mille"], response: "😊 Prego! Sono felice di essere stato d'aiuto!" },
            { keywords: ["cos'è un linguaggio di programmazione", "definizione linguaggio"], response: "💻 **COS'È UN LINGUAGGIO DI PROGRAMMAZIONE**\n\nÈ un insieme di regole che permette di scrivere istruzioni eseguibili da un computer.\n\nEsistono oltre 700 linguaggi di programmazione!" },
            { keywords: ["python", "cos'è python"], response: "🐍 **PYTHON**\n\nCreato da Guido van Rossum nel 1991.\n• Interpretato, tipizzazione dinamica\n• Sintassi chiara e leggibile\n• Perfetto per AI, Data Science, Web" },
            { keywords: ["java", "cos'è java"], response: "☕ **JAVA**\n\nCreato da James Gosling nel 1995.\n• OOP puro, eseguito su JVM\n• 'Write Once, Run Anywhere'\n• Standard per applicazioni enterprise" },
            { keywords: ["c linguaggio", "linguaggio c"], response: "⚡ **LINGUAGGIO C**\n\nCreato da Dennis Ritchie nel 1972.\n• Linguaggio procedurale\n• Controllo totale della memoria\n• Usato per OS, embedded, database" },
            { keywords: ["javascript", "js"], response: "🟨 **JAVASCRIPT**\n\nCreato da Brendan Eich nel 1995.\n• Il linguaggio del web\n• Frontend (React, Vue) e Backend (Node.js)\n• Il più diffuso al mondo!" },
            { keywords: ["oop", "programmazione orientata oggetti"], response: "🎯 **PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)**\n\n**4 PRINCIPI:**\n1. Incapsulamento\n2. Ereditarietà\n3. Polimorfismo\n4. Astrazione" },
            { keywords: ["compilato interpretato", "differenza compilato interpretato"], response: "📊 **COMPILATO vs INTERPRETATO**\n\n| Caratteristica | COMPILATO | INTERPRETATO |\n|---------------|-----------|--------------|\n| Velocità | ⚡⚡⚡ Molto veloce | 🐢 Più lento |\n| Portabilità | Richiede ricompilazione | Qualsiasi piattaforma |\n| Debugging | Più difficile | Interattivo |" },
            { keywords: ["frontend backend", "differenza frontend backend"], response: "🌐 **FRONTEND vs BACKEND**\n\n| Aspetto | FRONTEND | BACKEND |\n|---------|----------|---------|\n| Tecnologie | HTML, CSS, JS | Python, Java, PHP |\n| Dove gira | Browser | Server |\n| Compiti | UI, animazioni | Database, API |" }
        ];

        const BLACKLIST = ["calcio", "sport", "politica", "film", "musica", "cucina"];

        function normalizzaTesto(testo) {
            return testo.toLowerCase()
                .replace(/[àáâä]/g, 'a').replace(/[èéêë]/g, 'e')
                .replace(/[ìíîï]/g, 'i').replace(/[òóôö]/g, 'o')
                .replace(/[ùúûü]/g, 'u').replace(/[^a-z0-9\s]/g, ' ')
                .replace(/\s+/g, ' ')
                .trim();
        }

        function ePertinente(testo) {
            for (let black of BLACKLIST) {
                if (testo.includes(black)) return false;
            }
            return true;
        }

        function trovaRisposta(domandaNorm) {
            for (const entry of KNOWLEDGE_BASE) {
                for (const kw of entry.keywords) {
                    if (domandaNorm.includes(normalizzaTesto(kw))) {
                        return entry.response;
                    }
                }
            }
            return null;
        }

        function rispondi(domandaUtente) {
            if (!domandaUtente || !domandaUtente.trim()) {
                return "🙂 Per favore, scrivi una domanda.";
            }

            const domandaNorm = normalizzaTesto(domandaUtente);

            if (domandaNorm === "esci") {
                return "EXIT";
            }

            if (!ePertinente(domandaNorm)) {
                return "⚠️ Sono specializzato solo in **linguaggi di programmazione**.\n\nProva con: 'cos'è Python?' o 'differenza C e C++'";
            }

            const risposta = trovaRisposta(domandaNorm);
            if (risposta) {
                return risposta;
            } else {
                return "🤔 Non ho trovato una risposta precisa.\n\nProva a chiedermi:\n• 'cos'è Python?'\n• 'cos'è Java?'\n• 'differenza frontend backend'";
            }
        }

        // Integrazione DOM
        const toggleBtn = document.getElementById('chatbotToggle');
        const closeBtn = document.getElementById('chatbotClose');
        const windowEl = document.getElementById('chatbotWindow');
        const messagesEl = document.getElementById('chatbotMessages');
        const inputEl = document.getElementById('chatbotInput');
        const sendBtn = document.getElementById('chatbotSend');

        function aggiungiMessaggio(testo, tipo) {
            const msgDiv = document.createElement('div');
            msgDiv.className = 'message ' + tipo;
            msgDiv.innerHTML = testo.replace(/\n/g, '<br>');
            messagesEl.appendChild(msgDiv);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }

        function mostraTyping() {
            const div = document.createElement('div');
            div.className = 'message bot';
            div.innerHTML = '<div class="typing-indicator"><span></span><span></span><span></span></div>';
            div.id = 'typing-indicator';
            messagesEl.appendChild(div);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }

        function rimuoviTyping() {
            const el = document.getElementById('typing-indicator');
            if (el) el.remove();
        }

        function inviaMessaggio() {
            const testo = inputEl.value.trim();
            if (!testo) return;

            aggiungiMessaggio(testo, 'user');
            inputEl.value = '';
            mostraTyping();

            setTimeout(() => {
                rimuoviTyping();
                const risposta = rispondi(testo);
                if (risposta === "EXIT") {
                    aggiungiMessaggio("Arrivederci! Alla prossima.", 'bot');
                    setTimeout(() => {
                        windowEl.classList.add('hidden');
                        if (toggleBtn) toggleBtn.style.display = 'flex';
                    }, 1500);
                } else {
                    aggiungiMessaggio(risposta, 'bot');
                }
            }, 500);
        }

        if (toggleBtn) {
            toggleBtn.addEventListener('click', () => {
                windowEl.classList.remove('hidden');
                toggleBtn.style.display = 'none';
                setTimeout(() => inputEl?.focus(), 150);
            });
        }

        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                windowEl.classList.add('hidden');
                if (toggleBtn) toggleBtn.style.display = 'flex';
                if (toggleBtn) toggleBtn.focus();
            });
        }

        if (sendBtn) sendBtn.addEventListener('click', inviaMessaggio);

        if (inputEl) {
            inputEl.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    inviaMessaggio();
                }
            });
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && windowEl && !windowEl.classList.contains('hidden')) {
                windowEl.classList.add('hidden');
                if (toggleBtn) toggleBtn.style.display = 'flex';
                if (toggleBtn) toggleBtn.focus();
            }
        });
    })();

    // --------------------------------------------------------
    // 11. GESTIONE ERRORI IMMAGINI
    // --------------------------------------------------------
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
            const placeholder = document.createElement('div');
            placeholder.style.cssText = 'width:' + (this.width || 60) + 'px;height:' + (this.height || 60) + 'px;background:var(--dark-surface);border-radius:var(--radius-lg);display:flex;align-items:center;justify-content:center;color:var(--text-muted);font-size:0.7rem;';
            placeholder.textContent = 'IMG';
            if (this.parentNode) {
                this.parentNode.insertBefore(placeholder, this);
            }
        });
    });

    console.log('AK Coding - Tesina Linguaggi di Programmazione');
    console.log('Autore: Amr Ahmed Kotb | Classe 3I | A.S. 2025/2026');
})();