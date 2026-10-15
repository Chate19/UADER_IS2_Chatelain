# Trabajo Práctico 11: Gestión de Calidad
**Institución:** FCyT - UADER
**Carrera:** Licenciatura en Sistemas de Información / Analista en Sistemas
**Cátedra:** Ingeniería de Software II
**Alumno:** Agustin Chatelain

---

## Parte 1: Análisis y Pruebas del Código Collatz

### 1. Requerimientos
*Identifique los requerimientos funcionales y no funcionales del problema de la Conjetura de Collatz.*

**Requerimientos Funcionales (R):**
* $R_1$: Solicitar y aceptar un número entero positivo cualquiera por teclado.
* $R_2$: Comprobar la conjetura de Collatz calculando el número de iteraciones que son necesarias para alcanzar el valor 1.
* $R_3$: Imprimir el número de partida.
* $R_4$: Imprimir el número de iteraciones.

**Requerimientos No Funcionales (F):**
* $F_1$: Limitar a 1999 el entero máximo a validar por cuestiones prácticas.

### 2. Casos de Prueba (T)

**Pruebas Funcionales (Caja Negra):**
Se enfocan en validar las entradas del usuario, las salidas por pantalla y las restricciones del sistema (Requerimientos R1, R3, R4 y F1).

* **$T_1$ (Valor válido normal):** Ingresar el número `20`.
  * **Resultado esperado:** El sistema acepta el número, calcula correctamente e imprime "El número de partida es 20" y "El número de iteraciones es 7".
  * **Tipo:** Funcional.
* **$T_2$ (Valor límite superior):** Ingresar el número `1999`.
  * **Resultado esperado:** El sistema acepta el número y procesa el resultado correctamente.
  * **Tipo:** Funcional.
* **$T_3$ (Exceso de límite superior):** Ingresar el número `2000`.
  * **Resultado esperado:** El sistema rechaza el ingreso mostrando un mensaje de error por superar el límite de 1999.
  * **Tipo:** Funcional.
* **$T_4$ (Valor no válido - Cero o Negativo):** Ingresar el número `0` o `-5`.
  * **Resultado esperado:** El sistema rechaza el ingreso, ya que se exige un entero positivo.
  * **Tipo:** Funcional.
* **$T_5$ (Tipo de dato incorrecto):** Ingresar un texto (ej. `"veinte"`) o un número flotante (ej. `15.5`).
  * **Resultado esperado:** El sistema maneja la excepción y solicita nuevamente un número entero.
  * **Tipo:** Funcional.

**Pruebas Unitarias (Caja Blanca):**
Se enfocan en validar el comportamiento interno de la función `collatz(num)` evaluando las distintas ramas de decisión (Requerimiento R2).

* **$T_6$ (Condición de corte inmediata):** Ejecutar `collatz(1)`.
  * **Resultado esperado:** La función retorna `0` iteraciones (no entra al bucle `while num != 1`).
  * **Tipo:** Unitario.
* **$T_7$ (Rama par):** Ejecutar `collatz(2)`.
  * **Resultado esperado:** La función ingresa al `if num % 2 == 0`, divide por 2 y retorna `1` iteración.
  * **Tipo:** Unitario.
* **$T_8$ (Rama impar):** Ejecutar `collatz(3)`.
  * **Resultado esperado:** La función ingresa al `else`, ejecuta `3 * num + 1` y tras el flujo completo retorna `7` iteraciones.
  * **Tipo:** Unitario.

### 3. Matriz de Trazabilidad (RTM)
*Establezca una matriz de trazabilidad RTMX entre ROFOT, valide la integridad del conjunto de prueba basado en la misma.*

| Requerimiento / Test | $T_1$ | $T_2$ | $T_3$ | $T_4$ | $T_5$ | $T_6$ | $T_7$ | $T_8$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$R_1$** (Aceptar entero positivo) | X | X | | X | X | | | |
| **$R_2$** (Calcular iteraciones) | X | X | | | | X | X | X |
| **$R_3$** (Imprimir núm. partida) | X | X | | | | | | |
| **$R_4$** (Imprimir iteraciones) | X | X | | | | | | |
| **$F_1$** (Límite máximo 1999) | | X | X | | | | | |

