FROM python:3.13-slim

EXPOSE 8080

WORKDIR /app

COPY src .
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

USER 1000:1000

CMD ["python", "merge_pdfs.py"]