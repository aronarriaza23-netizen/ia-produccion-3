import pandas as pd

# Leer el archivo 
df = pd.read_excel("plan_de_compras_2025.xlsx")

# Separar la columna 'Teléfono responsable'
temp = df['Teléfono responsable'].str.split('Anexo', n=1, expand=True)

# Crear columna Telefono (limpiando espacios y guiones)
df['Telefono'] = temp[0].str.replace(r'[\s-]', '', regex=True)

# Crear columna Anexo (si existe la segunda parte, la limpia; si no, deja vacío)
df['Anexo'] = temp[1].str.strip() if temp.shape[1] > 1 else ""

# Exportar el DataFrame
df.to_excel(r"C:\Users\Alumno\Proyectos\ia-produccion-3\notebooks\plan_de_compras_2025_limpio.xlsx", index=False)

print("Archivo exportado.")









