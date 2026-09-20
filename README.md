# break-even-calculator

Eine einfache FastAPI-Anwendung zur Berechnung des Break-even-Points eines Produkts.

Basierend auf dem Verkaufspreis pro Stück, den variablen Kosten pro Stück und den Fixkosten berechnet die Anwendung den Deckungsbeitrag sowie die benötigte Absatzmenge, um den Break-even-Point zu erreichen.

## Nutzung

### Eingabe (`POST /break-even`)

```json
{
  "verkaufspreis": 50,
  "variable_kosten": 30,
  "fixkosten": 1000
}
```

### Ausgabe

```json
{
  "deckungsbeitrag": 20,
  "break_even": 50
}
```

Der Deckungsbeitrag wird berechnet als:

`Verkaufspreis - variable Kosten`

Der Break-even-Point wird berechnet als:

`Fixkosten / Deckungsbeitrag`

Da nur ganze Produkte verkauft werden können, wird die benötigte Absatzmenge auf die nächste ganze Zahl aufgerundet.

## Validierung

Wenn die variablen Kosten gleich hoch oder höher als der Verkaufspreis sind, kann kein sinnvoller Break-even-Point berechnet werden. Die API gibt in diesem Fall eine Fehlermeldung zurück.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Danach kann die API im Browser geöffnet und getestet werden:

`http://127.0.0.1:8000/`

