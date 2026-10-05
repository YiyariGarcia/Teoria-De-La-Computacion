# Estado del Arte: Cinco articulos

1. **Articulo 1**. Gribkoff, E. (2013). *Applications of deterministic finite automata* [Documento de curso, ECS 120].
University of California, Davis. https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf   

   **Diferencia entre AFD y máquina de Mealy, y su uso en Apache Lucene**  
   Un Autómata Finito Determinista (AFD) funciona exclusivamente como un reconocedor: procesa una cadena completa y su única salida es binaria (acepta o rechaza la cadena dependiendo de si termina en un estado de aceptación). En contraste, una máquina de Mealy es un transductor: genera una salida específica durante cada transición de estado, permitiendo traducir secuencias de entrada en secuencias de salida paso a paso.  

   Apache Lucene requiere un modelo basado en máquinas de Mealy (implementado específicamente como un Transductor de Estados Finitos o FST) para su función de autocompletado porque el sistema no puede limitarse a decir "sí o no" ante un prefijo. Necesita generar salidas dinámicas; al recibir los caracteres que el usuario teclea, el autómata debe arrojar como resultado los caracteres restantes para formar sugerencias de palabras y devolver pesos numéricos que determinen la relevancia de cada sugerencia.  

   **Consecuencia de modelar un AFD con conjunto de aceptación vacío ($F = \emptyset$)**  
   En la teoría formal, si un AFD no tiene estados de aceptación, el lenguaje que reconoce es estrictamente el lenguaje vacío; es decir, la máquina rechazará matemáticamente cualquier cadena de entrada.  

   La consecuencia conceptual de esto al modelar una máquina expendedora es que el AFD abandona su propósito tradicional de analizar sintácticamente cadenas finitas de texto. En su lugar, se utiliza como un sistema de control reactivo. La máquina está diseñada para ejecutarse en un bucle continuo e infinito (recibir monedas, cambiar el saldo, entregar el producto y volver a empezar), donde lo que importa es el comportamiento de las transiciones de estado en el mundo físico, no la validación de un texto final.  

   **Afirmación que requiere verificación arbitrada**  
   Cualquier afirmación del documento que asegure ventajas absolutas de rendimiento o eficiencia de memoria de los Transductores de Estados Finitos (FST) frente a otras estructuras de diccionarios (como los árboles Trie o Hash maps) dentro de la arquitectura de Apache Lucene. Al ser un resumen de clase, estas métricas suelen simplificarse. Para citar estas superioridades de almacenamiento y velocidad de consulta en un trabajo formal, es necesario verificar los datos empíricos en literatura arbitrada especializada en Recuperación de Información (Information Retrieval) o en las publicaciones técnicas de los desarrolladores originales del algoritmo FST de Lucene.  

   **Ficha**: Aplicaciones de AFD (Gribkoff)  

   * **Cita**: Gribkoff, E. (2013). Applications of deterministic finite automata [Documento de curso, ECS 120]. University of California, Davis. https://www.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-dfa.pdf  

   * **Problema abordado**: Explica cómo los autómatas finitos pueden implementarse para resolver problemas cotidianos de la ingeniería de software y el diseño de sistemas, superando la visión puramente abstracta del modelo.  

   * **Método de los autores**: Expone estudios de caso descriptivos modelando sistemas reales como el motor de búsqueda Apache Lucene (mediante transductores de estados finitos) y máquinas expendedoras (como sistemas reactivos continuos).  

   * **Resultado principal**: Ilustra que las estructuras de datos basadas en autómatas finitos pueden optimizar drásticamente las búsquedas de cadenas, el autocompletado y el uso de memoria en comparación con otras alternativas de software.  

   * **Tema de la Unidad Temática I**: Concepto, formalización y diagramas de estados de los Autómatas Finitos Deterministas (AFD) y las máquinas de Mealy.  

   * **Aportación al curso**: Proporciona un puente directo entre la teoría matemática rígida de los AFD y su aplicación pragmática en la industria del software y la recuperación de información.  

   
