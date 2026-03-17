import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# 1. Setup & Auth
load_dotenv(override=True)
# Using st.secrets or environment variable
api_key = st.secrets.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# 2. Prompts
SYSTEM_PROMPT = "You are a snarky assistant that provides short, humorous summaries. Respond in markdown."
USER_PROMPT_PREFIX = "Here is the user input. Provide a short, funny, snarky reply/answer: "

def summarize(user_input):
    # Note: Use 'gpt-4o' or 'gpt-3.5-turbo' as current valid models
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_PREFIX + str(user_input)}
        ]
    )
    return response.choices[0].message.content

# 3. Streamlit UI
st.title("Snarky Assistant")

user_text = st.text_input("Enter your text/question here:")

if st.button("Run Model"):
    if user_text:
        with st.spinner("Processing..."):
            try:
                result = summarize(user_text)
                st.markdown(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text first.")
