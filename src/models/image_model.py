from pydantic import BaseModel
from typing import Optional

class ImageModel(BaseModel):
    id: str
    filename: str
    status: str
    original_path: Optional[str] = None
    processed_path: Optional[str] = None