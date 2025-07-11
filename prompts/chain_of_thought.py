from scripts.run_prompt import run_prompt

def chain_of_thought_example():
    prompt = (
        "Let's solve this step by step:\n"
        "Question: If you have 3 apples and you eat one, how many do you have left?\n"
        "Step 1: Start with 3 apples.\n"
        "Step 2: Eat 1 apple.\n"
        "Step 3: You are left with ->"
    )
    result = run_prompt(prompt)

    print("\n🔹 Chain-of-Thought Prompt:")
    print(prompt)
    print("\n🧠 LLM Response:")
    print(result)

if __name__ == "__main__":
    chain_of_thought_example()
