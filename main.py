import cv2
import numpy as np

def draw(mask, color, frame_c):
    countours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in countours:
        area = cv2.contourArea(c)
        if area > 1000:
            new_countour = cv2.convexHull(c)
            cv2.drawContours(frame_c, [new_countour], 0, color, 3)
            M = cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M['m01']/M['m00'])
            font = cv2.FONT_HERSHEY_COMPLEX
            if color == [0, 255, 255]:
                cv2.putText(frame_c, 'Amarillo', (x+10, y), font, 0.75, (0, 255,255), 1, cv2.LINE_AA)
            elif color == [0, 0, 255]:
                cv2.putText(frame_c, 'Rojo', (x+10, y), font, 0.75, (0, 0,255), 1, cv2.LINE_AA)
            elif color == [0, 255, 0]:
                cv2.putText(frame_c, 'Verde', (x+10, y), font, 0.75, (0, 255,0), 1, cv2.LINE_AA)
            elif color == [255, 0, 0]:
                cv2.putText(frame_c, 'Azul', (x+10, y), font, 0.75, (255, 0,0), 1, cv2.LINE_AA)  
            elif color == [0, 0, 0]:
                cv2.putText(frame_c, 'Black', (x+10, y), font, 0.75, (0, 0,0), 1, cv2.LINE_AA)  
def capture():
    cap = cv2.VideoCapture(0)
    low_yellow = np.array([25, 185, 20], np.uint8)
    high_yellow = np.array([35, 255, 255], np.uint8)
    low_green = np.array([47, 100, 20], np.uint8)
    high_green = np.array([75, 255, 255], np.uint8)
    low_blue = np.array([85, 200, 20], np.uint8)
    high_blue = np.array([125, 255, 255], np.uint8)
    low_red1 = np.array([0, 100, 20], np.uint8)
    high_Red1 = np.array([5, 255, 255], np.uint8)
    low_red2 = np.array([175, 100, 20], np.uint8)
    high_Red2 = np.array([180, 255, 255], np.uint8)
    low_black = np.array([0, 0, 0],np.uint8)
    high_black = np.array([0, 0, 0], np.uint8)
    white = np.array([255, 255, 255], np.uint8)

    while True:
        comp,frame = cap.read()
        if comp == True:
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            yellow_mask = cv2.inRange(frame_HSV, low_yellow, high_yellow)
            green_mask = cv2.inRange(frame_HSV, low_green, high_green)
            red_mask1 = cv2.inRange(frame_HSV, low_red1, high_Red1)
            red_mask2 = cv2.inRange(frame_HSV, low_red2, high_Red2)
            red_mask = cv2.add(red_mask1, red_mask2)
            blue_mask = cv2.inRange(frame_HSV, low_blue, high_blue)
            black_mask = cv2.inRange(frame_HSV, low_black, high_black)
            white_mask = cv2.inRange(frame_HSV, white, white)

            draw(yellow_mask, [0 , 255, 255], frame)
            draw(green_mask,[0, 255, 0], frame)
            draw(red_mask,[0, 0, 255], frame)
            draw(blue_mask,[255, 0, 0], frame)
            draw(black_mask,[55,0,0], frame)
            draw(white_mask, [255, 255, 255], frame)

            cv2.imshow('webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('d'):
                break
                cap.rlease()
                cv2.destroyAllWindows()

if __name__ == "__name__":
    capture()
