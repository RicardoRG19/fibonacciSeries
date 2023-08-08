# fibonacciSeries
API que devolverá el valor de Fibonacci que corresponde al índice dado "n"

La lógica de programación es la siguiente:
1.- Lo primero que hago es importar flask que es una librería en python para la creación de API's.
2.- Instacio la clase Flask para que pueda crear de manera adecuada la aplicación web.
3.- Creo una función llamada calc_fibonacci, con la cual primero que nada valido si el valor "n" es menor a 0 (osea es un valor negativo), si es así, entonces crearía una excepción mencionando dicho error.
4.- Cuando en la serie de fibonacci nos seleccionamos el índice 0, nos debe devolver 0, y si seleccionamos el índice 1, nos debe devolver el índice 1, justo eso es lo que se valida en los siguientes 2 elif's.
5.- En el else a continuación, creamos dos variables "a" y "b" de manera simultánea y con los valores "0" y "1" según corresponden.
Estas variables nos sevirán para partir desde donde vamos a tener que empezar a calcular los últimos 2 valores según el rango elegido partiendo de 2 hasta "n" + 1 (teniendo en cuenta que el índice comienza desde cero).
6.- El el ciclo for lo que hacemos es sólo ir actualizando los valores de las variables "a" y "b" utilizando la asignación múltiple, teniendo en cuenta que el valor b siempre estará obtieniendo el valor del cálculo entre "a" + "b" y que "a" estaría quedandose con el valor de "b", esto hasta terminar de recorrer el rango determinado por la variable "n" y retornando el valor final.
7.- En el código tambien veremos la definición del @app.route en donde estaremos estructurando el como vamos a llamar a nuestra API y por medio de que método, en este caso GET. Además, en la ruta definida, se esta agregando una variable de tipo entero para que pueda capturar el valor que se enviará.
8.- Luego de esto, la función get_fibonacci_value lo que hace es darle una estructura JSON a el valor que se va a devolver, o bien marcar un error de entrada.

