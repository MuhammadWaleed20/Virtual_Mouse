import pyautogui

# Remove the default 0.1-second delay PyAutoGUI adds to commands for real-time tracking
pyautogui.PAUSE = 0

class MouseController:
    def __init__(self):
        # Automatically grab your computer's monitor resolution (e.g., 1920x1080)
        self.screen_w, self.screen_h = pyautogui.size()
        
        # Disable the fail-safe so the script doesn't crash if your mouse hits the corner
        pyautogui.FAILSAFE = False

    def move_mouse(self, cam_x, cam_y, cam_w=640, cam_h=480):
        # Cross-multiply to scale the 640x480 webcam coordinates up to your monitor's size
        screen_x = int((cam_x / cam_w) * self.screen_w)
        screen_y = int((cam_y / cam_h) * self.screen_h)
        
        # Execute the operating system mouse movement
        pyautogui.moveTo(screen_x, screen_y)