import tkinter as tk

class OverlayWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True) # Xóa thanh tiêu đề
        self.root.attributes("-topmost", True) # Luôn đè lên trên game
        self.root.attributes("-alpha", 0.85)
        self.root.config(bg='black')
        
        # Đọc xem màn hình máy tính của người dùng to bao nhiêu
        screen_width = self.root.winfo_screenwidth()
        
        # Tự động xuống hàng nếu độ dài câu chữ vượt quá chiều ngang màn hình (Trừ đi 150px an toàn)
        wrap_width = screen_width - 150 if screen_width > 150 else 1000
        
        self.label = tk.Label(self.root, text="", font=("Segoe UI", 26, "bold"), fg="white", bg="black", wraplength=wrap_width, justify="center")
        self.label.pack(expand=True, fill='both', pady=30, padx=20)
        
        # Nâng khung chứa lên cực đại = 350px (Gấp 3 lần cũ). Dư chứa bài diễn văn.
        window_height = 350 
        window_width = screen_width
        
        y_pos = 20 # Chừa lề trên
        
        self.root.geometry(f"{window_width}x{window_height}+0+{y_pos}")
        
    def update_text(self, text):
        self.label.config(text=text)

    def process_events(self):
        self.root.update()
