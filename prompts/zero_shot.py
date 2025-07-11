from scripts.run_prompt import run_prompt

def zero_shot_example():
    prompt = "My name is Ravikiran"
    result = run_prompt(prompt)
    
    print("\n🔹 Zero-Shot Prompt:")
    print(prompt)
    print("\n🧠 LLM Response:")
    print(result)

if __name__ == "__main__":
    zero_shot_example()
