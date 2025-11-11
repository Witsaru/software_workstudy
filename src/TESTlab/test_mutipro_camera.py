import cv2
import concurrent.futures
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from module import holistucModule as hm

# Mediapipe hand detection initialization
mp_hands = hm.holistic_module()

def process_camera(camera_index):
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # ลดความละเอียด
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # แปลงภาพเป็น RGB สำหรับ Mediapipe
        mp_hands.show_action(frame)
        # แสดงภาพจากกล้อง
        cv2.imshow(f'Camera {camera_index}', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

# ใช้ multi-threading เพื่อเปิดกล้องและประมวลผลพร้อมกัน
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(process_camera, 0)  # เปิดกล้องตัวที่ 1
    executor.submit(process_camera, 1)  # เปิดกล้องตัวที่ 2
    executor.submit(process_camera, 2)  # เปิดกล้องตัวที่ 3

cv2.destroyAllWindows()
