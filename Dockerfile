FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools

RUN pip install -r requirements.txt

EXPOSE 800

CMD ["uvicorn", "src.main:app", "--host","0.0.0.0", "--port", "800"]