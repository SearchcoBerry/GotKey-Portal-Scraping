from fastapi import FastAPI, Query
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
def get_news(user: User, max_page: int = Query(default=30)):
    driver_path = './chromedriver'
    info_lists = fetch_portal(driver_path, user.id, user.password, max_page)
    return info_lists