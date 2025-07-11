from prompts.zero_shot import zero_shot_example
from prompts.few_shot import few_shot_example
from prompts.chain_of_thought import chain_of_thought_example
from prompts.reflection import reflection_example
from prompts.role_prompting import role_prompting_example
from prompts.tool_use import tool_use_example

def run_all():
    print("\n==============================")
    print("🧪 Running All Prompt Examples")
    print("==============================\n")

    zero_shot_example()
    print("\n------------------------------\n")
    
    few_shot_example()
    print("\n------------------------------\n")
    
    chain_of_thought_example()
    print("\n------------------------------\n")
    
    reflection_example()
    print("\n------------------------------\n")
    
    role_prompting_example()
    print("\n------------------------------\n")
    
    tool_use_example()
    print("\n==============================")
    print("✅ All prompts executed!")
    print("==============================\n")

if __name__ == "__main__":
    run_all()
