from langchain.document_loaders import WebBaseLoader
from langchain.memory import ConversationSummaryMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter


print("Welcome to the Retrieval Augemented Generation (RAG) LangChain Chatbot!")
print("This chatbot uses the OpenAI API to generate responses to your questions.")
print("Please enter a URL to a blog post or other text document.")
print("The chatbot will read the document and use it to answer your questions.")

doc = input("Enter a URL: ")

## Mainly works with markdown styled web pages (e.g. blog posts). 
## web-scraping coming soon...
loader = WebBaseLoader(doc)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

llm = ChatOpenAI()
retriever = vectorstore.as_retriever()
memory = ConversationSummaryMemory(llm=llm,memory_key="chat_history",return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

print('Chatbot: Hello, I am a chatbot. Type "exit" to quit.')

while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = qa(user_input)['answer']
    ## check for error message
    if "error" in response:
        print("Internal error, retrying...")
    else:
        print("Chatbot: ", response)
