FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p data output static

COPY index.html estados.json ./static/
COPY app.py filter_cfr_excel.py run.sh ./

EXPOSE 5000

CMD ["python3", "app.py"]


