from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'HEy'


@app.get('/about')
def about():
    return {'page': 'about'}
