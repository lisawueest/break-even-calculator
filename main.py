from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException #falls die Eingabe ungültig sein sollte
from break_even import deckungsbeitrag
from break_even import break_even

app = FastAPI(title="break_even_calculator")

class BreakEvenInput(BaseModel):
    verkaufspreis: float
    variable_kosten: float
    fixkosten: float

class BreakEvenResponse(BaseModel):
    deckungsbeitrag: float
    break_even: int

@app.post("/break-even", response_model=BreakEvenResponse)
async def berechnen(daten: BreakEvenInput):
    if daten.variable_kosten >= daten.verkaufspreis:
        raise HTTPException(
            status_code=400,
            detail="Der Breakeven kann mit einem Deckungsbeitrag von 0 oder kleiner nicht erreicht werden."
        )
    ergebnis_deckungsbeitrag = deckungsbeitrag(daten.verkaufspreis, daten.variable_kosten)
    ergebnis_break_even = break_even(daten.fixkosten, ergebnis_deckungsbeitrag)

    return BreakEvenResponse(
        deckungsbeitrag=ergebnis_deckungsbeitrag,
        break_even=ergebnis_break_even
    )