
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

#Data Ingestion--From the website we need to scrape the data 
from langchain_community.document_loaders import WebBaseLoader
loader=WebBaseLoader("https://docs.smith.langchain.com/tutorials/Administrators/manage_spend")
loader
docs=loader.load()
docs

### Load Data--> Docs-->Divide our Docuemnts into chunks dcouments-->text-->vectors-->Vector Embeddings--->Vector Store DB

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(docs) ## Split the loaded Documents into smaller Documents

documents

from langchain_openai import OpenAIEmbeddings
embeddings=OpenAIEmbeddings()

from langchain_community.vectorstores import FAISS
vectorstoredb=FAISS.from_documents(documents,embeddings)

vectorstoredb

from langchain_openai import ChatOpenAI
llm=ChatOpenAI(model="gpt-4o")

## Retrieval Chain, Document chain

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_template(
    """
Answer the following question based only on the provided context:
<context>
{context}
</context>


"""
)

document_chain=create_stuff_documents_chain(llm,prompt)
document_chain

from langchain_core.documents import Document
document_chain.invoke({
    "input":"LangSmith has two usage limits: total traces and extended",
    "context":[Document(page_content="LangSmith has two usage limits: total traces and extended traces. These correspond to the two metrics we've been tracking on our usage graph. ")]
})

retriever=vectorstoredb.as_retriever()
from langchain.chains import create_retrieval_chain
retrieval_chain=create_retrieval_chain(retriever,document_chain)
retrieval_chain


## Get the response form the LLM

response=retrieval_chain.invoke({"input":"LangSmith has two usage limits: total traces and extended"})
response['answer']


response

response['context']
