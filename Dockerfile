
FROM python:3.12-slim as builder

WORKDIR /app

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./


RUN poetry install --no-interaction --no-ansi  --no-root


FROM python:3.12-slim


WORKDIR /app


RUN useradd --create-home appuser
USER appuser


COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sua_app.main:app"]

CMD ["tail", "-f", "/dev/null"]