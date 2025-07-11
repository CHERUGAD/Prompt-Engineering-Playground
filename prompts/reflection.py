from scripts.run_prompt import run_prompt

def reflection_example():
    initial_prompt = "Why did the chicken cross the road?"
    reflection_instruction = (
        "Now reflect on whether this answer is logically sound and complete. "
        "Suggest how it could be improved if necessary."
    )

    full_prompt = f"{initial_prompt}\n\nAnswer: To get to the other side.\n\n{reflection_instruction}"
    result = run_prompt(full_prompt)

    print("\n🔹 Reflection Prompt:")
    print(full_prompt)
    print("\n🧠 LLM Response:")
    print(result)

if __name__ == "__main__":
    reflection_example()
