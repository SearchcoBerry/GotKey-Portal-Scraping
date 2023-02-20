from fastapi import FastAPI
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
from scraping import fetch_portal

app = FastAPI()

# リクエストbodyを定義
class User(BaseModel):
    id: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/news")
def get_news(user: User):
    driver_path = './chromedriver'
    max_page = 30
    fetch_portal(driver_path, user.id, user.password, max_page)
    return {"response": "Success"}