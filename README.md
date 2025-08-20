# 🚢 Filtro Semántico de Flota Pesquera Española

[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com/)
[![CI GitHub Actions](https://github.com/tu-org/filtro-flota/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-org/filtro-flota/actions)
[![Licencia EUPL v1.2](https://img.shields.io/badge/licencia-EUPL--1.2-green)](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)

Este proyecto permite **descargar, filtrar y transformar automáticamente** los datos oficiales de la flota pesquera española. Produce salidas en Excel, JSON-LD y RDF, y expone una interfaz web estática para facilitar su uso por analistas, organismos públicos y sistemas de IA semántica.

---

## 🎯 Objetivo

Automatizar la **extracción, clasificación y publicación estructurada** de datos públicos de buques de pesca, promoviendo:

* Transparencia institucional
* Ciencia reproducible
* Interoperabilidad semántica europea

---

## 🚀 Cómo usar (Script Python)

```bash
python filter_cfr_excel.py \
  --output output/resultado.xlsx \
  --jsonld output/resultado.jsonld \
  --rdf output/resultado.ttl \º
  --desde ESP000000100 \
  --hasta ESP000000150 \
  --estado "Alta Definitiva,Baja Provisional"
```

🧩 Argumentos disponibles:

* `--output`: ruta del Excel generado
* `--jsonld`: salida opcional estructurada (JSON-LD)
* `--rdf`: salida opcional para grafos semánticos (Turtle)
* `--desde`: CFR inicial (obligatorio)
* `--hasta`: CFR final (obligatorio)
* `--estado`: uno o varios estados separados por coma (opcional)

---

## ⚙️ Cómo usar (Script Bash)

Archivo: `run.sh`

```bash
#!/bin/bash

python3 filter_cfr_excel.py \
  --output output/resultado.xlsx \
  --jsonld output/resultado.jsonld \
  --rdf output/resultado.ttl \
  --desde ESP000000100 \
  --hasta ESP000000150
```

✅ Ejecuta con:

```bash
chmod +x run.sh
./run.sh
```

---

## 🐳 Cómo usar (Docker)

### 🔨 Construcción local

```bash
docker build -t buques-filter .
```

### ▶️ Ejecución

```bash
docker run -it --rm -p 8080:8080 buques-filter
```

Accede a: [http://localhost:8080](http://localhost:8080)

### 🌐 Contenido expuesto

* `index.html`: interfaz web para generación interactiva de comandos
* `output/resultado.xlsx`: Excel filtrado
* `output/resultado.jsonld`: JSON-LD estructurado
* `output/resultado.ttl`: RDF Turtle
* `output/estados.json`: lista dinámica para formulario web

---

## 📂 Estructura de Salidas

| Archivo                   | Descripción                                          |
| ------------------------- | ---------------------------------------------------- |
| `output/resultado.xlsx`   | Excel con filtros aplicados (CFR, Estado) y cabecera |
| `output/resultado.jsonld` | Datos compatibles con Schema.org (JSON-LD)           |
| `output/resultado.ttl`    | Exportación RDF (Turtle) para triplestores           |
| `output/estados.json`     | Estados únicos detectados, para carga web dinámica   |

---

## 🧠 Casos de uso

* Dashboards de sostenibilidad y transparencia
* Sistemas expertos marítimos
* Grafos legales y semánticos
* Publicaciones FAIR para investigación europea

---

## 🔄 Automatización CI/CD

* 🛠️ GitHub Actions (build/test/deploy)
* 📦 Docker multiuso (CLI + frontend)
* ☁️ Publicable en GitHub Pages, Netlify o servidores K3s/MicroK8s

---

## 🤝 Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para sumarte. Estilo AtlantyQA: modularidad, claridad, ética y trazabilidad pública.

---

## 🌍 Licencia

Distribuido bajo **EUPL v1.2**, favoreciendo su adopción pública, interoperabilidad legal y soberanía semántica.

> “Por una Europa con soberanía semántica y transparencia pesquera.”

---