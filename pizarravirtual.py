import cv2
import numpy as np

try:
    import mediapipe as mp
except Exception:
    mp = None

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Colores para pintar
colorCeleste = (255, 113, 82)
colorAmarillo = (89, 222, 255)
colorRosa = (128, 0, 255)
colorVerde = (0, 255, 36)
colorLimpiarPantalla = (29, 112, 246)

# Grosor de línea recuadros superior izquierda (color a dibujar)
grosorCeleste = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2

# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

#--------------------- Variables para el marcador / lápiz virtual -------------------------
color = colorVerde
grosor = 3
#------------------------------------------------------------------------------------------

x1 = None
y1 = None
imAux = None

if mp is None:
    print("Error: el paquete 'mediapipe' no está instalado. Instálalo con: pip install mediapipe")
    cap.release()
    cv2.destroyAllWindows()
    raise SystemExit(1)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

with mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.5, max_num_hands=1) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]
        if imAux is None:
            imAux = np.zeros(frame.shape, dtype=np.uint8)

        # Sección superior: dibujar cuadros y textos (igual que antes)
        cv2.rectangle(frame, (0, 0), (50, 50), colorAmarillo, grosorAmarillo)
        cv2.rectangle(frame, (50, 0), (100, 50), colorRosa, grosorRosa)
        cv2.rectangle(frame, (100, 0), (150, 50), colorVerde, grosorVerde)
        cv2.rectangle(frame, (150, 0), (200, 50), colorCeleste, grosorCeleste)
        cv2.rectangle(frame, (300, 0), (400, 50), colorLimpiarPantalla, 1)
        cv2.putText(frame, 'Limpiar', (320, 20), 6, 0.6, colorLimpiarPantalla, 1, cv2.LINE_AA)
        cv2.putText(frame, 'pantalla', (320, 40), 6, 0.6, colorLimpiarPantalla, 1, cv2.LINE_AA)
        cv2.rectangle(frame, (490, 0), (540, 50), (0, 0, 0), grosorPeque)
        cv2.circle(frame, (515, 25), 3, (0, 0, 0), -1)
        cv2.rectangle(frame, (540, 0), (590, 50), (0, 0, 0), grosorMedio)
        cv2.circle(frame, (565, 25), 7, (0, 0, 0), -1)
        cv2.rectangle(frame, (590, 0), (640, 50), (0, 0, 0), grosorGrande)
        cv2.circle(frame, (615, 25), 11, (0, 0, 0), -1)

        # Procesar con MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        fingertip_point = None
        finger_extended = False

        if results.multi_hand_landmarks:
            handLms = results.multi_hand_landmarks[0]
            # Landmarks: index finger tip = 8, pip = 6
            lm_tip = handLms.landmark[8]
            lm_pip = handLms.landmark[6]

            x2 = int(lm_tip.x * w)
            y2 = int(lm_tip.y * h)
            fingertip_point = (x2, y2)

            # Consideramos el dedo extendido si la punta está por encima del PIP (en coordenadas normales)
            if lm_tip.y < lm_pip.y - 0.02:
                finger_extended = True

        # Si no hay punto detectado, se comporta como no-detección
        if fingertip_point is None:
            x1, y1 = None, None
        else:
            x2, y2 = fingertip_point

            if finger_extended:
                # Selecciones superiores (si el dedo está en la franja superior)
                if 0 < x2 < 50 and 0 < y2 < 50:
                    color = colorAmarillo
                    grosorAmarillo = 6
                    grosorRosa = 2
                    grosorVerde = 2
                    grosorCeleste = 2
                elif 50 < x2 < 100 and 0 < y2 < 50:
                    color = colorRosa
                    grosorAmarillo = 2
                    grosorRosa = 6
                    grosorVerde = 2
                    grosorCeleste = 2
                elif 100 < x2 < 150 and 0 < y2 < 50:
                    color = colorVerde
                    grosorAmarillo = 2
                    grosorRosa = 2
                    grosorVerde = 6
                    grosorCeleste = 2
                elif 150 < x2 < 200 and 0 < y2 < 50:
                    color = colorCeleste
                    grosorAmarillo = 2
                    grosorRosa = 2
                    grosorVerde = 2
                    grosorCeleste = 6
                elif 490 < x2 < 540 and 0 < y2 < 50:
                    grosor = 3
                    grosorPeque = 6
                    grosorMedio = 1
                    grosorGrande = 1
                elif 540 < x2 < 590 and 0 < y2 < 50:
                    grosor = 7
                    grosorPeque = 1
                    grosorMedio = 6
                    grosorGrande = 1
                elif 590 < x2 < 640 and 0 < y2 < 50:
                    grosor = 11
                    grosorPeque = 1
                    grosorMedio = 1
                    grosorGrande = 6
                elif 300 < x2 < 400 and 0 < y2 < 50:
                    cv2.rectangle(frame, (300, 0), (400, 50), colorLimpiarPantalla, 2)
                    cv2.putText(frame, 'Limpiar', (320, 20), 6, 0.6, colorLimpiarPantalla, 2, cv2.LINE_AA)
                    cv2.putText(frame, 'pantalla', (320, 40), 6, 0.6, colorLimpiarPantalla, 2, cv2.LINE_AA)
                    imAux = np.zeros(frame.shape, dtype=np.uint8)
                else:
                    # Dibujar: si hay punto anterior trazamos línea
                    if x1 is not None and y1 is not None:
                        # Evitar dibujar si estamos en la franja superior
                        if not (0 < y1 < 60 or 0 < y2 < 60):
                            imAux = cv2.line(imAux, (x1, y1), (x2, y2), color, grosor)

                # Dibujar círculo indicador en la punta del dedo
                cv2.circle(frame, (x2, y2), grosor, color, 3)
                x1, y1 = x2, y2
            else:
                # Dedo no extendido (no dibujar)
                x1, y1 = None, None

        # Combinar imAux con frame como antes
        imAuxGray = cv2.cvtColor(imAux, cv2.COLOR_BGR2GRAY)
        _, th = cv2.threshold(imAuxGray, 10, 255, cv2.THRESH_BINARY)
        thInv = cv2.bitwise_not(th)
        frame = cv2.bitwise_and(frame, frame, mask=thInv)
        frame = cv2.add(frame, imAux)

        cv2.imshow('imAux', imAux)
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()