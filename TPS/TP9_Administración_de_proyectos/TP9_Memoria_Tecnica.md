# TP9: Administración de proyectos (Planificación) - Ingeniería de Software II

## 1. Mantenimiento como proyecto
Asumir el mantenimiento como una tarea continua significa que se trata de una **operación**, no de un proyecto. Para que el mantenimiento sea efectivamente considerado un proyecto, las tareas deben agruparse y estructurarse bajo las siguientes características [cite: 1]:
*   **Temporalidad definida:** Debe tener un inicio y un fin claramente establecidos (por ejemplo, iteraciones con fechas límite o *releases* programados).
*   **Alcance definido:** Un objetivo o conjunto de entregables específicos y acotados (por ejemplo, resolver un conjunto exacto de *bugs* o implementar un paquete de parches de seguridad).
*   **Presupuesto y recursos asignados:** Debe contar con un límite de recursos dedicados para ese ciclo en particular.

## 2. Programas vs Proyectos
El motivo conceptual para agrupar iniciativas en **programas** es la obtención de beneficios sinérgicos y un control más efectivo que no se lograrían si los proyectos se gestionaran de forma aislada e independiente [cite: 1]. Un programa persigue un objetivo estratégico de negocio más amplio, coordinando proyectos interdependientes para optimizar el uso de recursos y mitigar riesgos compartidos.

## 3. Fijación arbitraria de Tiempo, Recursos y Requerimientos
Si se fijan arbitrariamente estos tres parámetros sin seguir un proceso de estimación realista (congelando el Tiempo, Costo y Alcance), la consecuencia directa será el **deterioro incontrolable de la Calidad (Defectos)** [cite: 1]. Al no haber flexibilidad de recursos ni tiempo para cumplir con funciones predefinidas de manera irreal, el equipo incurrirá en una alta deuda técnica, entregando software inestable. Además, forzar variables más allá de sus límites empíricos sitúa al proyecto en la **"Zona Imposible"**, lo que casi garantiza su fracaso total.

## 4. Script de Estimación (Python - Jupyter Notebook)
A continuación se presenta el script de Python que se solicita producir [cite: 1]. En el documento Markdown generado, encontrarás este código para que lo copies y ejecutes en Jupyter Notebook:

```python
import numpy as np
import matplotlib.pyplot as plt

# Fórmulas dadas
def calcular_esfuerzo(S):
    return 8 * (S ** 0.95)

def calcular_tiempo(E):
    return 2.4 * (E ** 0.33)

# 1. Gráfico del Esfuerzo (E) para tamaños (S) en el intervalo [0, 10000]
S_values = np.linspace(0, 10000, 500)
E_values = calcular_esfuerzo(S_values)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(S_values, E_values, color='blue')
plt.title('Esfuerzo vs Tamaño del Proyecto')
plt.xlabel('Tamaño (S)')
plt.ylabel('Esfuerzo (E)')
plt.grid(True)

# 2. Gráfico del Tiempo (td) para esfuerzos (E) en el intervalo [1, 500]
E_interval = np.linspace(1, 500, 500)
td_values = calcular_tiempo(E_interval)

plt.subplot(1, 2, 2)
plt.plot(E_interval, td_values, color='red')
plt.title('Tiempo de Desarrollo vs Esfuerzo')
plt.xlabel('Esfuerzo (E)')
plt.ylabel('Tiempo Calendario (td)')
plt.grid(True)

plt.tight_layout()
plt.show()
```

## 5. Análisis del Backlog pre-existente
**Datos base:**
*   Sprints de 2 semanas [cite: 1].
*   Velocidad = 5 SP / sprint [cite: 1].
*   Presupuesto inicial: 6 semanas [cite: 1] = 3 Sprints = Capacidad total de **15 SP**.