2. **Articulo 2**. Luna-Benoso, B., Matinez-Perales, J. C., Cortes-Galicia, J., Flores-Carapia, R. y Silva-Garcia, V. M.(2022). Melanoma detection in dermoscopic images using a cellular automata classifier. *Computers*, 11(1), 8 https://www.mdpi.com/2073-431X/11/1/8  

   **Autómatas Celulares vs. Autómatas Finitos**  
   Ambos modelos son sistemas dinámicos discretos que operan en pasos de tiempo definidos y cuyos elementos pueden tomar valores de un conjunto finito. La diferencia principal radica en su topología y concurrencia. Un autómata finito procesa una cadena secuencial y la máquina completa se encuentra en un único estado a la vez. Un autómata celular (AC) consiste en una cuadrícula (o retícula) multidimensional donde múltiples celdas interactúan y cambian simultáneamente de forma paralela.  
      * **Estado**: Es el valor discreto que posee una celda individual en un instante específico (por ejemplo, en el procesamiento de imágenes del artículo, un estado binario 0 o 1 correspondiente a un píxel que pertenece o no a la lesión).  
      * **Vecindario**: Es el conjunto definido de celdas espacialmente adyacentes a una celda central (como el vecindario de Moore de 8 píxeles adyacentes) que influirán en el comportamiento de dicha celda.  
      * **Regla de transicion local**: Es la función matemática que determina cuál será el nuevo estado de una celda en la siguiente iteración, basándose exclusivamente en su estado actual y en los estados actuales de las celdas de su vecindario.  

   **El problema abordado y la eleccion del modelo**  
   Los autores abordan la segmentación y detección automática del melanoma (el cáncer de piel más agresivo) a partir de imágenes dermatoscópicas digitales, buscando separar con precisión la lesión del fondo de la piel sana para extraer sus características.  
   Eligen usar un Autómata Celular porque su estructura en cuadrícula mapea naturalmente con la matriz de píxeles de una imagen bidimensional. A diferencia de modelos secuenciales, los AC permiten aplicar operaciones de morfología matemática espacial (como erosiones y dilataciones) donde cada píxel se actualiza en función de sus vecinos. Esto los hace altamente eficientes para modelar variaciones locales de intensidad, eliminar ruido periférico y segmentar la geometría de la lesión con un costo computacional bajo en comparación con redes neuronales profundas.  
      * **Resultados**: El método propuesto basado en autómatas celulares demostró ser más efectivo para la detección de melanomas en comparación con otros métodos actuales del estado del arte, separando exitosamente el melanoma de otros tipos de lesiones.  
      * **Conjunto de imagenes**: Se midió utilizando el banco de imágenes dermatoscópicas (conocido como base de datos PH2) del servicio de dermatología del Hospital Pedro Hispano en Matosinhos, Portugal.  
      * **Metricas de evaluacion**: El rendimiento del clasificador se validó utilizando tres métricas estándar: sensibilidad, especificidad y exactitud (accuracy).  

   **Ficha**: Detección de Melanoma con Autómatas Celulares (Luna-Benoso et al.)  

   * **Cita**: Luna-Benoso, B., Martínez-Perales, J. C., Cortés-Galicia, J., Flores-Carapia, R., & Silva-García, V. M. (2022). Melanoma detection in dermoscopic images using a cellular automata classifier. Computers, 11(1), 8. https://doi.org/10.3390/computers11010008  

   * **Problema abordado**: La necesidad de métodos computacionales eficientes y precisos para segmentar automáticamente imágenes dermatoscópicas y asistir en el diagnóstico temprano del melanoma.  

   * **Método de los autores**: Desarrollan un clasificador aplicando autómatas celulares, usando reglas de transición local espaciales (morfología matemática) para que las celdas (píxeles) evolucionen e identifiquen la lesión separándola de la piel sana.  

   * **Resultado principal**: El modelo celular logró clasificar los melanomas de la base de datos PH2 con altos niveles de sensibilidad y exactitud, siendo altamente competitivo frente a algoritmos médicos actuales.  

   * **Tema de la Unidad Temática I**: Variantes de autómatas, demostrando que el concepto de "estados discretos y transiciones" puede extrapolarse a cuadrículas multidimensionales.  

   * **Aportación al curso**: Amplía la comprensión de los alumnos sobre los sistemas discretos dinámicos, demostrando que los modelos de estados y transiciones no se limitan a cadenas unidimensionales, sino a topologías visuales.  
  
