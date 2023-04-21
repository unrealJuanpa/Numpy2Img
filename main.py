from PIL import Image
import numpy as np
import datetime

# Crear un numpy array 2D
array_2d = np.array([[0, 255, 0], [255, 0, 255], [0, 255, 0]])
array_2d = np.random.uniform(low=0, high=255, size=(1024, 1024))

# Convertir el numpy array en una imagen PIL en modo "L" (escala de grises)
img = Image.fromarray(array_2d.astype('uint8'), 'L')

# Mostrar la imagen
img.save(f"image{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')}.png")
