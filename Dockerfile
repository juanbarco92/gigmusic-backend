FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /usr/src/app
COPY ./backend/gigmusic/requirements.txt /usr/src/app
RUN pip install -r requirements.txt