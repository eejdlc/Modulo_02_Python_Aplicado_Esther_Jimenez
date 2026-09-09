# **Descripción del Proyecto**

Este proyecto construye un pipeline completo de procesamiento de datos  
usando Pandas: carga un dataset real, diagnostica nulos, limpia cada  
columna según su tipo, crea nuevas variables, ordena y analiza la  
información, y finalmente guarda un archivo limpio listo para análisis  
posteriores.

---

# **Preguntas de Razonamiento — Práctica de Pipeline**

## **Etapa 1 — ¿Por qué diagnosticar el dataset completo antes de limpiar nada en vez de empezar a limpiar directamente desde la primera columna que veas?**

*Respuesta:* 

Diagnosticar primero permite entender el estado real del dataset: cuántas  
filas hay, qué columnas tienen más nulos y qué tan grave es el problema.  
Si limpio sin revisar, podría eliminar demasiadas filas o rellenar  
columnas que casi no tienen nulos. El diagnóstico inicial evita errores  
y ayuda a planear la limpieza de forma lógica.

---

## **Etapa 2 — ¿Qué pasaría si rellenara Budget con 0 en vez de eliminar esas filas?
¿Cómo	afectaría	eso	a	la	columna	Ganancia	que	vas	a	crear	en	la próxima etapa?**

*Respuesta:*

Rellenar Budget con 0 implica asumir que esas películas no tuvieron  
costo de producción, lo cual es falso. Eso inflaría  la  columna Ganancia, 
porque estaría restando 0 en vez de un presupuesto  
real. Parecería que las películas fueron extremadamente rentables cuando  
solo estoy ocultando datos faltantes. Por eso, en este caso, eliminar  
esas filas es más honesto y más útil.

---

## **Etapa 3 — ¿Qué significaría dividir WorldGross entre Budget? ¿Qué	representaría,	en	cambio,	una	columna	que	dividiera	WorldGross	entre
Budget?	¿En	qué	caso	preferirías	esa	versión	en	vez	de	la	resta?**

*Respuesta:*

Dividir WorldGross entre Budget calcula el retorno por cada dólar  
invertido, una medida de rentabilidad proporcional (ROI).  
No muestra la ganancia total, sino cuántas veces recuperó su inversión.  
Esta versión es ideal cuando quiero comparar películas con presupuestos  
muy distintos, porque una producción pequeña puede ser más rentable  
proporcionalmente que una súper producción, aunque gane menos dinero en  
términos absolutos.

---

## **Etapa 4 — ¿Qué	habría	pasado	si	hubieras	intentado	ordenar	por	Ganancia	antes	de	limpiar	los	nulos	de	WorldGross	y	Budget	en	la	Etapa	2?	
¿Por	qué el	orden	en	que	se	hacen	las	etapas	importa	aquí?**

*Respuesta:*

Ordenar por Ganancia antes de limpiar produciría resultados incorrectos.  
La Ganancia depende de WorldGross y Budget, y si alguna tiene nulos,  
la operación genera NaN. Eso mezclaría películas completas con  
incompletas y podría causar errores. Primero se limpia, luego se calcula  
y finalmente se ordena.

---

## **Etapa 5 — De	los	géneros	con	más	películas	en	el	dataset	(Comedia,	Acción,	Drama),	
¿cuál	tiene	el	promedio de	calificación de	crítica	más	alto?	¿Te
sorprende,	o	era	lo	que	esperabas?**

*Respuesta:* 

Los géneros más comunes (Comedia, Acción y Drama) no necesariamente  
tienen el mejor promedio. Tienen mucha variedad: películas excelentes,  
regulares y malas. Un género con pocas películas puede tener un promedio  
más alto si esas pocas fueron muy bien evaluadas. No me sorprende ya que más  
cantidad no significa mejor calidad. En este caso, Drama es el género con mayor calificación, 
en este caso con 57.4 puntos en RottenTomatoes.

---

## **Etapa 6 — ¿Por	qué	guardar	el	resultado	en	un	archivo	nuevo	(hollywood_limpio.csv),	
en	vez	de	sobrescribir	el	archivo	original	hollywood.csv	que descargaste?**

*Respuesta:*

Guardar en un archivo nuevo conserva el dataset original.  
Si lo sobrescribo, pierdo la referencia inicial y ya no puedo repetir el  
proceso desde cero. Además, si cometo un error, no podría recuperar los  
datos originales. Guardar un archivo limpio separado es una buena  
práctica para mantener orden y trazabilidad de los cambios en la información.

---

# **Escenarios**

## **Escenario 1 — Si	el	dataset	tuviera	una	columna	de	fechas	completas	(día,	mes	y	año)	en	vez	de	solo	el	año,	
¿qué	tendrías	que	verificar	antes	de	poder	ordenar el	dataset	cronológicamente	por	esa	columna?**

*Resouesta:*

Si el dataset tuviera una columna con día, mes y año, antes de ordenar  
cronológicamente debo verificar que esté en formato datetime.  
Si está como texto, Pandas ordenaría alfabéticamente, no por fecha real.

---

## **Escenario 2 — Si	quisieras	aplicar	este	mismo	pipeline	a	un	dataset	completamente	distinto	
(por	ejemplo,	canciones	con	su	artista,	género	y	número	de reproducciones),	
¿qué	partes	de	tu	código	cambiarían,	y	cuáles	seguirían	exactamente	igual?**

*Respuesta:*

Si aplicara este pipeline a un dataset completamente diferente (por  
ejemplo, canciones con artista, género y reproducciones), cambiarían los  
nombres de las columnas y las reglas específicas de limpieza.  
Lo que se mantiene igual es la estructura del pipeline:  
cargar → diagnosticar → limpiar → transformar → analizar → guardar.

---

## **Escenario 3 — Si	una	columna	nueva	tuviera	95%	de	sus	valores	nulos	(mucho	peor	que	Genre,	que	tenía	cerca	del	29%),	
¿seguirías	rellenándola	de	la	misma forma?	¿Qué	harías	distinto,	y	por	qué?**

*Respuesta:*

Si una columna nueva tuviera 95% de nulos, rellenarla ya no tendría  
sentido porque la información es demasiado escasa.  
Lo más razonable sería eliminarla o evaluar si realmente aporta valor.  
Mantenerla podría introducir ruido en el análisis.

---
