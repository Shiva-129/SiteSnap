import tkinter as tk

class AreaSelector:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', 0.3)
        self.root.configure(background='grey')
        
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        
        self.rect = None
        
        self.canvas = tk.Canvas(self.root, cursor="cross")
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        
        self.selection = None

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)

    def on_move_press(self, event):
        self.current_x = event.x
        self.current_y = event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.current_x, self.current_y)

    def on_button_release(self, event):
        self.current_x = event.x
        self.current_y = event.y
        
        # Calculate coordinates
        x1 = min(self.start_x, self.current_x)
        y1 = min(self.start_y, self.current_y)
        x2 = max(self.start_x, self.current_x)
        y2 = max(self.start_y, self.current_y)
        
        width = x2 - x1
        height = y2 - y1
        
        if width > 0 and height > 0:
            self.selection = (x1, y1, width, height)
        
        self.root.destroy()

    def get_selection(self):
        self.root.mainloop()
        return self.selection

if __name__ == "__main__":
    selector = AreaSelector()
    print(selector.get_selection())
