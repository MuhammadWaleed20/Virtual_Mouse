import cv2
import math
from modules.hand_tracker import HandTracker
from modules.mouse_controller import MouseController
import pyautogui

def main():
    cam_w, cam_h = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, cam_w)
    cap.set(4, cam_h)
    
    tracker = HandTracker()
    mouse = MouseController()

    while True:
        success, img = cap.read()
        if not success:
            break
            
        img = cv2.flip(img, 1)
        img = tracker.find_hands(img)
        lm_list = tracker.get_position(img)
        
        if len(lm_list) != 0:
            # Landmark 8: Index Finger Tip
            x1, y1 = lm_list[8][1], lm_list[8][2]
            
            # Landmark 4: Thumb Tip
            x2, y2 = lm_list[4][1], lm_list[4][2]
            
            # 1. Draw circles on both fingertips and a line between them
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            
            # 2. Calculate the length of the line between the fingers
            length = math.hypot(x2 - x1, y2 - y1)
            
            # 3. Move the mouse based on the index finger
            mouse.move_mouse(x1, y1, cam_w, cam_h)
            
            # 4. If the distance is short enough, trigger a click!
            # Note: 30 pixels is a good starting threshold, but you may need to adjust it
            if length < 30:
                # Change the circle color to green to visually confirm the click
                cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                
                # Execute the OS click
                pyautogui.click()
            
        cv2.imshow("AI Virtual Mouse", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()