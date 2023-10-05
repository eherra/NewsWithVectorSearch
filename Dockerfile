# Stage 1
FROM --platform=linux/amd64 node:16-alpine AS build

WORKDIR /app
COPY ./frontend ./frontend

RUN cd frontend && \
    npm install && \
    npm run build && \
    rm -rf node_modules

# Stage 2
FROM --platform=linux/amd64 python:3.9-alpine3.17

WORKDIR /app

COPY ./backend ./backend

RUN pip install --no-cache-dir -r /app/backend/requirements.txt && \
    rm -rf /root/.cache

WORKDIR /app/backend

COPY --from=build /app/frontend/build /app/backend/build

CMD gunicorn --bind 0.0.0.0:$PORT wsgi:app
