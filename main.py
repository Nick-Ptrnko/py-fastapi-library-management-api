from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return f"Hello World"


@app.get("/{name}")
def say_hello(name: str):
    return f"Привіт {name}"

