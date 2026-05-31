import cv2  # OpenCV 라이브러리 import
import sys  # sys 모듈 import
import mediapipe as mp  # MediaPipe 패키지 import하고 mp라는 별칭으로 사용하겠다는 뜻.
import math  # math 모듈 import
import serial
# 거리 계산 함수 선언
def distance(p1, p2):
    return math.dist((p1.x, p1.y), (p2.x, p2.y))  # 두 점 p1, p2의 x, y 좌표로 거리를 계산한다.
a=['$',0,0,0,0,0]
# MediaPipe 패키지에서 사용할 기능들.
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands  # 손 인식을 위한 객체
arduino= serial.Serial('COM8',9600)



cap = cv2.VideoCapture(0)  # 비디오 캡처 객체 생성

if not cap.isOpened():  # 연결 확인
    print("Camera is not opened")
    sys.exit(1)  # 프로그램 종료

hands = mp_hands.Hands()  # 손 인식 객체 생성

while True:  # 무한 반복
    res, frame = cap.read()  # 카메라 데이터 읽기

    if not res:  # 프레임 읽었는지 확인
        print("Camera error")
        break  # 반복문 종료

    frame = cv2.flip(frame, 1)  # 셀프 카메라처럼 좌우 반전
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 미디어파이프에서 인식 가능한 색공간으로 변경
    results = hands.process(image)  # 이미지에서 손을 찾고 결과를 반환

    if results.multi_hand_landmarks:  # 손이 인식되었는지 확인
        for hand_landmarks in results.multi_hand_landmarks:  # 반복문을 활용해 인식된 손의 주요 부분을 그림으로 그려 표현
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            points = hand_landmarks.landmark  #  landmark 좌표 정보들을 points라는 변수로 활용

            # 엄지손가락부터 새끼손가락까지 손가락이 펴졌는지 확인하고 이미지에 출력한다.
            # 엄지손가락 확인하기
            if distance(points[4], points[9]) < distance(points[3], points[9]):
                fingers = "0"  # 접혔으면 0
            else:
                fingers = "1"  # 펴졌으면 1
            cv2.putText(  # 0 또는 1을 이미지에 출력한다.
                frame,
                fingers,
                (int(points[4].x * frame.shape[1]), int(points[4].y * frame.shape[0])),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                5,
            )
            a[1]=fingers

            # 나머지 손가락 확인하기
            if distance(points[8], points[0]) < distance(points[7], points[0]):
                fingers = "0"  # 접혔으면 0
            else:
                fingers = "1"  # 펴졌으면 1
            cv2.putText(  # 0 또는 1을 이미지에 출력한다.
                frame,
                fingers,
                (int(points[8].x * frame.shape[1]), int(points[8].y * frame.shape[0])),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                5,
            )
            a[2]=fingers
            if distance(points[12], points[0]) < distance(points[11], points[0]):
                fingers = "0"  # 접혔으면 0
            else:
                fingers = "1"  # 펴졌으면 1
            cv2.putText(  # 0 또는 1을 이미지에 출력한다.
                frame,
                fingers,
                (int(points[12].x * frame.shape[1]), int(points[12].y * frame.shape[0])),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                5,
            )
            a[3]=fingers
            if distance(points[16], points[0]) < distance(points[15], points[0]):
                fingers = "0"  # 접혔으면 0
            else:
                fingers = "1"  # 펴졌으면 1
            cv2.putText(  # 0 또는 1을 이미지에 출력한다.
                frame,
                fingers,
                (int(points[16].x * frame.shape[1]), int(points[16].y * frame.shape[0])),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                5,
            )
            a[4]=fingers
            if distance(points[20], points[0]) < distance(points[19], points[0]):
                fingers = "0"  # 접혔으면 0
            else:
                fingers = "1"  # 펴졌으면 1
            cv2.putText(  # 0 또는 1을 이미지에 출력한다.
                frame,
                fingers,
                (int(points[20].x * frame.shape[1]), int(points[20].y * frame.shape[0])),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                5,
            )
            a[5]=fingers
            b= ''.join(a)
            b=b.encode('utf-8')
            arduino.write(b)
            
         
            
            
            
    cv2.imshow("MediaPipe Hands", frame)  # 영상을 화면에 출력.

    key = cv2.waitKey(5) & 0xFF  # 키보드 입력받기
    if key == 27:  # ESC를 눌렀을 경우
        break  # 반복문 종료

cv2.destroyAllWindows()  # 영상 창 닫기
cap.release()  # 비디오 캡처 객체 해제