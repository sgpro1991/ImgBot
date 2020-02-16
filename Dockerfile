FROM python:3.6

WORKDIR /home/BotImg
COPY BotImg /home/BotImg
RUN pip install -r /home/BotImg/requirements.txt

CMD python /home/BotImg/run.py