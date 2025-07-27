FROM python:3.12-slim

RUN pip install --no-cache-dir uv==0.7.13

WORKDIR /app

COPY . .

RUN uv pip install -r requirements.txt --system

EXPOSE 8080

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]