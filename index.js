// ============================================
// MODAL SYSTEM - CONTENUTI DETTAGLIATI
// ============================================

(function() {
    // Contenuti dettagliati per i linguaggi
    const languageDetails = {
        c: {
            title: "Linguaggio C - Approfondimento Accademico",
            content: `
                <h4>📅 Contesto Storico</h4>
                <p>Il linguaggio C fu sviluppato da Dennis Ritchie presso i Bell Labs tra il 1969 e il 1973. Nasce dall'esigenza di riscrivere il sistema operativo UNIX, inizialmente scritto in assembly.</p>
                
                <h4>⚙️ Caratteristiche Tecniche</h4>
                <ul>
                    <li><strong>Compilato</strong> - Il codice viene tradotto direttamente in linguaggio macchina</li>
                    <li><strong>Gestione manuale della memoria</strong> - Utilizzo di malloc() e free()</li>
                    <li><strong>Puntatori</strong> - Accesso diretto agli indirizzi di memoria</li>
                </ul>
                
                <h4>📝 Esempio di Codice</h4>
                <pre class="code-example">
#include &lt;stdio.h&gt;
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
            title: "Linguaggio Python - Approfondimento Accademico",
            content: `
                <h4>📅 Contesto Storico</h4>
                <p>Python fu creato da Guido van Rossum e rilasciato nel 1991. Il nome deriva dal gruppo comico "Monty Python".</p>
                
                <h4>⚙️ Caratteristiche Tecniche</h4>
                <ul>
                    <li><strong>Interpretato</strong> - Esecuzione tramite interprete</li>
                    <li><strong>Tipizzazione dinamica</strong> - Le variabili non hanno tipo fisso</li>
                    <li><strong>Multi-paradigma</strong> - Supporta OOP, funzionale e procedurale</li>
                </ul>
                
                <h4>📝 Esempio di Codice</h4>
                <pre class="code-example">
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrati_pari = [n**2 for n in numeri if n % 2 == 0]
print(f"Quadrati dei numeri pari: {quadrati_pari}")</pre>
            `
        },
        java: {
            title: "Linguaggio Java - Approfondimento Accademico",
            content: `
                <h4>📅 Contesto Storico</h4>
                <p>Java fu sviluppato da James Gosling alla Sun Microsystems, rilasciato nel 1995. Il motto è "Write Once, Run Anywhere".</p>
                
                <h4>⚙️ Caratteristiche Tecniche</h4>
                <ul>
                    <li><strong>JVM</strong> - Java Virtual Machine esegue il bytecode</li>
                    <li><strong>OOP puro</strong> - Tutto è un oggetto</li>
                    <li><strong>Garbage Collection</strong> - Gestione automatica della memoria</li>
                </ul>
                
                <h4>📝 Esempio di Codice</h4>
                <pre class="code-example">
public class Studente {
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

    // Contenuti dettagliati per i progetti
    const projectDetails = {
        flutter: {
            title: "AKnote - App per la gestione delle attività",
            content: `
                <h4>📱 Descrizione del Progetto</h4>
                <p>AKnote è un'applicazione mobile per la gestione delle note e delle attività quotidiane, sviluppata con Flutter e Dart.</p>
                <h4>🛠️ Tecnologie Utilizzate</h4>
                <ul><li>Flutter</li><li>Dart</li><li>Firebase</li><li>Provider</li></ul>
                <h4>✨ Funzionalità</h4>
                <ul><li>Registrazione e login</li><li>CRUD task</li><li>Sincronizzazione cloud</li></ul>
            `
        },
        recart: {
            title: "Task Gariboldi - Portale gestionale aziendale",
            content: `
                <h4>🏢 Descrizione del Progetto</h4>
                <p>Portale gestionale per azienda con dashboard interattiva, gestione task, clienti e dipendenti.</p>
                <h4>🛠️ Tecnologie</h4>
                <ul><li>JavaScript</li><li>Recart</li><li>Node.js</li><li>Firebase</li></ul>
                <h4>✨ Funzionalità</h4>
                <ul><li>Dashboard per ruoli</li><li>Export report PDF/Excel</li><li>Autenticazione</li></ul>
            `
        },
        website: {
            title: "Portfolio Creativo - Sito Web Professionale",
            content: `
                <h4>🌐 Descrizione del Progetto</h4>
                <p>Sito web responsive con animazioni CSS avanzate per presentare progetti e competenze.</p>
                <h4>🛠️ Tecnologie</h4>
                <ul><li>HTML5</li><li>CSS3</li><li>JavaScript</li></ul>
                <h4>✨ Caratteristiche</h4>
                <ul><li>Design responsive</li><li>Animazioni CSS</li><li>SEO ottimizzato</li></ul>
            `
        }
    };

    let modalOverlay = null;
    let modalContainer = null;

    function closeModal() {
        if (modalOverlay) modalOverlay.remove();
        if (modalContainer) modalContainer.remove();
        document.body.classList.remove('modal-open');
    }

    function openModal(title, content) {
        closeModal();
        modalOverlay = document.createElement('div');
        modalOverlay.className = 'modal-overlay';
        modalContainer = document.createElement('div');
        modalContainer.className = 'modal-container';
        modalContainer.innerHTML = `
            <div class="modal-header"><h3>${title}</h3><button class="modal-close">×</button></div>
            <div class="modal-body">${content}</div>
        `;
        document.body.appendChild(modalOverlay);
        document.body.appendChild(modalContainer);
        document.body.classList.add('modal-open');
        modalContainer.querySelector('.modal-close').addEventListener('click', closeModal);
        modalOverlay.addEventListener('click', closeModal);
        document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeModal(); });
    }

    // Click sulle card dei linguaggi
    document.querySelectorAll('.lang-card').forEach(card => {
        card.addEventListener('click', () => {
            const lang = card.getAttribute('data-lang');
            if (lang && languageDetails[lang]) openModal(languageDetails[lang].title, languageDetails[lang].content);
        });
    });

    // Click sulle card dei progetti
    document.querySelectorAll('.progetto-reale-card').forEach(card => {
        card.addEventListener('click', (e) => {
            if (e.target.closest('.btn-progetto')) return;
            const project = card.getAttribute('data-project');
            if (project && projectDetails[project]) openModal(projectDetails[project].title, projectDetails[project].content);
        });
    });

    // Navigazione mobile
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    if (hamburger) hamburger.addEventListener('click', () => navMenu.classList.toggle('active'));

    // Scroll navbar
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
    });

    // Contatori statistiche
    const stats = document.querySelectorAll('.stat-number');
    const animateNumbers = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.getAttribute('data-target'));
            if (!target) return;
            const rect = stat.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0 && !stat.classList.contains('counted')) {
                stat.classList.add('counted');
                let current = 0;
                const increment = target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) { stat.textContent = target.toLocaleString(); clearInterval(timer); }
                    else stat.textContent = Math.floor(current).toLocaleString();
                }, 30);
            }
        });
    };
    window.addEventListener('scroll', animateNumbers);
    animateNumbers();

    // Form supporto
    const form = document.getElementById('supportoForm');
    const successDiv = document.getElementById('formSuccess');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = 'Invio in corso...';
            submitBtn.disabled = true;
            try {
                const formData = new FormData(form);
                const response = await fetch(form.action, { method: 'POST', body: formData, headers: { 'Accept': 'application/json' } });
                if (response.ok) {
                    successDiv.style.display = 'block';
                    form.reset();
                    setTimeout(() => successDiv.style.display = 'none', 5000);
                } else throw new Error('Errore');
            } catch (error) { alert('Errore nell\'invio. Riprova più tardi.'); }
            finally { submitBtn.textContent = originalText; submitBtn.disabled = false; }
        });
    }

    // Smooth scroll
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target && this.getAttribute('href') !== '#') {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                if (navMenu && navMenu.classList.contains('active')) navMenu.classList.remove('active');
            }
        });
    });

    // Animazione barre statistiche
    const statBars = document.querySelectorAll('.stat-fill');
    const animateStatBars = () => {
        statBars.forEach(bar => {
            const rect = bar.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0 && !bar.classList.contains('animated')) {
                bar.classList.add('animated');
                const width = bar.style.width;
                bar.style.width = '0';
                setTimeout(() => bar.style.width = width, 100);
            }
        });
    };
    window.addEventListener('scroll', animateStatBars);
    animateStatBars();

    // Link attivo durante scroll
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    window.addEventListener('scroll', () => {
        let current = '';
        const scrollPosition = window.scrollY + 100;
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) current = section.getAttribute('id');
        });
        navLinks.forEach(link => {
            link.classList.remove('active');
            const href = link.getAttribute('href');
            if (href === `#${current}`) link.classList.add('active');
            else if (current === '' && href === '#home') link.classList.add('active');
        });
    });
})();

