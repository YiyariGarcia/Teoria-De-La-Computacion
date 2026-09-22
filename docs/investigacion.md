# Ejercicio 2. Investigacion: ¿Que es la Teoria de la Computacion?  

1. **¿Que es la Teoria de la Computaciuon y que preguntas se plantea. Incluya la definicion de al menos dos autores distintos y comparelas.**  

   * **R:** La Teoria de la Computacion es una rama de las Ciencias de la Computacion y de las Matematicas que estudia las capacidades, propiedades y limitaciones fundamentales del computo y de los algoritmos.  
   La Teoria de la computacion abstrae la maquina fisica y trabaja con **modelos matematicos puros**. Su objetivo no es estudiar como constuir una computadora mas rapida, sino entender que se puede resolver mediante procesos mecanicos o algoritmicos sin importar el poder del hardware.  

   **Dos definiciones de 2 autores sobre la Teoria de la Computacion**  

   * **Michael Sipser** (*Introduction to the Theory of Comnputation*)  
   Para Michael Sipser, la Teoria de la Computacion se divide en tres areas entrelazadas: **Automatas**, **Computabilidad** y **Complejidad**.
   "El objetivo principal de la teoria de la computacion es desarrollar modelos matematicos de computacion que permitan responder a las preguntas sobre que se puede y que no se puede computar, y clasificar los problemas segun su dificultad inherente."  

   * **Jhon E. Hopcroft, Rajeev Motwani y Jeffrey D. Ullman** (*Introduction to Automata Theory, Languages, and Computation*)  
   "La teoria de la computacion es el estudio de las maquinas abstractas (automatas) y los problemas que estas son capaces de resolver, estableciendo una equivalencia matematica entre las clases de lenguajes que puedan ser reconocidos y los modelos de computo necesarios para procesarlos".  
   
   **Dos preguntas que se plantea**  

   La Teoria de la Computacion gira en torno a tres preguntas:  

      * ¿Que es un modelo de computo?.
      * ¿Que se puede computar?.
      * ¿Con que eficiencia se puede computar?  

2. **Sus origenes: el programa de Hilbert, el Entscheidungsproblem y las paradojas de la logica matematica.**  
  
   **R:** La Teoria de la Computacion no nacio del intento de construir maquinas electronicas o procesadores de silicio, sino de una profunda crisis matematica y logica a principios del siglo XX. Los matematicos buscaban automatizar la verdad matematica y garantizar que la logica estuviera libre de contradicciones.  
   **Las Paradojas de la Logica Matematica**  
   A finales del siglo XIX, matematicos como Georg Cantor (Creador de la Teoria de Conjuntos) y Gottlob Frege intentaron reducir todas las matematicas a leyes puras de la logica (*Logicismo*). Sin embargo, este intento se desmorono debido al descubrimiento de paradojas logicas profundas:  
      * **La Paradoja de Russell (1901):** Descubierta por Bertrand Russell, expuso una falla en la teoria ingenua de conjuntos. Russell planteo el conjunto **`R`** de todos los conjuntos que no se contienen a si mismos como miembros:
      `R = {x | x no pertenece a x}`  
      Al preguntar si **`R`** pertenece a si mismo, surge la contradiccion: Si **`R`** pertenece al mismo **`R`**, entonces por definicion **`R`** no pertene a **`R`**, entonces por definicion **`R`** si pertenece a **`R`**.  
    
    **Impacto:** Esta contradiccion demostraron que la logica matematica podia colapsar si no se establecieron reglas extremadamente rigurosas. Esto desencadeno la llamada "Crisis de los Fundamentos de las Matematicas".

    * **El Programa de Hilbert**  
    Para rescatara las matematicas del caos de las paradojas, el renombrado matematico aleman David Hilbert propuso en la decada de 1920 un ambicioso plan de formalizacion conocido como el Programa de Hilbert.  
    Hilbert proponia reestructurar todas las matematicas sobre un sistema axiomatico formal unico y definitivo que cumpliera tres condicionesfundamentales:  
       * **Consistencia:** Demostrar matematicamente que el sistema jamas produciria una contradiccion.
       * **Completitud:** Probar que el sistema era capaz de demostrar o refutar cualquier enunciado matematico verdadero expresado dentro de el.
       * **Decibilidad:** Encontrar un metodo o procedimiento mecanico para determinar si una proposicion matematica dada era valida o no.  

    * **El Entscheidungsproblem (El Problema de la Decision)**  
    Formulado formalmente por David Hilbert y Wilhelm Ackermann en 1928, el Entscheidungsproblem fue el punto culminante del Programa de Hilbert.  
    *¿Existe un algoritmo o "procedimiento mecanico universal" que tome como entrada cualquier enunciado expresado en logica de primer orden y determine, en un numero finito de pasos de manera automatica, si dicho enunciado es verdaderamente valido?*  
    Para resolver esta pregunta, los matematicos se enfrentaron a una paradoja previa: para demostrar que un "procedimiento mecanico" exista o no, primero necesitaban definir matematicamente que es un "procedimiento mecanico" mejor conocido hoy en dia como algoritmo.  

