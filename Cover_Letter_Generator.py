!pip install openai

import os
import openai
import streamlit as st

# Connect to OpenAI API
openai.api_key = os.environ.get("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")

# Define the GPT-3 function to generate the cover letter
def generate_cover_letter(model, prompt, length):
    completions = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Define the Streamlit app
def write_cover_letter():
    st.title("Cover Letter Generator")
    model = "text-davinci-003"

    # Personal Information
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    # Work Experience
    company = st.text_input("Company")
    job_title = st.text_input("Job Title")
    job_description = st.text_area("Job Description")
    length = st.slider("Length of the Letter (in words)", 100, 500, 250)

    # Tone of the Letter
    tone = st.selectbox("Tone of the Letter", ["Formal", "Informal"])
    if tone == "Formal":
        tone = "formal"
    else:
        tone = "informal"

    # Cover Letter
    if st.button("Generate Cover Letter"):
        prompt = (f"Write a {tone} cover letter for the job of {job_title} "
                  f"at {company}. The letter should be {length} words long. "
                  f"Here is the information about the candidate:\n\n"
                  f"First Name: {first_name}\n"
                  f"Last Name: {last_name}\n"
                  f"Email: {email}\n"
                  f"Phone: {phone}\n"
                  f"Job Description: {job_description}")

        cover_letter = generate_cover_letter(model, prompt, length)
        st.write("Here's your cover letter:")
        st.write("---")
        st.write(cover_letter)

    if st.button("Download Cover Letter"):
        file_name = f"{first_name}_{last_name}_cover_letter.txt"
        with open(file_name, "w") as f:
            f.write(cover_letter)
        st.success("Cover Letter saved to disk as '{}'".format(file_name))

if __name__ == "__main__":
    write_cover_letter()
