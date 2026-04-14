import ctypes
try:
    ctypes.windll.user32.SetProcessDPIAware()
except:
    pass

import keyboard
import time
import sys
import queue
import threading
from ui.selector import RegionSelector
from ui.overlay import OverlayWindow
from core.capture import capture_region
from core.ocr import perform_ocr
from core.translator import translate_en_to_vi

def step_one_setup_region():
    print("\n" + "="*50)
    print("   DANGANRONPA SCREEN TRANSLATOR - AUTO MODE  ")
    print("="*50)
    print("\n--- BƯỚC 1: XÁC ĐỊNH VÙNG DỊCH ---")
    print("Một cửa sổ mờ vừa hiện ra. Hãy dùng chuột kéo một hộp chữ nhật bao quanh đoạn hội thoại Tiếng Anh trong game. Thả chuột để hoàn tất.")
    
    selector = RegionSelector()
    region = selector.get_region()
    
    if region:
        print(f"-> Đã lưu tọa độ vùng chọn chuẩn: {region}")
    return region

def main():    
    region = step_one_setup_region()
    if not region:
        print("Lỗi: Bạn chưa chọn vùng dịch. Vui lòng chạy lại chương trình.")
        input("Bấm phím Enter để thoát...")
        sys.exit()

    print("\n--- BƯỚC 2: BẮT ĐẦU DỊCH TỰ ĐỘNG ---")
    print("Cửa sổ phụ đề Tiếng Việt đã xuất hiện dưới chân màn hình (Trong suốt).")
    overlay = OverlayWindow()
    overlay.update_text("Chế độ [AUTO TRANSLATE] đang hoạt động. Bạn hãy bấm Next lời thoại...")

    print("\n*** HƯỚNG DẪN SỬ DỤNG MỚI ***")
    print(" > Ứng dụng sẽ TỰ ĐỘNG theo dõi khung hình và nảy Vietsub mỗi khi có lời thoại mới.")
    print(" > Bấm phím [F9] nếu bạn muốn bắt ép ứng dụng dịch lại câu hiện tại.")
    print(" > Giữ phím [Esc] để Thoát hoàn toàn ứng dụng.")
    print("-" * 40)
    
    is_translating = False
    gui_queue = queue.Queue()
    last_text = ""

    def translate_worker():
        nonlocal is_translating, last_text
        if is_translating:
            return
        is_translating = True
        
        try:
            image = capture_region(region)
            text = perform_ocr(image)
            
            # Logic Tự Động: Chỉ dịch nếu "có chữ" và "chữ đó không trùng với câu nói mới nãy"
            if text and text != last_text:
                print(f"[{time.strftime('%H:%M:%S')}] Phát hiện câu mới: {text}")
                gui_queue.put("... Đang nảy dịch ...")
                
                vn_text = translate_en_to_vi(text)
                print(f"[{time.strftime('%H:%M:%S')}] Dịch ra: {vn_text}\n")
                
                gui_queue.put(vn_text)
                
                # Lưu vào vỏ não để lát so sánh, tránh bị chạy vòng lặp dịch hoài 1 câu gây tốn mạng
                last_text = text
        except Exception as e:
            print(f"[!] Lỗi không xác định khi dịch tự động: {e}")
        finally:
            is_translating = False

    def auto_scan_loop():
        # Vòng lặp vĩnh cửu: Quét màn hình để tìm chữ mỗi 1.5 giây
        while True:
            translate_worker()
            time.sleep(1.5)

    def on_translate_manual():
        # Chế độ ép chạy (Manual F9): Xoá rỗng vỏ não đi để chữ trùng vẫn dịch lại được
        nonlocal last_text
        last_text = "" 
        threading.Thread(target=translate_worker, daemon=True).start()

    keyboard.add_hotkey('f9', on_translate_manual)
    
    # Chạy vòng lặp Auto vào một góc máy chủ riêng (Background Thread)
    auto_thread = threading.Thread(target=auto_scan_loop, daemon=True)
    auto_thread.start()
    
    try:
        while True:
            try:
                msg = gui_queue.get_nowait()
                overlay.update_text(msg)
            except queue.Empty:
                pass

            if keyboard.is_pressed('esc'):
                print("-> Nhận lệnh Thoát...")
                break
            
            overlay.process_events()
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        overlay.root.destroy()
        print("Cảm ơn đã sử dụng ứng dụng <3")

if __name__ == "__main__":
    main()
