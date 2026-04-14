from deep_translator import GoogleTranslator

def translate_en_to_vi(text):
    """
    Nhận chữ nguyên bản, xử lý rác và gọi API Google Translate.
    """
    if not text:
        return ""
    try:
        # Nối các câu với nhau, bỏ khoảng cách enter để dịch thoát ý nguyên đoạn
        text = text.replace('\n', ' ')
        
        # Dịch miễn phí và siêu giới hạn với deep_translator
        translated = GoogleTranslator(source='en', target='vi').translate(text)
        return translated
    except Exception as e:
        print(f"[!] Lỗi dịch thuật: {e}")
        return ""
