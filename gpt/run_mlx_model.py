import mlx.core as mx
from mlx_lm import load, generate
from mlx_lm.sample_utils import make_sampler # Import the utility

# The model identifier from the MLX Community on Hugging Face.
model_id = "mlx-community/Mistral-7B-Instruct-v0.3-4bit"

# 1. Load the model and tokenizer
print(f"Loading model: {model_id}...")
model, tokenizer = load(model_id)

# 2. Define the conversation
prompt = "Explain what MPS (Metal Performance Shaders) are."
messages = [
    {"role": "user", "content": prompt},
]

# 3. Apply the chat template and tokenize the prompt
processed_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# 4. Create the sampler object
sampler = make_sampler(temp=0.7)

# 5. Generate the response, passing the sampler
print("\nGenerating response...")
response_text = generate(
    model,
    tokenizer,
    prompt=processed_prompt,
    verbose=True,
    max_tokens=512,
    sampler=sampler, # Pass the sampler object here
)

# 6. Print the generated text
print("\n--- Generated Text ---")
print(response_text)
print("----------------------\n")

# Clear the GPU memory cache to free up resources
mx.clear_cache()

