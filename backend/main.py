from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from backend.model.cropper_from_coords import crop_from_coords
from backend.utils.combo_engine import suggest_combos
from backend.utils.recognizer import recognize_skills
import os

# === FastAPI setup ===
app = FastAPI(title="Dota 2 Ability Draft Helper")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Routes ===
@app.get("/")
def root():
    return {"message": "Ability Draft Combo API running with Coordinate-based Cropper ✅"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Upload a full screenshot of the Ability Draft screen.
    This will crop skills based on coordinates, recognize them, and suggest combos.
    """
    # (1) Save uploaded file temporarily
    temp_path = "backend/model/temp_upload.png"
    contents = await file.read()
    with open(temp_path, "wb") as f:
        f.write(contents)

    # (2) Crop icons using your manual coordinates (Coordinate.JSON)
    cropped_paths = crop_from_coords(temp_path)

    # (3) Recognize skills based on existing icons dataset
    recognized_names = recognize_skills(cropped_paths)

    # (4) Wrap recognized skill data
    recognized = [{"name": n, "tags": []} for n in recognized_names]

    # (5) Suggest combos using recognized skills
    combos = suggest_combos(recognized)

    # (6) Cleanup temporary cropped files
    for p in cropped_paths:
        try:
            os.remove(p)
        except:
            pass

    # (7) Return structured result
    return {
        "recognized": recognized,
        "combos": combos,
        "count": len(recognized),
    }
