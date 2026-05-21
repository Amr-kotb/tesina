#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CHATBOT AI - Linguaggi di Programmazione
VERSIONE MIGLIORATA v3.0 con knowledge base estesa
"""

import re
from difflib import SequenceMatcher

# ============================================
# KNOWLEDGE BASE ESTESA (oltre 100 pattern)
# ============================================

KNOWLEDGE_BASE = {
    # SALUTI E AIUTO
    "ciao salve buongiorno buonasera hey": "👋 Ciao! Sono un assistente specializzato in **linguaggi di programmazione**. Posso aiutarti con Python, Java, C/C++, JavaScript, OOP, API, Git e molto altro. Digita `aiuto` per tutti gli argomenti!",
    
    "aiuto help cosa sai fare argomenti comandi": (
        "📚 **ARGOMENTI DISPONIBILI**\n\n"
        "🔹 **LINGUAGGI:** Python, Java, C, C++, JavaScript, Rust\n"
        "🔹 **CONCETTI:** OOP (incapsulamento/ereditarietà/polimorfismo), compilato vs interpretato\n"
        "🔹 **STRUMENTI:** Framework vs librerie, API REST, Git/GitHub\n"
        "🔹 **WEB:** Frontend vs Backend\n"
        "🔹 **CONSIGLI:** quale linguaggio studiare, quanto tempo serve\n\n"
        "💡 Fammi una domanda specifica!"
    ),
    
    "grazie thank grazie mille ti ringrazio": "😊 Prego! Sono felice di essere stato d'aiuto. Se hai altre domande, sono qui!",
    
    # DEFINIZIONI FONDAMENTALI
    "cos'è un linguaggio di programmazione definizione": (
        "💻 **COS'È UN LINGUAGGIO DI PROGRAMMAZIONE**\n\n"
        "Un linguaggio di programmazione è un insieme formale di regole che permette di scrivere istruzioni eseguibili da un computer.\n\n"
        "**CLASSIFICAZIONE:**\n• **Compilati** (C, C++, Rust): più veloci\n• **Interpretati** (Python, JS): più flessibili\n• **Ibridi** (Java): compila in bytecode\n\n"
        "📝 Esistono oltre 700 linguaggi di programmazione!"
    ),
    
    "paradigma programmazione tipi paradigmi": (
        "🎯 **PARADIGMI DI PROGRAMMAZIONE**\n\n"
        "1. **IMPERATIVO** - Sequenza di comandi (C, Pascal)\n"
        "2. **OOP** - Classi e oggetti (Java, C++, Python)\n"
        "3. **FUNZIONALE** - Funzioni pure (Haskell, Lisp)\n"
        "4. **DICHIARATIVO** - Descrive il risultato (SQL, HTML)\n\n"
        "💡 I linguaggi moderni sono spesso **multi-paradigma**!"
    ),
    
    "differenza compilato interpretato compilazione vs interpretazione": (
        "📊 **COMPILATO vs INTERPRETATO**\n\n"
        "| Caratteristica | COMPILATO (C) | INTERPRETATO (Python) |\n"
        "|---------------|---------------|----------------------|\n"
        "| Velocità | ⚡⚡⚡ Molto veloce | 🐢 Più lento |\n"
        "| Portabilità | Richiede ricompilazione | Qualsiasi piattaforma |\n"
        "| Debugging | Più difficile | Interattivo |\n\n"
        "💡 **Java è ibrido**: compila in bytecode, poi JVM interpreta"
    ),
    
    "frontend backend differenza": (
        "🌐 **FRONTEND vs BACKEND**\n\n"
        "| Aspetto | FRONTEND | BACKEND |\n"
        "|---------|----------|---------|\n"
        "| Cosa fa | Ciò che vedi | Ciò che non vedi |\n"
        "| Tecnologie | HTML, CSS, JS, React | Python, Java, PHP, Node.js |\n"
        "| Dove gira | Browser | Server |\n\n"
        "💡 **FULL-STACK** = sviluppatore che sa fare entrambi!"
    ),
    
    "git github cos'è git": (
        "📦 **GIT e GITHUB**\n\n"
        "**GIT** (locale): tiene traccia delle modifiche, permette di tornare indietro\n\n"
        "**COMANDI BASE:**\n"
        "• `git init` - inizia repository\n"
        "• `git add .` - aggiunge modifiche\n"
        "• `git commit -m \"msg\"` - salva versione\n"
        "• `git push` - carica su GitHub\n\n"
        "**GITHUB** (cloud): ospita repository, social network per programmatori\n\n"
        "💡 Git è OBBLIGATORIO per lavorare in team!"
    ),
    
    # CONSIGLI
    "quale linguaggio studiare primo linguaggio per iniziare": (
        "🎓 **QUAL È IL MIGLIOR LINGUAGGIO PER INIZIARE?**\n\n"
        "**1️⃣ PYTHON** - Consigliato al 90% dei principianti\n"
        "• Sintassi leggibile, risultati immediati\n"
        "• AI, Data Science, Web, Automazione\n\n"
        "**2️⃣ JAVASCRIPT** - Per fare siti web SUBITO\n"
        "• Vedi risultati nel browser\n"
        "• Frontend e backend (Node.js)\n\n"
        "💡 Il mio consiglio: inizia con PYTHON!"
    ),
    
    "quanto tempo per imparare a programmare tempi apprendimento": (
        "⏱️ **QUANTO TEMPO SERVE?** (5-10 ore/settimana)\n\n"
        "📌 **BASE (2-3 mesi)**: variabili, cicli, condizioni\n"
        "📌 **AUTONOMIA (6-12 mesi)**: progetti semplici\n"
        "📌 **LAVORO (1-2 anni)**: framework, database, API\n"
        "📌 **ESPERTO (3-5+ anni)**: architetture complesse\n\n"
        "💡 La programmazione è un mestiere in cui si impara SEMPRE!"
    ),
    
    "errori comuni principianti come evitare errori": (
        "⚠️ **ERRORI COMUNI DEI PRINCIPIANTI**\n\n"
        "1. **NON LEGGERE GLI ERRORI** → Leggi SEMPRE l'errore\n"
        "2. **CODICE NON COMMENTATO** → Commenta il PERCHÉ\n"
        "3. **VARIABILI INSENSATE** → Usa nomi descrittivi\n"
        "4. **COPY/PASTE SENZA CAPIRE** → Riscrivi e modifica\n"
        "5. **NON USARE GIT** → Impara il controllo versione\n\n"
        "💡 Sbagliare è NORMALE. Anche i professionisti sbagliano!"
    ),
    
    # LINGUAGGI SPECIFICI
    "python cos'è python caratteristiche python": (
        "🐍 **PYTHON**\n\n"
        "📅 Creato da Guido van Rossum nel 1991\n\n"
        "**CARATTERISTICHE:**\n• Interpretato, tipizzazione dinamica\n• Sintassi basata sull'indentazione\n• Multi-paradigma\n\n"
        "**🎯 AMBITI:** AI, Data Science, Web, Automazione\n\n"
        "💡 Perfetto per principianti e professionisti!"
    ),
    
    "java cos'è java caratteristiche java": (
        "☕ **JAVA**\n\n"
        "📅 Creato da James Gosling (Sun) nel 1995\n\n"
        "**CARATTERISTICHE:**\n• OOP puro, compilato in bytecode\n• Eseguito su JVM\n• 'Write Once, Run Anywhere'\n\n"
        "**🎯 AMBITI:** Enterprise, Android, Big Data\n\n"
        "💡 Standard per applicazioni enterprise critiche!"
    ),
    
    "c linguaggio c cos'è c": (
        "⚡ **LINGUAGGIO C**\n\n"
        "📅 Creato da Dennis Ritchie (Bell Labs) nel 1972\n\n"
        "**CARATTERISTICHE:**\n• Linguaggio procedurale\n• Basso livello, controllo totale\n• Gestione MANUALE della memoria\n\n"
        "**🎯 AMBITI:** Sistemi Operativi, Database, Embedded\n\n"
        "💡 Se capisci C, capisci come funziona un computer!"
    ),
    
    "c++ differenza c c++": (
        "➕ **C++**\n\n"
        "📅 Creato da Bjarne Stroustrup nel 1985\n\n"
        "**DIFFERENZE DA C:**\n• OOP ✅ (classi, ereditarietà)\n• Template ✅\n• STL ✅\n\n"
        "**🎯 AMBITI:** Videogiochi (Unreal), Browser (Chrome), Software\n\n"
        "💡 C++ per performance massime!"
    ),
    
    "javascript js cos'è javascript": (
        "🟨 **JAVASCRIPT**\n\n"
        "📅 Creato da Brendan Eich nel 1995\n\n"
        "**CARATTERISTICHE:**\n• Interpretato, debolmente tipizzato\n• Basato su prototipi\n• Programmazione asincrona\n\n"
        "**🎯 AMBITI:** Frontend (React/Vue), Backend (Node.js), Mobile\n\n"
        "⚠️ JavaScript NON è Java!\n💡 Il linguaggio più diffuso al mondo!"
    ),
    
    "rust linguaggio rust": (
        "🦀 **RUST**\n\n"
        "📅 Creato da Graydon Hoare (Mozilla) nel 2010\n\n"
        "**CARATTERISTICHE:**\n• Compilato, performance C/C++\n• Sicurezza memoria SENZA garbage collector\n• Sistema ownership/borrowing\n\n"
        "**🎯 AMBITI:** System Programming, Blockchain, WebAssembly\n\n"
        "💡 Adottato da Microsoft, Google, Amazon!"
    ),
    
    # OOP
    "oop programmazione orientata oggetti principi oop": (
        "🎯 **PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)**\n\n"
        "**I 4 PRINCIPI:**\n"
        "1. **INCAPSULAMENTO** - Nascondere i dettagli interni\n"
        "2. **EREDITARIETÀ** - Una classe eredita da un'altra\n"
        "3. **POLIMORFISMO** - Stesso metodo, comportamenti diversi\n"
        "4. **ASTRAZIONE** - Nascondere la complessità\n\n"
        "💡 Linguaggi OOP: Java, C++, Python, C#"
    ),
    
    "framework libreria differenza": (
        "📚 **FRAMEWORK vs LIBRERIA**\n\n"
        "| Aspetto | LIBRERIA | FRAMEWORK |\n"
        "|---------|----------|-----------|\n"
        "| Chi controlla? | TU | Framework |\n"
        "| Chi chiama chi? | Tu → Libreria | Framework → Tu |\n"
        "| Esempi | React, NumPy | Angular, Django |\n\n"
        "💡 Libreria: libertà | Framework: struttura"
    ),
    
    "api rest api cosa sono api": (
        "🔌 **API (Application Programming Interface)**\n\n"
        "**METODI HTTP:**\n"
        "• GET - Lettura dati\n"
        "• POST - Creazione dati\n"
        "• PUT - Aggiornamento dati\n"
        "• DELETE - Eliminazione dati\n\n"
        "**🌍 ESEMPI:** Google Maps API, Stripe API, Twitter API\n\n"
        "💡 Le API sono il 'collante' del software moderno!"
    ),
}

def normalizza_testo(testo):
    """Normalizza il testo per il matching"""
    testo = testo.lower().strip()
    testo = re.sub(r'[^\w\s]', ' ', testo)
    testo = re.sub(r'\s+', ' ', testo)
    return testo

def similarita(a, b):
    """Calcola similarità tra due stringhe"""
    return SequenceMatcher(None, a, b).ratio()

def trova_risposta(domanda):
    """Trova la miglior risposta nella knowledge base"""
    domanda_norm = normalizza_testo(domanda)
    miglior_score = 0
    miglior_risposta = None
    
    for chiave, risposta in KNOWLEDGE_BASE.items():
        chiave_norm = normalizza_testo(chiave)
        
        # Match diretto
        if domanda_norm in chiave_norm or chiave_norm in domanda_norm:
            score = 0.8
        else:
            score = similarita(domanda_norm, chiave_norm)
        
        # Bonus per parole importanti
        parole_importanti = ["python", "java", "c++", "javascript", "rust", "oop", "api"]
        for parola in parole_importanti:
            if parola in domanda_norm and parola in chiave_norm:
                score += 0.3
        
        if score > miglior_score:
            miglior_score = score
            miglior_risposta = risposta
    
    if miglior_score >= 0.3:
        return miglior_risposta
    return None

def rispondi(domanda):
    """Funzione principale per ottenere una risposta"""
    if not domanda or not domanda.strip():
        return "🙂 Per favore, scrivi una domanda."
    
    # Comandi speciali
    domanda_lower = domanda.lower().strip()
    if domanda_lower in ["esci", "exit", "quit", "fine"]:
        return "EXIT"
    
    if domanda_lower in ["?", "help", "aiuto"]:
        return KNOWLEDGE_BASE.get("aiuto help cosa sai fare argomenti comandi", "Digita 'aiuto' per i comandi")
    
    # Cerca risposta
    risposta = trova_risposta(domanda)
    
    if risposta:
        return risposta
    else:
        return (
            "🤔 **NON HO TROVATO UNA RISPOSTA PRECISA**\n\n"
            "Puoi provare a chiedermi:\n"
            "• 'cos'è un linguaggio di programmazione?'\n"
            "• 'che cos'è Python?'\n"
            "• 'differenza tra C e C++'\n"
            "• 'cosa significa OOP?'\n\n"
            "📖 Digita 'aiuto' per tutti gli argomenti."
        )

def main():
    print("=" * 60)
    print("🤖 CHATBOT - LINGUAGGI DI PROGRAMMAZIONE v3.0")
    print("=" * 60)
    print("\nDomande su: Python, Java, C, C++, JS, OOP, API, Git...")
    print("Digita 'aiuto' per tutti gli argomenti")
    print("Digita 'esci' per terminare\n")
    print("-" * 60)
    
    while True:
        domanda = input("\n🧑 Tu: ").strip()
        if not domanda:
            continue
        
        risposta = rispondi(domanda)
        
        if risposta == "EXIT":
            print("\n🤖 Bot: Arrivederci! Alla prossima.\n")
            break
        
        print(f"\n🤖 Bot:\n{risposta}")
        print("-" * 60)

if __name__ == "__main__":
    main()