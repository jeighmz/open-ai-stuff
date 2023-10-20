# Open-AI-Stuff

## Notebook

- **Name**: `openai-google-text-to-speech.ipynb`
  
## Features

- LLM with command-line user input and voice sythensizer

## Tools

### Google Cloud Text-to-Speech API
- **URL**: [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/?hl=en_US&_ga=2.165032319.-1794441157.1692661063&_gac=1.222840681.1697749288.CjwKCAjwp8OpBhAFEiwAG7NaEiqKYJBONlZkAfD16w1bkZQZMRkhLQOBy28wqpXXem1fN3ZiVtWOzBoCacEQAvD_BwE)

### OpenAI API
- **URL**: [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

### Libraries Used

- `requests`: For making HTTP requests.
- `json`: For handling JSON data.
- `dotenv`: To manage environment variables.
- `os`: For operating system dependent functionalities.
- `openai`: For interacting with OpenAI's API.
- `base64`: For Base64 encoding and decoding.
- `IPython Audio`: For audio playback in Jupyter notebooks.

## Quick Note on API Keys

- We use a `.env` file for API keys.
- Don't upload your `.env` file. Add it to `.gitignore`.

---

## Python Script

- **Name**: `openai-langchain-chatbot.py`

## Features

- Interactive command-line chatbot on documents using Langchain and OpenAI

## Tools

### Langchain + OpenAI API
- **URL**: [Langchain Documentation](https://python.langchain.com/docs/use_cases/question_answering/)


### Chroma
- **URL**: [Chroma Documentation](https://docs.trychroma.com)

### Libraries and Modules Used

- `langchain.document_loaders.WebBaseLoader`: For loading web-based documents.
- `langchain.memory.ConversationSummaryMemory`: For managing chat history.
- `langchain.chat_models.ChatOpenAI`: For handling OpenAI-based chat functionalities.
- `langchain.chains.ConversationalRetrievalChain`: For managing the retrieval of chat responses.
- `langchain.embeddings.OpenAIEmbeddings`: For OpenAI-based text embeddings.
- `langchain.vectorstores.Chroma`: For vector storage.
- `langchain.text_splitter.RecursiveCharacterTextSplitter`: For splitting text into smaller chunks.

___
## Python Script

- **Name**: `openai-langchain-rag.py`

## Features

- An interactive chatbot utilizing Langchain agents and OpenAI for smarter Retrieval Augmented Generation (RAG) and document searching.

## Tools

### Langchain + OpenAI API
- **URL**: [Langchain RAG Agent Documentation](https://python.langchain.com/docs/use_cases/question_answering/conversational_retrieval_agents)

### FAISS
- **URL**: [FAISS Documentation](https://faiss.ai/index.html)
- Library for efficient similarity search and clustering of dense vectors.

### Libraries and Modules Used

- `langchain.document_loaders.WebBaseLoader`: For fetching and loading web-based documents.
- `langchain.text_splitter.CharacterTextSplitter`: For splitting text based on characters, with a specified chunk size and overlap.
- `langchain.vectorstores.FAISS`: For efficient similarity search in dense vector spaces.
- `langchain.embeddings.OpenAIEmbeddings`: For generating and handling OpenAI-based text embeddings.
- `langchain.agents.agent_toolkits.create_retriever_tool`: For creating a tool that retrieves information based on user queries.
- `langchain.agents.agent_toolkits.create_conversational_retrieval_agent`: For generating a conversational agent that can perform retrieval based on the user's input.
- `langchain.chat_models.ChatOpenAI`: For handling chat functionalities using OpenAI's GPT models.

## Usage

The script starts by initializing a language model (`llm`) and specifying a web document (`doc`) to be fetched and processed. It then loads the document and splits it into smaller chunks, which are embedded into a vector space using OpenAI embeddings. These embeddings are stored in a FAISS database (`db`), which is used to retrieve relevant information when the user interacts with the chatbot.

To interact with the chatbot, simply run the script and input your queries in the command line interface.




