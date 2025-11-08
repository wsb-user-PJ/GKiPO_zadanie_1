import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Nazwa wczytywanego pliku
filename = "entry.jpg"

# Walidacja czy plik istnieje
if not os.path.exists(filename):
    raise FileNotFoundError(f"Nie znaleziono pliku: {filename}")

# Wczytwanie obrazu BGR
img = cv2.imread(filename)

# Konwersja BGR na RGB (do matplotlib)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Wyświetlenie oryginału
plt.figure(figsize=(6,4))
plt.title("Oryginalny obraz")
plt.imshow(img)
plt.axis('off')
plt.show()

# Zmniejszenie rozdzielczości o 50%
h, w = img.shape[:2]
resized = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_AREA)

# Konwersja do skali szarości
gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)

# Obrót obrazu o 90 stopni 
rotated = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

# Wyświetlenie obrazu wynikowego
plt.figure(figsize=(5,5))
plt.title("Obraz po przetworzeniu")
plt.imshow(rotated, cmap='gray')
plt.axis('off')
plt.show()

# Wyświetlenie fragmentu macierzy obrazu
print("Fragment macierzy obrazu (pierwsze 10x10 pikseli):")
print(rotated[:10, :10])
print(f"Wymiary końcowego obrazu: {rotated.shape}")

# Opcjonalnie: zapis do pliku
cv2.imwrite("wynik.png", rotated)