3. **Articulo 3**: Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society*, s2-42(1), 230-265. [1].  
   **Resultado demostrado y modelo introducido**  
   El artículo introduce el modelo matemático de la "máquina computadora" (lo que hoy conocemos como la Máquina de Turing) y la invención de la "máquina universal" (capaz de simular a cualquier otra máquina al leer su descripción codificada en la cinta).  
   El resultado principal que demuestra es que el Entscheidungsproblem (el problema de decisión propuesto por David Hilbert) es matemáticamente irresoluble. Turing prueba que no existe ningún procedimiento mecánico o algoritmo general que pueda determinar de antemano si una fórmula matemática arbitraria es válida o no. Para llegar a esta conclusión, demuestra primero que es imposible construir una máquina que determine si otra máquina cualquiera llegará a detenerse alguna vez o si calculará para siempre (lo que hoy conocemos como la indecidibilidad del Problema de la Parada).  

   **La Tesis de Church-Turing**  
   * **Enunciado preciso**: Toda función que sea natural, intuitiva o efectivamente calculable (es decir, cualquier cálculo lógico que un ser humano pueda resolver siguiendo instrucciones precisas paso a paso con tiempo y papel ilimitados) es computable por una Máquina de Turing.  
   * **Por qué es una tesis y no un teorema**: Un teorema es una proposición que puede demostrarse lógicamente a partir de axiomas estrictos. La Tesis de Church-Turing no puede ser probada matemáticamente porque conecta un concepto formal, riguroso y exacto (la Máquina de Turing) con un concepto cognitivo, humano e informal ("lo que es un algoritmo" o "lo que es efectivamente calculable"). Se denomina tesis porque es un postulado fundacional aceptado universalmente por la abrumadora evidencia empírica (todo modelo de cómputo propuesto en los últimos 90 años ha resultado ser equivalente o inferior en poder a la Máquina de Turing), pero por la naturaleza informal de una de sus partes, no es susceptible de una demostración matemática formal.  
     
   **Dificultad de lectura y resolucion**  

   La mayor barrera al leer el texto original de Turing radica en su notación tipográfica y en cómo define el comportamiento de su máquina. A diferencia de los libros de texto actuales, Turing utiliza extensas tablas para definir las transiciones de estado (lo que él llama m-configurations) y emplea letras del alfabeto gótico alemán (Fraktur, como $\mathfrak{S}$, $\mathfrak{M}$) para representar dichas configuraciones y rutinas. Esto resulta visualmente confuso y muy ajeno a la notación estándar de funciones de transición de los cursos actuales. 
      
   **Resolución**: Para superar esta dificultad, es necesario traducir mentalmente (o en papel) sus tablas de comportamiento al modelo moderno de diagramas de estados (grafos dirigidos) y a la notación estándar de tuplas como $M=(Q,\Sigma,\delta,q_0,F)$. Apoyarse en literatura que disecciona este artículo original —como el libro The Annotated Turing de Charles Petzold, que traduce el documento de 1936 al lenguaje moderno de ciencias de la computación— facilita enormemente seguir la lógica matemática sin perderse en la tipografía antigua.  
     
     [1] **Nota sobre la fecha del artículo**: *En la literatura y los libros de texto, este artículo se cita de forma casi universal como un trabajo de 1936 porque Alan Turing lo terminó de escribir, lo entregó y fue leído ante la Sociedad Matemática de Londres en ese año (específicamente en noviembre). Sin embargo, el DOI oficial y muchos catálogos indexan el documento como de 1937 debido a que la revista (Proceedings) se imprimía y publicaba por fascículos, y las páginas correspondientes al trabajo de Turing salieron físicamente de la imprenta a principios de 1937.*  
  
**Ficha**: Números Computables y el Problema de la Parada (Turing)  

   * **Cita**: Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. Proceedings of the London Mathematical Society, s2-42(1), 230-265. https://doi.org/10.1112/plms/s2-42.1.230  

   * **Problema abordado**: Resolver el Entscheidungsproblem formulado por David Hilbert, determinando si existe un proceso puramente mecánico general para decidir si una fórmula matemática es verdadera o falsa.  

   * **Método de los autores**: Define teóricamente la "máquina computadora" (Máquina de Turing) usando una cinta infinita, estados finitos y una cabeza lectora/escritora para formalizar el concepto abstracto de "algoritmo" paso a paso.  

   * **Resultado principal**: Demuestra la irresolubilidad del Entscheidungsproblem al probar, de manera análoga al teorema de Gödel, que existen problemas (como predecir si una máquina se detendrá o no) que no pueden ser computados mecánicamente.  

   * **Tema de la Unidad Temática I**: Definición y componentes de la Máquina de Turing, la noción algorítmica y la Tesis de Church-Turing.  

   * **Aportación al curso**: Establece la base teórica fundamental de todas las Ciencias de la Computación, definiendo los límites matemáticos absolutos de lo que cualquier software y hardware puede llegar a calcular.  

