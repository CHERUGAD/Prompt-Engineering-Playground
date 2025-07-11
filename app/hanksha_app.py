# app/hanksha_app.py

import streamlit as st
import ollama

# Configure the Streamlit page
st.set_page_config(page_title="Hanksha", layout="centered")

# Styled App Title
st.markdown("""
    <h1 style='text-align: center; font-size: 60px;'>
        <span style='color:orange;'>Han</span><span style='color:blue;'>ksha</span>
    </h1>
""", unsafe_allow_html=True)

# Cache the Ollama model runner (not really needed with local models but simulates caching)
@st.cache_resource
def get_model_runner():
    return ollama

# Input section
prompt_input = st.text_area("✍️ Enter your prompt here:", height=150)
model_choice = st.selectbox("📦 Choose a model:", ["mistral", "llama2", "phi"])

# Inference function
def run_prompt(prompt: str, model: str = "mistral") -> str:
    try:
        ollama_runner = get_model_runner()
        response = ollama_runner.generate(
            model=model,
            prompt=prompt,
            stream=False
        )
        return response['response'].strip()
    except Exception as e:
        return f"❌ Error: {e}"

# Run the prompt
if st.button("🚀 Run Prompt"):
    if prompt_input.strip():
        with st.spinner("Generating response..."):
            response = run_prompt(prompt_input, model=model_choice)
        st.success("✅ Prompt processed successfully!")
        st.markdown("### 🤖 LLM Response")
        st.text_area("💬 Response:", value=response, height=400, max_chars=None, disabled=True)
    else:
        st.warning("⚠️ Please enter a prompt to proceed.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Ravikiran | Powered by Ollama")
