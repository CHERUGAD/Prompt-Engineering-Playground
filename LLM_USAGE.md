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



 python -m prompts.chain_of_thought
>>

🔹 Chain-of-Thought Prompt:
Let's solve this step by step:
Question: If you have 3 apples and you eat one, how many do you have left?
Step 1: Start with 3 apples.
Step 2: Eat 1 apple.
Step 3: You are left with ->

🧠 LLM Response:
3 - 1 = 2 apples. So, if you started with 3 apples and ate one, you will be left with 2 apples.



python -m prompts.reflection
>>

🔹 Reflection Prompt:
Why did the chicken cross the road?

Answer: To get to the other side.

Now reflect on whether this answer is logically sound and complete. Suggest how it could be improved if necessary.

🧠 LLM Response:
The answer "To get to the other side" is both logically sound and complete in the context of a classic joke or riddle about a chicken crossing a road. However, if we consider a more detailed or imaginative response for creative writing, the answer could be:

"The chicken crossed the road because it had heard rumors of fresh cornfields on the other side, where it could forage without competition from larger animals. With a confident strut and a glint in its eye, it took each step with determination, driven by the promise of a bountiful harvest."

This answer expands upon the original response by providing reasoning behind the chicken's actions, adding depth to the story, and creating a more engaging narrative.


python -m prompts.role_prompting
>>

🔹 Role Prompting:
You are a physics professor. Explain the theory of relativity in simple terms to a 10-year-old student.   

🧠 LLM Response:
Alright, let's imagine you're on a superfast spaceship traveling near the speed of light. Now, here on Earth, things seem normal because we're not moving that fast compared to our surroundings. But when you're traveling so quickly, some strange things happen!

Firstly, let me tell you about Einstein's Special Theory of Relativity. It says that space and time are connected into a single thing called spacetime, and it can bend or curve around massive objects like planets or stars. This is what we call gravity. But here's the cool part - if you travel really fast, spacetime gets stretched out in front of you! That means time slows down for you compared to us here on Earth.       

For example, if you were able to travel at 99% of the speed of light and stayed away for a year, when you returned, we would have aged much more than you because time passed faster for us. You'd be like, "Wow! I've only been gone for a year, but it seems like so much longer here!" That's one of the weird things about relativity.

Now, there's also General Theory of Relativity, which deals with gravity and larger objects like planets or stars. It says that as an object gets more massive, it creates stronger gravitational pull, and its spacetime gets warped even more. This means that planets move in elliptical (not circular) paths around the sun because of the Sun's mass causing spacetime to curve!

So, in simple terms, Einstein's theories tell us that space and time are linked together, massive objects can bend them, and if you travel very fast or very close to a massive object, things start acting differently than what we experience here on Earth. It helps scientists understand the universe better and even make predictions about black holes! Isn't that fascinating?


🔹 Tool Use Prompt:
You are a helpful assistant. You have access to a calculator.
User: What is the square root of 144?
Assistant: Let's use the calculator to compute sqrt(144). The answer is 12.

🧠 LLM Response:
The square root of 144 is 12.


 python -m scripts.run_all
>>

==============================
🧪 Running All Prompt Examples
==============================


🔹 Zero-Shot Prompt:
My name is Ravikiran

🧠 LLM Response:
Hello Ravikiran, it's nice to meet you! How can I help you today? If you have any questions or need assistance with something, feel free to ask. I'm here to help!

------------------------------


🔹 Few-Shot Prompt:
Classify the sentiment of the following sentences as Positive or Negative:

1. I absolutely loved the new Batman movie. -> Positive
2. The weather today is terrible and ruined my plans. -> Negative
3. This laptop works incredibly fast and looks sleek. -> Positive
4. I had to wait 30 minutes for my food and it was cold. ->

🧠 LLM Response:
Negative

------------------------------


🔹 Chain-of-Thought Prompt:
Let's solve this step by step:
Question: If you have 3 apples and you eat one, how many do you have left?
Step 1: Start with 3 apples.
Step 2: Eat 1 apple.
Step 3: You are left with ->

🧠 LLM Response:
3 - 1 = 2 apples left.

------------------------------


🔹 Reflection Prompt:
Why did the chicken cross the road?

Answer: To get to the other side.

Now reflect on whether this answer is logically sound and complete. Suggest how it could be improved if necessary.

🧠 LLM Response:
The given answer, "To get to the other side," is both logical and complete within the context of a classic joke or riddle. However, if we were to expand upon it for a more detailed response, we might consider addressing the chicken's motivation or reason behind crossing the road. This could result in a more engaging and imaginative answer:

"To get to the other side, because there was an inviting farmstand waiting with fresh greens, ripe berries, and tasty insects."

This expanded answer not only satisfies the original requirement but also provides a touch of whimsy by suggesting that the chicken had a purpose beyond simply crossing the road.

------------------------------


🔹 Role Prompting:
You are a physics professor. Explain the theory of relativity in simple terms to a 10-year-old student.   

🧠 LLM Response:
Hello there! Let's talk about the Theory of Relativity. The Theory of Relativity was created by a smart man named Albert Einstein. It has two main parts: Special Relativity and General Relativity.

Special Relativity is all about how things move really, really fast, like when a rocket goes into space. You see, there's something called the speed of light. No matter what or who tries to go faster than this speed of light, it just can't!

Now here comes something cool: if a spaceship were moving so fast that it came close to the speed of light, time would start to slow down inside the ship for anyone on board. It's as if time was stretched out compared to people standing still on Earth. That's mind-bending, isn't it?

General Relativity is a bit more complex because it talks about gravity. You know when you drop something, it falls towards the ground because of gravity, right? Well, Einstein said that gravity is not just a force pulling things together, but actually the curve of space itself! This means if you were in a spaceship and flew really close to a big planet like Earth, the spaceship would start to bend and curve around the Earth!

So, the Theory of Relativity helps us understand how very fast things move and how gravity works. It's all about how space and time work together. Aren't the mysteries of the universe fascinating?

------------------------------


🔹 Tool Use Prompt:
You are a helpful assistant. You have access to a calculator.
User: What is the square root of 144?
Assistant: Let's use the calculator to compute sqrt(144). The answer is 12.

🧠 LLM Response:
That's correct! The square root of 144 is indeed 12. I hope this helps! If you have any other math or general questions, feel free to ask!

By the way, if you want to find square roots without a calculator, here's a quick trick for perfect squares under 50:
1, 4, 9, 16, 25, 36, 49, 64, 81.
Just try to take the middle number of each pair and see if it squares with any other number on the list! It's a fun mental exercise for numbers under 25.

==============================
✅ All prompts executed!
==============================