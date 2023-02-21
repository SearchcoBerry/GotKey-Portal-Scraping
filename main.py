from fastapi import FastAPI, Query
from pydantic import BaseModel  # リクエストbodyを定義するために必要
from typing import List  # ネストされたBodyを定義するために必要
import scraping

app = FastAPI()

# リクエストbodyを定義
class User(BaseModel):
    id: str
    password: str


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/informations")
def get_news(user: User, max_page: int = Query(default=30)):
    driver_path = './chromedriver'
    login_info = scraping.login(driver_path, user.id, user.password)
    info_lists = scraping.fetch_info(login_info, max_page)
    return info_lists
