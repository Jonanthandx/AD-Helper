import json
import os
from PIL import Image

def crop_from_coords(image_path, coords_path="backend/model/Coordinate.JSON", output_dir="temp_crops_manual"):
    """
    Crop an Ability Draft screenshot using manually provided coordinates.
    Automatically swaps inverted coordinates if needed.
    JSON format: list of {x, y, w, h} meaning top-left (x,y), bottom-right (w,h).
    """
    os.makedirs(output_dir, exist_ok=True)

    # Load coordinate data
    with open(coords_path, "r", encoding="utf-8") as f:
        coords = json.load(f)

    img = Image.open(image_path)
    W, H = img.size
    print(f"Loaded image: {W}x{H}")

    cropped_paths = []
    for i, box in enumerate(coords):
        try:
            x1, y1, x2, y2 = int(box["x"]), int(box["y"]), int(box["w"]), int(box["h"])
        except KeyError:
            raise ValueError(f"Invalid box format at index {i}: {box}")

        # Fix reversed or out-of-bounds coordinates automatically
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1

        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(W, x2), min(H, y2)

        if x2 <= x1 or y2 <= y1:
            print(f"⚠️ Skipping invalid box #{i}: {box}")
            continue

        crop = img.crop((x1, y1, x2, y2))
        out_path = os.path.join(output_dir, f"skill_{i//8}_{i%8}.png")
        crop.save(out_path)
        cropped_paths.append(out_path)

    print(f"✅ Cropped {len(cropped_paths)} skill icons to {output_dir}/")
    return cropped_paths


if __name__ == "__main__":
    crop_from_coords("backend/model/Untitled.png")
