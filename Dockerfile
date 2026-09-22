ARG PYTHON_VERSION=3.12-slim
FROM python:${PYTHON_VERSION}
WORKDIR /app
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python" ]