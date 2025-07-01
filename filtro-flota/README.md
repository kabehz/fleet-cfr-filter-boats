# 🚢 Filtro Semántico de Flota Pesquera Española

[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://hub.docker.com/)
[![CI GitHub Actions](https://github.com/tu-org/filtro-flota/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-org/filtro-flota/actions)
[![Licencia EUPL v1.2](https://img.shields.io/badge/licencia-EUPL--1.2-green)](https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12)

Este repositorio permite filtrar y transformar datos oficiales de la flota pesquera española con salida en formatos Excel, JSON-LD y RDF, facilitando su uso por agentes inteligentes y sistemas de análisis semántico.

---

## 🎯 Objetivo

Automatizar la extracción y procesamiento semántico de los datos públicos de buques de pesca para facilitar transparencia, investigación y desarrollo de IA en soberanía digital.

---

## 🚀 Cómo usar

```bash
python filter_cfr_excel_autofilter.py \
  --input data/Listado_buques_pesca.xlsx \
  --output output/resultado.xlsx \
  --jsonld output/resultado.jsonld \
  --rdf output/resultado.ttl \
  --desde ESP000000100 \
  --hasta ESP000000150
```

---

## 📂 Salidas generadas

- `Excel` con filtros activados y cabecera contextual
- `JSON-LD` compatible con Schema.org y Linked Data
- `Turtle RDF` validado para triplestore semántico

---

## 🧠 Casos de uso

- Sistemas expertos pesqueros y marítimos
- Análisis por rango de CFR para organismos oficiales
- Integración en grafos de conocimiento
- Dashboards de sostenibilidad y transparencia

---

## 🔄 Automatización CI/CD

- GitHub Actions vía Docker
- CronJobs programables sobre K3s o MicroK8s
- Publicación GitHub Pages y filtrado interactivo por usuarios

---

## 🛡️ Contribuir

Ver [CONTRIBUTING.md](CONTRIBUTING.md) — guía ética y técnica estilo AtlantyQA para principiantes y expertos.

---

## 🌍 Licencia

Distribuido bajo **EUPL v1.2** — favoreciendo la reutilización pública y el cumplimiento europeo.

> “Por una Europa con soberanía semántica y transparencia pesquera.”