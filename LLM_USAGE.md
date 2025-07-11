## ✅ LLM Usage Log

## Local LLM Usage

We use Ollama to run local LLMs such as `mistral` for inference without relying on cloud APIs.

### Model Used:
- **mistral**: Lightweight transformer-based LLM loaded locally via Ollama.

### Inference Flow:
1. Prompt is defined inside each script (e.g., `zero_shot.py`)
2. `run_prompt()` function (from `scripts/run_prompt.py`) sends the prompt to Ollama.
3. Ollama runs the `mistral` model locally and returns the response.

## 🧪 Sample Inference (Zero-Shot)
🔹 Zero-Shot Prompt:
My name is Ravikiran

🧠 LLM Response:
Hello Ravikiran! It's nice to meet you. How can I assist you today? If you have any questions or need help with something, feel free to ask. I am here to help!


## 🧪 Sample Inference (Few-Shot)

**Prompt:**
Classify the sentiment of the following sentences as Positive or Negative:

I absolutely loved the new Batman movie. -> Positive

The weather today is terrible and ruined my plans. -> Negative

This laptop works incredibly fast and looks sleek. -> Positive

I had to wait 30 minutes for my food and it was cold. ->

markdown
Copy
Edit

**LLM Response:**
Negative