3. **Sus tres ramas, computabilidad, complejidad, y teoria de automatas y lenguajes formales, y la pregunta que responde cada una.**  
    * **Teoria de Automatas y Lenguajes Formales**  
    Esta rama estudia los modelos matematicos abstractos de dispositivos de computo y la estructura de los lenguajes que estos dispositivos pueden reconocer o generar.  
    **Pregunta**  
    *¿Cuales son las propiedades matyyematicas de los modelos abstractos de computo y que tipos de lenguajes o patrones pueden procesar?*  

    Define la jerarquia de las maquinas teoricas y establece que capacidad de memoria o procesamiento necesita un sistema para reconocer determinado tipo de lenguaje (Jerarquia de Chomsky).  

    **Modelos y conceptos clave:**  
       * **Automatas Finitos (DFA / NFA):** Sin memoria auxiliar: reconocen Lenguajes Libres Regulares (expresiones regulares, validacion de formatos).  
       * **Automata de Pila (PDA):** Memoria de tipo LIFO(Pila): reconocen Lenguajes Libres de Contexto (sintaxis de lenguajes de programacion, balanceo de parentesis).
       * **Maquina de Turing(TM):** Memoria infinita en cinta: reconocen Lenguajes Recursivamente Enumerables.  

    * **Teoria de la Computabilidad**  
    Esta rama explora los limites absolutos del computo. Se encarga de clasificar los problemas entre aquellos que pueden ser resueltos mediante un algoritmo y aquellos que son fundamentalmente irresolubles, independientemente de la potencia del hardware o del tiempo disponible.  
    **Pregunta**
    *¿Que problema son resolubles mediante un algoritmo (computables) y cuales son inherentemente irresolubles (indecidibles)?*  

    No le importa la velocidad o la memoria que tome la solucion, sino la existencia o inexistencia de un algoritmo que garantice llegar a una respuesta correcta en un numero finito de pasos.  

    **Conceptos clave:**
       * **Tesis de Church-Turing:** Afirma que la nocion intuitiva de "algoritmo" o "procedimiento mecanico" queda completamente capturada por la Maquina de Turing o el Calculo Lambda.
       * **Problemas Decidibles vs. Indecidibles:** Un problema es decidible si existe un algoritmo que siempre responde "Si" o "No" correctamente y se detiene.
       * **El Problema de la Parada (Halting Problem):** Demostracion formulada por Alan Turing de que no existe ningun algoritmo que pueda determinar si un programa cualquiera se detendra o se quedara en un bucle infinito.  

    * **Teoria de la Complejidad Computacional**  
    Esta rama estudia la cantidad de recursos computacionales que requiere un algoritmo para resolver un problema computable.  
    **Pregunta**  
    *Entre los problemas que si tienen solucion algoritmica, ¿cuanta memoria y tiempo se necesitan para resolverlos, y que un problema sea "facil" o "dificil" en la practica?*  

    Clasifica los problemas en clases de complejidad en funcion de como crece el consumo de recursos conforme aumenta el tamaño de la entrada (n).  

    **Conceptos y clases clave:**  
       * **Notacion Asintotica:** Mide el crecimiento del tiempo o espacio.  
       * **Clase P (Tiempo Pol;inomial):** Problemas considerados "faciles" o tratables en la practica.  
       * **Clase NP (Polinomial No Determinista):** Problemas cuyas soluciones son dificiles de encontrar, pero una vez dadas, son "faciles" de verificar en tiempo polinomial.  
       * **El Problema del Milenio (P vs NP):** ¿Es acaso P = NP? (Es decir, ¿todo problema cuya solucion se puede verificar rapidamente tambien se puede resolver rapidamente?).  

4. **Alfabeto, cadena y lenguaje, con sus definiciones formales. Las operaciones sobre cadenas y sobre lenguajes: concatenacion, potencia, reflexion, union, interseccion, diferencia, cerradura de Kleene y cerradura positiva. Explique porque Sigma^0 = {lambda} y que distingue a Sigma^ de Sigma^+**  
    * **Alfabeto:** Conjunto finito y no vacio de simbolos abstractos.  
    * **Cadena:** Secuencia finita de simbolos seleccionados a partir de un alfabeto. Su longitud corresponde al numero total de simbolos que la integran. La cadena vacia es la secuencia que no contiene ningun simbolo y cuya longitud es cero.  
    * **Lenguaje:** Conjunto de cadenas compuestas por simbolos de un determinado alfabeto. Un lenguaje puede ser finito, infinito o vacio.  

    **Operaciones sobre Cadenas**
    * **Concatenacion:** Operacion que une a dos cadenas en orden, colocando lkos simbolos de la segunda inmediatamente despues de los simbolos de la primera.  
    * **Potencia:** Repeticion y concatenacion secuencial de una cadena consigo misma una cantidad determinada de veces. La potencia cero de cualquier cadena siempre produce la cadena vacia.  
    * **La Reflexion:** Conjunto formado por la version invertida de cada una de lkas cadenas que pertenece al lenguaje original.  
    * **Union:** Conjunto de las cadenas que estan pertenecen al primer lenguaje, al segundo lenguaje o a ambos.  
    * **Interseccion:** Conjunto de las cadenas que estan presentes de manera simultanea en ambos lenguajes.  
    * **Diferencia:** Conjunto de cadenas que pertenecen al primer lenguaje pero que no forman parte del segundo.  
    * **Cerradura de Kleene (Estrella):** Conjunto formado por la combinacion de todas las potencias posibles de un lenguaje comenzando desde cero hasta erl infinito. Incluye la cadena vacia.  
    * **Cerradura positiva:** Conjunto formado por la union de todas las potencias de un lenguaje solo que sin incluir la cadena vacia.  

    **Explicaciones de Propiedades**  
    * **¿Porque Sigma^0 = {lambda}?**  
    Porque la potencia cero representa la cadena vacia.  
    * **¿Que distingue a Sigma^( * ) de Sigma+?**  
    Son equivalentes, lo unio que las distingue es que a la Cerradura de Kleene contiene la cadena vacia, mientra que la Cerradura positiva no contiene la cadena vacia.