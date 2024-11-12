# app/schemas/request_response.py

from pydantic import BaseModel
from typing import List, Optional

class ClassificationRequest(BaseModel):
    text: str
    labels: List[str]
    descriptions: Optional[List[str]] = None
    few_shot_examples: Optional[List[dict]] = None
    model_name: Optional[str] = None  # Optional model name for choosing model dynamically
    multi_label: bool = False         # Default to False for single-label classification

        
class ClassificationResponse(BaseModel):
    label: str