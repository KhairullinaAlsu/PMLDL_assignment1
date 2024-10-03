FROM python:3.10

WORKDIR /api

COPY code/deployment/api /api

RUN pip install --upgrade -r /api/requirements.txt

COPY code/models /api/models

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]