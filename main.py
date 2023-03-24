from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

files_root_directory = Path("/home/www-matteogatzner/public/files/")

url_root = "/file_server/"


def sanitize_str(s: str) -> str:
    keepcharacters = (" ", ".", "_")
    return "".join(c for c in s if c.isalnum() or c in keepcharacters).rstrip()


@app.get(url_root + "{file_name}", response_class=FileResponse)
async def main(file_name: str):
    file_path = files_root_directory / sanitize_str(file_name)
    if not file_path.exists():
        raise HTTPException(
            status_code=404, detail=f"File with file name {file_name} not found!"
        )
    return file_path
