import rasterio
import matplotlib.pyplot as plt
import os

def apply_colormap_to_ndwi(input_ndwi_path, output_image_path, cmap='BrBG'):
    """Wczytaj NDWI i zapisz jako kolorowy obraz PNG."""

    with rasterio.open(input_ndwi_path) as src:
        ndwi = src.read(1)


    plt.figure(figsize=(10, 6))
    plt.imshow(ndwi, cmap=cmap, vmin=-1, vmax=1)
    plt.colorbar(label="Wartość NDWI")
    plt.title("NDWI z mapą kolorów")
    plt.axis('off')


    plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()

    print(f"Zapisano kolorowy obraz do: {output_image_path}")


if __name__ == "__main__":
    input_ndwi_path = r"C:\Users\wilu\PyCharmMiscProject\NDWI_Convert\sentinel\Output\ndwi_output.tiff"
    output_image_path = r"C:\Users\wilu\PyCharmMiscProject\NDWI_Convert\sentinel\Color_Ndwi\ndwi_colored.png"

    apply_colormap_to_ndwi(input_ndwi_path, output_image_path)