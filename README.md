# 🚢 Filtro Semántico de Flota Pesquera Española

[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com/)
[![CI GitHub Actions](https://github.com/tu-org/filtro-flota/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-org/filtro-flota/actions)
[![Licencia EUPL v1.2](https://img.shields.io/badge/licencia-EUPL--1.2-green)](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)

Este proyecto permite descargar, filtrar y transformar automáticamente los datos oficiales de la flota pesquera española. Genera salidas en Excel, JSON-LD y RDF, y expone una interfaz web estática para facilitar su uso por agentes inteligentes, analistas, periodistas de datos y sistemas semánticos.

---

## 🎯 Objetivo

Automatizar la **extracción, clasificación y publicación semántica** de los datos públicos de buques de pesca, fomentando:

* Transparencia institucional
* Ciencia abierta y reproducible
* Soberanía digital e interoperabilidad en Europa

---

## 🚀 Cómo usar (CLI)

```bash
python filter_cfr_excel.py \
  --output output/resultado.xlsx \
  --jsonld output/resultado.jsonld \
  --rdf output/resultado.ttl \
  --desde ESP000000100 \
  --hasta ESP000000150 \
  --estado "Alta Definitiva,Baja Provisional"
```

> El script descarga automáticamente el Excel actualizado desde el Ministerio, filtra por rango de CFR y opcionalmente por tipo de Estado. Genera también `output/estados.json` para uso web.

---

## 💻 Cómo usar (Web)

Después de construir el contenedor Docker:

```bash
docker build -t buques-filter .
docker run -it --rm -p 8080:8080 buques-filter
```

Accede a [http://localhost:8080](http://localhost:8080) para:

* Seleccionar visualmente CFRs y Estados
* Generar el comando CLI
* Descargar salidas estructuradas

---

## 📂 Salidas generadas

* ✅ `output/resultado.xlsx`: Excel con filtros y encabezado contextual
* ✅ `output/resultado.jsonld`: Datos estructurados en JSON-LD (Schema.org-ready)
* ✅ `output/resultado.ttl`: RDF Turtle para grafos semánticos
* ✅ `output/estados.json`: Catálogo de estados detectados para interfaz web

---

## 🧠 Casos de uso

* Observatorios de flota pesquera
* Portales de transparencia y trazabilidad
* Sistemas expertos marítimos y de sostenibilidad
* Integración en knowledge graphs e inteligencia legal

---

## 🔄 Automatización CI/CD

* 🔁 GitHub Actions (build + test + deploy)
* 🐳 Docker con servidor web estático incluido
* ☁️ Publicable vía GitHub Pages, Netlify o S3
* 🕹️ Soporte para ejecución por cron o triggers legales

---

## 🤝 Colaboración

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para contribuir técnica o éticamente. Seguimos el estilo **AtlantyQA**: modular, documentado y ético.

---

## 🌍 Licencia

Distribuido bajo **EUPL v1.2**, garantizando uso público, interoperabilidad legal y retorno comunitario.

> “Por una Europa con soberanía semántica y transparencia pesquera.”

---

¿Deseas que te genere el `CONTRIBUTING.md` base con estilo AtlantyQA o el `.github/workflows/ci.yml` de CI?
