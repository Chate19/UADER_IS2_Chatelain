# Respuestas Teóricas y Prácticas - TP10 Administración de Proyectos (Gestión)

## 2. Resolución de escenarios financieros del proyecto

Para evaluar los escenarios, primero se calcula el equilibrio financiero base que el proveedor acordó contractualmente. Con una tasa mensual del 1% (0.01), un costo equivalente a $1000 por 12 meses y un pago final acordado de $14000 en el mes 12, el Valor Presente Neto (VPN) base esperado por el proveedor es de $1,169.23. Cualquier modificación contractual debe mantener este VPN base para ser financieramente neutra.

*   **a. Pago diferido al mes 14:** Dado que el proyecto termina en el mes 12 y no se mantienen los equipos técnicos durante el tiempo adicional, los costos no cambian. La neutralidad financiera se logra aplicando el interés compuesto por los dos meses de retraso al monto original. El patrocinante deberá pagar **$14,281.40** en el mes 14 (calculado como 14000 * 1.01^2).
*   **b. Entrega en mes 6, pago en mes 12:** Para reducir el tiempo a la mitad por presiones del negocio, se asume que se condensa el esfuerzo, elevando el costo a $2000 mensuales durante 6 meses. El Valor Presente (VP) de estos nuevos costos es $11,590.95. Sumando el VPN base ($1,169.23), el proveedor requiere un VP de ingresos de $12,760.18 para no perder dinero. Llevando este valor al momento de pago en el mes 12, el patrocinante deberá pagar **$14,378.29** (calculado como 12760.18 * 1.01^12).
*   **c. Entrega en mes 6, pago en mes 6:** Manteniendo la aceleración del proyecto a 6 meses (costos de $2000/mes) y el VP de ingresos requerido de $12,760.18, el pago se efectúa al finalizar. Se proyecta este valor solo 6 meses hacia el futuro, por lo que el patrocinante deberá pagar **$13,545.24** (calculado como 12760.18 * 1.01^6) en el mes 6 para mantener el equilibrio financiero del proyecto.

---

## 3. ¿Por qué la relación de calendarización es solo válida para un equipo unipersonal?
La fórmula asume una relación perfectamente lineal e inversamente proporcional respecto a la asignación de recursos (si se duplica el personal, el tiempo se reduce a la mitad). En la práctica, agregar personal a un proyecto de software incrementa exponencialmente los canales de comunicación y la sobrecarga de coordinación (Ley de Brooks). Por tanto, la fórmula pura solo es válida matemáticamente para un equipo de 1 persona, donde el esfuerzo de comunicación interpersonal y sincronización es cero.

## 4. ¿Por qué la estimación de duración dada por la suma de tiempos es sólo válida en proyectos triviales?
La sumatoria simple asume que todas las tareas se ejecutan en una secuencia estrictamente serial, una detrás de la otra (secuencial monótona). En proyectos reales, las tareas forman una red de dependencias donde muchas actividades se ejecutan en paralelo. El tiempo total del proyecto no es la suma de sus partes, sino que está determinado por el camino crítico (la secuencia más larga de tareas dependientes).

## 5. Razón por la cual retrasar una tarea del camino crítico retrasa el proyecto inexorablemente.
Las tareas que conforman el camino crítico tienen, por definición, un margen de holgura igual a cero. Al carecer de este "colchón" de tiempo extra, cualquier retraso en su ejecución desplaza de forma directa e inmediata el inicio de las tareas sucesoras, impactando inexorablemente la fecha final de todo el proyecto.

## 6. ¿Cuál es la razón por la cual no es conveniente agregar recursos para acelerar una actividad con margen distinto de cero?
Un margen distinto de cero indica que la actividad tiene holgura y no se encuentra en el camino crítico del proyecto. Invertir recursos adicionales (presupuesto o personal) para acelerar esta tarea solo logrará que termine antes de lo necesario, aumentando su holgura, pero no adelantará la fecha de finalización global del proyecto, resultando en un desperdicio financiero y de esfuerzo.

## 7. Viabilidad de reducir el calendario en un 50% utilizando únicamente la técnica de clocking.
No es viable en la práctica. Reducir el calendario a la mitad basándose únicamente en horas extras (clocking) implicaría exigir jornadas laborales excesivas (ej. 16 horas diarias). Esto provoca un rápido agotamiento del equipo (burnout), lo que disminuye drásticamente la productividad, reduce la calidad del código y aumenta de forma exponencial la introducción de errores (bugs). El tiempo aparentemente ganado se perderá posteriormente en el retrabajo necesario para corregir dichos defectos.

