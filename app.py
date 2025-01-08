import os
import openai
import streamlit as st
from dotenv import load_dotenv

#Welcome to the AI-powered lore generator! Input your prompt to create immersive stories in the world of League of Legends.

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Apply custom CSS
def apply_custom_css():
    st.markdown("""
    <style>
    /* Embed the Beaufort for LoL font */
    @font-face {
        font-family: 'Beaufort';
        src: url('fonts/BeaufortforLOL-Bold.ttf') format('truetype');
        font-weight: bold;
    }

    @font-face {
        font-family: 'Beaufort';
        src: url('fonts/BeaufortforLOL-Regular.ttf') format('truetype');
        font-weight: normal;
    }

    /* Global body styles */
    body {
        font-family: 'Beaufort', serif !important; /* Apply Beaufort font globally */
        background-color: #0e1117;
        color: #c9aa71;
    }

    /* Title */
    .stTitle {
        text-align: center;
        font-family: 'Beaufort', serif !important; /* Use Beaufort font */
        font-weight: bold;
        font-size: 48px;
        color: #c9aa71;
        text-shadow: 2px 2px 5px #000;
        margin-top: 20px;
    }
    
    /* Welcome Box */
    .welcome-box {
        font-family: 'Beaufort', serif !important;
        font-size: 22px;
        color: #f0f0f0;
        background-color: #1b1f23;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #c9aa71; /* Gold border */
        margin: 20px auto;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        line-height: 1.6;
    }
     
    /* Header for Generated Lore */
    h3 {
        text-align: center;
        font-family: 'Beaufort', serif !important;
        font-weight: bold;
        font-size: 35px;
        color: #c9aa71;
        margin-top: 20px;
    }

    /* Lore Text */
    .lore-text {
        font-family: 'Beaufort', serif !important; /* Ensure font applies */
        font-size: 20px;
        color: #f0f0f0;
        background-color: #1b1f23;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #c9aa71;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        line-height: 1.6;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Render the app title with custom styling
st.markdown(
    """
    <div class="stTitle">
        League of Legends AI-Generated Lore Expansion
    </div>
    """,
    unsafe_allow_html=True,
)

# Render the Welcome Box
st.markdown(
    """
    <div class="welcome-box">
        Welcome to the AI-powered lore generator! Input your prompt to create immersive stories in the world of League of Legends.
    </div>
    """,
    unsafe_allow_html=True,
)

user_prompt = st.text_input("Enter a description of a character, event, or region:")

# Handle the generated lore
if user_prompt:
    with st.spinner("Generating lore..."):
        try:
            # Generate lore using OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert writer for League of Legends lore. Generate detailed, immersive stories."},
                    {"role": "user", "content": user_prompt}
                ]
            )
            lore_text = response.choices[0].message["content"]

            # Render the Generated Lore header
            st.markdown("<h3>Generated Lore</h3>", unsafe_allow_html=True)

            # Render the user-generated lore
            st.markdown(
                f"""
                <div class="lore-text">
                    {lore_text}
                </div>
                """,
                unsafe_allow_html=True,
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

