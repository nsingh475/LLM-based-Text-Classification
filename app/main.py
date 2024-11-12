# app/main.py
## This file defines the FastAPI application and the endpoint.

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from app.schemas.request_response import ClassificationRequest, ClassificationResponse
from app.models.classification_model import LLMClassifier
from app.config.model_config import model_name_mapping, default_model

# ======================================================================================================================================== #

# Initialize the FastAPI application
app = FastAPI()

print('Loading model ...')
default_model_name = "google/flan-t5-large"
# default_model_name = "bigscience/bloom-560m"  ## Small model for testing the flow
classifier = LLMClassifier(default_model_name)
print('Model Loaded...')
#### Future Work: Option to use a client specific-model (fine-tuned version)

# ======================================================================================================================================== #

@app.post("/classify", response_model=ClassificationResponse)
async def classify_text(request: ClassificationRequest):
    
    """
    Endpoint to classify text based on the provided model, labels, and examples.

    This endpoint receives a POST request with text, labels, descriptions, few-shot examples,
    and other parameters, and returns the predicted label based on the selected classification model.

    Args:
        request (ClassificationRequest): The request body containing the text and classification details.

    Returns:
        ClassificationResponse: The response body containing the predicted label.
    
    Raises:
        HTTPException: If any error occurs during the classification process.
    """
    
#     return JSONResponse(content={"message": "Request reached classify_text endpoint"}, status_code=200)    ## Debug

    try:
        # Perform the classification
        result_label = classifier.classify(
            text=request.text,
            labels=request.labels,
            descriptions=request.descriptions,
            few_shot_examples=request.few_shot_examples,
            is_multi_label=request.multi_label)
        
        # If classification fails and returns None, raise an error
        if result_label is None:
            raise HTTPException(status_code=500, detail="Classification failed.")
        
        # Return the predicted label in the response
        return ClassificationResponse(label=result_label)
    
    except Exception as e:
        # Handle any exceptions that occur during the classification process
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")