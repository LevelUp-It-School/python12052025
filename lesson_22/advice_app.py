from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Случайный совет по API")

class Advice(BaseModel):
    text: str

advice_list = [
    'Пейте больше воды!',
    "Делайте перерывы во время работы",
    "Не забывайте физическую активность",
    "Читайте каждый день",
    "Чистите зубы утром и вечером",
    "Учите питон!"
]

@app.get('/advice', summary= "Получить случайный совет")
def get_random_advice():
    return {"advice": random.choice(advice_list)}

@app.get('/', summary= "Главная страница")
def read_root():
    return {'message':"Добро пожаловать в API случайных советов. Перейдите на /advice для получения важного совета"}

@app.post("/advice", summary="Добавить новый совет")
def add_advice(advice: Advice):
    if advice.text in advice_list:
        raise HTTPException(status_code=400, detail="Такой совет уже есть!")
    advice_list.append(advice.text)
    return {"message": "Совет успешно добавлен"}