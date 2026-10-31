# CheckPoint 8: Método de Euler

Este proyecto resuelve una ecuación diferencial mediante el método de Euler y compara los resultados con su solución exacta. El objetivo es observar cómo se aproxima una solución numérica y qué diferencias presenta respecto a la solución analítica.

## Planteamiento del problema

Se considera el siguiente problema de valor inicial:

$$
\frac{dy}{dt}=-2y, \qquad y(0)=1
$$

Se busca calcular el valor de $y(t)$ en el intervalo $0 \leq t \leq 1$, utilizando un tamaño de paso $h=0.2$.

La ecuación describe un decaimiento exponencial: la rapidez con la que disminuye la variable es proporcional a su valor actual. Como ejemplo, puede representar una cantidad que se reduce con el tiempo.

## Solución exacta

Al separar variables e integrar se obtiene:

$$
\frac{dy}{y}=-2\,dt
\quad\Longrightarrow\quad
y(t)=Ce^{-2t}
$$

Aplicando la condición inicial $y(0)=1$, resulta $C=1$. Por lo tanto:

$$
y(t)=e^{-2t}
$$

## Método de Euler

El método aproxima el siguiente valor de la solución utilizando la pendiente en el punto actual:

$$
y_{n+1}=y_n+h f(t_n,y_n)
$$

Para este problema, $f(t,y)=-2y$ y $h=0.2$, de modo que:

$$
y_{n+1}=y_n+0.2(-2y_n)=0.6y_n
$$

Se inicia con $t_0=0$ y $y_0=1$. Por ejemplo, la primera aproximación es $y_1=0.6$, correspondiente a $t_1=0.2$.

## Resultados esperados

| Tiempo | Solución exacta | Euler |
| --- | --- | --- |
| 0.0 | 1.000000 | 1.000000 |
| 0.2 | 0.670320 | 0.600000 |
| 0.4 | 0.449329 | 0.360000 |
| 0.6 | 0.301194 | 0.216000 |
| 0.8 | 0.201897 | 0.129600 |
| 1.0 | 0.135335 | 0.077760 |

Con este tamaño de paso, Euler produce valores menores que la solución exacta después del punto inicial. En $t=1$, el error absoluto es aproximadamente $0.057575$. Reducir el tamaño de paso permite mejorar la aproximación en este problema.

## Requisitos y ejecución

Se necesita Python 3 con las bibliotecas NumPy y Matplotlib. Desde una terminal ubicada en la carpeta del proyecto, instala las dependencias:

```powershell
python -m pip install numpy matplotlib
```

Ejecuta el programa:

```powershell
python checkpoimt8.py
```

El programa imprime una tabla con el tiempo, la solución exacta y la aproximación de Euler. Después muestra una gráfica para comparar ambas soluciones en los puntos calculados.

## Archivo principal

- `checkpoimt8.py`: define la ecuación diferencial, realiza las iteraciones de Euler, calcula la solución exacta y muestra los resultados.
