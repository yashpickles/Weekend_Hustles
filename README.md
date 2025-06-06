# AI-Powered Knowledge Agent: Because Thinking is Hard (For Us, Not the AI)

Let's face it, in this fast-paced world, who has time to actually read? Certainly not you, and definitely not your humble AI assistant. This project is your ultimate procrastination enabler, an AI-powered knowledge agent designed to summarize information from Wikipedia, perform web searches, and even solve those pesky mathematical equations you strategically "forgot" how to do in high school. It leverages a Large Language Model (LLM) – because why use a small one when a large one can confuse us all just as effectively? – and integrates various "tools" to provide answers so comprehensive, you'll wonder if you even need to possess critical thinking skills anymore. (Spoiler: you probably don't, just kidding... mostly.) And Shushhhh It's me Ryan Gos...NOT

## Features

- **Wikipedia Integration**: Why bother clicking through endless Wikipedia links when this AI can extract and summarize content for you? It's like having a very enthusiastic, slightly over-caffeinated research assistant, but without the awkward small talk.

- **Web Search Capability**: Utilizes DuckDuckGo for general web searches. Because sometimes, even Wikipedia isn't quick enough to satisfy your insatiable thirst for immediate, mildly reliable information.

- **Mathematical Solver**: Employs SymPy to solve mathematical expressions and equations. Finally, a use for all those complex math problems you promised yourself you'd revisit "someday." That someday is today, and the AI is doing all the heavy lifting. You're welcome.

- **Hugging Face LLM**: Integrates a Hugging Face LLM (specifically, the MBZUAI/LaMini-Flan-T5-783M). It's a fancy way of saying I've trained a digital brain to churn out answers, so you don't have to strain your own.

- **Modular and Extensible**: Designed for easy addition of new tools and functionalities. Because, let's be honest, I'm all still figuring out what this AI can really do. Expect more shenanigans in the future!

## Project Structure

```
.
└──APKA/
    ├── .env.example
    ├── main.py
    ├── requirements.txt
    └── tools/
        ├── __init__.py
        ├── duckduckgo_searcher.py
        └── math_solver.py
```

-**APKA folder**: This is the main folder where the supposed magic happens, as claimed by Ryan Gos... NOT me.
-  **main.py**: The core application file, where all the AI agent's "magic" happens. Think of it as the control center for your digital minion.
- **requirements.txt**: The definitive list of Python packages you'll need. If it's not on this list, it's probably not important (or I haven't gotten around to adding it yet).
- **.env.example**: A template for setting up environment variables. Because exposing your super-secret tokens is so last season.
- **tools/**: A directory containing individual scripts for different functionalities. This is where the AI's "brains" are divided into bite-sized, manageable pieces, so it doesn't get overwhelmed (unlike some of us on a Monday morning).

## Getting Started

Follow these incredibly complex steps to set up and run the project locally. Don't worry, I'm here to help ;).

### Prerequisites

- Python 3.8+ (Because older Pythons are so... basic.)
- pip (Python package installer). If you don't have this, frankly, I'm not sure how you even found this repository.
- CUDA Toolkit. A toolkit for the OGs (optional though!), trust me it runs faster like Usain Bolt in Olympics Final.  

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
   
   Yes, I know, groundbreaking stuff.

2. **Create a virtual environment** (highly recommended, unless you enjoy dependency hell):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   
   This creates a cozy little bubble for your project, so it doesn't mess with your other Python endeavors.

3. **Install dependencies:**
   
   Install the required Python packages using pip from the requirements.txt file.

   ```bash
   pip install -r requirements.txt
   ```
   
   This is where the magic happens – your computer becomes slightly smarter.

### Hugging Face Access Token

This project uses a Hugging Face model. Because I'm not just pulling answers out of thin air, I'm pulling them from highly sophisticated, pre-trained models. You'll need a Hugging Face access token, unless you enjoy error messages.

1. **Obtain a Hugging Face Token:**
   - Go to [Hugging Face](https://huggingface.co/)
   - Sign in or create an account. (Yes, even AI assistants have gatekeepers.)
   - Navigate to "Settings" -> "Access Tokens" and generate a new token with "read" access. Because this AI is a reader, not a writer... yet.

2. **Set up Environment Variable:**
   
   Create a `.env` file in the root directory of your project (same level as `main.py`) and add your Hugging Face token:

   ```ini
   HUGGINGFACE_TOKEN_KEY="YOUR_ACTUAL_HUGGING_FACE_TOKEN"
   ```
   
   **Note:** Replace "YOUR_ACTUAL_HUGGING_FACE_TOKEN" with the token you obtained from Hugging Face. Don't worry, we won't judge your token for being long and random.

## Running the Application

To start the AI agent, execute the main.py script:

```bash
python main.py
```

The application will then gracefully prompt you to "Ask me Anything:". Feel free to unleash your deepest, darkest, and most trivial questions.

## Usage Examples

Here are some examples of queries you can ask the AI agent. Prepare to be amazed (or mildly amused):

- **Wikipedia Query**: "Tell me about the history of artificial intelligence." (Because clearly, you're not going to read the actual Wikipedia page.)
- **Mathematical Query**: "What is the derivative of x^2 + 2x?" (Don't worry, the AI won't ask you to show your work.)
- **Web Search Query**: "What is the latest news on climate change?" (Because who has time for actual news sites when you have an AI to do the skimming?)

## Technical Details

The core of the project resides in `main.py`, which, in a nutshell, initializes a MBZUAI/LaMini-Flan-T5-783M model from Hugging Face for text generation. Think of it as giving this AI a tiny, pre-trained brain. The `AiAgent` class is the ringleader of this digital circus, orchestrating the query processing with a flair for the dramatic:

- It first attempts to identify the nature of your query (Is it math? Is it web search? Or are you just lonely and want someone to talk to?).
- For mathematical queries, it dispatches to the `solve_math_expression` function (from `tools/math_solver.py`), which, in turn, pokes SymPy with a stick until it solves the problem. It's like having a very tiny, very fast math tutor.
- For web search queries, it uses `web_search` (from `tools/duckduckgo_searcher.py`) to fetch relevant information. Because sometimes, even Wikipedia is too slow for your immediate gratification needs.
- For general knowledge questions (a.k.a., "Wikipedia, please do my homework"), it bravely interacts with the Wikipedia API to extract summaries. It even includes fancy logic for handling "disambiguation" and "page errors," because sometimes Wikipedia is just as confused as you are.
- Finally, the extracted context is fed into the Hugging Face pipeline to generate a concise (or sometimes hilariously brief) summary as a response.

## Future Enhancements

As a "fun weekend project," this agent is continuously evolving. I promise to add more features as soon as I finish my current Netflix binge. Planned future enhancements include:

- Integration of more specialized tools for diverse domains. Because why stop at general knowledge when I can bore you with incredibly specific facts?
- Advanced natural language understanding for better query intent recognition. So it can finally understand what you really mean, even if you don't.
- Support for conversational AI and multi-turn interactions. Get ready for some truly awkward AI-human conversations.
- Improved error handling and user feedback. Because "Sorry, I couldn't find that" is just so unhelpful.

## Contributing

Contributions are welcome!! If you have suggestions for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request. I promise to read them... eventually.

## License

This project is open-sourced under the MIT License. Because sharing is caring, especially when it comes to AI.
