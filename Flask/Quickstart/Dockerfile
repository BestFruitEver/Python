FROM python:3.7-slim
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 80
ENV NOM Romain
CMD ["python","app.py"]

