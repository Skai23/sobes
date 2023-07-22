FROM python:3.12.0b4-slim-bullseye
WORKDIR /app

ADD server.py server.py
ADD req.txt req.txt
RUN pip3 install -r req.txt
RUN rm -f req.txt

EXPOSE 8000
EXPOSE 8001

CMD ["python3", "server.py"]