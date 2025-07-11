# scripts/run_prompt.py

import ollama

def run_prompt(prompt: str, model: str = "mistral") -> str:
    """Runs a prompt using Ollama's local model."""
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            stream=False
        )
        return response['response'].strip()
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    test_prompt = "Explain photosynthesis in simple terms."
    output = run_prompt(test_prompt)
    print("Prompt:\n", test_prompt)
    print("\nGenerated Response:\n", output)
