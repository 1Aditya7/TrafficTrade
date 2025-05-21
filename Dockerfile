FROM seleniarm/standalone-chromium:latest

USER root

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run_strategy.py"]
