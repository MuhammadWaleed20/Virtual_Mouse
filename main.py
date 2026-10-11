import cv2
from modules.hand_tracker import HandTracker

def main():
    # 0 is usually the default built-in webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # Width
    cap.set(4, 480) # Height
    
    # Initialize our custom tracker
    tracker = HandTracker()

    while True:
        success, img = cap.read()
        if not success:
            break
            
        # Flip image horizontally for a mirror effect
        img = cv2.flip(img, 1)
        
        # Detect hands and draw the red dots/lines
        img = tracker.find_hands(img)
        
        # Get the exact coordinates of all 21 points
        lm_list = tracker.get_position(img)
        
        # If a hand is on screen, print the Index Finger Tip (Landmark 8)
        if len(lm_list) != 0:
            print(f"Index Finger Tip - X: {lm_list[8][1]} Y: {lm_list[8][2]}")
        
        # Show the video window
        cv2.imshow("AI Virtual Mouse", img)
        
        # Break the loop and close if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()