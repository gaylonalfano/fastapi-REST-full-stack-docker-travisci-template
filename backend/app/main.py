from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `notes = await get_all_notes()`
    return {"ping": "pong!"}


# Here's a super long comment that will eventually trigger an issue with flake8.
