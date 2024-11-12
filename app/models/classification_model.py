# app/models/classification_model.py
## This file contains the main LLMClassifier class.

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, AutoModelForCausalLM

# ======================================================================================================================================== #

class LLMClassifier:
    
    """
    LLMClassifier class for performing text classification using a pre-trained Seq2Seq model.
    This class uses Hugging Face's transformers library to load a model and tokenizer
    for classifying text into specified labels based on provided descriptions and examples.
    """
    
    def __init__(self, model_name: str):
        
        """
        Initialize the LLMClassifier with a specified pre-trained model.

        Args:
            model_name (str): The name or path of the pre-trained model to be used.
        """
        
        # Load the tokenizer and model
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        

    def classify(self, text: str, labels: list[str], descriptions: list[str] = None, few_shot_examples: list[dict] = None, is_multi_label: bool = False) -> str:
        
        """
        Classify the input text into one or more of the provided labels based on the 
        descriptions and few-shot examples (if provided). 

        Args:
            text (str): The text to be classified.
            labels (list[str]): A list of possible labels for classification.
            descriptions (list[str], optional): A list of descriptions for each label. Defaults to None.
            few_shot_examples (list[dict], optional): A list of few-shot examples to guide the classification. Defaults to None.
            multi_label (bool, optional): Flag indicating whether multiple labels can be selected. Defaults to False.

        Returns:
            str: The predicted label(s) for the input text.
        """
        
        # Addition to prompt based on whether multi-label classification is needed
        multiple_labels = 'or more' if is_multi_label else ''
        
        # Construct the label-description prompt
        label_description_prompt = "\n".join([f"{label}: {desc}" for label, desc in zip(labels, descriptions)]) if descriptions else ", ".join(labels)
        
         # Create the base prompt for classification
        prompt = f"Classify the following text into one {multiple_labels} of the labels:\n\nLabels:\n{label_description_prompt}\n\n. IMPORTANT: ONLY choose one label from this list: [{labels}]. Do not suggest or create any labels that are NOT part of the provided list. If the text doesn't fit any label, please return 'None' or a label that best matches from the list. Be STRICT in following the given labels."
        
    # Add few-shot examples to the prompt if provided
        if few_shot_examples:
            example_text = "\n\n".join([f"Example:\nText: {ex['text']}\nLabel: {ex['label']}" for ex in few_shot_examples])
            prompt += f"{example_text}\n\n"
        
        # Add the text to be classified to the prompt
        prompt += f"Text: {text}\nLabel:"
        

        # Tokenize the prompt and generate the output
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=50)
        
        # Decode the label
        label = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return label.strip()
    
    
#### prompt experiments:

# 1. prompt = f"Classify the following text into one {multiple_labels} of the labels:\n\nLabels:\n{label_description_prompt}\n\n. Only use the provided labels for classification, and do not suggest labels outside of this list.\n\n"

# 2. prompt = f"Classify the following text into one {multiple_labels} of the labels:\n\nLabels:\n{label_description_prompt}\n\n. IMPORTANT: ONLY choose one label from this list: [{labels}]. Do not suggest or create any labels that are NOT part of the provided list. If the text doesn't fit any label, please return 'None' or a label that best matches from the list. Be STRICT in following the given labels."