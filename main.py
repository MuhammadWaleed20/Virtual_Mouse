import cv2
from modules.hand_tracker import HandTracker
from modules.mouse_controller import MouseController

def main():
    # Store webcam dimensions in variables so we can pass them to the controller
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
            # Landmark 8 is the tip of the Index Finger
            x1, y1 = lm_list[8][1], lm_list[8][2]
            
            # Draw a purple circle on the fingertip so we can see the driving point
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            
            # Pass the coordinates to PyAutoGUI to move the cursor
            mouse.move_mouse(x1, y1, cam_w, cam_h)
            
        cv2.imshow("AI Virtual Mouse", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()