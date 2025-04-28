import matplotlib.pyplot as plt
import rasterio


def apply_colormap_to_ndwi(input_ndwi_path, output_image_path, cmap='BrBG'):
    """Wczytaj NDWI i zapisz jako kolorowy obraz PNG."""
    # Wczytaj plik NDWI
    with rasterio.open(input_ndwi_path) as src:
        ndwi = src.read(1)

    # Tworzenie wykresu z mapą kolorów
    plt.figure(figsize=(10, 6))
    plt.imshow(ndwi, cmap=cmap, vmin=-1, vmax=1)  # vmin/vmax dostosowane do typowych wartości NDWI
    plt.colorbar(label="Wartość NDWI")
    plt.title("NDWI z mapą kolorów")
    plt.axis('off')

    # Zapis obrazu
    plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    print(f"[SUCCESS] Zapisano kolorowy obraz do: {output_image_path}")

# --- PRZYKŁAD UŻYCIA ---
if __name__ == "__main__":
    input_ndwi_path = r"C:\Users\sambo\PycharmProjects\Sentinel-convert\pic_out\ndwi_output.tiff"  # <-- Ścieżka do pliku NDWI (.tif)
    output_image_path = r"C:\Users\sambo\PycharmProjects\Sentinel-convert\pic_out\ndwi_colored.png"  # <-- Gdzie zapisać kolorowy obraz (.png)

    apply_colormap_to_ndwi(input_ndwi_path, output_image_path)