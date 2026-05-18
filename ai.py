#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CHATBOT AI - Linguaggi di Programmazione
VERSIONE MIGLIORATA v2.0
- Gestione false positivi
- Memoria conversazione
- Rilevamento negazioni
- Logging integrato
- Knowledge base estesa
"""

import re
import nltk
import logging
from difflib import SequenceMatcher
from datetime import datetime
from nltk.stem.snowball import SnowballStemmer

# ============================================
# CONFIGURAZIONE LOGGING
# ============================================

logging.basicConfig(
    filename=f'chatbot_log_{datetime.now().strftime("%Y%m%d")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ============================================
# CONFIGURAZIONE INIZIALE NLTK
# ============================================

def setup_nltk():
    """Scarica le risorse NLTK necessarie una sola volta"""
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('stemmers/snowball_data')
    except LookupError:
        nltk.download('snowball_data', quiet=True)
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

setup_nltk()

# Inizializza lo stemmer italiano
stemmer = SnowballStemmer("italian")

# ============================================
# KNOWLEDGE BASE ESTESA (VERSIONE MIGLIORATA)
# ============================================

KNOWLEDGE_BASE = {
    # ========== SALUTI E AIUTO ==========
    "ciao salve buongiorno buonasera": (
        "👋 Ciao! Sono un assistente specializzato in **linguaggi di programmazione**.\n\n"
        "Posso aiutarti con:\n"
        "• Domande su Python, Java, C/C++, JavaScript, Rust\n"
        "• Spiegazioni su paradigmi e concetti OOP\n"
        "• Differenze tra linguaggi compilati e interpretati\n"
        "• Consigli su quale linguaggio studiare\n"
        "• Frontend vs Backend, Git, API\n\n"
        "Digita `aiuto` per vedere tutti gli argomenti disponibili!"
    ),
    
    "aiuto help cosa sai fare argomenti comandi": (
        "📚 **ARGOMENTI DISPONIBILI**\n\n"
        "**🔹 DEFINIZIONI FONDAMENTALI**\n"
        "• Cos'è un linguaggio di programmazione\n"
        "• Paradigmi di programmazione (OOP, funzionale, ecc.)\n"
        "• Differenza tra compilato e interpretato\n"
        "• Differenza tra frontend e backend\n\n"
        "**🔹 LINGUAGGI SPECIFICI**\n"
        "• Python - caratteristiche, usi, esempi\n"
        "• Java - JVM, portabilità, applicazioni\n"
        "• C e C++ - differenze, performance\n"
        "• JavaScript - frontend/backend\n"
        "• Rust - sicurezza e performance\n\n"
        "**🔹 CONCETTI GENERALI**\n"
        "• OOP (incapsulamento, ereditarietà, polimorfismo)\n"
        "• Variabili e tipi di dato\n"
        "• Framework vs Librerie\n"
        "• API REST\n"
        "• Git e GitHub\n"
        "• Debugging e IDE\n"
        "• Algoritmi e Database\n\n"
        "**🔹 CONSIGLI**\n"
        "• Quale linguaggio studiare per primo\n"
        "• Quanto tempo serve per imparare\n"
        "• Come evitare errori comuni\n\n"
        "**🔹 COMANDI SPECIALI**\n"
        "• `dimmi di più` - approfondisce l'ultimo argomento\n"
        "• `cosa mi hai detto prima` - mostra ultima risposta\n"
        "• `inoltre` - continua sul tema precedente\n"
        "• `esci` - termina la conversazione\n\n"
        "💡 *Fammi una domanda specifica per ottenere una risposta dettagliata!*"
    ),
    
    "grazie thank grazie mille ti ringrazio": (
        "😊 Prego! Sono felice di essere stato d'aiuto.\n\n"
        "Se hai altre domande sui linguaggi di programmazione, sono sempre qui per te!\n"
        "Puoi chiedermi anche di approfondire l'ultimo argomento con `dimmi di più`."
    ),
    
    # ========== DEFINIZIONI FONDAMENTALI ==========
    
    "cos'è un linguaggio di programmazione definizione linguaggio programmazione": (
        "💻 **COS'È UN LINGUAGGIO DI PROGRAMMAZIONE**\n\n"
        "Un **linguaggio di programmazione** è un insieme formale di regole sintattiche e semantiche\n"
        "che permette di scrivere istruzioni eseguibili da un computer.\n\n"
        "**📊 CLASSIFICAZIONE PRINCIPALE:**\n\n"
        "┌─────────────────┬──────────────────┬──────────────────┐\n"
        "│                 │   COMPILATI      │   INTERPRETATI   │\n"
        "├─────────────────┼──────────────────┼──────────────────┤\n"
        "│ Esempi          │ C, C++, Rust     │ Python, JS, Ruby │\n"
        "├─────────────────┼──────────────────┼──────────────────┤\n"
        "│ Vantaggi        │ Più veloci       │ Più flessibili   │\n"
        "├─────────────────┼──────────────────┼──────────────────┤\n"
        "│ Svantaggi       │ Richiedono       │ Più lenti        │\n"
        "│                 │ compilazione     │                  │\n"
        "└─────────────────┴──────────────────┴──────────────────┘\n\n"
        "📝 **ESEMPIO PRATICO (Python):**\n"
        "```python\n"
        "nome = \"Mario\"\n"
        "print(f\"Ciao, {nome}!\")\n"
        "```\n\n"
        "🌍 *Esistono oltre 700 linguaggi di programmazione nel mondo!*"
    ),
    
    "paradigma programmazione tipi paradigmi stili programmazione": (
        "🎯 **PARADIGMI DI PROGRAMMAZIONE**\n\n"
        "I paradigmi rappresentano diversi **stili** o **filosofie** di scrittura del codice.\n\n"
        "**🔹 PRINCIPALI PARADIGMI:**\n\n"
        "1. **IMPERATIVO** - Sequenza di comandi che modificano lo stato\n"
        "   📌 Esempi: C, Pascal, Fortran\n\n"
        "2. **ORIENTATO AGLI OGGETTI (OOP)** - Organizzazione in classi e oggetti\n"
        "   📌 Esempi: Java, C++, Python, C#\n\n"
        "3. **FUNZIONALE** - Basato su funzioni pure e immutabilità\n"
        "   📌 Esempi: Haskell, Lisp, Scala, Elixir\n\n"
        "4. **LOGICO** - Definizione di regole e fatti\n"
        "   📌 Esempi: Prolog, Datalog\n\n"
        "5. **DICHIARATIVO** - Descrive il risultato, non i passi\n"
        "   📌 Esempi: SQL, HTML\n\n"
        "💡 *I linguaggi moderni sono spesso **multi-paradigma**!*"
    ),
    
    "differenza compilato interpretato compilazione vs interpretazione confronto": (
        "📊 **CONFRONTO: COMPILATO vs INTERPRETATO**\n\n"
        "┌────────────────────┬─────────────────────┬─────────────────────┐\n"
        "│    CARATTERISTICA  │     COMPILATO       │     INTERPRETATO    │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Traduzione         │ Prima dell'esecuzione│ Durante esecuzione │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Velocità           │ ⚡⚡⚡ MOLTO VELOCE   │ 🐢 ABBASTANZA LENTO │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Output             │ File eseguibile    │ Nessun file         │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Portabilità        │ Richiede           │ Qualsiasi           │\n"
        "│                    │ ricompilazione     │ piattaforma         │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Debugging          │ Più difficile      │ Interattivo         │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Rilevamento errori │ A compile-time     │ A runtime           │\n"
        "└────────────────────┴─────────────────────┴─────────────────────┘\n\n"
        "**💡 CASO PARTICOLARE: JAVA**\n"
        "Java è **ibrido**: compila in bytecode, poi JVM interpreta/esegue."
    ),
    
    "differenza frontend backend front-end back-end": (
        "🌐 **FRONTEND vs BACKEND - Differenze fondamentali**\n\n"
        "┌────────────────────┬─────────────────────┬─────────────────────┐\n"
        "│                    │     FRONTEND        │      BACKEND        │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Cosa fa            │ Ciò che vedi        │ Ciò che non vedi    │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Tecnologie         │ HTML, CSS, JS       │ Python, Java, PHP   │\n"
        "│                    │ React, Vue, Angular │ Node.js, Django     │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Dove gira          │ Nel browser         │ Sul server          │\n"
        "├────────────────────┼─────────────────────┼─────────────────────┤\n"
        "│ Compiti            │ UI, animazioni      │ Database, API       │\n"
        "│                    │ interazione utente  │ logica, autenticaz. │\n"
        "└────────────────────┴─────────────────────┴─────────────────────┘\n\n"
        "**💡 FULL-STACK** = Sviluppatore che sa fare entrambi!\n"
        "📌 *Il frontend si occupa dell'esperienza utente, il backend della logica e dei dati.*"
    ),
    
    "git github cos'è git a cosa serve github": (
        "📦 **GIT e GITHUB - Il controllo versione**\n\n"
        "**GIT** (strumento locale)\n"
        "• Tiene traccia di OGNI modifica al codice\n"
        "• Permette di tornare indietro nel tempo\n"
        "• Facilita il lavoro in team senza conflitti\n"
        "• Creato da Linus Torvalds (stesso di Linux)\n\n"
        "**COMANDI GIT FONDAMENTALI:**\n"
        "```bash\n"
        "git init          # Inizia un repository\n"
        "git add .         # Aggiunge modifiche\n"
        "git commit -m \"msg\" # Salva una versione\n"
        "git push          # Carica su GitHub\n"
        "git pull          # Scarica aggiornamenti\n"
        "```\n\n"
        "**GITHUB** (piattaforma cloud)\n"
        "• Dove si OSPITANO i repository Git\n"
        "• Social network per programmatori\n"
        "• Portfolio dei tuoi progetti\n"
        "• Alternativa: GitLab, Bitbucket\n\n"
        "💡 *Git è OBBLIGATORIO per lavorare in team!*"
    ),
    
    # ========== CONSIGLI E TEMPI ==========
    
    "quale linguaggio studiare primo linguaggio per iniziare linguaggio più facile": (
        "🎓 **QUAL È IL MIGLIOR LINGUAGGIO PER INIZIARE?**\n\n"
        "**La risposta dipende dai tuoi obiettivi!**\n\n"
        "1️⃣ **PYTHON** - Consigliato al 90% dei principianti\n"
        "   • ✅ Sintassi leggibile come l'inglese\n"
        "   • ✅ Nessuna gestione complicata della memoria\n"
        "   • ✅ Risultati immediati\n"
        "   • 🎯 Per: AI, Dati, Automazione, Web\n\n"
        "2️⃣ **JAVASCRIPT** - Se vuoi fare siti web SUBITO\n"
        "   • ✅ Vedi risultati nel browser\n"
        "   • ✅ Puoi fare frontend E backend (Node.js)\n"
        "   • 🎯 Per: Siti web, app, giochi\n\n"
        "3️⃣ **SCRATCH** - Se sei completamente nuovo (<14 anni)\n"
        "   • ✅ Programmazione a blocchi visuale\n"
        "   • ✅ Impara i concetti senza sintassi\n\n"
        "4️⃣ **C** - Se vuoi capire COME funziona il computer\n"
        "   • ✅ Capisci memoria e puntatori\n"
        "   • ⚠️ Curva di apprendimento ripida\n"
        "   • 🎯 Per: Sistemi operativi, embedded\n\n"
        "💡 *Il mio consiglio: inizia con PYTHON, non te ne pentirai!*"
    ),
    
    "quanto tempo per imparare a programmare tempi apprendimento": (
        "⏱️ **QUANTO TEMPO SERVE PER IMPARARE A PROGRAMMARE?**\n\n"
        "**Le tempistiche realistiche (studiando 5-10 ore/settimana):**\n\n"
        "📌 **BASE (2-3 mesi)**\n"
        "• Variabili, cicli, condizioni, funzioni\n"
        "• Riuscirai a leggere e scrivere programmi semplici\n\n"
        "📌 **AUTONOMIA (6-12 mesi)**\n"
        "• Costruire progetti semplici da solo\n"
        "• Capire e usare la documentazione\n"
        "• Risolvere bug in autonomia\n\n"
        "📌 **PRONTO PER LAVORARE (1-2 anni)**\n"
        "• Conoscere framework e librerie\n"
        "• Lavorare con database e API\n"
        "• Collaborare in team con Git\n\n"
        "📌 **ESPERTO (3-5+ anni)**\n"
        "• Architetture software complesse\n"
        "• Ottimizzazione performance e sicurezza\n"
        "• Insegnare ad altri\n\n"
        "💡 *La programmazione è un mestiere in cui si impara SEMPRE!*\n"
        "• I migliori programmatori studiano anche 1-2 ore al giorno."
    ),
    
    "errori comuni principianti come evitare errori": (
        "⚠️ **ERRORI COMUNI DEI PRINCIPIANTI (E COME EVITARLI)**\n\n"
        "**1. NON LEGGERE GLI ERRORI**\n"
        "• ❌ Ignorare i messaggi di errore\n"
        "• ✅ Leggi SEMPRE l'errore, ti dice COSA e DOVE\n\n"
        "**2. CODICE NON COMMENTATO**\n"
        "• ❌ \"Tanto lo capisco io\"\n"
        "• ✅ Commenta spiegando il PERCHÉ, non il COSA\n\n"
        "**3. VARIABILI CON NOMI INSENSATI**\n"
        "• ❌ `a`, `b`, `x1`, `temp`\n"
        "• ✅ `numero_utenti`, `prezzo_totale`, `lista_studenti`\n\n"
        "**4. COPY/PASTE SENZA CAPIRE**\n"
        "• ❌ Copiare codice da Stack Overflow senza capirlo\n"
        "• ✅ Riscrivilo a mano, modificalo, sperimenta\n\n"
        "**5. NON USARE IL CONTROLLO VERSIONE**\n"
        "• ❌ Salvare file come `finale_v3_copia2.py`\n"
        "• ✅ Impara GIT, ti salverà la vita\n\n"
        "**6. VOLER IMPARARE TUTTO IN UNA VOLTA**\n"
        "• ❌ Studiare 10 linguaggi contemporaneamente\n"
        "• ✅ Impara BENE un linguaggio, gli altri dopo\n\n"
        "💡 *Sbagliare è NORMALE. Anche i professionisti sbagliano ogni giorno!*"
    ),
    
    # ========== LINGUAGGI SPECIFICI ==========
    
    "python cos'è python caratteristiche python": (
        "🐍 **PYTHON - Il linguaggio più amato**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **Guido van Rossum** nel 1991\n"
        "• Nome ispirato ai Monty Python\n\n"
        "**⚙️ CARATTERISTICHE**\n"
        "• Interpretato, tipizzazione dinamica\n"
        "• Sintassi basata sull'indentazione\n"
        "• Multi-paradigma (OOP, funzionale)\n"
        "• Vasta libreria standard\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🤖 **AI** - TensorFlow, PyTorch\n"
        "• 📊 **Data Science** - Pandas, NumPy\n"
        "• 🌐 **Web** - Django, Flask\n"
        "• 🔧 **Automazione** - Selenium, Scrapy\n\n"
        "**📝 ESEMPIO:**\n"
        "```python\n"
        "numeri = [1, 2, 3, 4, 5]\n"
        "pari_quadrati = [n**2 for n in numeri if n%2==0]\n"
        "print(pari_quadrati)  # [4, 16]\n"
        "```\n\n"
        "💡 *Perfetto per principianti e professionisti!*"
    ),
    
    "java cos'è java caratteristiche java": (
        "☕ **JAVA - Write Once, Run Anywhere**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **James Gosling** (Sun) nel 1995\n"
        "• Ora di proprietà Oracle\n\n"
        "**⚙️ CARATTERISTICHE**\n"
        "• OOP puro, compilato in bytecode\n"
        "• Eseguito su JVM (Java Virtual Machine)\n"
        "• Garbage collection automatica\n"
        "• Multi-threading nativo\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🏢 **Enterprise** - banche, assicurazioni\n"
        "• 📱 **Android** - sviluppo nativo\n"
        "• 📊 **Big Data** - Hadoop, Spark\n"
        "• 🌐 **Web** - Spring Framework\n\n"
        "**📝 ESEMPIO:**\n"
        "```java\n"
        "public class Main {\n"
        "    public static void main(String[] args) {\n"
        "        System.out.println(\"Ciao Mondo!\");\n"
        "    }\n"
        "}\n"
        "```\n\n"
        "💡 *Standard per applicazioni enterprise critiche!*"
    ),
    
    "c linguaggio c caratteristiche c": (
        "⚡ **LINGUAGGIO C - Il padre di tutti**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **Dennis Ritchie** (Bell Labs) nel 1972\n"
        "• Sviluppato per scrivere UNIX\n\n"
        "**⚙️ CARATTERISTICHE**\n"
        "• Linguaggio procedurale\n"
        "• Basso livello, controllo totale\n"
        "• Gestione MANUALE della memoria\n"
        "• Utilizzo di puntatori\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🐧 **Sistemi Operativi** - Linux, Windows\n"
        "• 📦 **Database** - MySQL, PostgreSQL\n"
        "• 🔌 **Embedded** - microcontrollori\n"
        "• 🔐 **Crittografia** - OpenSSL\n\n"
        "**📝 ESEMPIO:**\n"
        "```c\n"
        "#include <stdio.h>\n"
        "int main() {\n"
        "    printf(\"Ciao Mondo!\\n\");\n"
        "    return 0;\n"
        "}\n"
        "```\n\n"
        "💡 *Se capisci C, capisci come funziona un computer!*"
    ),
    
    "c++ differenza c c++ caratteristiche c++": (
        "➕ **C++ - L'evoluzione potente di C**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **Bjarne Stroustrup** nel 1985\n"
        "• Standard C++11, C++14, C++17, C++20\n\n"
        "**DIFFERENZE PRINCIPALI DA C:**\n"
        "┌─────────────────┬──────────────┬──────────────┐\n"
        "│ Caratteristica  │      C       │     C++      │\n"
        "├─────────────────┼──────────────┼──────────────┤\n"
        "│ Paradigma       │ Procedurale  │ Multi-parad. │\n"
        "├─────────────────┼──────────────┼──────────────┤\n"
        "│ OOP             │ ❌ No        │ ✅ Sì        │\n"
        "├─────────────────┼──────────────┼──────────────┤\n"
        "│ Template        │ ❌ No        │ ✅ Sì        │\n"
        "├─────────────────┼──────────────┼──────────────┤\n"
        "│ STL             │ ❌ No        │ ✅ Sì        │\n"
        "└─────────────────┴──────────────┴──────────────┘\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🎮 **Game Development** - Unreal Engine\n"
        "• 🌐 **Browser** - Chrome, Firefox\n"
        "• 💻 **Software** - Photoshop, Office\n"
        "• 🚗 **Automotive** - sistemi critici\n\n"
        "💡 *C++ per performance massime!*"
    ),
    
    "javascript js cos'è javascript": (
        "🟨 **JAVASCRIPT - Il linguaggio del web**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **Brendan Eich** in 10 giorni (1995)\n"
        "• Standard ECMAScript (ES6, ES2023...)\n\n"
        "**⚙️ CARATTERISTICHE**\n"
        "• Interpretato, debolmente tipizzato\n"
        "• Basato su prototipi\n"
        "• Programmazione asincrona\n"
        "• Event-driven\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🌐 **Frontend** - React, Vue, Angular\n"
        "• 🖥️ **Backend** - Node.js, Deno\n"
        "• 📱 **Mobile** - React Native\n"
        "• 💻 **Desktop** - Electron (VS Code, Discord)\n\n"
        "**📝 ESEMPIO:**\n"
        "```javascript\n"
        "const numeri = [1, 2, 3, 4, 5];\n"
        "const pari = numeri.filter(n => n % 2 === 0);\n"
        "console.log(pari); // [2, 4]\n"
        "```\n\n"
        "⚠️ *JavaScript NON è Java!*\n"
        "💡 *Il linguaggio più diffuso al mondo!*"
    ),
    
    "rust caratteristiche rust linguaggio rust": (
        "🦀 **RUST - Il futuro della programmazione**\n\n"
        "**📅 STORIA**\n"
        "• Creato da **Graydon Hoare** (Mozilla) nel 2010\n"
        "• Linguaggio più amato su SO per 8 anni\n\n"
        "**⚙️ CARATTERISTICHE**\n"
        "• Compilato, performance C/C++\n"
        "• Sicurezza memoria SENZA garbage collector\n"
        "• Sistema ownership/borrowing\n"
        "• Previene data race a compile-time\n\n"
        "**🎯 AMBITI DI UTILIZZO**\n"
        "• 🔧 **System Programming**\n"
        "• ⛓️ **Blockchain** - Solana, Polkadot\n"
        "• 🌐 **WebAssembly**\n"
        "• 🛠️ **Tooling** - ripgrep, fd\n\n"
        "**📝 ESEMPIO:**\n"
        "```rust\n"
        "fn main() {\n"
        "    let numeri = vec![1, 2, 3, 4, 5];\n"
        "    let pari: Vec<_> = numeri.iter()\n"
        "        .filter(|&&x| x % 2 == 0)\n"
        "        .collect();\n"
        "    println!(\"{:?}\", pari);\n"
        "}\n"
        "```\n\n"
        "💡 *Adottato da Microsoft, Google, Amazon!*"
    ),
    
    "oop programmazione orientata oggetti principi oop": (
        "🎯 **PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)**\n\n"
        "**I 4 PRINCIPI FONDAMENTALI:**\n\n"
        "1. **INCAPSULAMENTO**\n"
        "   • Nascondere i dettagli interni\n"
        "   • Protegge l'integrità dei dati\n\n"
        "2. **EREDITARIETÀ**\n"
        "   • Una classe eredita da un'altra\n"
        "   • Riutilizzo del codice\n\n"
        "3. **POLIMORFISMO**\n"
        "   • Stesso metodo, comportamenti diversi\n"
        "   • Dipende dall'oggetto a runtime\n\n"
        "4. **ASTRAZIONE**\n"
        "   • Rappresentare concetti complessi\n"
        "   • Nasconde la complessità\n\n"
        "**📝 ESEMPIO (Python):**\n"
        "```python\n"
        "class Animale:\n"
        "    def verso(self): pass\n"
        "\n"
        "class Cane(Animale):\n"
        "    def verso(self): return \"Bau!\"\n"
        "\n"
        "class Gatto(Animale):\n"
        "    def verso(self): return \"Miao!\"\n"
        "```\n\n"
        "💡 *Linguaggi OOP: Java, C++, Python, C#*"
    ),
    
    "framework libreria differenza framework vs libreria": (
        "📚 **FRAMEWORK vs LIBRERIA**\n\n"
        "┌────────────────────┬──────────────────┬──────────────────┐\n"
        "│    ASPETTO         │    LIBRERIA      │    FRAMEWORK     │\n"
        "├────────────────────┼──────────────────┼──────────────────┤\n"
        "│ Chi controlla?     │ TU controlli     │ Framework        │\n"
        "│                    │                  │ controlla        │\n"
        "├────────────────────┼──────────────────┼──────────────────┤\n"
        "│ Chi chiama chi?    │ Tu → Libreria    │ Framework → Tu   │\n"
        "├────────────────────┼──────────────────┼──────────────────┤\n"
        "│ Flessibilità       │ Alta             │ Limitata         │\n"
        "├────────────────────┼──────────────────┼──────────────────┤\n"
        "│ Esempi             │ React, NumPy     │ Angular, Django  │\n"
        "└────────────────────┴──────────────────┴──────────────────┘\n\n"
        "**REGOLA PRATICA:**\n"
        "• Libreria: sei tu al comando\n"
        "• Framework: sei 'ospite' nella sua architettura\n\n"
        "💡 *Con le librerie hai libertà, con i framework hai struttura*"
    ),
    
    "api rest api cosa sono api": (
        "🔌 **API (Application Programming Interface)**\n\n"
        "Un'API permette a sistemi software diversi di comunicare.\n\n"
        "**📋 METODI HTTP (CRUD):**\n\n"
        "┌──────────┬─────────────┬──────────────────────────┐\n"
        "│ METODO   │ OPERAZIONE  │ ESEMPIO                  │\n"
        "├──────────┼─────────────┼──────────────────────────┤\n"
        "│ GET      │ Lettura     │ GET /api/studenti/123    │\n"
        "├──────────┼─────────────┼──────────────────────────┤\n"
        "│ POST     │ Creazione   │ POST /api/studenti       │\n"
        "├──────────┼─────────────┼──────────────────────────┤\n"
        "│ PUT      │ Aggiornamento │ PUT /api/studenti/123   │\n"
        "├──────────┼─────────────┼──────────────────────────┤\n"
        "│ DELETE   │ Eliminazione │ DELETE /api/studenti/123│\n"
        "└──────────┴─────────────┴──────────────────────────┘\n\n"
        "**🌍 ESEMPI FAMOSI:**\n"
        "• Google Maps API, Stripe API, Twitter API\n\n"
        "💡 *Le API sono il 'collante' del software moderno!*"
    ),
    
    "variabile tipi dato variabili programmazione": (
        "📦 **VARIABILI E TIPI DI DATO**\n\n"
        "**TIPI DI DATO FONDAMENTALI:**\n\n"
        "┌─────────────┬──────────────┬─────────────────────────┐\n"
        "│ TIPO        │ ESEMPIO      │ DESCRIZIONE              │\n"
        "├─────────────┼──────────────┼─────────────────────────┤\n"
        "│ Interi      │ 42, -10, 0   │ Numeri senza decimali    │\n"
        "├─────────────┼──────────────┼─────────────────────────┤\n"
        "│ Float       │ 3.14, -2.5   │ Numeri con decimali      │\n"
        "├─────────────┼──────────────┼─────────────────────────┤\n"
        "│ Stringhe    │ \"Ciao\", 'A'  │ Testo                    │\n"
        "├─────────────┼──────────────┼─────────────────────────┤\n"
        "│ Booleani    │ True/False   │ Vero/Falso               │\n"
        "├─────────────┼──────────────┼─────────────────────────┤\n"
        "│ Liste/Array │ [1,2,3]      │ Collezioni ordinate      │\n"
        "└─────────────┴──────────────┴─────────────────────────┘\n\n"
        "**TIPIZZAZIONE:**\n"
        "• **Statica** (C, Java): tipo dichiarato, non cambia\n"
        "• **Dinamica** (Python, JS): tipo determinato a runtime\n\n"
        "💡 *La scelta dipende da flessibilità vs sicurezza*"
    ),
}

# ============================================
# FUNZIONI DI UTILITÀ (MIGLIORATE)
# ============================================

def normalizza_testo(testo):
    """Normalizza il testo: lowercase, rimuove punteggiatura, stemming."""
    testo = testo.lower().strip()
    testo = re.sub(r'[^\w\sàèéìòù]', ' ', testo)
    testo = re.sub(r'\s+', ' ', testo)
    
    parole = testo.split()
    parole_stemmate = [stemmer.stem(parola) for parola in parole]
    
    return " ".join(parole_stemmate)


def similarità_testuale(a, b):
    """Calcola la similarità tra due stringhe."""
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def contiene_negazione(testo):
    """Rileva se la domanda contiene una negazione"""
    negazioni = ["non è", "non e'", "non sia", "ma non", "non un", 
                 "non una", "non lo", "non viene", "sbaglio", 
                 "non penso", "non credo"]
    for neg in negazioni:
        if neg in testo:
            return True
    return False


def è_argomento_pertinente(domanda_normalizzata, punteggio_match=0):
    """Verifica se la domanda è pertinente (VERSIONE MIGLIORATA)"""
    
    # 1. Se il punteggio di match è troppo basso, rifiuta
    if punteggio_match < 0.25:
        return False
    
    # 2. Domande di aiuto/saluto sono sempre pertinenti
    parole_aiuto = ["ciao", "salve", "buongiorno", "aiut", "help", "grazie"]
    for parola in parole_aiuto:
        if parola in domanda_normalizzata:
            return True
    
    # 3. Lista nera di domande da NON rispondere
    domande_blacklist = [
        "calcio", "sport", "politica", "film", "musica", "cucina",
        "ricetta", "viaggio", "vacanza", "moda", "attualità",
        "tempo meteo", "che tempo fa"
    ]
    
    for black in domande_blacklist:
        if black in domanda_normalizzata:
            return False
    
    # 4. Verifica parole tecniche
    parole_tecniche = [
        "linguagg", "programm", "python", "java", "javascript", 
        "c++", "rust", "oop", "api", "database", "variabil",
        "sintass", "paradigm", "compil", "interpret", "algoritm",
        "framework", "libreri", "frontend", "backend", "git", "github",
        "errore", "tempo", "impar", "studia"
    ]
    
    parole_utente = domanda_normalizzata.split()
    conteggio_tecniche = sum(1 for p in parole_utente if p in parole_tecniche)
    
    return conteggio_tecniche >= 1


def trova_miglior_risposta(domanda_normalizzata):
    """Trova la risposta migliore (VERSIONE MIGLIORATA)"""
    miglior_punteggio = 0
    miglior_risposta = None
    chiave_trovata = None
    
    domanda_parole = set(domanda_normalizzata.split())
    
    for chiave, risposta in KNOWLEDGE_BASE.items():
        chiave_stemmata = normalizza_testo(chiave)
        chiave_parole = set(chiave_stemmata.split())
        
        # Calcolo punteggio
        parole_comuni = domanda_parole & chiave_parole
        punteggio_parole = len(parole_comuni) / max(len(chiave_parole), 1)
        punteggio_globale = similarità_testuale(domanda_normalizzata, chiave_stemmata)
        
        # Bonus per match esatto di parole chiave importanti
        parole_importanti = ["python", "java", "javascript", "c++", "rust", "oop", "api"]
        bonus = 0
        for p in parole_importanti:
            if p in domanda_normalizzata and p in chiave_stemmata:
                bonus += 0.2
        
        punteggio = punteggio_parole * 0.6 + punteggio_globale * 0.4 + bonus
        
        if punteggio > miglior_punteggio:
            miglior_punteggio = punteggio
            miglior_risposta = risposta
            chiave_trovata = chiave
    
    # Soglia per considerare valida
    if miglior_punteggio >= 0.2:
        return miglior_risposta, chiave_trovata, miglior_punteggio
    
    return None, None, 0


# ============================================
# CLASSE CHATBOT (VERSIONE MIGLIORATA)
# ============================================

class ChatbotProgrammazione:
    """Chatbot specializzato con memoria e contesto"""
    
    def __init__(self):
        self.ultimo_argomento = None
        self.ultima_risposta = None
        self.storico = []
        self.storico_max = 10  # Massimo di messaggi da ricordare
    
    def rispondi(self, domanda_utente):
        """Processa la domanda e restituisce risposta (VERSIONE MIGLIORATA)"""
        
        if not domanda_utente or not domanda_utente.strip():
            return "🙂 Per favore, scrivi una domanda."
        
        domanda_originale = domanda_utente
        domanda_normalizzata = normalizza_testo(domanda_utente)
        
        # Log della domanda
        logging.info(f"DOMANDA: {domanda_originale}")
        logging.info(f"NORMALIZZATA: {domanda_normalizzata}")
        
        # ===== COMANDI SPECIALI =====
        
        # Comando per uscire
        if domanda_normalizzata in ["esci", "exit", "quit", "fine"]:
            logging.info("COMANDO: EXIT")
            return "EXIT"
        
        # Comando per aiuto
        if domanda_utente in ["?", "help", "aiuto", "comandi"]:
            return KNOWLEDGE_BASE["aiuto help cosa sai fare argomenti"]
        
        # Comando per vedere ultima risposta
        if any(word in domanda_normalizzata for word in ["cosa mi hai detto prima", "ultima risposta", "cosa hai detto"]):
            if self.storico:
                ultima = self.storico[-1]
                return f"📜 **ULTIMA CONVERSAZIONE:**\n\nTu chiedesti: '{ultima[0]}'\n\nIo risposi:\n{ultima[1][:400]}..."
            else:
                return "Non abbiamo ancora parlato. Fammi una domanda!"
        
        # Comando per continuare sul tema precedente
        if any(word in domanda_normalizzata for word in ["inoltre", "poi", "dopo", "anche", "continua"]):
            if self.ultimo_argomento and self.ultimo_argomento in KNOWLEDGE_BASE:
                return f"📚 **CONTINUANDO SUL TEMA '{self.ultimo_argomento[:30]}...'**\n\n{KNOWLEDGE_BASE[self.ultimo_argomento]}"
            else:
                return "Non ho un tema precedente da approfondire. Fammi una nuova domanda!"
        
        # Comando di approfondimento
        if domanda_normalizzata in ["dimmi di più", "approfondisci", "approfondimento"]:
            if self.ultimo_argomento and self.ultimo_argomento in KNOWLEDGE_BASE:
                return f"📚 **APPROFONDIMENTO**\n\n{KNOWLEDGE_BASE[self.ultimo_argomento]}"
            else:
                return "Non ho un argomento precedente da approfondire."
        
        # ===== RILEVAMENTO NEGAZIONI =====
        if contiene_negazione(domanda_normalizzata):
            logging.warning(f"NEGAZIONE RILEVATA in: {domanda_originale}")
            return (
                "⚠️ **ATTENZIONE**\n\n"
                "Ho notato una possibile negazione o dubbio nella tua domanda.\n\n"
                "Potresti riformulare in modo più chiaro? Ad esempio:\n"
                "• 'Cos'è Python?' invece di 'Python non è un linguaggio?'\n"
                "• 'Qual è la differenza tra C e C++?'\n\n"
                "Oppure, se il dubbio era un'altra cosa, riscrivimi pure la domanda!"
            )
        
        # ===== CERCA RISPOSTA =====
        risposta, chiave, punteggio = trova_miglior_risposta(domanda_normalizzata)
        
        # ===== VERIFICA PERTINENZA =====
        if not è_argomento_pertinente(domanda_normalizzata, punteggio):
            logging.info(f"DOMANDA NON PERTINENTE - Punteggio: {punteggio}")
            return (
                "⚠️ **DOMANDA NON PERTINENTE**\n\n"
                "Sono specializzato solo in **linguaggi di programmazione**.\n\n"
                "📌 **Posso parlare di:**\n"
                "• Python, Java, C/C++, JavaScript, Rust\n"
                "• Paradigmi di programmazione (OOP, funzionale)\n"
                "• Sintassi, variabili, tipi di dato\n"
                "• Framework vs librerie, API, database\n"
                "• Frontend vs Backend, Git, GitHub\n"
                "• Tempi e consigli per imparare\n\n"
                "💡 *Prova con: 'cos'è Python?', 'differenza C e C++', o 'quale linguaggio studiare'*\n"
                "📖 *Digita 'aiuto' per vedere tutti gli argomenti*"
            )
        
        # ===== RESTITUISCI RISPOSTA =====
        if risposta:
            # Salva nello storico
            self.ultimo_argomento = chiave
            self.ultima_risposta = risposta
            self.storico.append((domanda_originale, risposta))
            
            # Mantieni storico limitato
            if len(self.storico) > self.storico_max:
                self.storico.pop(0)
            
            logging.info(f"RISPOSTA TROVATA: {chiave[:50] if chiave else 'N/A'} - Punteggio: {punteggio:.2f}")
            return risposta
        else:
            logging.warning(f"RISPOSTA NON TROVATA - Punteggio: {punteggio}")
            return (
                "🤔 **NON HO TROVATO UNA RISPOSTA PRECISA**\n\n"
                "Puoi provare a chiedermi:\n"
                "• 'cos'è un linguaggio di programmazione?'\n"
                "• 'che cos'è Python?'\n"
                "• 'differenza tra C e C++'\n"
                "• 'cosa significa OOP?'\n"
                "• 'quale linguaggio studiare per primo?'\n"
                "• 'quanto tempo serve per imparare?'\n\n"
                "📖 *Oppure digita 'aiuto' per vedere TUTTI gli argomenti disponibili.*"
            )


# ============================================
# FUNZIONE MAIN
# ============================================

def main():
    """Funzione principale per eseguire il chatbot"""
    print("=" * 70)
    print("🤖 CHATBOT - LINGUAGGI DI PROGRAMMAZIONE v2.0".center(70))
    print("=" * 70)
    print("\n📚 Sono un assistente specializzato in domande sui linguaggi di programmazione.")
    print("💡 Digitare 'aiuto' per vedere tutti gli argomenti disponibili.")
    print("🚪 Digitare 'esci' per terminare la conversazione.\n")
    print("-" * 70)
    
    chatbot = ChatbotProgrammazione()
    
    while True:
        try:
            domanda = input("\n🧑 Tu: ").strip()
            
            if not domanda:
                continue
            
            risposta = chatbot.rispondi(domanda)
            
            if risposta == "EXIT":
                print("\n🤖 Bot: Arrivederci! Alla prossima.\n")
                print("=" * 70)
                break
            
            print(f"\n🤖 Bot:\n{risposta}")
            print("-" * 70)
            
        except KeyboardInterrupt:
            print("\n\n🤖 Bot: Arrivederci! Alla prossima.\n")
            print("=" * 70)
            break
        except EOFError:
            print("\n🤖 Bot: Arrivederci! Alla prossima.\n")
            print("=" * 70)
            break
        except Exception as e:
            logging.error(f"ERRORE: {e}")
            print(f"\n⚠️ Errore imprevisto: {e}")
            print("🤖 Bot: Si è verificato un errore. Riprova pure!\n")


if __name__ == "__main__":
    main()