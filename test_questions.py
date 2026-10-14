# -*- coding: utf-8 -*-
import json

questions = [
    # =========================================================================
    # UNIDAD I: INTRODUCCIÓN A LA INGENIERÍA DE SOFTWARE (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 1,
        "q": "¿Qué es el software profesional según Ian Sommerville?",
        "options": [
            "a) Cualquier código fuente ejecutable compilado sin advertencias",
            "b) Programas de cómputo y toda su documentación asociada (manuales, diseño, pruebas)",
            "c) Aplicaciones diseñadas exclusivamente para clientes corporativos de gran escala",
            "d) Algoritmos matemáticos implementados en hardware de propósito específico"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 5) establece que el software profesional no es sólo código, sino programas más su documentación asociada de requerimientos, diseño del sistema y especificaciones de pruebas."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 2,
        "q": "¿Cómo define Sommerville a la Ingeniería de Software en comparación con las Ciencias de la Computación?",
        "options": [
            "a) La ingeniería de software estudia las teorías matemáticas abstractas, mientras las ciencias de la computación crean los productos",
            "b) La ingeniería de software es una disciplina de ingeniería enfocada en el sentido práctico de la producción de software de calidad",
            "c) Son disciplinas idénticas y sinónimas en el ámbito universitario",
            "d) La ingeniería de software solo se ocupa de la codificación y las ciencias de la computación del hardware"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 6) aclara que las ciencias de la computación se enfocan en teoría y fundamentos, mientras la ingeniería de software es una disciplina de ingeniería que se enfoca en todos los aspectos prácticos de la producción de software."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 3,
        "q": "¿Cuáles son los cuatro atributos esenciales de un buen software profesional (Figura 1.2)?",
        "options": [
            "a) Velocidad, Bajo precio, Interfaz gráfica y Tamaño reducido",
            "b) Mantenibilidad, Confiabilidad y Seguridad, Eficiencia y Aceptabilidad",
            "c) Complejidad, Portabilidad absoluta, Licencia propietaria y Concurrencia",
            "d) Código abierto, Arquitectura monolítica, Modularidad estricta y Algoritmia avanzada"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 8, Fig. 1.2) define formalmente cuatro atributos esenciales: Mantenimiento (Mantenibilidad), Confiabilidad y seguridad, Eficiencia y Aceptabilidad."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 4,
        "q": "¿Qué suceso histórico impulsó formalmente el nacimiento de la Ingeniería de Software?",
        "options": [
            "a) El lanzamiento del microprocesador Intel 4004 en 1971",
            "b) La Conferencia de la OTAN en Garmisch (Alemania) en 1968 ante la 'Crisis del Software'",
            "c) La publicación del Manifiesto Ágil en Utah en 2001",
            "d) La creación del lenguaje C en los Laboratorios Bell en 1972"
        ],
        "correct": 1,
        "explanation": "El concepto 'ingeniería de software' se propuso oficialmente en 1968 en una conferencia de la OTAN en Garmisch para abordar la 'Crisis del Software' (retrasos, sobrecostos y fallos catastróficos en grandes sistemas)."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 5,
        "q": "¿Cuáles son las cuatro actividades fundamentales comunes a todo proceso de software?",
        "options": [
            "a) Codificación, Compilación, Depuración y Despliegue",
            "b) Especificación, Desarrollo (diseño e implementación), Validación y Evolución",
            "c) Análisis financiero, Contratación, Instalación y Capacitación",
            "d) Reunión inicial, Prototipado, Venta y Mantenimiento preventivo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1 y 2) define cuatro actividades universales en cualquier proceso de software: Especificación, Desarrollo, Validación y Evolución."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 6,
        "q": "¿Bajo qué condiciones es técnicamente adecuado utilizar el Modelo en Cascada (Waterfall)?",
        "options": [
            "a) Cuando los requerimientos son muy volátiles y cambian semanalmente",
            "b) Cuando los requerimientos son estables, bien comprendidos y el sistema es crítico o parte de un proyecto de ingeniería mayor",
            "c) Exclusivamente en aplicaciones web para startups con prototipado rápido",
            "d) Cuando el equipo de programación no tiene ninguna experiencia técnica previa"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 2, p. 30) señala que el modelo en cascada es adecuado sólo cuando los requerimientos se entienden bien y es poco probable que cambien radicalmente durante el desarrollo."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 7,
        "q": "¿Cuál es la principal ventaja del Desarrollo Incremental frente al modelo en cascada?",
        "options": [
            "a) Elimina por completo la necesidad de realizar pruebas de software",
            "b) Reduce significativamente el costo de acomodar requerimientos cambiantes y entrega valor temprano al cliente",
            "c) Garantiza que el código no requerirá mantenimiento posterior",
            "d) Permite prescindir de la arquitectura y la documentación técnica"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 2, p. 32) explica que el desarrollo incremental reduce el costo de acomodar requerimientos variables y facilita la entrega y retroalimentación rápida de versiones operativas."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 8,
        "q": "¿Cuáles son las cuatro fases secuenciales del Proceso Unificado Racional (RUP)?",
        "options": [
            "a) Análisis, Diseño, Codificación y Pruebas",
            "b) Concepción (Inception), Elaboración, Construcción y Transición",
            "c) Planificación, Estimación, Programación y Lanzamiento",
            "d) Inicialización, Refactorización, Aceptación y Auditoría"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 2, p. 50) describe las cuatro fases canónicas de RUP: Concepción (Inception), Elaboración (Elaboration), Construcción (Construction) y Transición (Transition)."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 9,
        "q": "¿Qué distingue a los métodos ágiles frente a los métodos dirigidos por un plan?",
        "options": [
            "a) Los métodos ágiles no prueban el código y los tradicionales sí",
            "b) En los métodos ágiles la planeación es incremental y continua, priorizando software funcional y adaptación al cambio",
            "c) Los métodos ágiles solo funcionan con un único programador",
            "d) En los métodos ágiles la especificación debe congelarse antes de comenzar el desarrollo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 3, pp. 58-62) detalla que los métodos ágiles se centran en el código, iteraciones cortas, involucramiento directo del cliente y capacidad de adaptación rápida ante cambios inevitables."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 10,
        "q": "¿Cómo se distribuyen habitualmente los costos en el ciclo de vida del software profesional?",
        "options": [
            "a) El 90% se gasta en la codificación inicial y el 10% en mantenimiento",
            "b) Aproximadamente 60% en desarrollo y 40% en pruebas inicialmente, pero los costos de evolución superan con frecuencia a los de desarrollo",
            "c) Los costos de hardware superan siempre a los costos de ingeniería de software",
            "d) El costo se distribuye en partes iguales: 25% especificación, 25% diseño, 25% codificación y 25% pruebas"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 6 y p. 27) destaca que para el software comercial a medida, los costos de evolución y mantenimiento a largo plazo superan ampliamente a los costos del desarrollo inicial."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 11,
        "q": "¿En qué consiste la Ingeniería de Software orientada a la reutilización?",
        "options": [
            "a) En volver a ejecutar el mismo código compilado varias veces en la misma computadora",
            "b) En un proceso de desarrollo enfocado en integrar componentes existentes y sistemas COTS en lugar de escribir código desde cero",
            "c) En reutilizar el hardware obsoleto de la empresa",
            "d) En reciclar los manuales de usuario de versiones anteriores"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 2, p. 34 y Cap. 16) define la ingeniería orientada a la reutilización como la integración de software preexistente (componentes o COTS), reduciendo tiempos y costos de desarrollo."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 12,
        "q": "¿Por qué la heterogeneidad es uno de los mayores retos de la ingeniería de software actual?",
        "options": [
            "a) Porque impide el uso de cables Ethernet en las oficinas",
            "b) Porque el software debe operar en redes distribuidas con múltiples tipos de hardware, móviles y coexistir con sistemas heredados",
            "c) Porque los programadores utilizan teclados con diferentes distribuciones de idioma",
            "d) Porque las leyes laborales exigen equipos multidisciplinarios"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 10) señala que la heterogeneidad exige construir software confiable capaz de operar en diversos dispositivos, arquitecturas y comunicarse con sistemas heredados más antiguos."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 13,
        "q": "¿Cuál es la diferencia primordial entre un producto genérico y uno personalizado (a la medida)?",
        "options": [
            "a) Los genéricos se desarrollan en C y los personalizados en Python",
            "b) En los genéricos la empresa desarrolladora controla la especificación; en los personalizados la especificación la controla el cliente comprador",
            "c) Los productos genéricos nunca se venden y los personalizados son gratuitos",
            "d) Los genéricos carecen de requerimientos de seguridad"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 7) enfatiza que la diferencia clave radica en quién controla la especificación: la organización desarrolladora (genéricos) vs el cliente que contrató el desarrollo (a la medida)."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 14,
        "q": "¿Qué establece el principio de 'Interés Público' en el Código de Ética de ACM/IEEE?",
        "options": [
            "a) Que el código debe publicarse siempre como software libre",
            "b) Que los ingenieros de software deberán actuar congruentemente con el interés social y la seguridad pública",
            "c) Que el gobierno debe supervisar cada línea de código escrita en empresas privadas",
            "d) Que las tarifas de los ingenieros deben ser de dominio público"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, pp. 14-16) cita el principio fundamental del Código de Ética de la IEEE-CS/ACM: los ingenieros deben comprometerse a que el software sea benéfico y seguro para la sociedad."
    },
    {
        "unit": 1,
        "unitName": "Unidad I: Introducción",
        "num": 15,
        "q": "¿Por qué no existe un único método universal óptimo en la ingeniería de software?",
        "options": [
            "a) Porque los autores de libros no logran ponerse de acuerdo",
            "b) Porque diferentes tipos de sistemas (ej. juegos vs sistemas críticos de aviónica) tienen requisitos, riesgos y restricciones operacionales radicalmente distintos",
            "c) Porque los lenguajes de programación se inventaron en diferentes países",
            "d) Porque la ley prohíbe usar el mismo método en dos empresas distintas"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 1, p. 6) subraya que un sistema de control de vuelo requiere especificación formal exhaustiva, mientras un juego web requiere prototipos rápidos; cada contexto exige sus propias técnicas."
    },

    # =========================================================================
    # UNIDAD II: ADMINISTRACIÓN DE PROYECTOS DE SOFTWARE (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 1,
        "q": "¿Cuáles son los tres pilares de gestión esenciales en la administración de proyectos de software?",
        "options": [
            "a) Código, Compiladores y Computadoras",
            "b) Personas (personal), Proceso y Producto",
            "c) Publicidad, Ventas y Cobranza",
            "d) Hardware, Conectividad y Licencias"
        ],
        "correct": 1,
        "explanation": "La gestión de proyectos eficaz equilibra a las personas (selección y liderazgo de equipo), el proceso (métodos aplicados) y el producto (calidad y alcance a entregar)."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 2,
        "q": "¿Qué es el modelo COCOMO II y quién lo propuso?",
        "options": [
            "a) Un modelo de arquitectura propuesto por Alan Turing",
            "b) Un modelo algorítmico y empírico de estimación de esfuerzo, coste y calendario propuesto por Barry Boehm",
            "c) Un estándar de pruebas unitarias formulado por Edsger Dijkstra",
            "d) Una metodología ágil creada por Kent Beck"
        ],
        "correct": 1,
        "explanation": "COCOMO II (Constructive Cost Model II) fue desarrollado por Barry Boehm como el estándar algorítmico más influyente para predecir personas-mes y calendario."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 3,
        "q": "¿Para qué etapa de desarrollo está diseñado el submodelo de 'Composición de Aplicación' de COCOMO II?",
        "options": [
            "a) Para la etapa final de pruebas de estrés",
            "b) Para las primeras etapas de prototipado rápido con interfaces basadas en Puntos de Objeto",
            "c) Para el mantenimiento correctivo de sistemas de 20 años de antigüedad",
            "d) Para la redacción de contratos legales con clientes"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 637) explica que este submodelo se usa en la exploración inicial mediante herramientas de desarrollo rápido utilizando Puntos de Objeto."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 4,
        "q": "¿En qué consiste el submodelo de 'Diseño Temprano' de COCOMO II y qué métrica utiliza?",
        "options": [
            "a) En contar líneas de código ensamblador",
            "b) En estimar el esfuerzo antes de diseñar la arquitectura detallada a partir de Puntos de Función no ajustados",
            "c) En medir la temperatura de los servidores de desarrollo",
            "d) En evaluar la cantidad de errores descubiertos en producción"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 638) indica que el modelo de diseño temprano se utiliza antes de que la arquitectura esté cerrada, usando Puntos de Función traducidos a KLOC."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 5,
        "q": "¿Cuál es la fórmula canónica del submodelo Post-Arquitectura de COCOMO II?",
        "options": [
            "a) Esfuerzo = Líneas de Código / Número de Programadores",
            "b) Esfuerzo (PM) = A × (Tamaño)^B × ∏ Mi",
            "c) Esfuerzo = Presupuesto × Días Restantes",
            "d) Esfuerzo = V(G) × Complejidad Ciclomática"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 639) formula el esfuerzo en Personas-Mes como PM = A × (Tamaño)^B × ∏ Mi, donde B modela economías/deseconomías de escala y Mi son 17 multiplicadores de coste."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 6,
        "q": "¿Qué mide la técnica de Puntos de Función (FP) propuesta por Allan Albrecht?",
        "options": [
            "a) La cantidad física de bytes que ocupa el archivo ejecutable",
            "b) El tamaño funcional del software a partir de entradas, salidas, consultas externas y archivos lógicos",
            "c) La velocidad del procesador en megahercios requerida por el programa",
            "d) La cantidad de funciones matemáticas escritas en el código"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 634) describe los Puntos de Función como una medida de tamaño independiente del lenguaje de programación basada en la funcionalidad externa entregada al usuario."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 7,
        "q": "¿Qué propósito fundamental cumple la Estructura de Desglose del Trabajo (EDT / WBS)?",
        "options": [
            "a) Servir como manual de instalación para el usuario final",
            "b) Descomponer jerárquicamente el proyecto en paquetes de trabajo y tareas discretas manejables",
            "c) Definir las reglas gramaticales del lenguaje de programación elegido",
            "d) Asignar los salarios individuales de cada miembro de la organización"
        ],
        "correct": 1,
        "explanation": "La EDT/WBS descompone el alcance global del proyecto en componentes menores para permitir estimación precisa, asignación de responsabilidades y seguimiento temporal."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 8,
        "q": "¿Qué representa la Ruta Crítica (Critical Path) en una red de actividades PERT/CPM?",
        "options": [
            "a) El conjunto de tareas que tienen mayor riesgo de ataque cibernético",
            "b) La secuencia de actividades dependientes de principio a fin cuya duración acumulada determina la duración mínima del proyecto",
            "c) Las tareas que pueden retrasarse indefinidamente sin afectar al cliente",
            "d) La lista de programadores que tienen más experiencia en el equipo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 628) define la ruta crítica como la secuencia más larga de tareas dependientes; determina el tiempo mínimo indispensable para completar el proyecto."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 9,
        "q": "¿Por qué la holgura total (float) de las tareas en la Ruta Crítica es exactamente CERO?",
        "options": [
            "a) Porque las tareas críticas no requieren recursos financieros",
            "b) Porque cualquier retraso en cualquiera de esas tareas retrasa inmediatamente la fecha final de todo el proyecto",
            "c) Porque se realizan al principio del proyecto antes de que empiece a correr el reloj",
            "d) Porque son tareas automáticas realizadas por la computadora"
        ],
        "correct": 1,
        "explanation": "La holgura es cero porque no hay margen de demora: si una actividad crítica se retrasa un solo día, la entrega final del proyecto se posterga un día."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 10,
        "q": "¿Cuál es la diferencia conceptual entre un Hito (Milestone) y un Entregable (Deliverable)?",
        "options": [
            "a) Un hito es un artefacto tangible y un entregable es una fecha en el calendario",
            "b) Un hito es un punto de referencia temporal o de fin de etapa; un entregable es un resultado o producto tangible verificado",
            "c) Son conceptos exactamente sinónimos en la gestión de proyectos",
            "d) Los hitos solo existen en proyectos ágiles y los entregables en cascada"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 23, p. 624) aclara que un hito es un punto final de una actividad lógica para evaluar avance, mientras que un entregable es un resultado concreto entregado formalmente al cliente o evaluador."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 11,
        "q": "¿Cuáles son las cuatro etapas ordenadas de la gestión proactiva de riesgos según Sommerville?",
        "options": [
            "a) Ignorar, Suponer, Lamentar y Corregir",
            "b) Identificación de riesgos, Análisis/Valoración, Planeación y Supervisión/Monitoreo",
            "c) Compilación, Ejecución, Perfilado y Optimización",
            "d) Contratación, Negociación, Despido y Reemplazo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 22, p. 595) define el proceso de gestión de riesgos en 4 fases iterativas: Identificación, Análisis, Planeación y Supervisión continua."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 12,
        "q": "¿Cómo clasifica Sommerville los riesgos en un proyecto de software?",
        "options": [
            "a) Riesgos del Proyecto (calendario/recursos), del Producto (calidad/rendimiento) y del Negocio (mercado)",
            "b) Riesgos de Hardware, de Red y de Electricidad",
            "c) Riesgos Financieros, Legales y Personales",
            "d) Riesgos Menores, Medios y Mayores únicamente"
        ],
        "correct": 0,
        "explanation": "Sommerville (Cap. 22, p. 596) divide formalmente los riesgos en: del proyecto (afectan recursos o fechas), del producto (afectan funcionalidad/calidad) y del negocio (afectan viabilidad comercial)."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 13,
        "q": "¿Cuál es la diferencia fundamental entre Aseguramiento de Calidad (QA) y Control de Calidad (QC)?",
        "options": [
            "a) QA y QC son términos idénticos para referirse a la depuración de código",
            "b) QA es preventivo y se orienta a definir procesos y estándares organizacionales; QC es detectivo y evalúa productos individuales",
            "c) QA lo realizan los programadores y QC los clientes finales exclusivamente",
            "d) QA se realiza al final del proyecto y QC al inicio"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 24, p. 653) distingue QA (orientado a procesos y estándares para prevenir defectos) de QC (orientado a inspeccionar y probar productos para detectar defectos)."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 14,
        "q": "¿Qué es una Inspección Formal de Software (inspección de Fagan) y cuál es su gran ventaja?",
        "options": [
            "a) Un proceso de pruebas dinámicas donde la computadora compila con opciones estrictas",
            "b) Una revisión estática y rigurosa por un equipo de pares que encuentra hasta el 90% de defectos antes de ejecutar el código",
            "c) Una auditoría fiscal gubernamental sobre las licencias de software",
            "d) Una encuesta de satisfacción enviada a los usuarios de la aplicación"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 24, pp. 663-667) demuestra que las inspecciones formales de código por pares descubren defectos de forma estática antes de las pruebas, ahorrando enormes costes de corrección tardía."
    },
    {
        "unit": 2,
        "unitName": "Unidad II: Administración de Proyectos",
        "num": 15,
        "q": "¿Qué calcula la Complejidad Ciclomática de McCabe y qué indica un valor V(G) superior a 50?",
        "options": [
            "a) Calcula el costo financiero; un valor superior a 50 significa déficit presupuestario",
            "b) Calcula la cantidad de caminos lógicos independientes; un valor superior a 50 indica código altamente complejo, riesgoso e intratable",
            "c) Calcula la velocidad en milisegundos; un valor de 50 significa rendimiento óptimo",
            "d) Calcula el porcentaje de satisfacción de los clientes"
        ],
        "correct": 1,
        "explanation": "Thomas McCabe diseñó la métrica V(G) = E - N + 2P para medir la complejidad estructural del flujo de control; valores >50 indican módulos inmanejables e imposibles de probar exhaustivamente."
    },

    # =========================================================================
    # UNIDAD III: REQUERIMIENTOS Y ESPECIFICACIÓN DEL SOFTWARE (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 1,
        "q": "¿Qué es la Ingeniería de Requerimientos y cuál es su meta primordial?",
        "options": [
            "a) Comprar las computadoras y licencias necesarias para los desarrolladores",
            "b) Descubrir, analizar, documentar y verificar los servicios del sistema y sus restricciones operacionales",
            "c) Escribir las líneas de código del backend de la aplicación",
            "d) Realizar la campaña de marketing para el lanzamiento comercial"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 82) define la ingeniería de requerimientos como el proceso de establecer los servicios que el cliente requiere y los límites bajo los cuales el sistema debe operar."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 2,
        "q": "¿Qué define con exactitud a un Requerimiento Funcional?",
        "options": [
            "a) Una restricción de ancho de banda o memoria impuesta por el servidor",
            "b) Un enunciado acerca de los servicios específicos que el sistema debe proveer y cómo debe reaccionar ante entradas concretas",
            "c) El salario que debe percibir el analista de sistemas",
            "d) La normativa de propiedad intelectual del software"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 84) define los requerimientos funcionales como declaraciones de servicios que el sistema debe brindar, cómo debe reaccionar a entradas particulares y comportarse ante situaciones específicas."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 3,
        "q": "¿Cuáles son las tres categorías de Requerimientos No Funcionales según la clasificación de Ian Sommerville?",
        "options": [
            "a) Requerimientos Rápidos, Medios y Lentos",
            "b) Requerimientos del Producto, Organizacionales y Externos",
            "c) Requerimientos de Frontend, Backend y Base de Datos",
            "d) Requerimientos Fáciles, Complejos e Imposibles"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 86) clasifica los requerimientos no funcionales en: del producto (rendimiento, fiabilidad), organizacionales (estándares, procesos) y externos (interoperabilidad, leyes, ética)."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 4,
        "q": "¿En qué consiste la técnica de observación etnográfica en la elicitación de requerimientos?",
        "options": [
            "a) En enviar un formulario anónimo por correo electrónico a los directivos",
            "b) En sumergirse en el entorno real de trabajo de los usuarios para observar cómo interactúan y ejecutan sus labores cotidianas",
            "c) En revisar el código fuente de competidores comerciales",
            "d) En diseñar la base de datos sin consultar a ningún usuario"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, pp. 106-108) describe la etnografía como una técnica observacional directa que permite descubrir requerimientos tácitos o sociales que los usuarios omiten en entrevistas."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 5,
        "q": "¿Por qué un error de requerimientos detectado durante la operación es tan costoso de resolver (Boehm)?",
        "options": [
            "a) Porque los clientes cobran una multa fija de dinero",
            "b) Porque el error ya se propagó y materializó en el diseño, arquitectura, código fuente y casos de prueba",
            "c) Porque los lenguajes de programación no permiten editar código viejo",
            "d) Porque las computadoras se descomponen físicamente si el requerimiento estaba mal"
        ],
        "correct": 1,
        "explanation": "El principio del costo exponencial de Boehm establece que corregir un error de requerimientos en fases tardías cuesta hasta 100-200 veces más debido al retrabajo masivo en cascada."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 6,
        "q": "¿Qué normas internacionales regulan la estructura del Documento de Especificación de Requerimientos (SRS)?",
        "options": [
            "a) IEEE 830 y la norma contemporánea ISO/IEC/IEEE 29148",
            "b) ISO 9000 e ISO 14001 únicamente",
            "c) RFC 791 y RFC 2616 del protocolo HTTP",
            "d) ANSI C y C++20 Standard Library"
        ],
        "correct": 0,
        "explanation": "El estándar histórico IEEE 830 y su evolución moderna ISO/IEC/IEEE 29148 definen las mejores prácticas y la plantilla estructural para la especificación formal de requerimientos."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 7,
        "q": "¿Qué significa que un requerimiento especificado sea técnicamente 'Verificable'?",
        "options": [
            "a) Que el programador afirme verbalmente que lo entendió",
            "b) Que existe un proceso o prueba objetiva y cuantificable mediante la cual una persona o máquina puede demostrar si el sistema lo satisface o no",
            "c) Que el requerimiento contiene términos ambiguos como 'rápido' o 'amigable'",
            "d) Que no tiene costo económico implementarlo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 110) subraya que un requerimiento es verificable sólo si se puede diseñar una prueba objetiva con métricas precisas para validar su cumplimiento."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 8,
        "q": "¿Qué significado semántico tiene la relación <<include>> entre dos Casos de Uso en UML?",
        "options": [
            "a) Que el caso de uso base puede ejecutarse opcionalmente sin el caso de uso incluido",
            "b) Que el comportamiento del caso de uso incluido se incorpora de manera obligatoria e incondicional en la ejecución del caso de uso base",
            "c) Que ambos casos de uso fueron escritos por el mismo programador",
            "d) Que un caso de uso hereda todos los atributos de una clase Java"
        ],
        "correct": 1,
        "explanation": "La relación <<include>> modela funcionalidad compartida común que se ejecuta obligatoriamente como parte intrínseca del caso de uso principal (ej. Validar Identidad)."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 9,
        "q": "¿Qué significado semántico tiene la relación <<extend>> entre dos Casos de Uso en UML?",
        "options": [
            "a) Que la ejecución del caso base se interrumpe y borra para siempre",
            "b) Que el caso de uso extensor amplía el comportamiento del caso base únicamente si se cumple una condición o punto de extensión específico",
            "c) Que el sistema operativo debe extender la memoria swap",
            "d) Que el caso de uso se extiende a múltiples pantallas físicas"
        ],
        "correct": 1,
        "explanation": "La relación <<extend>> modela comportamiento opcional o excepcional que solo se ejecuta bajo condiciones específicas definidas en un punto de extensión (ej. Solicitar Préstamo Especial)."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 10,
        "q": "¿Qué diferencia esencial existe entre un Prototipo Desechable (Throwaway) y uno Evolutivo?",
        "options": [
            "a) El prototipo desechable cuesta más dinero que el evolutivo",
            "b) El desechable se construye para aclarar requerimientos ambiguos y luego se descarta; el evolutivo se refina iterativamente hasta ser el producto final",
            "c) El prototipo evolutivo nunca se prueba",
            "d) El desechable siempre se implementa en código máquina binario"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 2, p. 43) explica que el prototipo desechable mitiga riesgos de requerimientos y se tira para evitar código frágil, mientras el evolutivo usa arquitectura sólida para convertirse en el sistema final."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 11,
        "q": "¿Qué modela un Diagrama de Secuencia UML y qué representa la línea vertical punteada?",
        "options": [
            "a) La jerarquía de herencia entre clases de datos",
            "b) La secuencia cronológica de mensajes entre objetos y la línea de vida (lifeline) que indica la existencia temporal del objeto",
            "c) La topología de cables de la red local",
            "d) La cantidad de memoria asignada a cada variable"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 5, p. 126) detalla que los diagramas de secuencia modelan interacciones de mensajes temporales donde la línea punteada vertical es la 'línea de vida' del participante."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 12,
        "q": "¿Cuáles son los cinco criterios clave de validación de requerimientos según Sommerville?",
        "options": [
            "a) Rapidez, Belleza, Precio, Publicidad y Originalidad",
            "b) Validez, Consistencia, Completitud, Realismo y Verificabilidad",
            "c) Licencia, Autoría, Idioma, Tipografía y Extensión",
            "d) Frontend, Backend, Base de Datos, Servidor y Dominio"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 110) define formalmente: Comprobaciones de Validez, de Consistencia (sin contradicciones), de Completitud (sin omisiones), de Realismo y de Verificabilidad."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 13,
        "q": "¿Para qué se construye y mantiene una Matriz de Trazabilidad de Requerimientos?",
        "options": [
            "a) Para calcular automáticamente los impuestos de la empresa",
            "b) Para vincular cada requerimiento con su origen de negocio, módulos de diseño, código fuente y casos de prueba asociados",
            "c) Para convertir código Java en C++",
            "d) Para encriptar la base de datos contra intrusos"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4, p. 113) subraya que la trazabilidad permite rastrear el impacto de cambios: si un requerimiento cambia, se sabe exactamente qué diseño, código y pruebas deben ajustarse."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 14,
        "q": "¿Cuál es la función del Comité de Control de Cambios (Change Control Board - CCB)?",
        "options": [
            "a) Escribir las pruebas automatizadas del sistema",
            "b) Evaluar el impacto técnico, costo y viabilidad de cada solicitud de cambio antes de aprobar su implementación",
            "c) Instalar los sistemas operativos en las computadoras de la empresa",
            "d) Supervisar los horarios de entrada y salida del personal"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 4 y Cap. 25) explica que el CCB formaliza la gobernanza del cambio para evitar que solicitudes no evaluadas destruyan el presupuesto o la arquitectura del proyecto."
    },
    {
        "unit": 3,
        "unitName": "Unidad III: Requerimientos y Especificación",
        "num": 15,
        "q": "¿En qué tipo de aplicaciones está plenamente justificada la Especificación Formal con notaciones matemáticas (Z, VDM)?",
        "options": [
            "a) En tiendas de comercio electrónico para ropa",
            "b) En sistemas críticos de alta seguridad, reactores nucleares, medicina intensiva o aviónica donde las fallas causan pérdida de vidas",
            "c) En páginas web informativas estáticas",
            "d) En videojuegos móviles casuales"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 12, p. 333) aclara que los métodos formales son costosos pero indispensables en sistemas críticos de vidas humanas, donde se requiere demostración matemática de corrección."
    },

    # =========================================================================
    # UNIDAD IV: DISEÑO DE SOFTWARE Y ARQUITECTURA (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 1,
        "q": "¿Cómo define Ian Sommerville al Diseño Arquitectónico de Software?",
        "options": [
            "a) El acto de elegir el color de fondo y tipografía de las pantallas",
            "b) El proceso crítico de identificar los subsistemas que componen el software y establecer el marco de control y comunicación entre ellos",
            "c) El ensamblado físico de las tarjetas madre de los servidores",
            "d) La traducción literal de diagramas a código binario ejecutable"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 147) define el diseño arquitectónico como el nivel más temprano y crítico del diseño, donde se definen subsistemas y las directrices de interconexión."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 2,
        "q": "¿Qué es la Alta Cohesión en un módulo o clase y por qué es un principio de calidad?",
        "options": [
            "a) La cantidad de conexiones de red que mantiene abiertas el módulo",
            "b) La concentración lógica donde todos los elementos internos del módulo colaboran estrechamente para cumplir una única función bien definida",
            "c) La dependencia excesiva de variables globales externas",
            "d) La cantidad total de líneas de código que contiene el archivo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 7) y los principios de diseño modular señalan que la alta cohesión garantiza módulos enfocados, atómicos, fácilmente testeables y reutilizables."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 3,
        "q": "¿Qué es el Bajo Acoplamiento y qué beneficio aporta a la mantenibilidad?",
        "options": [
            "a) La desconexión física de la red de área local",
            "b) La mínima interdependencia entre módulos independientes, permitiendo que cambios en un componente no rompan el resto del sistema",
            "c) La ausencia total de funciones en el código fuente",
            "d) La lentitud en la transmisión de datos entre cliente y servidor"
        ],
        "correct": 1,
        "explanation": "El bajo acoplamiento minimiza los efectos colaterales; módulos independientes permiten refactorizaciones y mantenimiento sin propagación de fallos imprevistos."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 4,
        "q": "¿Qué principio formuló David Parnas en relación con la modularidad?",
        "options": [
            "a) El principio de compartir todas las estructuras de datos internamente",
            "b) El principio de Ocultamiento de Información (Information Hiding): exponer sólo interfaces públicas estables y ocultar decisiones de diseño internas",
            "c) El principio de evitar el uso de funciones y clases",
            "d) La ley de Moore aplicada al procesamiento lógico"
        ],
        "correct": 1,
        "explanation": "David Parnas (1972) estableció el concepto seminal de Information Hiding: encapsular la lógica interna vulnerable tras interfaces públicas para proteger al sistema del cambio."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 5,
        "q": "¿Cuáles son las '4+1 Vistas' del modelo arquitectónico propuesto por Philippe Kruchten?",
        "options": [
            "a) Vista Norte, Sur, Este, Oeste y Central",
            "b) Vista Lógica, Vista de Proceso, Vista de Desarrollo, Vista Física y la vista unificadora de Escenarios / Casos de Uso",
            "c) Vista HTML, CSS, JavaScript, SQL y Bash",
            "d) Vista Estudiante, Docente, Director, Rector y Administrador"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 153) describe el modelo 4+1 de Kruchten: Lógica (descomposición en objetos), Proceso (concurrencia), Desarrollo (módulos), Física (hardware) y Escenarios."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 6,
        "q": "¿Cómo se dividen las responsabilidades en el patrón arquitectónico Modelo-Vista-Controlador (MVC)?",
        "options": [
            "a) El Modelo maneja la red, la Vista procesa pagos y el Controlador guarda archivos",
            "b) El Modelo gestiona los datos y lógica de negocio, la Vista presenta la interfaz al usuario, y el Controlador gestiona eventos e interacción",
            "c) Son tres nombres para la misma capa de software",
            "d) El Modelo es el hardware, la Vista es el monitor y el Controlador es el ratón"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 156) explica que MVC separa la representación de datos (Modelo) de su visualización (Vista) y de la gestión de entradas del usuario (Controlador)."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 7,
        "q": "¿Cuál es la regla fundamental de una Arquitectura en Capas (Layered)?",
        "options": [
            "a) Cualquier capa puede llamar arbitrariamente a cualquier otra capa sin orden",
            "b) Cada capa proporciona servicios a la capa inmediatamente superior y consume servicios únicamente de la capa inmediatamente inferior",
            "c) Las capas inferiores dependen de las capas superiores de interfaz",
            "d) El sistema sólo puede tener una única capa activa a la vez"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 158) señala que la arquitectura en capas organiza el sistema jerárquicamente; cada capa consume solo los servicios del estrato inferior directo."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 8,
        "q": "¿Cuándo es especialmente adecuado el Patrón de Repositorio o Pizarrón (Repository Pattern)?",
        "options": [
            "a) Cuando los subsistemas no comparten ningún dato entre sí",
            "b) Cuando grandes volúmenes de información persistente deben ser compartidos, consultados y modificados por múltiples subsistemas independientes",
            "c) Exclusivamente en sistemas de tiempo real duro embebidos",
            "d) Cuando no se cuenta con espacio en disco duro"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 160) aclara que el patrón repositorio centraliza los datos compartidos, permitiendo que subsistemas independientes interactúen a través del repositorio central."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 9,
        "q": "¿Cuáles son las ventajas del patrón arquitectónico Cliente-Servidor distribuido?",
        "options": [
            "a) Elimina la necesidad de utilizar protocolos de comunicación de red",
            "b) Los servidores ofrecen servicios centralizados a múltiples clientes distribuidos de forma transparente a través de una red",
            "c) Garantiza que el software nunca se quede sin memoria RAM",
            "d) Requiere que todos los clientes conozcan el código fuente interno del servidor"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 162) expone que cliente-servidor distribuye los datos y el procesamiento, permitiendo clientes delgados o gruesos consumiendo servicios de red."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 10,
        "q": "¿Cómo opera el patrón de Tuberías y Filtros (Pipe and Filter)?",
        "options": [
            "a) Los datos fluyen de forma bidireccional caótica entre todos los módulos",
            "b) Cada componente (filtro) transforma un flujo secuencial de datos de entrada y emite la salida a través de una tubería hacia el siguiente filtro",
            "c) Es un patrón exclusivo para sistemas de plomería y agua potable",
            "d) Requiere una base de datos relacional para funcionar"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 6, p. 163) describe el modelo de tuberías y filtros (típico de UNIX): procesamiento secuencial donde la salida de una transformación es la entrada de la siguiente."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 11,
        "q": "En UML, ¿qué diferencia semántica existe entre Agregación y Composición?",
        "options": [
            "a) La agregación usa rombo negro y la composición rombo blanco",
            "b) La agregación representa una relación 'tiene un' débil donde las partes pueden existir sin el todo; la composición es fuerte y el ciclo de vida de las partes depende del todo",
            "c) Son dos nombres exactamente idénticos en notación UML",
            "d) La composición sólo se aplica a interfaces gráficas"
        ],
        "correct": 1,
        "explanation": "En UML, la composición (rombo relleno negro) implica propiedad estricta: si el contenedor se destruye, sus partes mueren con él; en la agregación (rombo vacío), las partes tienen vida independiente."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 12,
        "q": "¿Cuáles son las tres categorías en que el Gang of Four (GoF) clasifica los 23 patrones de diseño?",
        "options": [
            "a) Simples, Medios y Complejos",
            "b) Creacionales, Estructurales y de Comportamiento",
            "c) Frontend, Backend y Fullstack",
            "d) Síncronos, Asíncronos y Reactivos"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 7, p. 189) cita la taxonomía canónica de Gamma et al. (GoF): Creacionales (creación de objetos), Estructurales (composición de clases) y de Comportamiento (interacción dinámica)."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 13,
        "q": "¿Qué garantiza el patrón de diseño creacional Singleton?",
        "options": [
            "a) Que una clase tenga infinitas instancias simultáneas en memoria",
            "b) Que una clase tenga exactamente una única instancia globalmente accesible durante toda la ejecución",
            "c) Que el código no compile si se detectan errores lógicos",
            "d) Que todas las variables sean de tipo entero"
        ],
        "correct": 1,
        "explanation": "El patrón Singleton restringe la instanciación de una clase a un único objeto y proporciona un punto de acceso global uniforme (ej. gestor de conexiones a base de datos)."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 14,
        "q": "¿Cuál es la diferencia crítica entre un sistema de tiempo real duro (hard) y uno blando (soft)?",
        "options": [
            "a) El tiempo real duro está programado en C y el blando en Java",
            "b) En tiempo real duro, no cumplir un plazo de tiempo constituye una falla catastrófica total del sistema; en tiempo real blando, causa solo degradación de calidad",
            "c) El tiempo real blando se ejecuta exclusivamente en computadoras cuánticas",
            "d) En tiempo real duro las computadoras son físicamente de metal resistente"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 20) explica que en hard real-time (ej. frenos ABS, aviónica) el incumplimiento del plazo temporal es catastrófico; en soft real-time (ej. streaming de video) causa pérdida de calidad."
    },
    {
        "unit": 4,
        "unitName": "Unidad IV: Diseño de Software y Arquitectura",
        "num": 15,
        "q": "¿Qué significa la sigla COTS en el contexto de reutilización y arquitectura de software?",
        "options": [
            "a) Centralized Operating Tracking System",
            "b) Commercial Off-The-Shelf (productos comerciales listos para usar sin modificación)",
            "c) Code Optimization and Testing Standard",
            "d) Customer Oriented Technical Service"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 16, p. 440) define COTS como sistemas o componentes de software comerciales estándar que se adquieren ya construidos para integrarlos en una solución mayor."
    },

    # =========================================================================
    # UNIDAD V: VERIFICACIÓN Y VALIDACIÓN DEL SOFTWARE (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 1,
        "q": "¿Cuál es la distinción formal de Barry Boehm entre Verificación y Validación?",
        "options": [
            "a) Verificación: ¿El código es rápido? Validación: ¿El código es barato?",
            "b) Verificación: «¿Construimos el producto correctamente?» / Validación: «¿Construimos el producto correcto?»",
            "c) Son dos palabras con el mismo significado técnico exacto",
            "d) Verificación la realizan las máquinas y validación la realizan los inversores"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 206) cita la regla mnemotécnica canónica de Boehm: Verificación comprueba conformidad con la especificación; Validación comprueba si satisface las necesidades reales del usuario."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 2,
        "q": "¿Cuáles son los tres niveles secuenciales de pruebas de desarrollo?",
        "options": [
            "a) Pruebas de Sintaxis, Pruebas de Gramática y Pruebas Ortográficas",
            "b) Pruebas Unitarias, Pruebas de Componentes (Integración) y Pruebas de Sistema",
            "c) Pruebas de Mañana, Pruebas de Tarde y Pruebas Nocturnas",
            "d) Pruebas en Windows, Pruebas en Linux y Pruebas en Mac"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 210) detalla los tres niveles de pruebas de desarrollo: unitarias (métodos/clases aislados), de componentes (módulos integrados) y de sistema (comportamiento global interactivo)."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 3,
        "q": "¿Cuál es el principio rector de las Pruebas de Caja Negra (Funcionales)?",
        "options": [
            "a) Inspeccionar el código fuente línea por línea con un depurador",
            "b) Diseñar casos de prueba basados exclusivamente en las especificaciones funcionales externas sin examinar la estructura interna del código",
            "c) Probar el software con la pantalla de la computadora apagada",
            "d) Probar exclusivamente sistemas que utilicen interfaces en modo texto"
        ],
        "correct": 1,
        "explanation": "En las pruebas de caja negra el probador trata al sistema como opaco, evaluando qué salidas produce ante determinadas entradas en relación con su especificación."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 4,
        "q": "¿En qué consiste la técnica de Partición de Clases de Equivalencia?",
        "options": [
            "a) En dividir el sueldo de los probadores en partes iguales",
            "b) En dividir el dominio de entrada en subconjuntos donde se asume que todos los valores de una clase se comportarán de forma equivalente",
            "c) En particionar el disco duro en varias unidades virtuales",
            "d) En probar todos los números enteros del 1 al infinito"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 216) describe la partición de equivalencia: si el programa funciona para un representante de la clase, se asume que funcionará para todos los demás valores del grupo."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 5,
        "q": "¿Por qué el Análisis de Valores Límite es una de las técnicas de prueba funcional más eficaces?",
        "options": [
            "a) Porque los programadores cometen la mayor cantidad de errores en las fronteras y bordes de las condiciones lógicas (<, <=, >, >=)",
            "b) Porque solo prueba valores impares que consumen menos memoria",
            "c) Porque elimina la necesidad de escribir pruebas unitarias",
            "d) Porque se realiza en el último minuto antes de entregar el software"
        ],
        "correct": 0,
        "explanation": "La experiencia empírica demuestra que las fallas de programación ocurren con enorme frecuencia en los límites extremos de las clases de entrada (ej. 0, -1, valor máximo)."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 6,
        "q": "¿Cuál es el principio rector de las Pruebas de Caja Blanca (Estructurales)?",
        "options": [
            "a) Diseñar casos de prueba analizando directamente la lógica interna, bifurcaciones y caminos del código fuente",
            "b) Probar solo software que tenga interfaces con fondo blanco",
            "c) Ignorar las especificaciones y probar al azar",
            "d) Probar exclusivamente software de código cerrado comercial"
        ],
        "correct": 0,
        "explanation": "Las pruebas de caja blanca examinan la estructura lógica interna, buscando garantizar cobertura de sentencias, caminos y condiciones booleanas."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 7,
        "q": "¿Qué diferencia existe entre Cobertura de Sentencias y Cobertura de Ramas?",
        "options": [
            "a) Son métricas idénticas que arrojan siempre el mismo porcentaje",
            "b) La cobertura de sentencias verifica que cada línea se ejecute al menos una vez; la de ramas exige que cada decisión lógica se evalúe tanto en su rama verdadera como falsa",
            "c) La cobertura de ramas se aplica solo a árboles binarios",
            "d) La cobertura de sentencias solo mide comentarios en el código"
        ],
        "correct": 1,
        "explanation": "La cobertura de ramas es más rigurosa: un código puede tener 100% de cobertura de sentencias y aun así no haber probado condiciones de rama falsas que oculten errores graves."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 8,
        "q": "¿Qué representa la Complejidad Ciclomática de McCabe en las pruebas de caja blanca?",
        "options": [
            "a) El número de programadores que deben renunciar al proyecto",
            "b) El límite superior del número de casos de prueba necesarios para garantizar cobertura de todos los caminos básicos independientes",
            "c) La cantidad de memoria consumida por las variables locales",
            "d) El tiempo en segundos que demora la compilación del módulo"
        ],
        "correct": 1,
        "explanation": "El valor V(G) determina cuántos casos de prueba linealmente independientes deben diseñarse como mínimo para garantizar que cada camino básico se ejecute al menos una vez."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 9,
        "q": "¿Cuál es la secuencia estricta del ciclo Red-Green-Refactor en Test-Driven Development (TDD)?",
        "options": [
            "a) Escribir el código, probarlo manualmente y cambiar los colores del botón",
            "b) 1. Escribir prueba automatizada que falle (Red) -> 2. Escribir código mínimo para que pase (Green) -> 3. Refactorizar y limpiar (Refactor)",
            "c) Compilar (Red), Ejecutar (Green), Borrar (Refactor)",
            "d) Escribir código perfecto (Green), probarlo (Red) y documentarlo (Refactor)"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 221) detalla TDD: primero se escribe una prueba que falla para definir la especificación, luego se escribe el código mínimo para pasarla, y finalmente se refactoriza."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 10,
        "q": "¿Por qué son indispensables las Pruebas de Regresión y cuándo deben ejecutarse?",
        "options": [
            "a) Para volver a instalar el sistema operativo cada semana",
            "b) Para comprobar que modificaciones o correcciones de defectos no hayan introducido nuevos errores colaterales en funciones previamente probadas",
            "c) Para obligar a los clientes a regresar a versiones obsoletas",
            "d) Para probar el software exclusivamente cuando retrocede el reloj del sistema"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 223) recalca que toda modificación o bugfix puede romper partes sanas del sistema; las pruebas de regresión automatizadas previenen esta degradación."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 11,
        "q": "¿En qué se diferencian las Pruebas de Versión (Release Testing) de las pruebas de desarrollo?",
        "options": [
            "a) Las de versión las realizan los programadores del sistema",
            "b) Las de versión las realiza un equipo de pruebas independiente con el objetivo de validar que el sistema cumple los requerimientos antes de entregarlo a los clientes",
            "c) Las pruebas de versión no utilizan casos de prueba formales",
            "d) Las pruebas de versión solo se ejecutan en computadoras portátiles"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 224) explica que las pruebas de versión son realizadas por un equipo separado e independiente para evitar el sesgo natural del desarrollador que construyó el código."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 12,
        "q": "¿Cuál es la diferencia entre las Pruebas Alfa y las Pruebas Beta de un software?",
        "options": [
            "a) Alfa es para software en inglés y Beta para software en español",
            "b) Las pruebas Alfa se realizan con usuarios en el entorno controlado del desarrollador; las Beta las realizan usuarios reales en sus propios entornos de trabajo",
            "c) Las pruebas Alfa son pagadas y las Beta son gratuitas",
            "d) Las pruebas Beta se realizan antes que las pruebas Alfa"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 228) diferencia Alfa (usuarios interactuando con el software en la sede del desarrollador bajo supervisión) de Beta (usuarios ejecutando la versión candidata en sus propios entornos)."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 13,
        "q": "¿Qué propósito formal tienen las Pruebas de Aceptación (Acceptance Testing)?",
        "options": [
            "a) Verificar que el código respete las guías estilísticas del lenguaje",
            "b) Permitir que el cliente evalúe formalmente el sistema para decidir contractualmente si acepta y aprueba el software para su despliegue y pago final",
            "c) Probar si el sistema operativo acepta instalar el programa",
            "d) Evaluar si los desarrolladores aceptan trabajar horas extra"
        ],
        "correct": 1,
        "explanation": "Las pruebas de aceptación constituyen el hito contractual donde el cliente verifica que el software resuelve sus necesidades de negocio reales antes de firmar la entrega final."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 14,
        "q": "¿Qué objetivo persiguen las Pruebas de Estrés (Stress Testing)?",
        "options": [
            "a) Estresar emocionalmente al equipo de desarrollo para medir su resistencia laboral",
            "b) Someter al sistema a cargas extremas que sobrepasan su capacidad de diseño para observar si se degrada de forma elegante o colapsa catastróficamente",
            "c) Verificar que el tamaño de las fuentes no cause fatiga visual",
            "d) Probar si el servidor resiste vibraciones mecánicas"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 8, p. 226) indica que las pruebas de estrés llevan al sistema más allá del límite de diseño para evaluar su tolerancia a sobrecargas y evitar fallos catastróficos silenciosos."
    },
    {
        "unit": 5,
        "unitName": "Unidad V: Verificación y Validación",
        "num": 15,
        "q": "¿Qué quiso advertir Edsger Dijkstra con la célebre frase: «Las pruebas pueden demostrar la presencia de errores, pero nunca su ausencia»?",
        "options": [
            "a) Que realizar pruebas de software es una pérdida de tiempo innecesaria",
            "b) Que aunque una suite de pruebas apruebe exitosamente el 100% de sus casos, siempre existe la posibilidad matemática de que existan fallos no descubiertos en caminos no probados",
            "c) Que los errores de software desaparecen automáticamente con el tiempo",
            "d) Que solo los lenguajes interpretados pueden tener errores"
        ],
        "correct": 1,
        "explanation": "Dijkstra advirtió sobre la falsa sensación de seguridad: probar el software encuentra defectos, pero una prueba exitosa no demuestra matemáticamente que el sistema esté libre de cualquier error."
    },

    # =========================================================================
    # UNIDAD VI: EVOLUCIÓN Y MANTENIMIENTO DEL SOFTWARE (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 1,
        "q": "¿Por qué afirma Ian Sommerville que la evolución del software es un proceso continuo e inevitable?",
        "options": [
            "a) Porque las computadoras se desgastan físicamente como los automóviles",
            "b) Porque el software opera en un entorno empresarial, legal y tecnológico en constante cambio, y si no evoluciona pierde utilidad y valor",
            "c) Porque los contratos de software obligan a cobrar mensualidades perpetuas",
            "d) Porque los lenguajes de programación caducan cada 6 meses"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 234) sostiene que el software no es estático: las organizaciones cambian, las leyes cambian y el software debe modificarse para continuar reflejando la realidad del negocio."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 2,
        "q": "¿Qué postula la Primera Ley de Lehman (Ley del Cambio Continuo) sobre los sistemas tipo E?",
        "options": [
            "a) Un programa nunca debe modificarse después de ser compilado",
            "b) Un programa que se usa en un entorno real debe cambiar continuamente o se volverá progresivamente menos útil en dicho entorno",
            "c) El costo del hardware disminuye a la mitad cada año",
            "d) El software bien diseñado no requiere cambios durante al menos una década"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 241) cita a Meir Lehman: los sistemas del mundo real (tipo E) deben adaptarse continuamente para mantener la satisfacción del usuario ante un entorno dinámico."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 3,
        "q": "¿Qué postula la Segunda Ley de Lehman (Ley de la Complejidad Creciente)?",
        "options": [
            "a) Conforme un sistema evoluciona, su complejidad se incrementa a menos que se dedique trabajo deliberado para mantenerla o reducirla",
            "b) El código fuente siempre se vuelve más simple y limpio a medida que se agregan funciones",
            "c) Los procesadores computacionales aumentan su complejidad de transistores",
            "d) Los clientes se vuelven más inteligentes cada año"
        ],
        "correct": 0,
        "explanation": "La segunda ley de Lehman explica que los parches y cambios sucesivos degradan la arquitectura del software a menos que se invierta esfuerzo activo en refactorización y reingeniería."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 4,
        "q": "¿En qué consiste el Mantenimiento Correctivo de software según la norma ISO/IEC 14764?",
        "options": [
            "a) En agregar nuevas pantallas solicitadas por el director",
            "b) En reparar fallas, defectos y bugs descubiertos durante la operación real del sistema que no fueron detectados en las pruebas iniciales",
            "c) En cambiar los servidores de la empresa a la nube",
            "d) En reescribir todo el código fuente en un nuevo lenguaje"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 243) define el mantenimiento correctivo como la reparación de fallas para que el sistema cumpla con la especificación previamente pactada (representa ~17% del esfuerzo total)."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 5,
        "q": "¿En qué consiste el Mantenimiento Adaptativo y qué factores del entorno lo detonan?",
        "options": [
            "a) En reparar errores ortográficos en los comentarios del código",
            "b) En modificar el software para que continúe operando ante cambios en su entorno técnico (nuevo sistema operativo, hardware, motor de base de datos o regulaciones legales)",
            "c) En adaptar el software para que funcione sin electricidad",
            "d) En reducir el precio de venta de la aplicación"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 243) indica que el mantenimiento adaptativo ocurre cuando el entorno operativo del software cambia (ej. actualización de Windows o nuevas leyes tributarias) (~18% del esfuerzo)."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 6,
        "q": "¿Por qué el Mantenimiento Perfectivo suele consumir aproximadamente el 65% del esfuerzo total?",
        "options": [
            "a) Porque los desarrolladores trabajan muy lentamente en esa fase",
            "b) Porque responde a nuevas demandas del negocio: implementar nuevas funcionalidades, optimizar velocidad de procesamiento y mejorar la usabilidad",
            "c) Porque es el mantenimiento más barato de todos",
            "d) Porque las leyes internacionales exigen que el 65% del presupuesto sea perfectivo"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 244) demuestra que la mayor parte del presupuesto de evolución se destina al perfeccionamiento: los usuarios descubren nuevas oportunidades de negocio y solicitan mejoras continuas."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 7,
        "q": "¿Cuál es el propósito del Mantenimiento Preventivo o Refactorización?",
        "options": [
            "a) Agregar nuevas características visuales al frontend",
            "b) Mejorar la estructura interna, legibilidad y modularidad del software para evitar fallas futuras y facilitar su evolución, sin alterar su comportamiento funcional externo",
            "c) Despedir a los programadores que cometieron errores",
            "d) Encriptar el código para que nadie pueda leerlo"
        ],
        "correct": 1,
        "explanation": "La refactorización preventiva no añade funciones visibles, sino que 'paga la deuda técnica', simplificando la lógica interna para que futuras modificaciones sean rápidas, seguras y económicas."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 8,
        "q": "¿Qué es la 'Deuda Técnica' (Technical Debt) en un proyecto de software?",
        "options": [
            "a) Un préstamo de dinero solicitado a un banco para comprar servidores",
            "b) El costo futuro acumulado de retrabajo provocado por elegir soluciones rápidas, frágiles y de mala calidad en lugar de aplicar buen diseño",
            "c) La factura de electricidad del centro de datos",
            "d) El sueldo que se le debe a los ingenieros de software"
        ],
        "correct": 1,
        "explanation": "Ward Cunningham acuñó 'deuda técnica' como metáfora financiera: tomar atajos de mala calidad ahorra tiempo hoy, pero genera 'intereses' que encarecen exponencialmente cualquier cambio futuro."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 9,
        "q": "¿Qué define formalmente a un Sistema Heredado (Legacy System)?",
        "options": [
            "a) Cualquier software descargado gratuitamente de Internet",
            "b) Un sistema informático antiguo pero crítico para la operación del negocio, construido con tecnología obsoleta y difícil de modificar",
            "c) Un programa que fue donado a una escuela pública",
            "d) Un sistema que no tiene base de datos"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 252) define los sistemas legados como sistemas sociotécnicos esenciales para la compañía desarrollados hace muchos años con lenguajes, hardware o arquitecturas superadas."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 10,
        "q": "¿Cuáles son los componentes de un sistema sociotécnico heredado?",
        "options": [
            "a) Solamente el archivo ejecutable compilado",
            "b) Hardware del sistema, software base/SO, software de aplicación, datos de la empresa, procesos de negocio y políticas organizacionales",
            "c) El teclado, el ratón y la pantalla",
            "d) Los manuales impresos únicamente"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 253) subraya que un sistema heredado es una capa sociotécnica completa: cambiar el software exige a menudo cambiar los procesos humanos y las reglas del negocio."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 11,
        "q": "¿Cuándo es aconsejable la estrategia de 'Desechar' (Scrap) un sistema heredado según Sommerville?",
        "options": [
            "a) Cuando el sistema es el más utilizado por los clientes",
            "b) Cuando el sistema ya no realiza una contribución efectiva a los procesos de negocio de la empresa",
            "c) Siempre que el software cumpla más de dos años de antigüedad",
            "d) Cuando el equipo de desarrollo cambia de director"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 255) indica que si los procesos empresariales han cambiado y el sistema ya no aporta valor real al negocio, la decisión racional es desmantelarlo."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 12,
        "q": "¿Cuándo es técnicamente viable la estrategia de 'Mantener' (Continue maintenance) un sistema heredado?",
        "options": [
            "a) Cuando el sistema falla diariamente y nadie sabe cómo arreglarlo",
            "b) Cuando el sistema todavía se requiere, es razonablemente estable y los usuarios hacen relativamente pocas solicitudes de cambio",
            "c) Cuando no se cuenta con copias de seguridad",
            "d) Cuando el sistema fue programado en un lenguaje desconocido"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 255) explica que si el sistema funciona bien, los costos de intervención son bajos y las demandas de cambio son escasas, lo más económico es continuar con mantenimiento rutinario."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 13,
        "q": "¿En qué consiste la estrategia de 'Reingeniería' (Re-engineer) de un sistema heredado?",
        "options": [
            "a) En tirar el software a la basura y comprar otro producto",
            "b) En reestructurar y rediseñar el software existente para volverlo más mantenible y comprensible, sin modificar su funcionalidad de negocio esencial",
            "c) En cambiar a los ingenieros de la empresa por personal nuevo",
            "d) En agregar publicidad comercial dentro del programa"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 248) define la reingeniería de software: mejorar la estructura interna, convertir código a lenguajes modernos y rediseñar datos preservando la lógica empresarial valiosa."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 14,
        "q": "¿Cuándo se debe recurrir a la estrategia de 'Reemplazar' (Replace) un sistema heredado?",
        "options": [
            "a) Cuando el sistema tiene un alto valor para el negocio pero factores como hardware obsoleto hacen inviable continuar manteniéndolo, sustituyéndolo por un paquete COTS o desarrollo nuevo",
            "b) Cuando el sistema funciona a la perfección y no genera ningún gasto",
            "c) Cada vez que se actualiza el navegador web",
            "d) Únicamente si la empresa se declara en quiebra"
        ],
        "correct": 0,
        "explanation": "Sommerville (Cap. 9, p. 255) señala que cuando el mantenimiento se vuelve técnica y económicamente inviable, se debe reemplazar por un sistema comercial estándar (ej. ERP) o desarrollar desde cero."
    },
    {
        "unit": 6,
        "unitName": "Unidad VI: Evolución y Mantenimiento",
        "num": 15,
        "q": "¿Qué dos dimensiones evalúa la Matriz de Diagnóstico de Sistemas Heredados de Ian Sommerville?",
        "options": [
            "a) Color de la interfaz vs Cantidad de pantallas",
            "b) Calidad Técnica (arquitectura, mantenibilidad) vs Valor para el Negocio (contribución a los objetivos organizacionales)",
            "c) Antigüedad del código vs Número de líneas de texto",
            "d) Velocidad del procesador vs Capacidad de disco duro"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 9, p. 254, Fig. 9.13) estructura la toma de decisiones evaluando la calidad técnica del software frente al valor real que aporta a los procesos del negocio."
    },

    # =========================================================================
    # UNIDAD VII: HERRAMIENTAS CASE Y ENTORNOS DE DESARROLLO (15 PREGUNTAS)
    # =========================================================================
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 1,
        "q": "¿Qué significa exactamente el acrónimo CASE en la ingeniería de software?",
        "options": [
            "a) Computer Algorithms and System Execution",
            "b) Computer-Aided Software Engineering (Ingeniería de Software Asistida por Computadora)",
            "c) Centralized Automated Software Environment",
            "d) Code Analysis and Standard Evaluation"
        ],
        "correct": 1,
        "explanation": "CASE se refiere al software computacional diseñado explícitamente para automatizar y dar soporte a las diferentes actividades del proceso de desarrollo de software."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 2,
        "q": "¿Qué actividades del ciclo de vida son asistidas por las herramientas Upper CASE (front-end)?",
        "options": [
            "a) La compilación binaria y la depuración a nivel de ensamblador",
            "b) Las fases tempranas: elicitación de requerimientos, análisis conceptual y modelado formal de sistemas con UML",
            "c) El formateo del disco duro del servidor",
            "d) El empaquetado de instaladores para teléfonos móviles"
        ],
        "correct": 1,
        "explanation": "Las herramientas Upper CASE brindan soporte al análisis y diseño (ej. editores de diagramas de casos de uso y clases, diccionarios de datos y verificadores de consistencia semántica)."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 3,
        "q": "¿Qué actividades del ciclo de vida son asistidas por las herramientas Lower CASE (back-end)?",
        "options": [
            "a) La redacción de los contratos financieros",
            "b) Las fases tardías: generación automática de código, compilación, depuración y ejecución de pruebas automatizadas",
            "c) La negociación de requerimientos con el cliente",
            "d) Las entrevistas etnográficas con usuarios"
        ],
        "correct": 1,
        "explanation": "Las herramientas Lower CASE apoyan las actividades de implementación y verificación (compiladores, suites de pruebas como JUnit, depuradores y generadores automáticos de código)."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 4,
        "q": "¿Qué caracteriza a un entorno I-CASE (Integrated CASE)?",
        "options": [
            "a) Que solo puede ejecutarse en procesadores Intel",
            "b) La integración transparente de herramientas Upper y Lower que comparten un repositorio común de información y metadatos",
            "c) Que no requiere conexión a Internet para compilar",
            "d) Que es completamente gratuito para el público"
        ],
        "correct": 1,
        "explanation": "Un entorno I-CASE integra herramientas de todo el ciclo de vida mediante un repositorio unificado de datos, asegurando trazabilidad directa desde el diseño hasta el código y las pruebas."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 5,
        "q": "¿Qué es la Administración de la Configuración del Software (SCM)?",
        "options": [
            "a) El proceso de comprar cables de red y monitores nuevos",
            "b) El conjunto de disciplinas y procesos para gestionar de forma controlada y trazable la evolución y cambios en todos los artefactos de software",
            "c) El ajuste del brillo y contraste en la pantalla del programador",
            "d) La configuración de la cuenta de correo electrónico institucional"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 25, p. 681) define SCM como el proceso de gestionar los cambios en sistemas de software en evolución: gestión de versiones, control de cambios y construcción del sistema."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 6,
        "q": "¿Cuál es la función del control de versiones en el desarrollo colaborativo de software?",
        "options": [
            "a) Impedir que los desarrolladores usen más de una computadora",
            "b) Registrar el historial cronológico de modificaciones, permitir trabajo concurrente en ramas aisladas y facilitar la fusión (merging) de código sin conflictos",
            "c) Aumentar artificialmente el número de archivos en el disco duro",
            "d) Bloquear el acceso a internet durante la jornada laboral"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 25, p. 690) explica que los sistemas de control de versiones registran quién, cuándo y por qué modificó el código, permitiendo volver a cualquier versión previa si ocurre un fallo."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 7,
        "q": "¿Cuál es la diferencia primordial entre un sistema centralizado (como Subversion) y uno distribuido (como Git)?",
        "options": [
            "a) Subversion funciona en celulares y Git en mainframes",
            "b) En Git cada desarrollador posee una copia completa y local de todo el repositorio con su historial completo, permitiendo commits y ramas sin conexión al servidor central",
            "c) En Git no se pueden crear ramas de código",
            "d) Subversion fue inventado por Linus Torvalds"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 25, p. 691) subraya que en los DVCS (como Git), cada clon es un repositorio completo con historial local autónomo, eliminando el cuello de botella del servidor central."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 8,
        "q": "¿Qué es la 'Construcción del Sistema' (System Building) y qué herramientas la asisten?",
        "options": [
            "a) El ensamble de los escritorios de los ingenieros",
            "b) El proceso automatizado de compilar código fuente, vincular librerías y dependencias para generar un artefacto ejecutable (ej. Make, Maven, Gradle, Webpack)",
            "c) La redacción de la misión y visión de la empresa",
            "d) El trámite de patentes de propiedad intelectual"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 25, p. 693) describe la construcción del sistema como la automatización reproducible del proceso de compilación, enlazado de dependencias y generación de ejecutables."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 9,
        "q": "¿En qué consiste la Gestión de Entregas (Release Management) en el ciclo de vida del software?",
        "options": [
            "a) En el reparto en camiones de las computadoras compradas",
            "b) En preparar, versionar, documentar formalmente y distribuir versiones estables del software destinadas a los clientes y usuarios finales",
            "c) En publicar estados financieros en redes sociales",
            "d) En archivar el código fuente en cintas magnéticas"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 25, p. 699) define la gestión de entregas como la preparación rigurosa de versiones listas para producción con notas de versión, guías de instalación y compatibilidad."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 10,
        "q": "¿Cuál es el principio fundamental de la Integración Continua (Continuous Integration - CI)?",
        "options": [
            "a) Integrar el código de todos los desarrolladores una sola vez al año",
            "b) Fusionar los cambios de código frecuentemente en una rama compartida y disparar automáticamente compilaciones y suites de pruebas para detectar errores de inmediato",
            "c) Prohibir que los programadores hagan commits sin permiso del director",
            "d) Trabajar sin control de versiones"
        ],
        "correct": 1,
        "explanation": "CI garantiza que cada cambio integrado sea compilado y verificado por pruebas automatizadas al instante, erradicando el 'infierno de la integración' en proyectos de software."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 11,
        "q": "¿Qué diferencia existe entre Entrega Continua (Continuous Delivery) y Despliegue Continuo (Continuous Deployment)?",
        "options": [
            "a) Son exactamente sinónimos sin ninguna diferencia",
            "b) En Entrega Continua cada versión pasa las pruebas y queda lista para producción pero requiere aprobación manual humana; en Despliegue Continuo el paso a producción es 100% automático",
            "c) Despliegue continuo es manual y entrega continua es automática",
            "d) Entrega continua solo aplica a software empaquetado en cajas físicas"
        ],
        "correct": 1,
        "explanation": "Continuous Delivery automatiza todo el pipeline hasta dejar la versión lista para despliegue con un clic; Continuous Deployment despliega automáticamente a producción sin intervención humana."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 12,
        "q": "¿Qué función realizan las herramientas de Análisis Estático de Código (como SonarQube)?",
        "options": [
            "a) Ejecutar el software a toda velocidad en un cluster",
            "b) Analizar el código fuente sin ejecutarlo para descubrir vulnerabilidades de seguridad, code smells, violaciones de estándares y medir deuda técnica",
            "c) Diseñar logotipos e interfaces gráficas",
            "d) Optimizar el consumo de batería de los teclados"
        ],
        "correct": 1,
        "explanation": "Sommerville (Cap. 15, p. 395) detalla que el análisis estático examina representaciones del programa para encontrar defectos, vulnerabilidades y fallos de estilo sin requerir ejecución dinámica."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 13,
        "q": "¿Qué papel cumplía el 'Diccionario de Datos' o Repositorio en las herramientas CASE tradicionales?",
        "options": [
            "a) Traducir palabras de inglés a español en los menús",
            "b) Almacenar de forma centralizada definiciones de tipos de datos, entidades, relaciones y diagramas para asegurar consistencia en todo el proyecto",
            "c) Guardar las contraseñas de los usuarios en texto plano",
            "d) Almacenar canciones y videos para los programadores"
        ],
        "correct": 1,
        "explanation": "El repositorio o diccionario centralizado de datos aseguraba que los nombres, entidades y reglas de negocio fueran coherentes y estuvieran sincronizados entre análisis, diseño y código."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 14,
        "q": "¿Por qué los Entornos de Desarrollo Integrados (IDEs) modernos desplazaron a las antiguas herramientas CASE monolíticas?",
        "options": [
            "a) Porque las herramientas CASE eran demasiado baratas",
            "b) Porque los IDEs modernos son modulares, rápidos, ofrecen completado inteligente, depuración en vivo e integración extensible con Git, linters y CI/CD mediante plugins",
            "c) Porque las herramientas CASE fueron prohibidas por ley",
            "d) Porque los programadores dejaron de usar diagramas UML"
        ],
        "correct": 1,
        "explanation": "Los IDEs contemporáneos (VS Code, IntelliJ) proporcionan ecosistemas abiertos y ultrarrápidos con soporte de extensiones para modelado, depuración, análisis estático y despliegue integrado."
    },
    {
        "unit": 7,
        "unitName": "Unidad VII: Herramientas CASE",
        "num": 15,
        "q": "¿Cómo contribuyen herramientas ágiles como Jira, GitHub Issues o Trello a la ingeniería de software?",
        "options": [
            "a) Reemplazan al compilador de código",
            "b) Proporcionan visibilidad del flujo de trabajo, trazabilidad de tareas e incidentes (bugs), y soporte para la planificación de sprints y tableros Kanban",
            "c) Diseñan automáticamente la arquitectura del software",
            "d) Calculan el hardware necesario para la base de datos"
        ],
        "correct": 1,
        "explanation": "Estas herramientas digitalizan y transparentan la gestión del trabajo colaborativo: priorización de backlog, asignación de responsabilidades, seguimiento del ciclo de vida de defectos y velocidad del equipo."
    }
]

print(f"Total questions compiled: {len(questions)}")
unit_counts = {}
for q in questions:
    unit_counts[q['unit']] = unit_counts.get(q['unit'], 0) + 1
print("Counts per unit:", unit_counts)
