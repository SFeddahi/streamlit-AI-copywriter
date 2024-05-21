import streamlit as st
import pandas as pd
import openai
import io

Languages = ["Dutch", "English", "French", "German", "Italian"]


# Function to generate responses using OpenAI's API
def generate_response(prompt, language, min_words, max_words, additional_config):
    system_message = (
        "You are a copywriter who writes product descriptions for products in "
        + language
        + ". You always write product descriptions with a minimum of "
        + str(min_words)
        + " words and a maximum of "
        + str(max_words)
        + " words. You always stick to the data you are provided with and incorporate it in your writing. "
        + additional_config
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": "Please write a product description using the following data: "
                + prompt,
            },
        ],
    )
    return response.choices[0].message.content.strip()


def process_file(
    df, selected_columns, language, min_words, max_words, additional_config
):
    df["GPT4_Response"] = ""
    df["GPT4_Response"] = df["GPT4_Response"].astype(str)

    for index, row in df.iterrows():
        prompt_values = [
            f"{col}: {row[col]}" for col in selected_columns if pd.notna(row[col])
        ]
        prompt = ", ".join(prompt_values)

        try:
            response = generate_response(
                prompt, language, min_words, max_words, additional_config
            )
            df.at[index, "GPT4_Response"] = response
        except Exception as e:
            st.error(f"Error occurred for row {index}: {str(e)}")
    return df


def main():
    # Initialize session state for login
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    st.title("🔮 WriteWizard AI")

    # Check if the user is logged in
    if not st.session_state["logged_in"]:
        password = st.text_input(
            "Enter the password to access the app", type="password"
        )
        if st.button("Login"):
            if password == "boterkoek":
                st.session_state["logged_in"] = True
                st.experimental_rerun()  # This forces the script to rerun
            else:
                st.error("Incorrect password. Access denied.")
    else:
        openai.api_key = st.text_input("🙈 Enter your OpenAI API key", type="password")

        uploaded_file = st.file_uploader("📂 Upload your Excel file", type=["xlsx"])
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file)
            st.success("✅ File Uploaded Successfully!")

            columns = df.columns.tolist()
            selected_columns = st.multiselect(
                "⚙️ What columns should your AI include?", columns
            )

            # Language selection
            language = st.selectbox("🌍 What language should your AI speak?", Languages)

            # Word count inputs
            min_words = st.number_input(
                "Minimum words:", min_value=0, max_value=500, value=150
            )
            max_words = st.number_input(
                "Maximum words:", min_value=0, max_value=500, value=300
            )

            # Additional configuration input
            additional_config = st.text_area(
                "🤖 Tell your AI all about your copy guidelines! (Tip: train your AI by pasting an example of a perfect product description into this field.)"
            )

            if st.button("🔮 Magic!"):
                with st.spinner("⏳ Processing..."):
                    processed_df = process_file(
                        df,
                        selected_columns,
                        language,
                        min_words,
                        max_words,
                        additional_config,
                    )

                    output_buffer = io.BytesIO()
                    processed_df.to_excel(output_buffer, index=False)
                    output_buffer.seek(0)

                    st.download_button(
                        label="⬇️ Download your copy!",
                        data=output_buffer,
                        file_name="Processed_File.xlsx",
                        mime="application/vnd.ms-excel",
                    )


if __name__ == "__main__":
    main()
