import os
import mss
from PIL import Image

def capture_region(region):
    with mss.mss() as sct:
        monitor = region
        sct_img = sct.grab(monitor)
        
        # Chuyển đổi siêu nhạy
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        if os.environ.get("SCREEN_TRANSLATOR_DEBUG") == "1":
            img.save("debug.png")
        
        return img
