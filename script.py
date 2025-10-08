import cv2
import serial
import time
import numpy as np
import torch

# ================= Arduino Bağlantısı =================
try:
    arduino = serial.Serial('COM3', 9600)
    time.sleep(2)
    use_arduino = True
except:
    print("⚠️ Arduino bulunamadı! Sadece simülasyon modunda çalışacak.")
    arduino = None
    use_arduino = False

# ================= YOLOv5 Modeli =================
model = torch.hub.load('yolov5-master', 'yolov5s', source='local', pretrained=True)
model.conf = 0.35

# ================= Kamera =================
cap = cv2.VideoCapture(0)

# PID parametreleri
Kp = 0.005
Ki = 0.0002
Kd = 0.001
integral_error = 0
prev_error = 0

# Engel algılanacak sınıflar
ENGEL_CLASSES = [
    'person','chair','bottle','cell phone','laptop','keyboard','mouse','sofa',
    'diningtable','tvmonitor','pottedplant','bed','toilet','refrigerator',
    'microwave','oven','book','clock','vase','cup','knife','spoon','fork',
    'teddy bear','hair drier','toothbrush','bench','wall'
]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    # ===== Frame başında engel bilgilerini sıfırla =====
    yolo_engel_var = False
    engel_side = None
    engel_distance = 0

    # ===== Duvar Kenarı Algılama =====
    roi = frame[h//2:, :]
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    edges = cv2.Canny(blur, 80, 200)

    left_val = cv2.countNonZero(edges[:, :w//2])
    right_val = cv2.countNonZero(edges[:, w//2:])

    # ===== Engel Algılama (YOLOv5) =====
    results = model(frame)
    pred = results.pred[0]

    for *box, conf, cls in pred:
        label = model.names[int(cls)]
        if label in ENGEL_CLASSES:
            yolo_engel_var = True
            x1, y1, x2, y2 = map(int, box)
            center_x = (x1 + x2) // 2
            distance = y2 - y1  # yüksekliği (yakınlık göstergesi)
            if distance > engel_distance:
                engel_distance = distance  # en büyük olanı al
                if center_x < w//3:
                    engel_side = 'left'
                elif center_x > (2*w)//3:
                    engel_side = 'right'
                else:
                    engel_side = 'center'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    # ===== PID Hesaplama =====
    error = left_val - right_val
    if abs(error) < 300:
        error = 0
    integral_error += error
    derivative = error - prev_error
    turn = Kp*error + Ki*integral_error + Kd*derivative
    prev_error = error

    # ===== Karar Mekanizması =====
    if yolo_engel_var:
        if engel_distance < h*0.3:
            karar = "F"  # uzaksa yok say
        elif engel_side == 'center' and engel_distance > h*0.6:
            karar = "S"  # ortada ve çok yakınsa dur
        elif engel_side == 'left':
            karar = "R"  # soldaysa sağdan kaç
        elif engel_side == 'right':
            karar = "L"  # sağdaysa soldan kaç
        else:
            karar = "R"  # ortada ama orta mesafede sağdan kaç
    else:
        # Engel yok → normal PID ile düzeltme
        if turn < -0.5:
            karar = "L"
        elif turn > 0.5:
            karar = "R"
        else:
            karar = "F"  # düz git

    # ===== Arduino'ya Komut Gönder =====
    print("Karar:", karar, " | Engel Boyu:", engel_distance)
    if use_arduino and arduino:
        arduino.write(f"{karar}\n".encode())

    # ===== Görselleştirme =====
    cv2.putText(frame, f"Karar: {karar}", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Kamera", frame)
    cv2.imshow("Kenarlar", edges)

    key = cv2.waitKey(30) & 0xFF
    if key == ord('q') or key == 27:
        break

cap.release()
cv2.destroyAllWindows()
if use_arduino and arduino:
    arduino.close()
