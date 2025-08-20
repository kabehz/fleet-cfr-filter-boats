# 🤝 Guía de Contribución – Filtro Semántico de Flota Pesquera

Gracias por tu interés en contribuir. Este proyecto sigue principios de modularidad, ética digital y trazabilidad pública, en línea con la filosofía **AtlantyQA**.

---

## 📌 Requisitos Previos

- Python 3.10+
- Docker (para validación automatizada)
- Git y cuenta GitHub
- Acceso al archivo Excel oficial de buques

---

## 🧬 Principios

- **Claridad semántica**: nombres descriptivos, estructura modular, comentarios claros.
- **Interoperabilidad**: salidas estructuradas y accesibles desde otros sistemas.
- **Ética digital**: priorizar el uso público, evitar acoplamientos propietarios.
- **Legalidad europea**: datos bajo dominio público, código bajo licencia EUPL.

---

## 📌 Cómo contribuir

1. **Fork del repositorio**
2. Crea una rama descriptiva:  
   `git checkout -b feature/filtrado-por-puerto`
3. Asegúrate de incluir:
   - [ ] Código comentado
   - [ ] Pruebas básicas si aplica
   - [ ] Documentación actualizada (`README.md`, ayuda CLI o JS)
4. Abre un Pull Request con descripción clara:
   - Qué resuelve
   - Qué afecta
   - Cómo probarlo

---

## ✅ Buenas prácticas

- Usa `black` o `autopep8` para estilo Python.
- Evita código hardcoded: todo configurable por parámetros.
- Revisa `output/estados.json` si cambias lógica de carga.
- Documenta nuevos scripts o rutas web en el README.

---

## 🛡️ Seguridad

No aceptamos:

- Código que recopile datos personales
- Dependencias sin licencia abierta o con vulnerabilidades activas
- Scripts que suban datos automáticamente sin control humano

---

## 🙌 Código de conducta

Nos regimos por el [Código de Conducta de la comunidad AtlantiQA](https://github.com/kabehz/atlantyde-kit-adoption).

Gracias por hacer de este proyecto un bien común digital.
