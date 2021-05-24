FROM python:3.9-slim as dev

WORKDIR /dsalgo

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONDONTWRITEBYTECODE=pleasedont

RUN pip install pytest pytest-cov

from dev

COPY setup.py setup.py
ADD dsalgo dsalgo

RUN pip install .
