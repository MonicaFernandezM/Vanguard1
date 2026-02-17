# Vanguard A/B Test 

## Description 
Este proyecto consiste en el análisis de un experimento A/B realizado por Vanguard para evaluar el impacto de un nuevo diseño de interfaz digital en el proceso online de los clientes.

El objetivo principal es determinar si el rediseño mejora el rendimiento del proceso mediante el análisis de KPIs clave como:
* Tasa de finalización
* Tiempo dedicado a cada paso
* Tasa de retrocesos (errores)
* Evaluación de rentabilidad (umbral del 5%)
* Tasa de abandono
* Impacto por segmento de edad

## Tabla de Contenidos
- [Instalación](#instalación)
- [Uso](#uso)
- [Dataset](#dataset)
- [Preguntas de Investigación](#preguntas-de-investigación)
- [Análisis](#análisis)
- [Resultados](#resultados)
- [Evaluación del Experimento](#evaluacion-del-experimento)
- [Contribución](#contribución)

## Instalación
1. Clonar el repositorio:
   git clone https://github.com/MonicaFernandezM/Vanguard1

2. Abrir el proyecto en Jupyter Notebook.

3. Ejecutar el notebook principal para reproducir el análisis.

Dependencias principales:
* pandas
* numpy
* scipy
* statsmodels
* matplotlib
* seaborn

## Uso 
* Abrir el notebook del proyecto.
* Ejecutar las celdas en orden.
* Revisar los resultados estadísticos y conclusiones.

El análisis está organizado en secciones:
1. Limpieza y preparación de datos
2. Creación del dataset maestro
3. Cálculo de KPIs
4. Pruebas de hipótesis
5. Análisis avanzado (efecto, potencia, segmentación)

## Dataset

El análisis integra cuatro datasets:
* df_exp_clients → Asignación experimental (Control / Test)
* df_web1 y df_web2 → Eventos web (interacciones por visita)
* df_demo → Información demográfica y financiera del cliente

Variables clave utilizadas:
* client_id
* Variation (Control/Test)
* process_step
* date_time
* clnt_age
* bal
* logons_6_mnth

Los datos fueron limpiados para:
* Eliminar duplicados
* Estandarizar client_id
* Eliminar valores nulos críticos
* Filtrar visitas válidas (que comienzan en “start”)

## Preguntas de Investigación
- ¿El nuevo diseño aumenta la tasa de finalización?
- ¿El incremento supera el umbral económico del 5%?
- ¿El nuevo diseño reduce la tasa de abandono?
- ¿El rediseño mejora la eficiencia del proceso (tiempo total)?
- ¿El efecto es mayor en clientes jóvenes?
- ¿Existen diferencias en el número de pasos por visita?
- ¿Fue el experimento suficientemente potente?

## Análisis realizado
El proyecto incluye:
* Limpieza y consolidación de datos
* Construcción del dataset maestro (df_master)
* Cálculo de tasa de finalización por visita
* Prueba Z de proporciones (A/B test)
* Cálculo de intervalo de confianza
* Evaluación de umbral de rentabilidad (5%)
* Cálculo de tasa de abandono
* Análisis de tiempo por paso
* Identificación de retrocesos
* Regresión logística con interacción (edad × variación)
* Cálculo de tamaño del efecto (Cohen’s h)
* Análisis de potencia post-hoc
* Cálculo de tamaño mínimo de muestra

## Resultados 

### Tasa de Finalización

El grupo Test presentó una tasa de finalización mayor que el grupo Control.
* Diferencia estadísticamente significativa (p-value < 0.05)
* Se rechaza H0: p_test = p_control

Conclusión:
El nuevo diseño mejora significativamente la conversión.

### Umbral de Rentabilidad (5%)

Aunque el incremento fue estadísticamente significativo:
* El lift observado fue aproximadamente +2.5%
* No alcanza el umbral económico mínimo del 5%

Conclusión:
Desde perspectiva financiera, el rediseño no justifica aún su implementación.

### Tasa de Abandono
* El grupo Test redujo el abandono en aproximadamente −5.8 puntos porcentuales.
* Diferencia estadísticamente significativa.

Conclusión:
El nuevo diseño reduce la fricción en el proceso.

### Tiempo por Paso

El rediseño:
* Es más rápido en algunos pasos intermedios.
* Es significativamente más lento en el paso final (“confirm”).

Esto sugiere posible fricción en la etapa de confirmación.

### Tasa de Retrocesos
* Test: 27.1% de visitas con retroceso
* Control: 20.6%

El nuevo diseño presenta mayor proporción de retrocesos

### Segmentación por Edad

Se utilizó regresión logística con interacción:

completed ~ Variation + young + Variation:young

El efecto del rediseño es mayor en clientes jóvenes.

### Tamaño del Efecto y Potencia
* Se calculó Cohen’s h.
* La potencia post-hoc indicó que el experimento estuvo sobredimensionado.
* Tamaño mínimo requerido por grupo: ~1,569 usuarios.

## Evaluación del Experimento

- ¿Estuvo bien estructurado?\
Sí.
* Asignación clara a Control/Test.
* Balance adecuado entre segmentos.
* Gran tamaño muestral.

- ¿Hubo sesgo?
No se detectan desequilibrios relevantes en variables demográficas.

- ¿Fue adecuada la duración?

Sí.\
Periodo del experimento: 15/03/2017 – 20/06/2017.\
Tiempo suficiente para obtener estabilidad estadística.

## Contribución

Las contribuciones son bienvenidas.

Si deseas mejorar el análisis o añadir nuevas visualizaciones:
	1.	Haz un fork del repositorio.
	2.	Crea una nueva rama.
	3.	Realiza tus cambios.
	4.	Abre un Pull Request.