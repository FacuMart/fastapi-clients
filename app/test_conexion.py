import pyodbc

# Reemplazá los valores si tenés una contraseña distinta
conn_str = (
    "DRIVER={FreeTDS};"
    "SERVER=localhost,1433;"
    "DATABASE=FastAPI_DB;"
    "UID=sa;"
    "PWD=TGDOlmos144omala220"
)

try:
    conn = pyodbc.connect(conn_str)
    print("Conectado correctamente a SQL Server")
    conn.close()
except Exception as e:
    print("❌ Error de conexión:")
    print(e)