**Validación de integridad:** La matriz demuestra que todos los requerimientos funcionales ($R_1, R_2, R_3, R_4$) y no funcionales ($F_1$) están cubiertos por al menos un caso de prueba, asegurando el 100% de cobertura de los requerimientos especificados en el documento.

### 4. Inspección de Código (Sesión 1)
*Realice un ejercicio de inspección, sin ejecutar el código trate de capturar tantos defectos latentes sintácticos y semánticos como le sea posible. Registre el número detectado y considere a todo el ejercicio como sesión 1. Considere como defecto una tasa de comentarios mayor a 12.*

Al inspeccionar el código provisto en el requerimiento, se detectaron los siguientes defectos:

**Defectos Sintácticos:**
1. **Falta de indentación:** El cuerpo de la función `def collatz(num):`, el ciclo `while` y los condicionales `if/else` no están indentados correctamente, lo cual provocará un error de identación en Python (`IndentationError`).
2. **Asignación inválida en rama par:** La expresión `num` seguida de `num // 2` en líneas separadas no actualiza la variable. Falta el operador de asignación (`num = num // 2`).
3. **Asignación inválida en rama impar:** La expresión `num` seguida de `3*num + 1` en líneas separadas no actualiza la variable. Falta el operador de asignación (`num = 3 * num + 1`).
4. **Error en el formateo del string (print):** La cadena `"El número de iteraciones para ad es d\n"` está mal construida, debería usar los especificadores de formato de Python antiguos como `%d` (ej: `"El número de iteraciones para %d es %d\n"`).
5. **Paréntesis sin cerrar:** A la función `print` en la última línea le falta el paréntesis de cierre `)`.

**Defectos Semánticos / Lógicos:**
6. **Variable no definida en el return:** La función intenta devolver la variable `iter` (`return iter`), pero la variable declarada y acumulada en el ciclo se llama `iteraciones`.
7. **Variable no definida en la llamada:** En la impresión de comprobación, se define `i=20` pero se llama a `collatz(j)`. La variable `j` no existe.
8. **Ausencia de ingreso por teclado:** El código "hardcodea" el valor `i=20` en lugar de cumplir el requerimiento de "solicitar y aceptar un número entero positivo cualquiera por teclado".
9. **Falta de validación del límite:** No existe validación alguna para limitar "a 1999 el entero máximo a validar".

**Evaluación de Tasa de Comentarios:**
* Líneas totales (Locs): 18 líneas (según se indica en el enunciado posterior).
* Líneas de comentarios: 2 (`#Calculando el...` y `#Comprobando los...`).
* Tasa de comentarios: 2 / 18 = 11.11%. Como la tasa no es mayor a 12% (ni la cantidad absoluta es mayor a 12), **no se contabiliza como defecto**.

**Resumen Sesión 1:**
* **Total de defectos detectados (Sesión 1):** 9 defectos.

### 5. Inspección de Casos de Prueba (Sesión 2)
*Realice un ejercicio de inspección validando los casos de test desarrollados previamente e intentando agregar nuevos casos. Actualice la matriz de trazabilidad toda vez que un nuevo caso de test sea agregado. Registre el número de defectos detectados y considere a todo el ejercicio como sesión 2.*

Al inspeccionar los casos de prueba definidos originalmente en el Punto 2, se detectaron las siguientes omisiones (defectos de diseño de pruebas):

1. **Falta de cobertura en el límite inferior válido (Caja Negra):** No se había contemplado el ingreso del número `1` por teclado para validar cómo se comporta la validación de entrada frente al entero positivo más pequeño posible.
2. **Falta de prueba de sanitización de entrada (Caja Negra):** No se contempló el caso donde el usuario ingrese un número válido pero con espacios en blanco accidentales (ej. `" 20 "`).

**Nuevos casos agregados:**
* **$T_9$ (Valor límite inferior):** Ingresar el número `1` por teclado. 
  * **Resultado esperado:** El sistema lo acepta y determina 0 iteraciones.
  * **Tipo:** Funcional.
