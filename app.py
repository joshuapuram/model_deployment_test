import streamlit as st
import os
import json
from dotenv import load_dotenv
# from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI

# Initialize and constants

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj-') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key? Please visit the troubleshooting notebook!")
    
MODEL = 'gpt-5-nano'
# openai = OpenAI()

openai = OpenAI()

response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)
response.choices[0].message.content

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

# Define our user prompt

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

# def messages_for(website):
#     return [
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": user_prompt_prefix + website}
#     ]

# And now: call the OpenAI API. You will get very familiar with this!

def summarize(url):
    website = fetch_website_contents(url)
    response = openai.chat.completions.create(
        model = "gpt-4.1-mini",
        # messages = messages_for(website),

        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": messages_for(url)}
          ],
        stream=True

        
    )
    return response.choices[0].message.content
    st.write_stream(stream)


# Streamlit UI
st.title("Website Summarizer")

# Create input boxes for your function parameters
# name = st.text_input("Enter Name of Company")
link = st.text_input("Enter link here")

# Add a button to trigger the function
if st.button("Run Model"):
    if link:
        with st.spinner("Processing..."):
            # Call your function with the user inputs
            result = summarize(url)
            st.success(result)
    else:
        st.warning("Please provide a link.")