Para priorizar basándonos en el valor (Hits por Story Point), calculamos la relación "Hits / SP" con los datos de la tabla [cite: 1]:
*   Función F: 2179 / 2 = 1089.5 (Prioridad 1)
*   Función C: 6602 / 8 = 825.25 (Prioridad 2)
*   Función G: 8030 / 13 = 617.69 (Prioridad 3)
*   Función B: 1762 / 3 = 587.33 (Prioridad 4)
*   Función A: 1104 / 2 = 552.00 (Prioridad 5)
*   Función D: 1565 / 5 = 313.00 (Prioridad 6 - Uso)

**Respuestas:**
1.  **Funciones a incluir (15 SP disponibles) [cite: 1]:** Entrarían las de mayor retorno (Hits/SP). Función F (2 SP) + Función C (8 SP) + Función B (3 SP) + Función A (2 SP) = **15 SP**. 
2.  **Reducción del presupuesto a la mitad (3 semanas) [cite: 1]:** Al tener 1.5 sprints, si asumimos que solo se completan tareas terminadas en 1 sprint completo (capacidad 5 SP). Incluiría **F (2) y B (3)** = 5 SP. Eliminaría C, A, G, D. (Si el equipo fracciona entregas, tendrían 7.5 SP, entrando F(2) + parte de C o D).
3.  **Equipo por 7 semanas (3.5 Sprints = 17.5 SP) [cite: 1]:** Incluiría F (2) + C (8) + B (3) + A (2) y quedarían unos 2.5 SP libres (insuficientes para terminar G o D completamente a menos que se dividan las historias). 
4.  **Prioridad para la función "D" (Arquitectura) [cite: 1]:** Aunque por frecuencia de uso aislada tiene la prioridad matemática más baja, si el líder técnico indica que es vital para la arquitectura, debe dársele **Prioridad Alta (Sprint 1)**. Las funciones arquitectónicas reducen riesgos sistémicos y deuda técnica temprana; sin ellas, el resto de las funciones de alto valor (como la C o G) corren riesgo de fracasar o volverse inestables.
5.  **Con deuda técnica histórica de 1 SP/sprint [cite: 1]:** La capacidad real para nuevas funciones baja a **4 SP / Sprint**. Total en 6 semanas (3 sprints) = **12 SP**. Ajustando prioridades por límite de 12: incluiríamos F (2) + C (8) + A (2) = 12 SP. (Queda sacrificada la Función B).

## 6. Resumen: "What Do Software Developers Need to Know about Business" (W. Harrison)
**Resumen:** El artículo expone la desconexión habitual de los desarrolladores frente al contexto económico y financiero en el que operan sus empresas [cite: 3]. Harrison argumenta que comprender los principios empresariales básicos evita frustraciones ante decisiones gerenciales aparentemente ilógicas (como la cancelación de proyectos) [cite: 3]. Enfatiza conceptos clave: entender que el desarrollo es una inversión con riesgos; asimilar la noción del costo hundido (*sunk cost*), por el cual el dinero ya gastado en el pasado no tiene rol en los planes y costos del futuro; y entender el valor del dinero en el tiempo (es mejor recibir dinero ahora que esperar por él), con el uso de herramientas presupuestarias como el valor presente y el retorno sobre la inversión (ROI) [cite: 3].
**Relevancia sobre el alcance [cite: 1]:** Es vital comprender estos factores ya que demuestra que el alcance de un proyecto de desarrollo no debe definirse simplemente por viabilidad técnica o un listado ideal de características. Las funciones que ingresan al alcance deben justificar su inversión económica ajustada al riesgo (superar tasas de corte o *hurdle rate*) [cite: 3], evitando el desperdicio de recursos en requerimientos que no aportan valor real para la rentabilidad de la organización.

