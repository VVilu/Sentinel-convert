import matplotlib.pyplot as plt
import rasterio

# Wczytaj NDVI
ndvi_path = r"C:\Users\sambo\PycharmProjects\Sentinel-convert\pic_out\ndvi_file.tiff"
with rasterio.open(ndvi_path) as src:
    ndvi = src.read(1)

# Wyświetl z kolorową mapą
plt.figure(figsize=(10,10))
plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(label='NDVI')
plt.title("Mapa NDVI")
plt.axis('off')
plt.show()
