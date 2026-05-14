from transformers import pipeline

# The model identifier for gpt-oss-20b
model_id = "openai/gpt-oss-20b"

# Create a text-generation pipeline with device_map="auto"
# This automatically handles loading the large model and placing it on the M3 GPU.
print("Loading model and creating pipeline...")
generator = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype="auto",
    device_map="auto"
)

# Define the conversation. The pipeline handles applying the chat template.
messages = [
    {"role": "user", "content": "Explain what MXFP4 quantization is."},
]

# Generate a response from the model
print("Generating response...")
try:
    outputs = generator(
        messages,
        max_new_tokens=256,  # Maximum number of tokens to generate
        temperature=0.7,     # Controls the randomness of the output
        do_sample=True       # Enables sampling
    )

    # The pipeline returns a list of dictionaries. Extract the generated text.
    generated_text = outputs[0]["generated_text"][-1]['content']
    print("\n--- Generated Text ---")
    print(generated_text)
    print("----------------------\n")
    
except Exception as e:
    print(f"An error occurred: {e}")
    print("Ensure you have enough memory (at least 16GB RAM) and the correct libraries are installed.")


