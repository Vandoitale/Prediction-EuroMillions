# python3 -m venv .venv
# source .venv/bin/activate
# pip install "fastapi[all]"
# uvicorn main:app --reload

import typing_extensions
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/numeros")
async def read_item(num1:int, num2:int, num3:int, num4:int, num5:int, numE1 :int, numE2 :int):
    """Read numeros and numeros

    Args:
       5 numbers

    Returns:
        The new minimum port.
    """

    if ((1<=num1) and (num1<=50) and
       (1<=num2) and (num2<=50) and 
       (1<=num3) and (num3<=50) and
       (1<=num4) and (num4<=50) and
       (1<=num5) and (num5<=50) and
       (1<=numE1) and (numE1<=12) and
       (1<=numE2) and (numE2<=12)):
        return {"succes": "traitement des données"}
    else :
        return {"erreur" : "Chaque nombre doit être compris entre 1 et 50 et chaque nombre étoile entre 1 et 12"}

    