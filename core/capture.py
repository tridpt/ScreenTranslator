import mss
from PIL import Image

def capture_region(region):
    with mss.mss() as sct:
        monitor = region
        sct_img = sct.grab(monitor)
        
        # Chuyển đổi siêu nhạy
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        # [MỚI] Xuất thử ảnh chụp ra file debug.png để người dùng biết đã cắt trúng đoạn nào
        img.save("debug.png")
        
        return img
