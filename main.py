from fastapi import FastAPI


app = FastAPI()

@app.get('/home')
async def homePage() -> dict:
    return {"name": "Roman"}

@app.get('/items')
async def total_items() -> dict:
    return {"naiming": "Penopl",
            "quantity":100
            }