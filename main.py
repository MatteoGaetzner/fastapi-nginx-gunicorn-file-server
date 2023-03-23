from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

files_root_directory = Path("/home/www-matteogatzner/public/files/")

url_root = "/file_server/"


@app.get(url_root + "{file_name}", response_class=FileResponse)
async def main(file_name: str):
    file_path = files_root_directory / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"File with file name {file_name} not found!")
    return file_path
