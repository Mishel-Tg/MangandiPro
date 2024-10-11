import requests
from typing import Union

class VideoUploader:
    URL = "https://mangandi-2-0.onrender.com"

    def __init__(self, file_path: str):
        self.file_path = file_path

    def _read_file(self) -> bytes:
        with open(self.file_path, "rb") as f:
            return f.read()

    def _upload(self) -> Union[str, dict]:
        data = self._read_file()
        files = {"file": data}
        response = requests.post(
            f"{self.URL}/vupload",
            files=files
        )

        if response.status_code == 200:
            return response.json()
        else:
            return "not found"

    def upload(self) -> str:
        response_json = self._upload()
        if "link" in response_json:
            return response_json["link"]
        else:
            return "not found"
