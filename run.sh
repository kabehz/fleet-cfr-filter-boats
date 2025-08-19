#!/bin/bash

# Ejecuta el script principal con parámetros de ejemplo
python3 filter_cfr_excel.py \
  --output output/resultado.xlsx \
  --jsonld output/resultado.jsonld \
  --rdf output/resultado.ttl \
  --desde ESP000000100 \
  --hasta ESP000000150
