#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TEST UNITARI PER CHATBOT
Testa tutte le funzionalità del chatbot
"""

import sys

def test_chatbot():
    """Suite di test completa"""
    
    # Importa il chatbot
    try:
        from ai import ChatbotProgrammazione
        print("✅ Chatbot importato correttamente")
    except ImportError:
        print("❌ Errore: assicurati che ai.py sia nella stessa directory")
        return False
    
    chatbot = ChatbotProgrammazione()
    
    # Lista dei test
    tests = [
        # (domanda, deve_rispondere, descrizione)
        ("Ciao", True, "Saluto base"),
        ("Cos'è Python?", True, "Domanda su Python"),
        ("Che cos'è Java?", True, "Domanda su Java"),
        ("Differenza tra C e C++", True, "Confronto linguaggi"),
        ("Quale linguaggio devo studiare?", True, "Consiglio"),
        ("Quanto tempo serve per imparare?", True, "Tempi"),
        ("Che tempo fa oggi?", False, "Domanda non pertinente (meteo)"),
        ("Come si fa la pizza?", False, "Domanda non pertinente (cucina)"),
        ("Python non è un linguaggio?", False, "Negazione (dovrebbe chiedere chiarimenti)"),
        ("aiuto", True, "Comando aiuto"),
        ("dimmi di più", True, "Comando approfondimento"),
        ("cosa mi hai detto prima", True, "Memoria conversazione"),
    ]
    
    print("\n" + "=" * 70)
    print("AVVIO TEST CHATBOT")
    print("=" * 70)
    
    risultati = []
    
    for domanda, deve_rispondere, descrizione in tests:
        print(f"\n📝 Test: {descrizione}")
        print(f"   Domanda: '{domanda}'")
        
        risposta = chatbot.rispondi(domanda)
        
        # Verifica se è una risposta valida (non errore di pertinenza se deve_rispondere=False)
        if deve_rispondere:
            # La risposta non dovrebbe essere il messaggio di "non pertinente"
            is_pertinente = "NON PERTINENTE" not in risposta and "non ho trovato" not in risposta
            if is_pertinente:
                print(f"   ✅ RISPOSTA: {risposta[:100]}...")
                risultati.append(True)
            else:
                print(f"   ❌ FALLITO: Dovrebbe rispondere ma ha detto: {risposta[:100]}")
                risultati.append(False)
        else:
            # La risposta dovrebbe essere di rifiuto
            is_rifiuto = "NON PERTINENTE" in risposta or "ATTENZIONE" in risposta or "non ho trovato" in risposta
            if is_rifiuto:
                print(f"   ✅ CORRETTO: Ha rifiutato correttamente")
                risultati.append(True)
            else:
                print(f"   ❌ FALLITO: Dovrebbe rifiutare ma ha risposto: {risposta[:100]}")
                risultati.append(False)
    
    # Statistiche
    print("\n" + "=" * 70)
    print("RISULTATI TEST")
    print("=" * 70)
    
    totali = len(risultati)
    superati = sum(risultati)
    
    print(f"\n✅ Test superati: {superati}/{totali}")
    print(f"📊 Percentuale successo: {superati/totali*100:.1f}%")
    
    if superati == totali:
        print("\n🎉 TUTTI I TEST SUPERATI! Il chatbot funziona perfettamente!")
        return True
    else:
        print(f"\n⚠️ {totali - superati} test falliti. Rivedi il codice.")
        return False

def test_manual():
    """Modalità test manuale interattiva"""
    try:
        from ai import ChatbotProgrammazione
    except ImportError:
        print("Importa ai.py")
        return
    
    chatbot = ChatbotProgrammazione()
    print("\n" + "=" * 70)
    print("MODALITÀ TEST MANUALE - Digita 'test_end' per uscire")
    print("=" * 70)
    
    while True:
        domanda = input("\n🧑 Tu: ").strip()
        if domanda.lower() == "test_end":
            break
        if not domanda:
            continue
        
        risposta = chatbot.rispondi(domanda)
        print(f"\n🤖 Bot: {risposta}")
        print("-" * 50)

if __name__ == "__main__":
    print("Scegli modalità:")
    print("1. Test automatici")
    print("2. Test manuale interattivo")
    
    scelta = input("\nScegli (1/2): ").strip()
    
    if scelta == "1":
        test_chatbot()
    elif scelta == "2":
        test_manual()
    else:
        print("Scelta non valida, eseguo test automatici...")
        test_chatbot()