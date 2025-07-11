
from scripts.run_prompt import run_prompt

def tool_use_example():
    prompt = (
        "You are a helpful assistant. You have access to a calculator.\n"
        "User: What is the square root of 144?\n"
        "Assistant: Let's use the calculator to compute sqrt(144). The answer is 12."
    )
    
    result = run_prompt(prompt)

    print("\n🔹 Tool Use Prompt:")
    print(prompt)
    print("\n🧠 LLM Response:")
    print(result)


if __name__ == "__main__":
    tool_use_example()
