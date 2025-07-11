from scripts.run_prompt import run_prompt

def role_prompting_example():
    prompt = (
        "You are a physics professor. Explain the theory of relativity "
        "in simple terms to a 10-year-old student."
    )
    result = run_prompt(prompt)

    print("\n🔹 Role Prompting:")
    print(prompt)
    print("\n🧠 LLM Response:")
    print(result)

if __name__ == "__main__":
    role_prompting_example()