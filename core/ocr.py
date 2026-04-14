import pytesseract
import os
from PIL import Image, ImageOps

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tesseract_path_user = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe")

if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
elif os.path.exists(tesseract_path_user):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path_user

def perform_ocr(image):
    try:
        # Ép về thang độ xám 'L' để an toàn cho thuật toán nới viền
        image = image.convert('L')
        
        # Phóng to ảnh (Upscale x3) Lanczos
        image = image.resize((image.width * 3, image.height * 3), Image.Resampling.LANCZOS)
        
        # Lọc Binarization - biến nhạt thành trắng, đậm thành đen
        threshold = 160
        image = image.point(lambda p: 0 if p > threshold else 255, mode='L')
        
        # [QUAN TRỌNG NHẤT]: Bơm thêm khung viền Trắng (Padding) dày 50px xung quanh ảnh.
        # Lý do: Khi bạn kéo chuột cắt lẹm quá sát mép viền, Tesseract sẽ hiểu nhầm đó là Rác chứ không phải Chữ. 
        # Đệm thêm 50px giấy trắng vào sẽ giúp tesseract luôn thấy trọn vẹn chữ ở căn giữa!
        image = ImageOps.expand(image, border=50, fill=255)
        
        image.save("debug_ocr.png")

        # Psm mode 3 = Hoàn toàn tự động, thông minh hơn và ít ăn mất chữ nằm lẻ loi hơn mode 6.
        text = pytesseract.image_to_string(image, lang='eng', config='--psm 3')
        
        text = text.strip()
        text = text.replace('|', 'I')
        text = text.replace('_', ' ')
        
        return text
    except Exception as e:
        print(f"[!] Lỗi máy quét OCR: {e}")
        return ""
