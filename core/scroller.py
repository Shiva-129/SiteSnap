import pyautogui
import time
import keyboard
from PIL import ImageChops

class Scroller:
    def __init__(self, region, scroll_amount=100, delay=0.5):
        self.region = region # (x, y, width, height)
        self.scroll_amount = scroll_amount
        self.delay = delay
        self.images = []
        self.stop_key = 'q'

    def capture_screen(self):
        return pyautogui.screenshot(region=self.region)

    def is_identical(self, img1, img2):
        if img1 is None or img2 is None:
            return False
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox() is None:
            return True
        return False

    def start_scrolling(self):
        print(f"Starting scroll capture. Press '{self.stop_key}' to stop manually.")
        
        # Click to ensure focus on the window
        print("Clicking to focus...")
        center_x = self.region[0] + self.region[2] // 2
        center_y = self.region[1] + self.region[3] // 2
        pyautogui.click(center_x, center_y)
        time.sleep(1.0)
        
        last_image = None
        
        while True:
            # Check for manual stop
            if keyboard.is_pressed(self.stop_key):
                print("Manual stop detected.")
                break

            # Capture current view
            current_image = self.capture_screen()
            
            # Check for end of page (duplicate content)
            if self.is_identical(last_image, current_image):
                print("End of page detected (content identical). Stopping.")
                break
            
            self.images.append(current_image)
            last_image = current_image
            
            # Scroll
            pyautogui.scroll(self.scroll_amount)
            # pyautogui.press('pagedown')
            time.sleep(self.delay)
            
        return self.images
