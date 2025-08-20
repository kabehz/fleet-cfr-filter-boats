FROM python:3.9-slim

WORKDIR /app

# Copiar dependencias
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

# Crear carpetas necesarias
RUN mkdir -p data output

# Copiar archivos principales
#COPY app.py filter_cfr_excel.py run.sh ./

# Copiar frontend correctamente
#COPY index.html ./static/index.html

# Copiar otros recursos si aplica
#COPY test_app.py ./
#COPY CONTRIBUTING.md ./
#COPY .gitignore ./

# Exponer puerto Flask
EXPOSE 5000

# Ejecutar app
CMD ["python3", "app.py"]

