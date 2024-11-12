# app/config/model_config.py
## model configuration file that maps clients to model names


# Mapping of client model names to Hugging Face model names
model_name_mapping = {
    "flan_t5": "google/flan-t5-large",
    "chat_glm": "THUDM/chatglm-6b",
    "distilbert": "distilbert-base-uncased-finetuned-sst-2-english"
}

# Default model to use if none is specified
default_model = "google/flan-t5-large"
# default_model = "EleutherAI/gpt-neo-2.7B"          # input loken limit of 50
# default_model = "bigscience/bloom-1b7"             # input loken limit of 50
# default_model = "NousResearch/Llama-2-7b-chat-hf"  # need hugging face login authentication