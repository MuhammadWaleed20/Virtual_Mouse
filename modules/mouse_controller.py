import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

class MouseController:
    def __init__(self, smoothening=5):
        self.screen_w, self.screen_h = pyautogui.size()
        
        # Higher number = smoother but slower. 5 to 7 is usually the sweet spot.
        self.smoothening = smoothening 
        
        # Variables to store previous and current locations
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0

    def move_mouse(self, cam_x, cam_y, cam_w=640, cam_h=480):
        # 1. Scale coordinates to monitor size
        screen_x = int((cam_x / cam_w) * self.screen_w)
        screen_y = int((cam_y / cam_h) * self.screen_h)
        
        # 2. Smooth the values
        self.clocX = self.plocX + (screen_x - self.plocX) / self.smoothening
        self.clocY = self.plocY + (screen_y - self.plocY) / self.smoothening
        
        # 3. Execute movement
        pyautogui.moveTo(self.clocX, self.clocY)
        
        # 4. Update the previous location for the next frame
        self.plocX, self.plocY = self.clocX, self.clocY