# 🤝 Contribuir al Proyecto: Flota Pesquera Semántica

Este repositorio forma parte de la iniciativa **AtlantyQA** para fomentar la soberanía digital y energética mediante datos abiertos interoperables. Aquí aprenderás cómo contribuir de forma técnica, ética y segura.

---

## 📌 Requisitos Previos

- Python 3.10+
- Docker (para validación automatizada)
- Git y cuenta GitHub
- Acceso al archivo Excel oficial de buques

---

## 🛠 Entorno de desarrollo

```bash
# Clona el repositorio
git clone https://github.com/tu-org/filtro-flota.git
cd filtro-flota

# Instala dependencias
pip install -r requirements.txt
```

---

## ⚙️ Ejecutar en local

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

## 📦 Contribuciones aceptadas

- Mejora de validaciones y testeo
- Integración semántica adicional (SKOS, GeoNames, etc.)
- Scripts de automatización para GitHub Actions y K3s
- Documentación clara para principiantes

---

## 🧭 Valores Éticos

- **Neutralidad climática**: datos orientados a transparencia pesquera
- **Soberanía semántica**: cumplimiento de ontologías públicas
- **Privacidad**: sin datos personales ni rastreo

---

## 🔐 Licencia y Derechos

Este código está bajo licencia **EUPL v1.2** para garantizar la reutilización pública compatible con normativas europeas.

---

Gracias por construir una Europa interoperable, abierta y soberana 🌍