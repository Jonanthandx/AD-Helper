from PIL import Image
import os

def crop_icons(image_path, save_dir="temp_crops"):
    """
    Crop Ability Draft screen (8x6 grid: 1 row of ultimates, 5 rows of standard skills)
    Adjusted for 1920x1080 screenshots from your example.
    """
    os.makedirs(save_dir, exist_ok=True)
    img = Image.open(image_path)
    w, h = img.size

    # --- Adjusted grid position (based on your full screenshot) ---
    grid_x = 640      # left start of first icon
    grid_y = 305      # top of ultimate row
    cell_w = 85
    cell_h = 85
    gap_x = 10
    gap_y = 14

    ult_gap = 30  # extra gap between ultimate and standard sections
    rows = 6
    cols = 8

    cropped_paths = []

    for r in range(rows):
        for c in range(cols):
            # For the standard section, apply the extra vertical gap after first row
            extra_y = ult_gap if r >= 1 else 0

            x1 = grid_x + c * (cell_w + gap_x)
            y1 = grid_y + r * (cell_h + gap_y) + extra_y
            x2 = x1 + cell_w
            y2 = y1 + cell_h

            crop = img.crop((x1, y1, x2, y2))
            save_path = os.path.join(save_dir, f"skill_{r}_{c}.png")
            crop.save(save_path)
            cropped_paths.append(save_path)

    return cropped_paths
