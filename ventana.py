from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Crear ventana primero
root = Tk()
root.title("primer tkinter")

# URL de la imagen
url = "https://tse3.mm.bing.net/th/id/OIP.y_skv2DrBaHi8SzwrtrAsgHaD8?pid=Api&P=0&h=180"

# Descargar la imagen
response = requests.get(url)
img_data = response.content
image = Image.open(BytesIO(img_data))
image = image.resize((300, 150))
photo = ImageTk.PhotoImage(image)

# Frame principal
frm = ttk.Frame(root, padding=10)
frm.grid()

# Elementos en el frame
ttk.Label(frm, text="Hello World! me llamo Dante").grid(column=0, row=0, columnspan=2)

label = tk.Label(frm, image=photo)
label.image = photo
label.grid(column=0, row=1, columnspan=2)

ttk.Button(frm, text="Cerrar", command=root.destroy).grid(column=1, row=2)

root.mainloop()