// ============================================
// CHATBOT AI - VERSIONE MIGLIORATA v3.0
// ============================================

(function() {
    const KNOWLEDGE_BASE = [
        { keywords: ["ciao", "salve", "buongiorno"], response: "👋 Ciao! Sono un assistente specializzato in linguaggi di programmazione. Digita 'aiuto' per tutti gli argomenti!" },
        { keywords: ["aiuto", "help", "cosa sai fare"], response: "📚 ARGOMENTI: Python, Java, C, C++, JavaScript, OOP, Compilato/Interpretato, Framework, API, Git, Frontend/Backend. Comandi: 'dimmi di più', 'cosa mi hai detto prima'" },
        { keywords: ["grazie"], response: "😊 Prego! Chiedimi pure altro!" },
        { keywords: ["linguaggio programmazione", "cos'è un linguaggio"], response: "💻 Un linguaggio di programmazione è un insieme di regole per scrivere istruzioni eseguibili da un computer. Esistono oltre 700 linguaggi!" },
        { keywords: ["differenza compilato interpretato"], response: "📊 Compilato (C, C++): più VELOCE. Interpretato (Python, JS): più FLESSIBILE." },
        { keywords: ["frontend", "backend"], response: "🌐 Frontend (HTML/CSS/JS): ciò che vedi. Backend (Python/Java): ciò che non vedi (server, database)." },
        { keywords: ["git", "github"], response: "📦 Git tiene traccia delle modifiche. GitHub è la piattaforma cloud per ospitare repository." },
        { keywords: ["quale linguaggio studiare", "primo linguaggio"], response: "🎓 Python è il più consigliato per iniziare! Sintassi semplice e tanti ambiti (AI, Dati, Web)." },
        { keywords: ["quanto tempo", "tempo per imparare"], response: "⏱️ Base: 2-3 mesi. Autonomia: 6-12 mesi. Lavorare: 1-2 anni. Esperto: 3-5+ anni." },
        { keywords: ["python"], response: "🐍 Python (1991, Guido van Rossum) - Interpretato, sintassi semplice. Usato per AI, Data Science, Web." },
        { keywords: ["java"], response: "☕ Java (1995, James Gosling) - OOP, 'Write Once Run Anywhere'. Usato per Enterprise, Android." },
        { keywords: ["c", "linguaggio c"], response: "⚡ C (1972, Dennis Ritchie) - Linguaggio procedurale, basso livello. Padre di tutti i linguaggi moderni." },
        { keywords: ["c++"], response: "➕ C++ (1985, Bjarne Stroustrup) - Estensione di C con OOP. Usato per videogiochi, browser." },
        { keywords: ["javascript", "js"], response: "🟨 JavaScript (1995, Brendan Eich) - Linguaggio del web. Frontend e backend con Node.js." },
        { keywords: ["oop", "orientato agli oggetti"], response: "🎯 OOP - 4 pilastri: Incapsulamento, Ereditarietà, Polimorfismo, Astrazione." },
        { keywords: ["framework", "libreria"], response: "📚 Libreria: TU controlli. Framework: controlla LUI (inversione del controllo)." },
        { keywords: ["api", "rest"], response: "🔌 API permettono comunicazione tra sistemi. REST usa HTTP (GET, POST, PUT, DELETE)." }
    ];

    const BLACKLIST = ["calcio", "sport", "politica", "film", "musica", "cucina", "ricetta", "meteo"];
    let ultimoArgomento = null;
    let storico = [];

    function normalizza(text) {
        return text.toLowerCase().replace(/[^\w\s]/g, ' ').replace(/\s+/g, ' ').trim();
    }

    function contieneNegazione(text) {
        return ["non è", "non e'", "non sia", "ma non"].some(neg => text.includes(neg));
    }

    function èPertinente(text) {
        if (["ciao", "salve", "aiuto", "grazie"].some(w => text.includes(w))) return true;
        if (BLACKLIST.some(b => text.includes(b))) return false;
        return ["linguaggio", "programmazione", "python", "java", "javascript", "c++", "oop", "api", "git"].some(k => text.includes(k));
    }

    function trovaRisposta(domanda) {
        const domandaNorm = normalizza(domanda);
        if (contieneNegazione(domandaNorm)) return "⚠️ Ho notato una negazione. Puoi riformulare?";
        if (!èPertinente(domandaNorm)) return "⚠️ Sono specializzato solo in linguaggi di programmazione. Prova con 'cos'è Python?' o 'aiuto'.";
        
        if (domandaNorm.includes("dimmi di più") && ultimoArgomento) return `📚 APPROFONDIMENTO\n\n${ultimoArgomento}`;
        if (domandaNorm.includes("cosa mi hai detto prima") && storico.length) return `📜 ULTIMA RISPOSTA:\n\n${storico[storico.length-1]}`;
        
        let bestScore = 0, bestResponse = null;
        for (const entry of KNOWLEDGE_BASE) {
            let score = entry.keywords.some(k => domandaNorm.includes(k)) ? 2 : 0;
            if (score > bestScore) { bestScore = score; bestResponse = entry.response; }
        }
        if (bestResponse) { ultimoArgomento = bestResponse; storico.push(bestResponse); if (storico.length > 5) storico.shift(); return bestResponse; }
        return "🤔 Non ho trovato risposta. Prova con 'cos'è Python?' o 'aiuto'.";
    }

    // UI Chatbot
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

    function rimuoviTyping() { document.getElementById('typing-indicator')?.remove(); }

    function inviaMessaggio() {
        const testo = inputEl.value.trim();
        if (!testo) return;
        aggiungiMessaggio(testo, 'user');
        inputEl.value = '';
        mostraTyping();
        setTimeout(() => {
            rimuoviTyping();
            aggiungiMessaggio(trovaRisposta(testo), 'bot');
        }, 600);
    }

    if (toggleBtn) toggleBtn.addEventListener('click', () => { windowEl.classList.remove('hidden'); toggleBtn.style.display = 'none'; setTimeout(() => inputEl.focus(), 100); });
    if (closeBtn) closeBtn.addEventListener('click', () => { windowEl.classList.add('hidden'); toggleBtn.style.display = 'flex'; });
    if (sendBtn) sendBtn.addEventListener('click', inviaMessaggio);
    if (inputEl) inputEl.addEventListener('keypress', (e) => { if (e.key === 'Enter') inviaMessaggio(); });
})();