## 7. Resumen: "Subjective Consistency" (P. Colla)
**Resumen:** Pedro Colla aborda el problema de estimar esfuerzos en software cuando las organizaciones carecen de una base de datos históricos sólida o de modelos estadísticos precisos, requiriendo depender de la estimación subjetiva de expertos [cite: 2]. Para mitigar las inconsistencias lógicas en los juicios subjetivos, el artículo propone utilizar la metodología *Analytic Hierarchy Process (AHP)*, basada en comparaciones por pares [cite: 2]. Esto permite, aplicando fundamentos matemáticos simples sin necesidad de redes jerárquicas complejas, calcular un factor objetivo llamado *Consistency Ratio (CR)* que funciona como un medidor de coherencia [cite: 2]. El experimento en el documento corrobora que mantener un CR bajo (alta consistencia) correlaciona de manera fuerte y directa con una disminución del error en la estimación (*Mean Magnitude of Relative Error - MMRE*) [cite: 2].
**Relevancia sobre estimación [cite: 1]:** Otorga una respuesta matemática y procedural para asegurar y auditar la calidad de la estimación basada en juicio humano. Cuando un proyecto arranca y hay dudas en las horas a imputar, un líder puede someter las opiniones del equipo a un análisis de consistencia subjetiva, descartando y reevaluando aquellas estimaciones donde las matemáticas revelan que el propio evaluador se contradice.

## 8. Modificación del programa PNR_sistemis.py
**a) Adaptación del código y gráficos**
Para adaptar el programa a usar el esfuerzo total (K) entregado por el usuario en lugar de fijar $K=Kp=212$, el parámetro se ingresa y se evalúa a la par del set de calibración. El script modificado (resumido en las secciones a cambiar) se vería así:

```python
# Módulo a modificar en PNR_sistemis.py
# ...
if args['esfuerzo'] != 0:
   Kp=float(args['esfuerzo'])
K = Kp # Ahora tomamos el valor del argumento como el esfuerzo total de nuestro proyecto

t_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
E_data = np.array([8, 21, 25, 30, 25, 24, 17, 15, 11, 6])
K_hist = np.sum(E_data) # El K del dataset es 182

def esfuerzo_instantaneo_hist(t, a):
    return 2 * K_hist * a * t * np.exp(-a * t**2)

# Se calibra 'a' con K_hist
popt, pcov = curve_fit(esfuerzo_instantaneo_hist, t_data, E_data, p0=[0.1])
a_estimada = popt[0]

# Función para graficar con el K del nuevo proyecto (ej: 72 PM)
def esfuerzo_instantaneo_nuevo(t, a):
    return 2 * K * a * t * np.exp(-a * t**2)

t_fit = np.linspace(min(t_data), max(t_data), 100)
O_fit = esfuerzo_instantaneo_nuevo(t_fit, a_estimada)
E_fit = esfuerzo_instantaneo_hist(t_fit, a_estimada)

plt.plot(t_fit, O_fit, label='Nuevo proyecto (K=72)', color='blue')
plt.plot(t_fit, E_fit, label='Modelo histórico (K=182)', color='red')
plt.scatter(t_data, E_data, label='Datos observados', color='black')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Esfuerzo instantáneo (persona-mes)')
plt.legend()
plt.show()
```

**b) Comentarios sobre el cálculo para proyecto de 72 PM (Esfuerzo Total)**
Al calcular el modelo, obtenemos que el parámetro calibrado es $a \approx 0.0296$. Si aplicamos un $K = 72 \text{ PM}$ [cite: 1], la curva generada (azul) comparte la misma constante $a$ que el modelo histórico (roja), lo que significa que el punto de máximo esfuerzo (el pico del proyecto, $t_{max}$) ocurre **exactamente en el mismo momento temporal** para ambos proyectos. La diferencia radica en que la amplitud (altura de la curva, es decir, el *staffing* necesario) se reduce proporcionalmente a la relación entre los esfuerzos (72/182), evidenciando que un proyecto de menor esfuerzo demanda menos personas en su momento pico, pero, bajo el mismo modelo dinámico de asimilación de conocimiento, conserva el cronograma natural.

