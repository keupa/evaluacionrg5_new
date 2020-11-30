FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY templates /usr/src/app/templates/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "src/web_service.py"]
