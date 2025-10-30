import os
from PIL import Image
import numpy as np

def image_similarity(img1, img2):
    """Return a simple pixel-based similarity score (0–1)."""
    img1 = img1.resize((64, 64)).convert("RGB")
    img2 = img2.resize((64, 64)).convert("RGB")
    arr1 = np.array(img1).astype(float)
    arr2 = np.array(img2).astype(float)
    diff = np.mean(np.abs(arr1 - arr2))
    return 1 - diff / 255.0

def recognize_skills(cropped_paths, skills_dir="backend/data/skills"):
    results = []
    skill_files = {os.path.splitext(f)[0]: os.path.join(skills_dir, f)
                   for f in os.listdir(skills_dir) if f.endswith(".png")}

    for path in cropped_paths:
        img = Image.open(path)
        best_match = None
        best_score = 0

        for skill_name, skill_path in skill_files.items():
            skill_img = Image.open(skill_path)
            score = image_similarity(img, skill_img)
            if score > best_score:
                best_score = score
                best_match = skill_name

        if best_score > 0.80:  # only accept confident matches
            results.append(best_match)

    return list(set(results))
