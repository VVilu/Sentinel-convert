import numpy as np
import rasterio
import os


def calculate_ndwi(green, nir):
    """Oblicz NDWI na podstawie Green i NIR."""
    ndwi = (green.astype(float) - nir.astype(float)) / (green.astype(float) + nir.astype(float) + 1e-10)
    return ndwi


def save_ndwi(ndwi_array, reference_path, output_path):
    """Zapisz wynikowy obraz NDWI jako GeoTIFF."""
    with rasterio.open(reference_path) as src:
        profile = src.profile

    profile.update(dtype=rasterio.float32, count=1)

    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(ndwi_array.astype(rasterio.float32), 1)


def process_ndwi(green_path, nir_path, output_dir):

    with rasterio.open(green_path) as green_src:
        green = green_src.read(1)

    with rasterio.open(nir_path) as nir_src:
        nir = nir_src.read(1)


    ndwi = calculate_ndwi(green, nir)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "ndwi_output.tiff")
    save_ndwi(ndwi, green_path, output_path)
    print(f"Zapisano NDWI do: {output_path}")

if __name__ == "__main__":

    green_path = r"C:\Users\wilu\PyCharmMiscProject\NDWI_Convert\sentinel\Input\B03.tiff"
    nir_path = r"C:\Users\wilu\PyCharmMiscProject\NDWI_Convert\sentinel\Input\B08.tiff"
    output_dir = r"C:\Users\wilu\PyCharmMiscProject\NDWI_Convert\sentinel\Output"
    process_ndwi(green_path, nir_path, output_dir)
