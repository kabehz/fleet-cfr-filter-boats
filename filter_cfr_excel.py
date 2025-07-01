
import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

INPUT_FILE = "data/Listado_buques_pesca.xlsx"
OUTPUT_FILE = "output/buques_filtrados_cfr.xlsx"

CFR_DESDE = os.getenv("CFR_DESDE", "ESP000000100")
CFR_HASTA = os.getenv("CFR_HASTA", "ESP000000150")

df = pd.read_excel(INPUT_FILE, header=3)
df_filtrado = df[(df["CFR"] >= CFR_DESDE) & (df["CFR"] <= CFR_HASTA)]

columnas = ["CFR", "Nombre", "Matrícula", "Estado", "Eslora total (m)",
            "Arqueo (GT)", "Potencia (kW)", "Material del casco", "Puerto base", "Censo por modalidad"]
columnas_validas = [col for col in columnas if col in df_filtrado.columns]

df_final = df_filtrado[columnas_validas]

with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
    df_final.to_excel(writer, startrow=1, index=False)
    ws = writer.book.active
    ws.cell(row=1, column=1, value=f"Filtro aplicado: CFR desde {CFR_DESDE} hasta {CFR_HASTA}")
