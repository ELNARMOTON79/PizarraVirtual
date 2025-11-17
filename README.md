# Pizarra Virtual

Este proyecto es una aplicación de pizarra virtual que utiliza la cámara web para detectar el movimiento de la mano y permitir al usuario dibujar en la pantalla en tiempo real.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- NumPy

## Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone <https://github.com/ELNARMOTON79/PizarraVirtual.git>
    cd PizarraVirtual
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Activar el entorno virtual:**
    -   En Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   En macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar la aplicación, ejecuta el siguiente comando en la terminal:

```bash
python pizarravirtual.py
```

Asegúrate de tener una cámara web conectada. La aplicación abrirá una ventana mostrando la imagen de la cámara.

## Controles

-   **Dibujar:** Levanta el dedo índice para empezar a dibujar en la pantalla. Baja el dedo para dejar de dibujar.
-   **Cambiar de color:** Mueve el dedo índice a uno de los cuadrados de colores en la esquina superior izquierda para seleccionar un color de dibujo.
-   **Cambiar el grosor del pincel:** Mueve el dedo índice a uno de los cuadrados en la esquina superior derecha para seleccionar un grosor de pincel.
-   **Limpiar la pantalla:** Mueve el dedo índice al botón "Limpiar pantalla" para borrar todos los dibujos.
-   **Salir:** Presiona la tecla `Esc` para cerrar la aplicación.