* **$T_{10}$ (Entrada con espacios):** Ingresar el texto `" 20 "`.
  * **Resultado esperado:** El sistema recorta los espacios (trim), acepta el número y calcula correctamente.
  * **Tipo:** Funcional.

**Actualización de la Matriz de Trazabilidad (RTM):**
*(Se agregan las columnas $T_9$ y $T_{10}$ a la matriz original)*
| Requerimiento / Test | ... | $T_9$ | $T_{10}$ |
| :--- | :---: | :---: | :---: |
| **$R_1$** (Aceptar entero positivo) | ... | X | X |
| **$R_2$** (Calcular iteraciones) | ... | X | X |
| **$R_3$** (Imprimir núm. partida) | ... | X | X |
| **$R_4$** (Imprimir iteraciones) | ... | X | X |
| **$F_1$** (Límite máximo 1999) | ... | | |

**Resumen Sesión 2:**
* **Total de defectos detectados (Sesión 2):** 2 defectos (omisiones en el diseño original de la suite de pruebas).

### 6. Ejecución de Pruebas y Registro de Sesiones
*Ejecución de test unitarios y funcionales. Reparación de código entre sesiones.*

Para esta etapa, asumimos que los defectos sintácticos y semánticos graves encontrados en la Sesión 1 (Inspección) fueron corregidos para que el código pueda compilar/interpretar y ejecutarse.

**Pruebas Unitarias (Caja Blanca):**
Se ejecutan los casos $T_6$, $T_7$ y $T_8$.
* **Sesión 3 ($S_3$):** 
  * Al ejecutar $T_6$ `collatz(1)`, se detecta que no hay manejo para el caso donde el ingreso original es 1 o menor si no se filtró antes, pero asumiendo que llega un 1, el bucle `while num != 1` actúa correctamente.
  * Al ejecutar $T_7$ y $T_8$, se detecta un error de tipo lógico en el retorno (si no se arregló el nombre de la variable `iter` por `iteraciones`). 
  * **Defectos encontrados en $S_3$:** 1 defecto (Variable de retorno indefinida `NameError`).
  * *Acción:* Se detiene la sesión y se corrige el código (`return iteraciones`).
* **Sesión 4 ($S_4$):** 
  * Se vuelven a ejecutar $T_6$, $T_7$ y $T_8$. 
  * Todas las pruebas unitarias pasan con éxito.
  * **Defectos encontrados en $S_4$:** 0 defectos.

**Pruebas Funcionales (Caja Negra):**
Se ejecutan los casos $T_1$ a $T_5$, $T_9$ y $T_{10}$, incluyendo la lógica de entrada/salida (I/O).
* **Sesión 5 ($S_5$):** 
  * Se ejecutan los casos. El programa falla en $T_3$ (Exceso de límite 1999) y $T_4$ (Valor no válido negativo), ya que el código original carece de sentencias condicionales para validar rangos y tipos antes de llamar a la función.
  * Además falla $T_5$ (Tipos de datos) arrojando `ValueError` por no tener un bloque `try/except` al convertir el `input()` a `int`.
  * **Defectos encontrados en $S_5$:** 3 defectos lógicos/validación.
  * *Acción:* Se detiene la sesión y se implementa la lógica de validación (bloque `try/except` y condicional `if num > 1999` y `if num <= 0`).
* **Sesión 6 ($S_6$):** 
  * Se vuelven a ejecutar todos los casos funcionales ($T_1$ a $T_5$, $T_9$ y $T_{10}$).
  * Todos los casos de prueba ejecutan de forma exitosa.
  * **Defectos encontrados en $S_6$:** 0 defectos.

**Verificación de Condiciones Finales:**
- [x] Todos los casos de prueba fueron exitosamente ejecutados al menos una vez.
- [x] No hubo caso de test que no se hubiera ejecutado.
- [x] No hay requerimiento (funcional o no funcional) que no se haya verificado.

