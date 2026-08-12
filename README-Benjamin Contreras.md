# EDA – Plan de Compras 2025

Este proyecto contiene un **Análisis Exploratorio de Datos (EDA)** realizado sobre el archivo `plan_de_compras_2025.xlsx`, con el objetivo de comprender la estructura de la información, evaluar su calidad y detectar patrones relevantes asociados a proyectos, ítems, órdenes de compra y montos.

## Objetivo

El análisis busca:

- Conocer la estructura general del conjunto de datos.
- Identificar valores nulos y posibles problemas de calidad.
- Revisar registros duplicados y duplicidades desde la lógica de negocio.
- Analizar la distribución de variables categóricas y numéricas.
- Identificar valores atípicos en variables monetarias.
- Comparar proyectos según tipo, estado y unidad de compra.
- Analizar la evolución temporal de las compras.
- Detectar posibles inconsistencias en la información.
- Resumir los principales hallazgos obtenidos durante el EDA.

## Archivos principales

```text
.
├── EDA_Plan_de_Compras_2025_mejorado.ipynb
├── plan_de_compras_2025.xlsx
└── README.md
```

- `EDA_Plan_de_Compras_2025_mejorado.ipynb`: notebook principal con el análisis exploratorio.
- `plan_de_compras_2025.xlsx`: archivo de datos utilizado como fuente.
- `README.md`: descripción general del proyecto.

## Tecnologías utilizadas

El análisis fue desarrollado en **Python** utilizando principalmente:

- `pandas`
- `numpy`
- `matplotlib`
- `Jupyter Notebook`

## Instalación

Se recomienda trabajar dentro de un entorno virtual de Python.

```bash
pip install pandas numpy matplotlib openpyxl jupyter
```

`openpyxl` es necesario para la lectura de archivos Excel con extensión `.xlsx`.

## Ejecución

1. Ubicar `plan_de_compras_2025.xlsx` en la ruta utilizada por el notebook.
2. Abrir el notebook:

```bash
jupyter notebook EDA_Plan_de_Compras_2025_mejorado.ipynb
```

3. Ejecutar las celdas en orden desde el inicio.

También puede utilizarse **JupyterLab** o **Visual Studio Code** con la extensión de Jupyter.

## Contenido del análisis

### 1. Exploración inicial

Se revisan:

- dimensiones del DataFrame;
- nombres de las columnas;
- tipos de datos;
- primeros registros;
- estadísticas descriptivas iniciales.

El conjunto de datos contiene variables relacionadas con:

- unidad de compra;
- identificación y descripción de proyectos;
- tipo y estado del proyecto;
- ítems de compra;
- montos unitarios y totales;
- órdenes de compra;
- responsables;
- fechas;
- ítems y montos de arrastre.

### 2. Calidad de datos

Se analizan los valores nulos tanto en cantidad como en porcentaje.

Además de identificar campos incompletos, se evalúa si algunos valores faltantes pueden corresponder a **nulos estructurales**, es decir, valores que no necesariamente representan un error porque pueden depender de la naturaleza del registro.

### 3. Duplicados

Se comprueba la existencia de filas completamente duplicadas mediante `duplicated()`.

También se recomienda revisar posibles duplicidades desde la lógica de negocio, considerando combinaciones como:

- `ID Proyecto`;
- `Nombre ítem`;
- órdenes de compra asociadas.

La ausencia de filas idénticas no implica necesariamente que no existan registros repetidos desde un punto de vista funcional.

### 4. Variables categóricas

Se analiza la distribución de variables como:

- `Unidad de Compra`;
- `Tipo Proyecto`;
- `Estado Proyecto`;
- `Tipo compra`.

Se utilizan conteos, porcentajes y gráficos para identificar categorías predominantes y posibles concentraciones de registros.

### 5. Variables monetarias

Las principales variables analizadas son:

- `Monto Unitario Ítem`;
- `Monto Total Ítem Año 2025`;
- `Monto De Arrastre`.

Se utilizan estadísticas descriptivas, histogramas y boxplots para evaluar:

- tendencia central;
- dispersión;
- asimetría;
- valores extremos.

También se incorpora una visualización en escala logarítmica para facilitar la interpretación cuando existen diferencias importantes entre montos pequeños y grandes.

### 6. Detección de outliers

Los valores atípicos se identifican mediante el método del **rango intercuartílico (IQR)**.

Este análisis tiene un propósito exploratorio. Los outliers no se eliminan automáticamente, ya que un monto elevado puede representar una compra válida y relevante para el negocio.

### 7. Análisis por proyecto y unidad de compra

Se realizan comparaciones como:

- proyectos con mayores montos;
- montos por tipo de proyecto;
- montos por estado de proyecto;
- unidades de compra con mayor participación;
- unidades de compra con mayores montos acumulados.


## Resultado esperado

Al finalizar el notebook se obtiene una visión general de:

- la calidad y estructura de los datos;
- la distribución de proyectos y compras;
- la concentración de los montos;
- posibles valores atípicos;
- patrones entre tipos y estados de proyecto;
- comportamiento temporal de las compras;
- posibles inconsistencias que requieren validación adicional.

## Autor

Proyecto desarrollado como parte de un análisis exploratorio sobre el **Plan de Compras 2025**.
