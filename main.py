from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}

# coba


@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):

    if published:
        return {"data": f"{limit} published blog from the database"}
    else:
        return {'data': f'{limit} blog from the database'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data blog': 'unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data blog': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    pubslished_at: Optional[bool]


@app.post('/blog')
def createBlog(request: Blog):
    return {'msg': f'Blog has created with title as {request.title}'}


# if __name__ == '__main__':
#     uvicorn.run(app, host="127.0.0.1", port='9000')
