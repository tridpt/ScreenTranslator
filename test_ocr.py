import pytesseract
import os
import sys
from PIL import Image, ImageEnhance, ImageOps

tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tesseract_path_user = os.path.expandvars(r"%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe")

if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
elif os.path.exists(tesseract_path_user):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path_user

try:
    img = Image.open('debug.png')
except Exception as e:
    print("Khong tim thay debug.png:", e)
    sys.exit()

print("Kich thuoc anh (Width x Height):", img.size)

if img.size[0] < 50 or img.size[1] < 20:
    print("Anh nho qua, the nay la do Scale roi!")

print("--- THỬ NGHIỆM TESSERACT ---")
# 1. Raw
print("1. Raw (Default):", repr(pytesseract.image_to_string(img, lang='eng').strip()))

# 2. Grayscale + Contrast
img_gray = img.convert('L')
img_contrast = ImageEnhance.Contrast(img_gray).enhance(2.0)
print("2. Contrast PSM 6:", repr(pytesseract.image_to_string(img_contrast, lang='eng', config='--psm 6').strip()))

# 3. Inverted (Black text on white background)
img_inv = ImageOps.invert(img_gray)
img_inv_contrast = ImageEnhance.Contrast(img_inv).enhance(2.0)
print("3. Inverted PSM 6:", repr(pytesseract.image_to_string(img_inv_contrast, lang='eng', config='--psm 6').strip()))
print("4. Inverted PSM 7:", repr(pytesseract.image_to_string(img_inv_contrast, lang='eng', config='--psm 7').strip()))

# 4. Upscale (zoom) for small fonts
img_zoom = img_inv_contrast.resize((img.size[0]*2, img.size[1]*2), Image.Resampling.LANCZOS)
print("5. Zoomed Inverted PSM 6:", repr(pytesseract.image_to_string(img_zoom, lang='eng', config='--psm 6').strip()))

print("Xong!")
