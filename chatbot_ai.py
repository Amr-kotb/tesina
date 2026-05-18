#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CHATBOT AI - Versione Leggera per Integrazione
Chatbot specializzato in linguaggi di programmazione
"""

import re
from difflib import SequenceMatcher

# Knowledge base essenziale
KNOWLEDGE_BASE = {
    "ciao salve buongiorno": "👋 Ciao! Sono un assistente sui linguaggi di programmazione. Posso parlarti di Python, Java, C/C++, JavaScript, e molto altro. Digita 'aiuto' per gli argomenti!",
    
    "aiuto help cosa sai fare": (
        "📚 **ARGOMENTI:**\n"
        "• Python, Java, C, C++, JavaScript\n"
        "• OOP (programmazione a oggetti)\n"
        "• Compilato vs Interpretato\n"
        "• Framework vs Librerie\n"
        "• API e REST\n"
        "• Git e GitHub\n"
        "• Frontend vs Backend\n"
        "• Quale linguaggio studiare\n\n"
        "Fammi una domanda specifica!"
    ),
    
    "python": "🐍 **Python** - Linguaggio interpretato, sintassi semplice. Usato per AI, Data Science, Web. Creato da Guido van Rossum nel 1991.",
    
    "java": "☕ **Java** - OOP, 'Write Once Run Anywhere'. Usato per enterprise, Android. Creato da James Gosling nel 1995.",
    
    "c linguaggio c": "⚡ **C** - Linguaggio procedurale, basso livello. Padre di tutti i linguaggi moderni. Creato da Dennis Ritchie nel 1972.",
    
    "c++": "➕ **C++** - Estensione di C con OOP. Usato per videogiochi, browser. Creato da Bjarne Stroustrup nel 1985.",
    
    "javascript": "🟨 **JavaScript** - Linguaggio del web. Frontend (React/Vue) e backend (Node.js). Creato da Brendan Eich nel 1995.",
    
    "oop programmazione oggetti": "🎯 **OOP** - 4 pilastri: Incapsulamento, Ereditarietà, Polimorfismo, Astrazione. Usato in Java, C++, Python.",
    
    "differenza compilato interpretato": "**Compilato** (C, C++): più veloce, richiede compilazione. **Interpretato** (Python, JS): più flessibile, più lento.",
    
    "frontend backend": "**Frontend** (HTML/CSS/JS): ciò che vedi. **Backend** (Python/Java/PHP): ciò che non vedi (server, database).",
    
    "git github": "**Git** = controllo versione locale. **GitHub** = piattaforma cloud per ospitare repository Git.",
    
    "quale linguaggio studiare": "🎓 **Python** è il più consigliato per iniziare! Sintassi semplice e tanti ambiti (AI, Dati, Web).",
    
    "grazie": "😊 Prego! Chiedimi pure altro sui linguaggi di programmazione!"
}

def normalizza(testo):
    testo = testo.lower().strip()
    testo = re.sub(r'[^\w\s]', ' ', testo)
    return re.sub(r'\s+', ' ', testo)

def similarità(a, b):
    return SequenceMatcher(None, a, b).ratio()

def trova_risposta(domanda):
    domanda_norm = normalizza(domanda)
    miglior_score = 0
    miglior_risposta = None
    
    for chiave, risposta in KNOWLEDGE_BASE.items():
        chiave_norm = normalizza(chiave)
        score = similarità(domanda_norm, chiave_norm)
        
        # Bonus per parole importanti
        for parola in domanda_norm.split():
            if parola in chiave_norm:
                score += 0.3
        
        if score > miglior_score:
            miglior_score = score
            miglior_risposta = risposta
    
    if miglior_score > 0.3:
        return miglior_risposta
    return None

def rispondi(domanda):
    if not domanda or not domanda.strip():
        return "Scrivi una domanda!"
    
    risposta = trova_risposta(domanda)
    
    if risposta:
        return risposta
    else:
        return "🤔 Non ho capito. Domande su: Python, Java, C, C++, JS, OOP, Git. Digita 'aiuto' per la lista."

def main():
    print("=" * 50)
    print("Chatbot Programmazione (leggero)")
    print("Domande: Python, Java, C, C++, JS, OOP, Git...")
    print("Digita 'esci' per uscire")
    print("-" * 50)
    
    while True:
        domanda = input("\nTu: ").strip()
        if domanda.lower() in ["esci", "exit"]:
            print("Arrivederci!")
            break
        print(f"\nBot: {rispondi(domanda)}")

if __name__ == "__main__":
    main()