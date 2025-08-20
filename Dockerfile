FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY static/ static/  # <-- Copia toda la carpeta con index.html
COPY app.py filter_cfr_excel.py run.sh ./

RUN mkdir -p data output

EXPOSE 5000

CMD ["python3", "app.py"]