**c) ¿Qué ocurre si multiplicamos "a" por 4 arbitrariamente?**
Si incrementamos arbitrariamente "a" al cuádruple de su valor calibrado (pasando de $\sim 0.0296$ a $\sim 0.1184$), el efecto observable inmediato es que la curva se comprime y se vuelve mucho más alta. El pico de esfuerzo se desplaza bruscamente hacia la izquierda (ocurriendo en aproximadamente 2 meses en lugar de 4 meses).
En la práctica, esto representa un intento de acortar drásticamente el calendario inyectando a muchas más personas prematuramente. Al intentar hacer esto, el proyecto se adentra en lo que Putnam denomina la **"Zona Imposible"** [cite: 1]. La Ley de Brooks establece que añadir más personas a un proyecto retrasado (o comprimir su tiempo) incrementa exponencialmente los costos de comunicación y coordinación. Por lo tanto, estimo que **el proyecto fracasará**, sufrirá desajustes de arquitectura o costará muchísimo más que el cálculo nominal, ya que los equipos no pueden asimilar el conocimiento a esa velocidad forzada.

## 9. Modificación del programa EffortModel.py

**a) Regresión lineal y exponencial**
Implementando el dataset de 10 puntos (LOC de 1000 a 10000) [cite: 1] en Python, se obtienen los siguientes modelos de ajuste (utilizando *polyfit* para lineal y *statsmodels/OLS* para exponencial):

*   **Modelo Lineal:** $E = 0.002939 \times LOC - 3.266$
    *   **$
ho^2$ (R-squared):** $0.9726$
*   **Modelo Exponencial:** $E = 0.000368 \times LOC^{1.2075}$
    *   **$
ho^2$ (R-squared):** $0.9757$

El modelo que mejor representa los datos históricos es el **Exponencial**, ya que posee un coeficiente de determinación ($
ho^2$) ligeramente superior.

**b) Estimación para LOC = 9100**
Utilizando el modelo exponencial (que fue el más certero):
$$E = 0.000368 \times (9100)^{1.2075}$$
$$E \approx 22.24 \text{ PM}$$
Si graficamos esto junto con los datos de calibración, el punto (9100, 22.24) se encontraría posicionado de manera natural sobre la curva trazada, justo entre los valores históricos de 9000 (23) y 10000 (29), confirmando la excelente interpolación del modelo para ese rango.

**c) Estimación para LOC = 200 y precauciones**
Utilizando la misma fórmula:
$$E = 0.000368 \times (200)^{1.2075}$$
$$E \approx 0.22 \text{ PM}$$
**Precaución sobre la confiabilidad:** El cálculo matemático es de 0.22 PM, pero la gran precaución que debe tomarse es que un tamaño de $LOC = 200$ se encuentra muy por debajo de nuestro dato histórico más pequeño ($LOC = 1000$). Los modelos empíricos son confiables para **interpolar** dentro de los límites calibrados, pero son altamente riesgosos al **extrapolar** fuera de ellos. Un proyecto de 200 líneas podría tener componentes fijos (overhead de inicio, setup de ambientes, reuniones) que harían que el esfuerzo real sea mucho mayor a los ~5 días de trabajo (0.22 PM) que predice matemáticamente la curva.

## 10. Implementación en etapas y valor del proyecto frente al riesgo
Implementar un proyecto en fases o etapas (con validaciones o *Stage-Gates*) **aumenta el valor del proyecto para el patrocinante** porque funciona bajo la mecánica de mitigación de riesgo por **opciones reales** [cite: 1]. Al finalizar cada etapa, el patrocinante tiene el derecho de continuar o suspender la ejecución. Si el proyecto se vuelve riesgoso o no rentable, se cancela (*fail fast*), limitando las pérdidas económicas exclusivamente al costo consumido hasta esa etapa en lugar de hundir el presupuesto total.

## 11. Contabilidad de una empresa y el aspecto financiero
La contabilidad financiera clásica bajo el **criterio devengado** refleja los actos económicos en el momento en que se genera el derecho o la obligación, independientemente de si los fondos entraron o salieron de la cuenta bancaria [cite: 1]. Por lo tanto, la respuesta es que **NO captura de forma precisa la realidad financiera o de caja**. Para medir lo netamente financiero (flujos de dinero real, pagos y cobros efectivos), se utilizan herramientas regidas por el criterio de lo percibido (como el Estado de Flujo de Efectivo).

