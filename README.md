# WriteWizard AI

PowerText Lite is a Streamlit application that generates product descriptions using OpenAI's GPT-4 model. It takes an Excel file with product data as input and produces high-quality, AI-generated product descriptions.

## Features

- Upload an Excel file containing product data.
- Select the columns to include in the product descriptions.
- Choose the language for the descriptions.
- Specify the minimum and maximum word count for the descriptions.
- Customize the AI's output with additional copywriting guidelines.
- Download the generated product descriptions in an Excel file.

## Prerequisites

- Python 3.11 or later
- Streamlit
- pandas
- openai

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/sfeddahi/PowerText-Lite.git
    cd PowerText-Lite
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the application, you need to ensure that the Streamlit executable is accessible from your command line. This is where Streamlit sometimes gets a little fuzzy with windows machines, the most simple way to achieve this is by adding the directory containing the Streamlit executable to your system's PATH. This can be done by running the following command:

**Windows PowerShell:**

```sh
$Env:PATH += ";C:\path\to\your\python\Scripts"
streamlit run "path\to\your\repository\app.py"
```

**Note:** Replace `C:\path\to\your\python\Scripts` with the actual path to your Python Scripts directory and `path\to\your\repository\app.py` with the actual path to your `app.py` file. The directory path will vary depending on your Python installation location.

For example:

```sh
$Env:PATH += ";C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python311\Scripts"
streamlit run "C:\path\to\PowerText-Lite\app.py"
```

### OpenAI API Key

You will need an OpenAI API key to use this application. You can obtain your API key from the OpenAI website. Once you have your API key, you can enter it in the application when prompted.

## Running the App

1. Start the Streamlit application:

    ```sh
    streamlit run "C:\path\to\PowerText-Lite\app.py"
    ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Log in using the password you created, the standard password is `boterkoek` but you can obviously change it. Any real-life applications would of course require more secure authentication measures.

4. Enter your OpenAI API key.

5. Upload your Excel file, select the desired columns, configure the AI settings with your own copy/brand guidelines, and generate the product descriptions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- Streamlit for the easy-to-use web app framework, if you're coming from using flask like me it's really a gamechanger in terms of intuitiveness and look-and-feel.
- OpenAI for providing the GPT-4 model.
