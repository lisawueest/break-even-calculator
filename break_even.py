import math

def deckungsbeitrag(verkaufspreis, variable_kosten):
    return verkaufspreis - variable_kosten

def break_even(fixkosten, ergebnis_deckungsbeitrag):
    return math.ceil(fixkosten / ergebnis_deckungsbeitrag)

if __name__ == "__main__":
    verkaufspreis = float(input('Geben Sie den Verkaufspreis Ihres Produktes ein:'))
    variable_kosten = float(input('Geben Sie die variablen Kosten pro Produkteinheit ein:'))
    fixkosten = float(input('Geben Sie die Fixkosten ein:'))
    
    while variable_kosten >= verkaufspreis:
        print ('Der Breakeven kann mit einem negativen Deckungsbeitrag nicht erreicht werden.')
        verkaufspreis = float(input('Geben Sie den Verkaufspreis Ihres Produktes ein:'))
        variable_kosten = float(input('Geben Sie die variablen Kosten pro Produkteinheit ein:'))
        
    ergebnis_deckungsbeitrag = deckungsbeitrag(verkaufspreis, variable_kosten)
    print(f"Der Deckungsbeitrag pro Stück ist: {ergebnis_deckungsbeitrag}")

    ergebnis_break_even = break_even(fixkosten, ergebnis_deckungsbeitrag)
    print(f"Der Breakeven Point wird erreicht bei {math.ceil(ergebnis_break_even)} Stück.")

