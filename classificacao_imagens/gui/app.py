import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from utils.visualization import visualize_prediction

def load_image_and_predict(model, class_names):
    file_path = filedialog.askopenfilename()
    if file_path:
        visualize_prediction(file_path, model, class_names)

def create_gui(model, class_names):
    root = tk.Tk()
    root.title("Classificacao da imagem no computador:")

    btn = tk.Button(root, text="Load Image", command=lambda: load_image_and_predict(model, class_names))
    btn.pack()

    root.mainloop()
