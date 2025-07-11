# Prompt-Engineering-Playground
Interactive Streamlit app to explore prompt engineering techniques like zero-shot, few-shot, chain-of-thought, role prompting, reflection, and tool use with LLMs. Useful for learning, experimentation, and GenAI prototyping.

### 🔧 Techniques Included:
- Zero-shot Prompting
- Few-shot Prompting
- Chain-of-Thought (CoT)
- Role Prompting
- Reflection-based Prompting
- Tool Use Integration

## 🗂 Project Structure
C:.
│   .gitignore
│   Dockerfile
│   LLM_USAGE.md
│   notepad
│   README.md
│   requirements.txt
│
├───app
│       hanksha_app.py
│
├───data
│   ├───processed
│   └───raw
├───prompts
│   │   chain_of_thought.py
│   │   few_shot.py
│   │   reflection.py
│   │   role_prompting.py
│   │   tool_use.py
│   │   zero_shot.py
│   │   __init__.py
│   │
│   └───__pycache__
│           chain_of_thought.cpython-312.pyc
│           few_shot.cpython-312.pyc
│           reflection.cpython-312.pyc
│           role_prompting.cpython-312.pyc
│           tool_use.cpython-312.pyc
│           zero_shot.cpython-312.pyc
│           __init__.cpython-312.pyc
│
├───scripts
│   │   run_all.py
│   │   run_prompt.py
│   │   __init__.py
│   │
│   └───__pycache__
│           run_all.cpython-312.pyc
│           run_prompt.cpython-312.pyc
│           __init__.cpython-312.pyc
│
└───utils
        io_utils.py
        __init__.py

### 📦 How to Run
```bash
pip install -r requirements.txt
python scripts/run_prompt.py --technique zero_shot


---

## 🐳 Docker Deployment

You can containerize and run the app using Docker.

### Step 1: Build the Docker image

```bash
docker build -t hanksha-app .
