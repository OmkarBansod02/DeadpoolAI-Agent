# Deadpool AI Agent

Welcome to the Deadpool AI Agent project! This application leverages Streamlit to create an interactive AI agent that responds to user queries in the style of Deadpool, the "Merc with a Mouth." The agent provides information about Marvel movies and characters with humor, sarcasm, and pop culture references.

## Features

- **Interactive Q&A**: Ask anything about Marvel movies or characters, and receive witty, Deadpool-style responses.
- **Humorous Responses**: Enjoy responses filled with sarcasm, humor, and fourth-wall-breaking comments.
- **Dynamic Content**: The agent searches for information using ExaTools to provide detailed and up-to-date answers.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/deadpool-ai-agent.git
   ```
   ```bash
   cd deadpool-ai-agent
    ```

2. **Create a Virtual Environment**:
    ```bash
        python -m venv aienv
    ```
3. **Activate the Virtual Environment:

    -On Windows:

    ```bash
        aienv\Scripts\activate
    ```
    -On mac and linux :

    ```bash 
        source aienv/bin/activate

4. ***Install Dependencies***:

    ```bash
        pip install -r requirements.txt
    ```
5. **Set Up Environment Variables**:

    Create a .env file in the project directory and add your Google API key:

         GOOGLE_API_KEY=your_google_api_key_here
     

## Usage

**Run the Streamlit App**:
```bash 
    streamlit run app.py
```