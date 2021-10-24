FROM python:3.8.11-slim-buster as base_linux
RUN pip install -U pip setuptools pipenv;

RUN apt-get update \
    && apt-get install gcc -y libc-dev build-essential\
    && apt-get clean

FROM base_linux as base_pipenv
ENV PIPENV_VENV_IN_PROJECT=1
WORKDIR /app/
COPY ./Pipfile.lock ./Pipfile /app/
RUN  pipenv install --deploy

FROM base_pipenv

WORKDIR /app
COPY --from=base_pipenv /app/.venv /app/.venv
COPY ./ /app
ENV PATH="/app/.venv/bin:$PATH"

ENV PWPWORKERS 1