## 8. Implementación de una consigna de "cero cambios" en un proyecto con fuertes restricciones financieras y calendario agresivo.
Aunque financieramente pueda parecer una medida de control atractiva, en la ingeniería de software es inviable y contraproducente. El software es intrínsecamente dinámico y los requisitos del negocio evolucionan; aplicar "cero cambios" podría resultar en la entrega de un producto que cumpla el contrato inicial pero que ya no aporte valor al negocio al momento de la entrega. En su lugar, el marco teórico sugiere implementar un proceso riguroso de control de cambios o utilizar técnicas ágiles de priorización del alcance para asegurar el valor dentro de las restricciones dadas.

## 9. Plan de contingencia por actividad sísmica en UADER, Sede Concepción del Uruguay.
Basado en el marco teórico de la gestión de riesgos, la prioridad de un riesgo se determina multiplicando su Probabilidad por su Impacto. Según los datos del INPRES, Concepción del Uruguay se encuentra en una zona de riesgo sísmico nulo o muy reducido, haciendo que la probabilidad tienda a cero. La teoría indica que los riesgos con probabilidad despreciable no justifican la inversión de recursos, tiempo y dinero en elaborar, mantener y auditar un plan de contingencia; en este caso, el riesgo simplemente se acepta.

## 10. Principal razón para transferir un riesgo en vez de intentar solucionarlo o mitigarlo.
Transferir un riesgo resulta deseable cuando otra organización (como una aseguradora o un proveedor especializado) posee mayor capacidad financiera, técnica o de infraestructura para absorber y gestionar dicho riesgo de manera más eficiente y económica que el propio equipo del proyecto. Esto se aplica cuando el costo de la transferencia es inferior al impacto financiero estimado si el riesgo llegara a materializarse, protegiendo así el capital del patrocinante.

## 11. Razón de controlar el trabajo del equipo y no a los trabajadores individuales.
Controlar el trabajo se centra en métricas objetivas del proceso (calidad, cumplimiento de hitos, entregables), lo que permite identificar cuellos de botella y mejorar el sistema en su conjunto. Controlar individualmente a las personas (micromanagement) deteriora la moral, fomenta una cultura de evasión de culpa y destruye la auto-organización y la sinergia, factores críticos para el éxito y la creatividad en los equipos de desarrollo de software modernos.

## 12. Evaluación de GitHub para la gestión de configuración.
GitHub satisface holísticamente las necesidades de la Gestión de Configuración de Software (SCM).

| Necesidad SCM | Función en GitHub | ¿Satisface? | Justificación |
| :--- | :--- | :---: | :--- |
| Identificación de Configuración | Repositorios, Commits (SHA) | Sí | Permite identificar unívocamente cualquier elemento en un punto exacto del tiempo. |
| Control de Versiones | Git (Ramas, Tags) | Sí | Gestiona el historial completo, permite ramificar para desarrollo paralelo y etiquetar releases. |
| Control de Cambios | Pull Requests, Issues | Sí | Obliga a la revisión de código y aprobación antes de integrar cambios al modelo base. |
| Auditoría de Estado | Insights, Blame, History | Sí | Provee trazabilidad total sobre quién cambió qué archivo, cuándo y con qué justificación. |
| Control de Acceso | IAM, Branch Protection | Sí | Permite definir permisos de lectura/escritura y bloquear alteraciones directas al código en producción. |

## 13. Diferencia entre modalidad "fábrica de software" y equipo de desarrollo convencional.
Un equipo operando bajo modalidad de fábrica de software se rige por principios industriales: estandarización extrema, procesos rígidos, métricas de volumen y alta especialización (separando estrictamente los roles de análisis, diseño, codificación y pruebas), tratando a los recursos como piezas intercambiables enfocadas en la eficiencia. En contraste, un equipo convencional de proyecto suele ser multidisciplinario, flexible y enfocado en la creatividad y la resolución holística de problemas complejos, donde la comunicación fluida y la adaptabilidad al cambio prevalecen sobre la rigidez del proceso.

## 14. Resolución de red de actividades, duraciones y caminos críticos
A partir de la tabla de tareas (A hasta J) y sus respectivas dependencias, el análisis de la red arrojó los siguientes resultados para cada escenario:

*   **Escenario A: Recursos Infinitos**
    *   **Condición:** Se asume que cada tarea requiere una persona para su realización de forma indivisible, lo que permite ejecutar en paralelo todas las tareas que tengan sus requisitos previos cumplidos.
    *   **Duración total del proyecto:** 47 días.
    *   **Camino Crítico:** La ruta más larga sin holgura está dada por la secuencia `A -> D -> H -> J`.

*   **Escenario B: Recursos Limitados (Staff de 2 personas)**
    *   **Condición:** Al disponer de un total de 2 personas como staff, se generan cuellos de botella por falta de disponibilidad. Esto obliga a secuenciar actividades que en el escenario anterior eran paralelas.
    *   **Duración total del proyecto:** 52 días.
    *   **Nuevo Camino Crítico:** La cadena crítica, ahora condicionada por los recursos, se modifica y pasa a ser la secuencia `A -> D -> E -> H -> J`.