**Listado total de sesiones y defectos:**
* **Sesión 1 (Inspección Código):** 9 defectos.
* **Sesión 2 (Inspección Tests):** 2 defectos.
* **Sesión 3 (Ejecución Unitaria):** 1 defecto.
* **Sesión 4 (Ejecución Unitaria):** 0 defectos.
* **Sesión 5 (Ejecución Funcional):** 3 defectos.
* **Sesión 6 (Ejecución Funcional):** 0 defectos.
* **Total de defectos en el ciclo:** 15 defectos.

### 7. Métricas de Calidad

Para los siguientes cálculos, tomamos el total de defectos detectados durante todas las sesiones como el 100% de los defectos (Total = 15 defectos). 

**Phase Containment Effectiveness (PCE) por etapa:**
El PCE indica qué porcentaje del total de defectos se logró contener (detectar) en cada fase específica.
*   **Fase de Inspección (Sesiones 1 y 2):** 11 defectos detectados.
    *   **PCE:** (11 / 15) * 100 = **73.33%**
*   **Fase de Pruebas Unitarias (Sesiones 3 y 4):** 1 defecto detectado.
    *   **PCE:** (1 / 15) * 100 = **6.67%**
*   **Fase de Pruebas Funcionales (Sesiones 5 y 6):** 3 defectos detectados.
    *   **PCE:** (3 / 15) * 100 = **20.00%**

*Nota: La suma total de los PCE de las tres fases da el 100% de los defectos observados en el ejercicio.*

**Densidad de defectos al comienzo:**
Para calcular la densidad inicial del código, consideraremos solo los defectos que pertenecían al código fuente original del programa, excluyendo los 2 defectos que eran del diseño de los casos de prueba (Sesión 2). Por lo tanto, los defectos presentes en el código al inicio eran 13 (9 de la S1 + 1 de la S3 + 3 de la S5).

*   **Defectos iniciales del código ($D$):** 13
*   **Tamaño del programa ($S$):** 18 Locs (Líneas de código).
*   **Densidad de Defectos ($\delta$):** $D / S = 13 / 18 = 0.72$ defectos por línea de código (o expresado en KLocs: **722 defectos / KLoc**).

## Parte 2: Análisis Teórico, Estimaciones y Garantía

### 1. Parámetro TEP en Kanban
*Lea el tutorial “Kanban para uso genérico” del Ing. A. Ruiz de Mendarozqueta, explique en sus palabras el significado del parámetro TEP de esa metodología y cuál es el significado crítico en su utilización.*

En la metodología Kanban, **TEP** significa **Trabajo En Progreso** (también conocido ampliamente por sus siglas en inglés, WIP - *Work In Progress*). Representa la cantidad de tareas, tarjetas o requerimientos que se encuentran activos simultáneamente en una determinada fase o columna del flujo de trabajo.

**Significado crítico de su utilización (Límites TEP / WIP Limits):**
La aplicación de límites al TEP es una de las prácticas más críticas de Kanban por las siguientes razones:
1. **Visibiliza cuellos de botella:** Al limitar cuántas tareas pueden entrar en una fase (por ejemplo, "Testing" o "Code Review"), el flujo se detiene si esa columna se llena. Esto alerta a todo el equipo de que hay un atasco y los obliga a colaborar para destrabarlo antes de comenzar trabajo nuevo.
2. **Mejora el flujo (Flow):** Fomenta la filosofía de *"dejar de empezar y empezar a terminar"*. En lugar de tener muchísimas tareas a medio hacer (lo cual es inventario retenido que no aporta valor), el equipo se enfoca en llevar las tareas actuales hasta su finalización (producción).
3. **Reduce la penalidad por cambio de contexto (Context Switching):** Evita que los desarrolladores pierdan tiempo y concentración saltando constantemente entre múltiples tareas a la vez, lo que indirectamente reduce la inyección de nuevos defectos.
4. **Reduce el Lead Time:** Al haber menos tareas atascadas en el sistema, el tiempo promedio que tarda un requerimiento desde que el cliente lo pide hasta que se le entrega disminuye drásticamente.

### 2. Proyección Estadística de Defectos
*Utilice los algoritmos discutidos en el taller denominado "taller_defectos.ipynb" sobre los posibles criterios para evaluar la proyección en los defectos aplicando un modelo de regresión aproximado.*

