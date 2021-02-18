FROM python:3.8.3-alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000