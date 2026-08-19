# Tablas Resumen — Plan de Compras 2025

Este notebook (`02_tablas_resumen_Carla.ipynb`) toma el archivo `plan_de_compras_2025.xlsx` y genera tres tablas resumen a partir de los datos del plan de compras del MINVU.

## 1. Carga de datos

La primera celda carga el archivo Excel `plan_de_compras_2025.xlsx` (hoja `PLAN DE COMPRAS 2025`) en un DataFrame llamado `df_plan_de_compras`. El archivo debe estar ubicado un nivel por encima de la carpeta donde corre el notebook (`Path.cwd().parents[0]`).

Cada fila del archivo original representa un ítem dentro de un proyecto de compra, con columnas como Unidad de Compra, ID Proyecto, Tipo Proyecto, Estado Proyecto, montos, fechas, responsables, etc.

## 2. Tabla por Tipo de Proyecto (`tabla_tipo_proyecto`)

Agrupa los datos por **Tipo Proyecto** y calcula, para cada tipo:

- **Cantidad_Registros**: número de filas (ítems) asociados.
- **Cantidad_Proyectos**: número de proyectos únicos (`ID Proyecto` distintos).
- **Monto_Total_2025**: suma del monto total del ítem para el año 2025.
- **Monto_Promedio_2025**: monto promedio por ítem en 2025.

Sirve para comparar el peso relativo (en cantidad y en dinero) de cada tipo de proyecto (por ejemplo, "Proyecto estratégico" vs. "Proyecto operacional").

## 3. Tabla por Unidad de Compra (`tabla_unidad_compra`)

Agrupa los datos por **Unidad de Compra** (por ejemplo, cada SEREMI o el Ministerio central) y calcula:

- **Cantidad_Proyectos**: proyectos únicos por unidad.
- **Cantidad_Items**: cantidad de ítems reportados.
- **Monto_Total_2025**: monto total 2025 por unidad.

El resultado se ordena de mayor a menor monto total, lo que permite identificar rápidamente qué unidades concentran el mayor gasto planificado.

## 4. Tabla por Estado de Proyecto (`tabla_estado`)

Agrupa los datos por **Estado Proyecto** (por ejemplo, "Actualizado" o "Publicado") y calcula:

- **Cantidad_Registros**: total de filas/ítems en ese estado.
- **Cantidad_Proyectos**: proyectos únicos en ese estado.
- **Monto_Total_2025**: monto total 2025 asociado.
- **Monto_Arrastre**: monto de arrastre (compromisos que vienen de años anteriores) asociado a ese estado.

Permite ver cuánto del plan de compras está actualizado versus solo publicado, y qué proporción corresponde a montos "de arrastre".

## Requisitos

- Python 3.12
- pandas
- El archivo `plan_de_compras_2025.xlsx` disponible en la carpeta padre del notebook

## Resumen general

En conjunto, las tres tablas ofrecen distintos cortes (por tipo de proyecto, por unidad compradora y por estado) del mismo plan de compras, facilitando el análisis de montos, cantidad de proyectos e ítems desde diferentes ángulos.
