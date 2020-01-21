FROM python:3.7
WORKDIR /opt/todo
EXPOSE 80
RUN pip install poetry
COPY server/pyproject.toml ./
COPY server/poetry.lock ./
RUN poetry install
CMD ["poetry", "run", "uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
