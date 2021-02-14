FROM python:3.8

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
	pip install -r requirements.txt
	
COPY . /app

CMD [ "python", "/app/bot.py" ]