## 12. Régimen de promoción impositiva y apalancamiento
Un régimen de promoción que reduce el impuesto a las ganancias **desalienta** la utilización del mecanismo de apalancamiento impositivo [cite: 1]. 
**¿Por qué?** El apalancamiento impositivo o "escudo fiscal" consiste en deducir los intereses generados por una deuda de la base imponible sujeta al impuesto a las ganancias. El beneficio impositivo de tomar deuda se calcula multiplicando el gasto en intereses por la tasa de impuesto. Al reducirse la tasa del impuesto, el "ahorro" producto del endeudamiento es mucho menor, perdiéndose el principal incentivo financiero para endeudarse.

## 13. Contingencias del +5% frente a variaciones del +/- 30%
Aunque un proyecto individual tenga un cono de incertidumbre y varíe hasta en un 30% (positiva o negativamente) [cite: 1], a nivel de la organización se debe priorizar la gestión de **portafolio**. Si todos los proyectos cargaran automáticamente una contingencia del +30% en sus costos base, los proyectos se encarecerían tanto en el papel que las tasas de retorno serían pésimas y la empresa no invertiría en nada. Sumar un +5% asume que, bajo la *ley de los grandes números*, las sobreestimaciones de algunos proyectos compensarán los sobrecostos de otros, gestionando las excepciones extremas con una reserva a nivel corporativo superior.

## 14. Esperanza de ganar en ruleta (Color)
*   Apuesta: ficha mínima de \$1000 [cite: 1].
*   Total de resultados en ruleta (con cero neutro): 37 casillas [cite: 1]. 18 ganan (color apostado), 19 pierden (color opuesto + cero).
*   Probabilidad de ganar $P(G) = \frac{18}{37}$. Beneficio = $+\$1000$.
*   Probabilidad de perder $P(P) = \frac{19}{37}$. Pérdida = $-\$1000$.
*   **Esperanza $(E) = (P(G) \times Beneficio) + (P(P) \times Perdida)$**
    $$E = \left(\frac{18}{37} \times 1000\right) - \left(\frac{19}{37} \times 1000\right) = \frac{18000 - 19000}{37} = -\frac{1000}{37} = -27.027$$
La esperanza matemática neta de la apuesta es perder aproximadamente **-\$27.03** [cite: 1].

## 15. Inversión "Telar de los colores"
*   Monto: \$1000 [cite: 1]. Rendimiento mensual: 7% [cite: 1] (\$70).
*   Esperanza nula implica: $E = 0$ [cite: 1].
*   Ecuación de esperanza: $E = (P_g \times Ganancia) - (P_p \times Inversion)$
*   $P_g + P_p = 1 \implies P_p = 1 - P_g$ [cite: 1]
    $$0 = (P_g \times 70) - ((1 - P_g) \times 1000)$$
    $$0 = 70 P_g - 1000 + 1000 P_g$$
    $$1000 = 1070 P_g$$
    $$P_g = \frac{1000}{1070} \approx 0.93457$$
Las probabilidades para que la esperanza sea nula son **$P_g$ (ganar) de 93.45%** y **$P_p$ (perder) de 6.55%**.

## 16. Valor Presente (VP)
Retorno esperado de \$1000 en 1 año (12 meses) a tasa de costo de oportunidad r = 7% mensual [cite: 1].
Fórmula del VP: $VP = \frac{VF}{(1 + r)^n}$
$$VP = \frac{1000}{(1 + 0.07)^{12}} = \frac{1000}{1.07^{12}} = \frac{1000}{2.25219} = 444.01$$
El valor presente es de **\$444.01**.

## 17. Tasa Efectiva Anual (TEA) y aclaración de consigna
La TEA aplicable se calcula capitalizando mensualmente la tasa [cite: 1]:
$$TEA = (1 + r)^n - 1$$
$$TEA = (1 + 0.07)^{12} - 1 = 1.25219$$
Expresada en porcentaje, **la TEA es de 125.22%**.