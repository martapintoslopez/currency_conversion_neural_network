# Currency Conversion Neural Network
ESte proyecto se centró en desarrollar una red neuronal capaz de realizar conversiones entre distintas divisas. Se llevó a cabo un proceso de recopilación de datos y una vez preparados, se procedió al diseño y entrenamiento de la red neuronal. Durante esta fase, se utilizó un enfoque de aprendizaje supervisado para ajustar iterativamente el modelo a los datos conocidos. Posteriormente, se realizaron pruebas para evaluar su rendimiento y precisión en la conversión de divisas, incluyendo la comparación con datos reales y la identificación de posibles áreas de mejora en la arquitectura del modelo.

Este repositorio consta de dos archivos, uno para el manejo principal y otro para las funciones de conversión.

## Archivo Main
### Uso
El archivo main.py maneja la interacción principal con el usuario. Al ejecutar este archivo, el programa solicitará al usuario que elija entre varias opciones para realizar conversiones de divisas. Las opciones disponibles son las siguientes:

1. Euros a dólares
2. Dólares a euros
3. Euros a libras
4. Libras a euros
5. Euros a yenes
6. Yenes a euros

Una vez que el usuario elige una opción, el programa invocará las funciones correspondientes del archivo conversion.py para realizar la conversión deseada.

## Archivo Conversion
El archivo conversion.py contiene las funciones necesarias para realizar las conversiones de divisas. Se incluyen funciones para convertir entre euros, dólares, libras y yenes.

Las funciones disponibles son las siguientes:

- euros_dolars(): Convierte euros a dólares.
- dolars_euros(): Convierte dólares a euros.
- euros_pounds(): Convierte euros a libras.
- pounds_euros(): Convierte libras a euros.
- euros_yen(): Convierte euros a yenes.
- yen_euros(): Convierte yenes a euros.

Las tasas de conversión utilizadas en estas funciones se basan en modelos de redes neuronales entrenados previamente.

