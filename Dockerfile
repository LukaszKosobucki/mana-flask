ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

# python config
ENV PYTHONUNBUFFERED=1 \ 
  PYTHONDONTWRITEBYTECODE=1

# update dependencies
RUN apt-get update && apt-get upgrade -y \
 && apt-get install --no-install-recommends -y \
    build-essential \
    curl 

# add user with home catalog -> for security
RUN useradd -m -d /code appuser

# activate user and specify working directory
USER appuser
WORKDIR /code

# poetry config 
# ENV POETRY_VERSION=1.8.0 \ 
#   POETRY_NO_INTERACTION=1 \
#   POETRY_VIRTUALENVS_CREATE=false \
#   POETRY_HOME='/usr/local'

ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/code/poetry
ENV POETRY_VENV=/code/poetry-venv
ENV POETRY_CACHE_DIR=/code/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"    

# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# RUN apt-get update && apt-get upgrade -y \
#  && apt-get install --no-install-recommends -y \
#     build-essential \
#     curl 

# RUN curl -sSL https://install.python-poetry.org | python - \
#   && poetry --version 

FROM base AS deps


# COPY poetry.lock pyproject.toml /code/
# RUN poetry install 

COPY --chown=appuser:appuser poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-interaction --no-cache

# USER appuser
# COPY . /code
# EXPOSE 8000

FROM deps AS project
COPY --chown=appuser:appuser . /code

FROM project AS appuser

ENTRYPOINT ["bash", "run.sh"]

# CMD ["bash", "run.sh"]
# RUN ["python", "postgres/create_db.py"]
# CMD ["python", "wsgi.py"]
