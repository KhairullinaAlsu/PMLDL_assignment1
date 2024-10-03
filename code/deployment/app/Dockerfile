FROM python:3.10-slim

WORKDIR /app

COPY code/deployment/app /app

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501"]