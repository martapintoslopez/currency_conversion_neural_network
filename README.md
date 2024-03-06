# Currency Conversion Neural Network

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