4. **Articulo 4**. Sadredini, E., Rahimi, R., Lenjani, M., Stan, M., & Skadron, K. (2020). Impala: Algorithm/Architecture Co-Design for In-Memory Multi-Stride Pattern Matching. 2020 *IEEE International Symposium on High Performance Computer Architecture (HPCA)*, 442-455. https://doi.org/10.1109/HPCA47549.2020.00017  
   **Resumen y analisis**  
   * **Problema abordado**: La Inspección Profunda de Paquetes (DPI, por sus siglas en inglés) en los sistemas de detección de intrusiones de red requiere procesar masivamente el tráfico contra miles de reglas de seguridad expresadas como patrones. Tradicionalmente, esto se implementa mediante autómatas finitos que leen la entrada byte por byte, lo cual genera un cuello de botella severo que limita el ancho de banda y la velocidad de detección de ataques en tiempo real.  

   * **Modelo formal aplicado**: El artículo reestructura la implementación algorítmica de los Autómatas Finitos No Deterministas (AFN) y Deterministas (AFD) utilizando un enfoque matemático de "zancada múltiple" (multi-stride automata). Esto modifica las funciones de transición para que el autómata pueda procesar y consumir múltiples símbolos (bytes) en un solo ciclo de reloj de forma equivalente a la versión de un solo byte.  

   * **Resultado principal**: Los autores introducen una arquitectura basada en memoria (SRAM) específicamente diseñada para evaluar estos autómatas modificados, logrando un aumento drástico en la velocidad del escaneo de red sin que se dispare exponencialmente el uso de memoria RAM (el principal problema al convertir AFNs a AFDs puros).  
   
**Ficha**: Autómatas para Inspección de Redes (Sadredini et al.)  

   * **Cita**: Sadredini, E., Rahimi, R., Lenjani, M., Stan, M., & Skadron, K. (2020). Impala: Algorithm/Architecture Co-Design for In-Memory Multi-Stride Pattern Matching. 2020 IEEE International Symposium on High Performance Computer Architecture (HPCA), 442-455. https://doi.org/10.1109/HPCA47549.2020.00017  

   * **Problema abordado**: La inspección masiva de paquetes en los sistemas de ciberseguridad mediante expresiones regulares sufre cuellos de botella severos porque los AFDs tradicionales procesan un solo carácter a la vez.  

   * **Método de los autores**: Proponen autómatas espaciales de "zancada múltiple" (multi-stride) diseñados junto con una arquitectura en memoria para evaluar múltiples transiciones y caracteres simultáneamente en cada ciclo de reloj.  

   * **Resultado principal**: La arquitectura logró acelerar exponencialmente la detección de intrusiones sin causar la explosión inmanejable de consumo de memoria RAM que tradicionalmente ocurre al optimizar AFNs.  

   * **Tema de la Unidad Temática I**: Transformación de expresiones regulares a AFN y de AFN a AFD (Algoritmo de subconjuntos) y evaluación de la complejidad espacial de los estados.  

   * **Aportación al curso**: Ilustra un compromiso de la vida real entre tiempo de ejecución y espacio en memoria, evidenciando por qué es crucial minimizar los estados de un autómata en arquitecturas computacionales.  
     
5. **Articulo 5**. Eggers, D., Höner zu Siederdissen, C., & Stadler, P. F. (2022). Accuracy of RNA Structure Prediction Depends on the Pseudoknot Grammar. En *Lecture Notes in Computer Science* (Vol. 13619, pp. 20-31). Springer. https://doi.org/10.1007/978-3-031-21175-1_3  
   **Resumen y analisis**  
   * **Problema abordado**: La predicción computacional de las estructuras secundarias de las moléculas de ARN. Históricamente, el plegamiento del ARN se modelaba bien con gramáticas de Tipo 2 (Libres de Contexto), pero ciertas estructuras tridimensionales entrelazadas, biológicamente cruciales y conocidas como "seudonudos" (pseudoknots), presentan dependencias cruzadas que las gramáticas libres de contexto tradicionales son matemáticamente incapaces de reconocer.  

   * **Modelo formal aplicado**: El trabajo recurre a las Gramáticas Múltiples Libres de Contexto (MCFG), una clase de lenguajes ligeramente sensibles al contexto (ubicadas entre el Tipo 1 y el Tipo 2 en la jerarquía de Chomsky). Los autores diseñan reglas de producción sintáctica para "analizar" (hacer el parsing de) la secuencia de bases nitrogenadas como si fuera un lenguaje de programación.  

   * **Resultado principal**: Demuestran que la biología molecular y la lingüística formal están íntimamente ligadas en este nivel; concluyen experimentalmente que el diseño matemático estricto de las reglas de producción en la gramática elegida altera de forma crítica la exactitud computacional al predecir la estructura biológica final de la molécula frente a conjuntos de datos del mundo real.  
  
