# Ejercicio 5. Aplicacion con Interfaz grafica

**Sobre la Operación 1 (Subcadenas, prefijos y sufijos)**  

   * **Prefijos de longitud $n$**: Una cadena de longitud $n$ posee siempre $n + 1$ prefijos, porque se cuenta desde el prefijo de longitud 0 hasta el prefijo de longitud $n$ (la cadena completa).  

   * **Subcadenas distintas máximas**: El límite máximo de subcadenas distintas (si todos los caracteres son diferentes) está dado por la fórmula $\frac{n(n+1)}{2} + 1$.  

   * **Justificación de la cadena vacía**: El programa sí incluye la cadena vacía ($\epsilon$) tanto en los prefijos como en los sufijos y subcadenas. En la teoría de lenguajes formales, el símbolo $\epsilon$ denota la cadena de longitud cero. Dado que la concatenación de $\epsilon$ con cualquier cadena $w$ resulta en la propia cadena ($\epsilon \cdot w = w \cdot \epsilon = w$), la cadena vacía es estructuralmente un prefijo y un sufijo trivial de cualquier secuencia de caracteres.  
   
**Sobre la Operación 2 (Cerraduras y el límite de 200,000)**  

   * **Relación del límite con la teoría**: La cerradura de Kleene ($\Sigma^*$) representa el conjunto infinito de todas las cadenas posibles sobre un alfabeto. En computación práctica, calcular este conjunto infinito es imposible, por lo que lo restringimos a una longitud máxima $n$.  

   * Sin embargo, el crecimiento del conjunto es exponencial. Para un alfabeto de tamaño $k$, la cantidad de cadenas generadas hasta longitud $n$ obedece a la serie geométrica $\frac{k^{n+1}-1}{k-1}$. El límite de 200,000 implementado demuestra la "explosión combinatoria": ilustra físicamente cómo una estructura finita de reglas formales (un alfabeto pequeño y operaciones de concatenación) puede saturar rápidamente los recursos de memoria temporal (RAM) y procesamiento al intentar enumerar los elementos del lenguaje.  
   
   **Tabla de Ejecución en Contenedores**  

<div align="center">

| Entorno Docker | Comando Utilizado | Resultado Pytest | Observaciones de Ejecución |  
| :--- | :--- | :--- | :--- |  
| **Python 3.11** | docker compose run --rm py311 pytest -q | 5 passed | Ejecución estándar sin advertencias de deprecación. |  
| **Python 3.12** | docker compose run --rm py312 pytest -q | 5 passed | Se utilizó este contenedor además para montar el puerto 8000 de Flet. |  
| **Python 3.13** | docker compose run --rm py313 pytest -q | 5 passed | Tiempo de ejecución marginalmente menor; sintaxis 100% compatible. |  

</div>

## Anexo evidencias

**Evidencia**

![3.11](<../evidencias/Ejercicio 5/prueba1.png>)  

![3.12](<../evidencias/Ejercicio 5/Prueba2.png>)  

![3.13](<../evidencias/Ejercicio 5/prueba3.png>)  

![App](<../evidencias/Ejercicio 5/Screenshot 2026-10-05 185750.png>)

![Codigo App](<../evidencias/Ejercicio 5/Screenshot 2026-10-05 190924.png>)
