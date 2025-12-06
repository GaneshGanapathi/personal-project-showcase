from calculator.main import Calculator
from fastapi import FastAPI
app = FastAPI()

cals = Calculator()

@app.get("/add")
def add(a:int,b:int):
    return {"result" : cals.addition(a,b)}
@app.get("/sub")
def sub(a:int,b:int):
    return {"result" : cals.subtraction(a,b)}
@app.get("/mul")
def mul(a:int,b:int):
    return {"result" : cals.multiply(a,b)}
@app.get("/div")
def div(a:int,b:int):
    return {"result" : cals.division(a,b)}

