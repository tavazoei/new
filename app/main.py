from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Product API is running"}
