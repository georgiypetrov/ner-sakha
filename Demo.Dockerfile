FROM python:3.6-stretch
COPY demo/main.py emb100.bin ner.json requirements.txt ./
COPY ner/ ./ner/
RUN pip install -r requirements.txt
CMD uvicorn main:apdockp --port 8000 --host 0.0.0.0