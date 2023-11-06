from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return "hi"


@app.get('/message')
def index():
    return {'data': 'FastAPI is great!'}


@app.get('/lol')
def index():
    return "LOL"


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
