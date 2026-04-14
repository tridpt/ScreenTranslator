@echo off
echo.
echo ==============================================
echo    DANGANRONPA SCREEN TRANSLATOR
echo ==============================================
echo.

cd /d "D:\App\ScreenTranslator"

REM Kiem tra file Tesseract
if exist "C:\Program Files\Tesseract-OCR\tesseract.exe" (
    echo [OK] Tesseract OCR da san sang.
) else (
    if exist "%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe" (
        echo [OK] Tesseract OCR da san sang.
    ) else (
        echo [CANH BAO] Ban chua cai dat Tesseract OCR thanh cong!
        echo Ung dung ban dau vua chay lenh tai, nhung co the bi huy do mang lag.
        echo Neu Tesseract khong chay duoc, ban hay mo Google Chrome:
        echo 1. Tim kiem "Tesseract OCR Windows"
        echo 2. Tai bang cai dat danh cho Windows UB-Mannheim va cai no vao ban nhe.
    )
)

echo.
echo [!] DANG KHOI DONG GIAO DIEN...
python main.py

echo.
pause
