FROM python:3.9-slim

# Crear entorno
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar archivos
COPY filter_cfr_excel.py .
COPY index.html .
COPY run.sh .

# Crear carpetas de datos
RUN mkdir -p data output

# Ejecutar el script de descarga y filtrado por defecto
RUN chmod +x run.sh && ./run.sh

# Exponer contenido estático
WORKDIR /app
CMD ["python3", "-m", "http.server", "8080"]
