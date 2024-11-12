# Text Classification Project

This project is a FastAPI-based application for performing text classification tasks using large languge models. It currently supports binary classification and multi-class classification, with an option for using few-shot learning.

This project evaluates a classification model on three classification tasks:
1. Classifies the sentiment of tweets as either "Positive" or "Negative"
2. Categorizes BBC articles into one of five classes: "sport", "business", "tech", "entertainment", or "politics"
3. Assign an appropriate disease label based on the symptoms described 

Each dataset is evaluated using a specific set of metrics relevant to its classification type, as defined in the `task_metric_mapping.json file`. Results are saved in **JSON** files within the `evaluation/results` directory.

**Future Work**: Implement support for multi-label classification tasks.

---

## Project Structure

```plaintext
Text Classification/
├── app/
│   ├── __init__.py
│   ├── main.py                         # The entry point for the FastAPI application
│   ├── config/
│   │   └── model_config.py             # Contains model configuration parameters
│   ├── models/
│   │   ├── __init__.py
│   │   └── classification_model.py     # Implements the LLMClassifier logic
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── request_response.py         # Defines Pydantic schemas for request and response models to enforce data validation.
├── datasets/
│   ├── *.csv                           # Datasets for different classification tasks, each containing labeled examples
│   └── *.json                          # Descriptions and label mappings for each classification task.
├── evaluation/
│   ├── evaluate_classification.py      # Script for evaluating models on multiple datasets and calculating metrics for comparison.
│   ├── task_metric_mapping.json        # Maps each task type (binary, multi-class) to its evaluation metrics.
│   ├── dataset_config.json             # Configuration for dataset paths and formats.
│   └── results/                        # Folder for storing evaluation reports
├── requirements.txt                    # Specifies project dependencies
├── README.md
└── run.sh                              # A shell script for launching the FastAPI app and running any additional setup.
```


## Setup Instructions
1. Clone the Repository and navigate to Text Classification
2. Run the Application using the run.sh script:
```
bash ./run.sh
```
This will install the required dependencies from requirements.txt (if not already installed) and start the FastAPI application using Uvicorn.
3. Verify That the FastAPI Application is Running:
After running the script, you should see output indicating that the FastAPI application is starting. Look for a message like this:
```
INFO:     Will watch for changes in these directories: ['app']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**Note**: You can also run `uvicorn app.main:app --reload` manually on terminal


## How to Test the API Using Postman
1. **Open Postman**: Launch the Postman application to test the API endpoint.
2. **Set Up the Request**
   - **Request Type**: Choose POST.
   - **URL**: Use the following URL for the classification endpoint:
     ```
     http://127.0.0.1:8000/classify
     ```
3. **Set the Headers**: Go to the **Headers** tab and add the following key-value pair:
   - **Key**: `Content-Type`
   - **Value**: `application/json`
4. **Add the Request Body**
    - Go to the Body tab.
    - Select **raw** and set the format to **JSON**.
    - Add your request payload. 
    For example:
    ```json
        {
           "text": "The product is great and the service was excellent.",
           "labels": ["Positive", "Negative"],
           "descriptions": ["A positive sentiment", "A negative sentiment"],
           "few_shot_examples": [
               {"text": "I love this!", "label": "Positive"},
               {"text": "This is terrible.", "label": "Negative"}
                  ]
         }
    ```
5. **Send the Request**: Click Send to submit the request. 
6. You should see the model's classification response in the output.


## Steps to Run the Evaluation
To evaluate the model on these datasets, follow these steps:
1. **Set up and start the API server**: Ensure that the model's API is running locally on 
```http://127.0.0.1:8000/classify```
2. **Navigate to the project directory**: 
```cd "Text Classification"```
3. **Run the evaluation script**: 
```
python evaluation/evaluate_classification.py
```
4. **Check the results**: After running the script, the evaluation results for each task will be saved as **JSON** files in the `evaluation/results` directory, named according to the classification type (e.g., binary_report.json, multi-class_report.json, multi-label_report.json).
