# Administrador_Aguas_cordobesas
 
// Instalación

Para poder utilizar el programa se necesita Python3 de 32-bit (Version de python utilizada en el desarrollo: Python 3.9.1 32-bit).
Python3 se puede descargar del siguiente link: 'https://www.python.org/downloads/release/python-391/'
Asegurarse de incluir Python3 al PATH.

Para poder usar el programa se deben instalar los siguientes modulos (se puede copiar y pegar en una terminal o cmd):
    - selenium (pip3 install selenium)
    - openpyxl (pip3 install openpyxl)
    - PySide2 (pip3 install PySide2)
    - pyodbc (pip3 install pyodbc)
    - pyautogui (pip3 install pyautogui)

También se necesita actualizar el 'chromedriver.exe' a medida que Chrome se actualiza.
ChromeDriver se puede descargar del siguiente link: 'https://chromedriver.chromium.org/downloads'



// Ejecución

Para ejecutar el programa se debe correr el archivo 'main_code.py'.

Para correr un archivo python se puede abrir un cmd en la carpeta del archivo y ejecutar el comando "python3 'nombre_del_archivo'.py"


// Funcionamiento

El objetivo de este proyecto es poder administrar los clientes de una inmobiliaria. La funcionalidad del programa consta en poder buscar datos en internet por medio de Python.

Primero el programa tiene que cargar la base de datos access donde se guardan los clientes con su informacion.
Despues el programa puede buscar los montos a pagar de esos clientes para así actualizar los valores. (proceso automático que demora 5 min)
También el programa permite buscar el monto a pagar de un cliente por separado, si este posee cuenta en Aguas Cordobesas.

