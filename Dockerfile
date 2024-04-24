
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN python -m venv virtualenv

RUN /bin/bash -c "source virtualenv/bin/activate"

RUN pip install -r requirements.txt


RUN mkdir -p data/key data/encrypted_files

COPY . .

EXPOSE 8000


CMD ["python3.11", "main.py"]