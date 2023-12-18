import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.image_path = tk.StringVar()
        left_frame = tk.Frame(root, padx=10, pady=10)
        left_frame.grid(row=0, column=0, sticky="nsew")
        right_frame = tk.Frame(root, padx=10, pady=10)
        right_frame.grid(row=0, column=1, sticky="nsew")
        upload_button = tk.Button(left_frame, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)
        self.image_label = tk.Label(right_frame, text="Uploaded Image will be displayed here")
        self.image_label.pack()
        render_button = tk.Button(left_frame, text="convert to b/w", command=self.toblack)
        render_button.pack(pady=10)
        render_button = tk.Button(left_frame, text="process 2", command=self.toblack)
        render_button.pack(pady=10)
        render_button = tk.Button(left_frame, text="render output", command=self.render_image)
        render_button.pack(pady=10)
        

    def upload_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path.set(file_path)
            self.display_image()
        

    def display_image(self):
        image_path = self.image_path.get()
        if image_path:
            img = Image.open(image_path)
            img.thumbnail((500, 500))  # Resize image if necessary
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
    def toblack(self):
        image_path = self.image_path.get()
        if image_path:
            img = Image.open(image_path)
            img.thumbnail((500, 500))  # Resize image if necessary
            img=img.convert("L")
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img

    def render_image(self):
        image_path = self.image_path.get()
        if image_path:
            img = Image.open(image_path)
            img.thumbnail((500, 500))   
            render_window = tk.Toplevel(self.root)
            render_window.title("Rendered Image")
            img_label = tk.Label(render_window, image=ImageTk.PhotoImage(img))
            img_label.pack()
            img_label.image = ImageTk.PhotoImage(img)
            img_label.configure(image=img_label.image)
            textt=tk.Label(render_window, text="disease:Downy mildew  | leaf age:2 weeks")
            textt.pack()
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
