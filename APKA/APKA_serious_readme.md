# AI-Powered Knowledge Agent

In today's fast-paced world, quick access to information is essential. This project is an AI-powered knowledge agent designed to summarize information from Wikipedia, perform web searches, and solve mathematical equations efficiently. It leverages a Large Language Model (LLM) and integrates various tools to provide comprehensive answers to your questions quickly and accurately.

## Features

- **Wikipedia Integration**: Access and summarize Wikipedia content efficiently without navigating through multiple pages. It's like having a dedicated research assistant that can quickly extract relevant information.

- **Web Search Capability**: Utilizes DuckDuckGo for comprehensive web searches when you need information beyond Wikipedia's scope.

- **Mathematical Solver**: Employs SymPy to solve mathematical expressions and equations. Perfect for those complex math problems you encounter in your work or studies.

- **Hugging Face LLM**: Integrates a Hugging Face LLM (specifically, the MBZUAI/LaMini-Flan-T5-783M) for intelligent text generation and response formatting.

- **Modular and Extensible**: Designed for easy addition of new tools and functionalities, making it simple to expand capabilities as needed.

## Project Structure

```
.
├── .env.example
├── main.py
├── requirements.txt
└── tools/
    ├── __init__.py
    ├── duckduckgo_searcher.py
    └── math_solver.py
```

- **main.py**: The core application file where all the AI agent functionality is implemented. This serves as the main control center for the application.
- **requirements.txt**: The complete list of Python packages required for the project.
- **.env.example**: A template for setting up environment variables securely.
- **tools/**: A directory containing individual scripts for different functionalities, organized in a modular way for easy maintenance and expansion.

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment** (recommended for project isolation):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   
   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

### Hugging Face Access Token

This project uses a Hugging Face model for text generation. You'll need a Hugging Face access token to use the model.

1. **Obtain a Hugging Face Token:**
   - Go to [Hugging Face](https://huggingface.co/)
   - Sign in or create an account
   - Navigate to "Settings" -> "Access Tokens" and generate a new token with "read" access

2. **Set up Environment Variable:**
   
   Create a `.env` file in the root directory of your project (same level as `main.py`) and add your Hugging Face token:

   ```ini
   HUGGINGFACE_TOKEN_KEY="YOUR_ACTUAL_HUGGING_FACE_TOKEN"
   ```
   
   **Note:** Replace "YOUR_ACTUAL_HUGGING_FACE_TOKEN" with the token you obtained from Hugging Face.

## Running the Application

To start the AI agent, execute the main.py script:

```bash
python main.py
```

The application will prompt you with "Ask me Anything:" where you can enter your questions.

## Usage Examples

Here are some examples of queries you can ask the AI agent:

- **Wikipedia Query**: "Tell me about the history of artificial intelligence."
- **Mathematical Query**: "What is the derivative of x^2 + 2x?"
- **Web Search Query**: "What is the latest news on climate change?"

## Technical Details

The core of the project resides in `main.py`, which initializes a MBZUAI/LaMini-Flan-T5-783M model from Hugging Face for text generation. The `AiAgent` class orchestrates the query processing:

- It analyzes the nature of your query to determine the appropriate response method
- For mathematical queries, it uses the `solve_math_expression` function (from `tools/math_solver.py`) with SymPy to solve equations
- For web search queries, it uses `web_search` (from `tools/duckduckgo_searcher.py`) to fetch relevant information
- For general knowledge questions, it interacts with the Wikipedia API to extract summaries, including logic for handling disambiguation and page errors
- The extracted context is then fed into the Hugging Face pipeline to generate a comprehensive response

## Future Enhancements

This project is continuously evolving with planned future enhancements including:

- Integration of more specialized tools for diverse domains
- Advanced natural language understanding for better query intent recognition
- Support for conversational AI and multi-turn interactions
- Improved error handling and user feedback mechanisms

## Contributing

Contributions are welcome! If you have suggestions for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is open-sourced under the MIT License.
