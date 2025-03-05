Detección de colores con OpenCV y Python
Este proyecto permite detectar colores en tiempo real utilizando una cámara web. Está desarrollado en Python y utiliza la librería OpenCV para el procesamiento de imágenes y la detección de colores basada en rangos HSV.

Características principales
Detección de colores en tiempo real.

Configuración personalizable de rangos de color (HSV).

Interfaz sencilla y fácil de usar.

Requisitos
Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

Python 3.9.2

OpenCV (opencv-python)

NumPy (numpy)

Instalación
Clona este repositorio en tu máquina local:

bash
Copy
git clone https://github.com/emdraw/Python_ColorOpenCV.git

cd deteccion-colores-opencv

Instala las dependencias necesarias:

bash

Copy

pip install -r requirements.txt

Si no tienes un archivo requirements.txt, puedes instalar las dependencias manualmente:

bash

Copy

pip install opencv-python numpy

Uso

Ejecuta el script principal:

bash

Copy

python deteccion_colores.py

Ajusta los rangos de color HSV utilizando los trackbars en la ventana de la cámara para detectar el color deseado.

Presiona la tecla d para salir del programa.

Estructura del proyecto

Copy

deteccion-colores-opencv/

├── deteccion_colores.py   # Script principal

├── README.md              # Este archivo

└── requirements.txt       # Dependencias del proyecto

Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama con tu nueva característica (git checkout -b feature/nueva-caracteristica).

Realiza tus cambios y haz commit (git commit -am 'Añade nueva característica').

Haz push a la rama (git push origin feature/nueva-caracteristica).

Abre un Pull Request.

Licencia

Este proyecto está bajo la licencia MIT.