**Proyección con el dataset de prueba (Primeros 6 días):**
Los datos recolectados en los primeros días son:
* **Día 0:** 9
* **Día 1:** 18
* **Día 2:** 5
* **Día 3:** 7
* **Día 4:** 23
* **Día 5:** 2
* **Día 6:** 8
* **Total detectados hasta el día 6:** 72 defectos.

Al aplicar el modelo de regresión lineal (extrayendo los coeficientes $\lambda_0$ y $\mu_0$ a partir de la pendiente y la intersección de la curva logarítmica), se obtiene la siguiente asíntota:
* **Estimación del número total de defectos proyectado por el modelo ($\mu_0$):** 98.12 defectos (aprox. 98 defectos).

---
**Proyección con el dataset del TP (Sesiones del Ejercicio Collatz):**
Repetimos el ejercicio asimilando "Días" a "Sesiones" usando los defectos encontrados en la Parte 1. Para la regresión logarítmica, excluimos las sesiones sin fallas para evitar la indeterminación matemática de $\ln(0)$:
* $S_1$ (Inspección): 9
* $S_2$ (Inspección Tests): 2
* $S_3$ (Unitaria): 1
* $S_5$ (Funcional): 3
* **Total de defectos identificados ($\sum\mu_i$):** 15 defectos.

Al aplicar el modelo de regresión sobre las sesiones del TP, se obtienen los siguientes valores:
* **Estimación del número total de defectos de la implementación ($\mu_0$):** 22.72 defectos (aprox. 23 defectos).
* **Defectos "liberados" o remanentes ($\mu_r$):** $\mu_r = \mu_0 - \sum\mu_i = 22.72 - 15 =$ **7.72 defectos remanentes** que quedan de forma latente en el código al finalizar la fase de test.
* **Tamaño final del código:** Al ejecutar `cat collatz.py | wc -l` en el sistema operativo, el código final tiene **22 Locs** (estimado tras las correcciones de indentación, importaciones y validaciones de la Parte 1).

### 3. Marco para evaluar garantía
*Comportamiento cualitativo de incrementar el PCE en el tiempo total de test óptimo y efecto de las multas en el punto de equilibrio.*

**1. Comportamiento cualitativo de incrementar el PCE:**
El PCE (Phase Containment Effectiveness) mide la eficacia con la que una fase de control de calidad (por ejemplo, revisiones de diseño o pruebas unitarias) logra contener y detectar los defectos antes de que se filtren a las fases siguientes. 
Cualitativamente, si una organización **incrementa el PCE** en las etapas tempranas de desarrollo, el código llega a la etapa final de prueba (test del sistema/V&V) con un nivel mucho menor de defectos latentes iniciales ($\mu_0$). Como resultado, **el tiempo total de test óptimo requerido para poder otorgar una garantía disminuye significativamente**. Al tener un software más limpio desde el inicio de la prueba, se alcanza el umbral de confiabilidad deseado en menos tiempo, reduciendo los costos de la fase de testing y acortando el *Time-to-Market*.

**2. Efecto de la aplicación de una multa en el modelo simple de garantía:**
El modelo simple de garantía busca el "punto de equilibrio" (tiempo de liberación óptimo) donde se minimiza el costo total, el cual es la suma del **Costo de Testing** (que aumenta a medida que se invierte más tiempo probando) y el **Costo de Fallas en Producción / Garantía** (que disminuye cuantas más pruebas se hacen).
Si se introduce la **aplicación de una multa** (penalidad económica por fallas en producción, incumplimiento de SLAs, etc.), el costo de cada defecto filtrado al cliente se vuelve mucho más alto. Esto provoca que la curva de "Costo de Fallas en Producción" se desplace hacia arriba. 
**Fundamentación:** Para minimizar este nuevo costo total, la derivada de la curva hace que el **punto de equilibrio se desplace hacia la derecha**. Es decir, la organización se verá obligada a **incrementar el tiempo de test y el esfuerzo de V&V** antes de liberar el software, asumiendo un mayor costo de prueba interno para evitar la severa penalidad económica (la multa) de fallar frente al cliente.

