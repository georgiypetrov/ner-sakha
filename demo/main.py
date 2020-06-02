from fastapi import FastAPI
from pydantic import BaseModel
from deeppavlov import build_model
from starlette.middleware.cors import CORSMiddleware


class Text(BaseModel):
    text: str


model = build_model('ner.json')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.post('/')
def ner_text(text: Text):
    output = model([text.text])
    return {"text": output[0][0], "tags": output[1][0]}
