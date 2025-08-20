from flask import Flask, request, send_file, jsonify, send_from_directory
import subprocess
import os
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/generar", methods=["POST"])
def generar():
    data = request.json
    desde = data.get("desde")
    hasta = data.get("hasta")
    estados = data.get("estado", [])

    cmd = [
        "python3", "filter_cfr_excel.py",
        "--output", "output/resultado.xlsx",
        "--jsonld", "output/resultado.jsonld",
        "--rdf", "output/resultado.ttl",
        "--desde", desde,
        "--hasta", hasta
    ]

    if estados and "Todos" not in estados:
        cmd += ["--estado", ",".join(estados)]

    try:
        subprocess.run(cmd, check=True)
        return jsonify({"success": True, "file": "/descargar"})
    except subprocess.CalledProcessError as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/descargar")
def descargar():
    path = "output/resultado.xlsx"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "Archivo no encontrado", 404

if hasattr(app, "before_first_request"):
    @app.before_first_request
    def generar_estados():
        path = "data/Listado_buques_pesca.xlsx"
        if os.path.exists(path):
            try:
                df = pd.read_excel(path, header=3)
                estados_unicos = sorted(df["Estado"].dropna().unique())
                with open("output/estados.json", "w", encoding="utf-8") as f:
                    json.dump(estados_unicos, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error al generar estados.json: {e}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
