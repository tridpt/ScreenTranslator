import tkinter as tk

class RegionSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-alpha", 0.6) # Cửa sổ mờ mờ để có thể nhìn xuyên game
        self.root.attributes("-topmost", True) # Luôn nằm ở trên cùng
        self.root.attributes("-fullscreen", True) # Trải đều toàn màn hình
        self.root.config(cursor="cross") # Con trỏ chuột chuyển thành hình dấu thập
        
        self.canvas = tk.Canvas(self.root, cursor="cross", bg="black")
        self.canvas.pack(fill="both", expand=True)
        
        # In Hướng dẫn
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, 80, 
                                text="HƯỚNG DẪN: NHẤN GIỮ VÀ KÉO CHUỘT THÀNH Ô CHỮ NHẬT BAO QUANH LỜI THOẠI CỦA TRONG GAME.\nTHẢ CHUỘT ĐỂ XÁC NHẬN.", 
                                fill="white", font=("Segoe UI", 24, "bold"), justify="center")
        
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.region = None
        
        # Theo dõi sự kiện click và kéo thả chuột
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
    def on_press(self, event):
        # Bắt đầu vẽ hìn chữ nhật màu xanh lá cây
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='#00ff00', width=3)
        
    def on_drag(self, event):
        # Mở rộng hình chữ nhật theo chuột
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)
        
    def on_release(self, event):
        # Thả chuột -> lưu tọa độ
        end_x, end_y = (event.x, event.y)
        left = min(self.start_x, end_x)
        top = min(self.start_y, end_y)
        width = abs(self.start_x - end_x)
        height = abs(self.start_y - end_y)
        
        # Đảm bảo không chọn nhầm vùng bé tí teo do lỡ click
        if width > 15 and height > 15:
            self.region = {
                'left': left,
                'top': top,
                'width': width,
                'height': height
            }
        else:
            print("Vùng chọn quá bé, bỏ qua.")
            
        self.root.destroy()
        
    def get_region(self):
        # Block ứng dụng đến khi tắt cửa sổ này
        self.root.mainloop()
        return self.region
