from fastapi import FastAPI
from pydantic import BaseModel
import os
import yaml

app = FastAPI()

#Get Required Data
cwd = os.getcwd()
media_folder = cwd + "/server/media/"
files = os.listdir(media_folder)

stripped_files = [
    os.path.splitext(file)[0]  # Remove extension
    for file in files
    if file.lower().endswith(".mp4")  # Only handle mp4 files
]

metadataFiles = [file + ".metadat" for file in stripped_files]





@app.get("/list/videos")
async def list_videos():
    metaList = []
    for metadataFile in metadataFiles:
        with open(media_folder + metadataFile, "r") as f:
            metadata = yaml.safe_load(f)
            metaList.append(metadata)

    return {"files": metaList}

@app.get("/get/metadata/{thing}")
async def get_metadata(thing: str):
    return {"thing": thing}


