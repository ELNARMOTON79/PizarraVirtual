# PizarraVirtual

**Descripción**:

PizarraVirtual es una pizarra interactiva que permite dibujar en pantalla usando la punta del dedo índice detectada por MediaPipe. Sustituye la detección por color por detección de la mano para dibujar sin necesitar objetos físicos.

**Requisitos**:

- **Python** 3.8 o superior
- Dependencias listadas en `requirements.txt` (`mediapipe`, `opencv-python`, `numpy`)

**Instalación** (Windows PowerShell):

```powershell
python -m pip install --upgrade pip
pip install -r "c:\Users\rafae\OneDrive\Documents\Pizarra virtual\requirements.txt"
```

Si la instalación de `mediapipe` falla en Windows, prueba con una versión específica compatible con tu Python, por ejemplo:

```powershell
pip install mediapipe==0.10.1
```

También es recomendable utilizar un entorno virtual (`venv`) para aislar dependencias.

**Ejecución**:

```powershell
python "c:\Users\rafae\OneDrive\Documents\Pizarra virtual\pizarravirtual.py"
```

**Uso**:

- **Dibujar:** Extiende el dedo índice (apunta la punta hacia la cámara). Cuando el dedo está extendido, mueve la punta para dibujar.
- **Detener dibujo:** Dobla el dedo índice (o retíralo del campo de visión) para dejar de dibujar.
- **Seleccionar color:** Lleva la punta del dedo a los cuadros de color en la franja superior izquierda para cambiar color.
- **Cambiar grosor:** Lleva la punta a los cuadrados de la parte superior derecha para seleccionar pequeño/medio/grande.
- **Limpiar pantalla:** Lleva la punta a la caja 'Limpiar pantalla' (centro superior) para borrar la pizarra.

Consejos: usa buena iluminación y apunta la palma hacia la cámara para que MediaPipe reconozca correctamente los landmarks.

**Solución de problemas**:

- Si no se detecta la mano: prueba mejor iluminación y aleja/acerca la mano a la cámara.
- Si `mediapipe` no se instala: verifica la versión de Python y prueba una versión compatible de `mediapipe` o instala desde ruedas oficiales si es necesario.

**Archivos clave**:

- `pizarravirtual.py` — script principal
- `requirements.txt` — dependencias para instalar
- `README.md` — este documento

Si quieres que añada instrucciones para ejecutar dentro de un entorno virtual, o una versión en inglés, dímelo y lo agrego.