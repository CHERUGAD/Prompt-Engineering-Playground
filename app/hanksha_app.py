import streamlit as st
import ollama

# Page configuration
st.set_page_config(page_title="Hanksha", layout="centered")

# Inject fixed CSS for dark/light theme compatibility
st.markdown("""
    <style>
        /* Force white background everywhere */
        html, body, [class*="css"] {
            background-color: white !important;
            color: black !important;
        }

        /* Prompt input */
        textarea, .stTextArea textarea, .stTextInput input {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
        }

        /* ✅ FIX: Make disabled response textarea show black text always */
        .stTextArea textarea:disabled {
            color: black !important;
            background-color: white !important;
            opacity: 1 !important;
            -webkit-text-fill-color: black !important; /* for Safari/Chrome */
            caret-color: transparent;
        }

        /* Button styling */
        .stButton > button {
            background-color: #ff8800 !important;
            color: white !important;
            border-radius: 8px;
        }

        .stButton > button:hover {
            background-color: #ffaa33 !important;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("""
    <h1 style='text-align: center; font-size: 60px; margin-bottom: 10px;'>
        <span style='color:orange;'>Han</span><span style='color:blue;'>ksha</span>
    </h1>
""", unsafe_allow_html=True)

# Cache the model
@st.cache_resource
def get_model_runner():
    return ollama

# Prompt input
prompt_input = st.text_area("✍️ Enter your prompt here:", height=150)
model_choice = st.selectbox("📦 Choose a model:", ["mistral", "llama2", "phi"])

# Run inference
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

# Run button logic
if st.button("🚀 Run Prompt"):
    if prompt_input.strip():
        with st.spinner("Generating response..."):
            response = run_prompt(prompt_input, model=model_choice)
        st.success("✅ Prompt processed successfully!")
        st.markdown("### 🤖 LLM Response")
        # Response box: disabled, but styled to show black text
        st.text_area("💬 Response:", value=response, height=400, disabled=True)
    else:
        st.warning("⚠️ Please enter a prompt to proceed.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Ravikiran | Powered by Ollama")
