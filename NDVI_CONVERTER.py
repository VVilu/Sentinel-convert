import os

import rasterio


def read_green_red(filepath):
    """Wczytaj kanały Green i Red z pliku TIFF."""
    with rasterio.open(filepath) as src:
        green = src.read(2)  # Band 2 – Green
        red = src.read(3)    # Band 3 – Red
    return green, red

def calculate_pseudo_ndvi(green, red):
    """Oblicz pseudo-NDVI na podstawie Green i Red."""
    pseudo_ndvi = (green.astype(float) - red.astype(float)) / (green + red + 1e-10)
    return pseudo_ndvi

def save_ndvi(ndvi_array, reference_path, output_path):
    """Zapisz wynikowy obraz NDVI jako GeoTIFF."""
    with rasterio.open(reference_path) as src:
        profile = src.profile
        profile.update(dtype=rasterio.float32, count=1)

        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(ndvi_array.astype(rasterio.float32), 1)

def process_tiff(input_tiff, output_dir):
    """Pełny proces odczytu i zapisu pseudo-NDVI."""
    green, red = read_green_red(input_tiff)
    pseudo_ndvi = calculate_pseudo_ndvi(green, red)

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "ndvi_file.tiff")
    save_ndvi(pseudo_ndvi, input_tiff, output_path)

    print(f"[SUCCESS] Zapisano pseudo-NDVI do: {output_path}")

# --- PRZYKŁADOWE UŻYCIE ---
if __name__ == "__main__":
    input_tiff = r"C:\Users\sambo\PycharmProjects\Sentinel-convert\pic_samples\2025-04-25-00_00_2025-04-25-23_59_Sentinel-2_L2A_True_color.tiff"
    output_dir = r"C:\Users\sambo\PycharmProjects\Sentinel-convert\pic_out"

    process_tiff(input_tiff, output_dir)