**Ficha**: Gramáticas en el Plegamiento de ARN (Eggers et al.)   

   * **Cita**: Eggers, D., Höner zu Siederdissen, C., & Stadler, P. F. (2022). Accuracy of RNA Structure Prediction Depends on the Pseudoknot Grammar. En Lecture Notes in Computer Science (Vol. 13619, pp. 20-31). Springer. https://doi.org/10.1007/978-3-031-21175-1_3  

   * **Problema abordado**: Las gramáticas libres de contexto (Tipo 2) estándar son insuficientes para predecir los entrecruzamientos espaciales complejos (seudonudos) que se forman al plegarse la cadena de ARN.  

   * **Método de los autores**: Usan y analizan Gramáticas Múltiples Libres de Contexto (una subclase más expresiva que el Tipo 2) para modelar sintácticamente las reglas de unión de las bases nitrogenadas moleculares.  

   * **Resultado principal**: Comprueban empíricamente que la precisión final de la estructura biológica predicha en los simuladores depende estrictamente del rigor de las reglas formales de producción definidas en la gramática elegida.  

   * **Tema de la Unidad Temática I**: La Jerarquía de Chomsky, específicamente los límites formales de las Gramáticas Libres de Contexto frente a lenguajes más complejos.  

   * **Aportación al curso**: Demuestra la asombrosa interdisciplinariedad de la teoría, probando que las reglas de producción usadas para compilar lenguajes de programación sirven igualmente para parsear el "código fuente" de la genética biológica.  

<div align="center">

| Texto | Arbitrado | Año | Modelo que usa | Campo de apllicacion |  
| :--- | :--- | :--- | :--- | :--- |  
| **1. Gribkoff** | No | 2013 | AFD / Maquinas de Mealy | Recuperacion de informacion / Software |  
| **2. Luna Benoso** | Si | 2022 | Automatas Celulares | Procesamiento de imagenes / Medicina |  
| **3. Turing** | Si | 1936 | Maquina de Turing | Fundamentos de Matematicas /Computabilidad |  
| **4. Sadredini** | Si | 2020 | AFD y AFND Modificados | Ciberseguridad / Arquitectura de Redes |  
| **5. Eggers** | Si | 2022 | Gramaticas (Libres y Multiples) | Bioinformatica / Genetica |  

</div>  

**Comparativa**  
A pesar de sus distintos contextos y épocas, los cinco textos comparten un núcleo metodológico: utilizan las abstracciones de la Teoría de la Computación (autómatas, estados, transiciones y gramáticas) para gobernar el comportamiento de sistemas complejos. Ya sea evaluando una proposición matemática (Turing), detectando un ataque cibernético (Sadredini) o descifrando las secuencias de ARN (Eggers), todos emplean conjuntos finitos de reglas estrictas para procesar o clasificar cadenas de datos de entrada.  

Sin embargo, difieren radicalmente en propósito y rigor formal. Mientras que el texto fundacional de Turing es puramente teórico, riguroso y busca definir los límites absolutos de lo matemático, el documento de Gribkoff persigue un fin puramente educativo sin validación por pares. Por el contrario, los artículos de Luna-Benoso, Sadredini y Eggers representan investigaciones empíricas y aplicadas. No buscan probar teoremas absolutos sobre los autómatas o las gramáticas en sí mismos, sino adaptarlos, medirlos estadísticamente (sensibilidad, tiempos de reloj, exactitud predictiva) y explotar sus propiedades para resolver problemas contemporáneos de otras disciplinas.  

A partir de estas lecturas, surge un problema abierto significativo en la intersección de la teoría de lenguajes y la arquitectura de computadoras: la escalabilidad temporal y espacial de los reconocedores para lenguajes superiores al Tipo 3 de Chomsky. Actualmente, aunque existe hardware altamente optimizado (como el abordado por Sadredini) para escanear en paralelo patrones de expresiones regulares a gigabits por segundo, no contamos con arquitecturas y algoritmos equivalentes de ultra alta velocidad capaces de analizar masivamente reglas gramaticales superiores (Tipos 1 y 2, como los necesarios en la bioinformática de Eggers) o lenguajes que exigen reconocimiento mediante autómatas de pila de manera fluida y en tiempo real bajo severas restricciones de memoria y energía eléctrica.  
