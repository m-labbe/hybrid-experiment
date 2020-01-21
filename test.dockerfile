FROM python:3.7
WORKDIR /opt/todo
EXPOSE 80
RUN pip install poetry
COPY server/pyproject.toml ./
COPY server/poetry.lock ./
RUN poetry install
CMD ["poetry", "run", "python", "-m", "pytest"]
