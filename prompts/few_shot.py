# prompts/few_shot.py

from scripts.run_prompt import run_prompt

def few_shot_example():
    prompt = """Classify the sentiment of the following sentences as Positive or Negative:

1. I absolutely loved the new Batman movie. -> Positive
2. The weather today is terrible and ruined my plans. -> Negative
3. This laptop works incredibly fast and looks sleek. -> Positive
4. I had to wait 30 minutes for my food and it was cold. ->"""

    result = run_prompt(prompt)

    print("\n🔹 Few-Shot Prompt:")
    print(prompt)
    print("\n🧠 LLM Response:")
    print(result)

if __name__ == "__main__":
    few_shot_example()
