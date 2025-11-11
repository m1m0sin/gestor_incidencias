from fastapi import FastAPI

app = FastAPI(title="Mi API Rest", version="1.0")

@app.get("/")
def get_root():
    return {"message": "Hola mundo"}

@app.get("/health")
def get_health():
    return {"status": "ok"}