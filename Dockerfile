ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  POETRY_VERSION=1.8.0 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_HOME='/usr/local'

WORKDIR /code

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN apt-get update && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y \
    build-essential \
    curl 

RUN curl -sSL https://install.python-poetry.org | python - \
  && poetry --version 

COPY poetry.lock pyproject.toml /code/
RUN poetry install 

USER appuser
COPY . /code
EXPOSE 8000

CMD ["python", "wsgi.py"]
