FROM python:3.7
WORKDIR /opt/todo
EXPOSE 80
COPY ./server .
RUN pip install poetry
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install
CMD ["poetry", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "80"]
