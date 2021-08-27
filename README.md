## Gluky Challenge
El proyecto consistió en lo siguiente:
 - Obtener los datos sobre ventas de E-commerce.
 - Limpiar la información con errores.
 - Crear la base de datos en Cloud Firestore con Firebase.
 - Conectar Firestore con Python.
 - Preparar e insertar en Firestore los datos en formato JSON.
 - Generar el pipeline que se encarga de Parsear los datos, obtener información del usuario, obtener los datos desde Firestore y generar reportes en formato Excel. 

## Manual de uso
Librarías que requieren ser instaladas en un entorno virtual de Python:
 - pip install firebase_admin
 - pip install pandas
 - pip install openpyxl

**Si tienes sistema operativo Windows:** El archivo **install_libraries.bat** facilita esta tarea de instalación del entorno virtual y librerías, solo requiere que se ejecute y esperar a que instale todo, una vez haya terminado informara y se cerrara la ventana. (En caso de que no se cierre automáticamente, se puede cerrar manualmente una vez haya informado que ha terminado) 

Una vez se ha iniciado el entorno virtual con las librerías instaladas, se debe ejecutar el archivo **main.py**. 
Se le pedirá informacion sobre el rango de fechas para poder generar el reporte, ingresar las fechas con el formato **YYYY-MM-DD**.

El pipeline obtendrá la informacion y generara el reporte dentro de la carpeta excel.