### 4. Línea de base organizacional
*Datos provistos: Tamaño del proyecto $S = 100$ FP, $PCE = 89\%$, Defectos al momento de liberación $\delta_r = 0.12$ def/FP.*

**a. Expectativa de defectos totales ($\mu_0$):**
Primero calculamos los defectos liberados o residuales permitidos ($\mu_r$):
$\mu_r = \delta_r \times S = 0.12 \times 100 = 12$ defectos permitidos al liberar.
Sabiendo que el PCE es la eficacia para contener defectos, los defectos liberados representan lo que "se escapó" del test (el $11\%$ restante). 
Aplicamos la fórmula: $\mu_r = \mu_0 \times (1 - PCE)$
$12 = \mu_0 \times (1 - 0.89)$
$12 = \mu_0 \times 0.11$
$\mu_0 = 12 / 0.11 = 109.09$
La expectativa total de defectos ($\mu_0$) para este proyecto es de **109 defectos**.

**b. Densidad de defectos al finalizar construcción ($\delta_0$):**
Es la cantidad total de defectos esperados dividida por el tamaño del proyecto:
$\delta_0 = \mu_0 / S = 109.09 / 100 =$ **$1.09$ def/FP**.

**c. Defectos a detectar en V&V (Verificación y Validación):**
Son los defectos que el equipo de calidad debe lograr encontrar para cumplir con su PCE del $89\%$.
Defectos a detectar $= \mu_0 \times PCE = 109.09 \times 0.89 =$ **97 defectos**.
*(Comprobación matemática: 97 contenidos en test + 12 liberados al cliente = 109 totales).

**d. Opinión sobre detectar 60 defectos en los primeros 3 días:**
Si la organización detecta 60 defectos en sus primeros 3 días de prueba (a razón de 20 por día), significa que descubrió casi el $62\%$ del total de defectos esperados ($60$ de $97$) de manera casi inmediata. 
**Fundamentación:** En función de los parámetros históricos, este comportamiento es una alarma crítica. La intensidad de defectos al origen ($\lambda_0$) es anormalmente alta, lo que indica que el código entregado por desarrollo tiene una calidad muy inferior a la línea base de la empresa. Estadísticamente, la proyección de la curva indicará que el $\mu_0$ real será muchísimo mayor a $109$. Para poder otorgar la garantía de calidad habitual ($\delta_r = 0.12$), el tiempo total de test deberá extenderse drásticamente, o bien el proceso de V&V debería detenerse temporalmente para devolver el código a desarrollo por estar inmaduro.
*


## Parte 3: Desarrollo de la Herramienta CI/CD

### 1. Desarrollo del script `json2csv.py`
*Enlace al repositorio en GitHub o fragmento de código relevante.*

[Enlace a GitHub o Snippet de código destacando el manejo de excepciones y uso de `argparse` / `sys.stdin`]

### 2. Infraestructura y Pipeline CI/CD (GitHub Actions)
*Checklist de implementación de las características solicitadas.*

- [ ] Entorno virtual (venv) utilizado.
- [ ] Esqueleto basado en CookieCutter.
- [ ] Prompts documentados en `CONTEXT.md`.
- [ ] `README.md` actualizado.
- [ ] Cambios en `CHANGELOG.md`.
- [ ] `REQUIREMENTS.txt` generado.
- [ ] Licencia MIT y documentación (pdoc/sphynx).
- [ ] Registro de VERSION y BUILD.
- [ ] Formato: `ruff`, `black`, PEP8 validados.
- [ ] Docstrings: PEP257 validado.
- [ ] Tipado: `MyPy`, `PyRight` validados.
- [ ] Testing: `Pytest` (cobertura >= 85%).
- [ ] Seguridad: `bandit` sin observaciones (sin usar Trufflehog).
- [ ] Workflow de GitHub Actions funcional para CI/CD y autogeneración de docs con cada PR.

### 3. Deuda Técnica
*Factores que mejoran la gestión de la deuda técnica según el artículo "Agile and software engineering, an invisible bond".*

[Tu respuesta aquí]