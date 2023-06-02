# Task Manager

Task manager es una aplicación CLI para la gestión de tareas.

# Instalación

Al estar todo escrito Python, simplemente se necesita instalar las dependencias necesarias, las cuales estan escritas en el archivo requirements.txt. 

Para hacer la instalación se puede utilizar pip:

```
pip install -r requirements.txt
```

Es recomendable utilizar un entorno virtual para la ejecución de este programa.

# Como usarlo

Este programa esta compuesto por dos elementos principales, un servidor a modo de backend y un programa de consola a modo de frontend.

Para utilizar Task Manager, primero se debe arrancar el servidor. Esto se puede hacer ejecutando el comando `python3 server.py`. Una vez que el servidor arranque, creará también la base de datos si es que esta no existe.

Cuando tengamos el servidor funcionando, podemos abrir otra consola y ejecutar el frontend, para ello se debe escribir `python3 task_manager.py`. 

Desde este frontend podremos mandar nuestras peticiones a la API.

