from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embedding = OpenAIEmbeddings(model= "ext-embedding-3-large",dimension= 300)

documents = [
    'Virat Kohli is known for his aggressive batting style and consistency across all formats.'
    'Sachin Tendulkar is called the “God of Cricket” and holds numerous world records.'
    'MS Dhoni is famous for his calm leadership and finishing matches under pressure.'
    'Rohit Sharma is known for his elegant batting and record-breaking double centuries.'
    'Jasprit Bumrah is one of the best fast bowlers with a unique bowling action.'

]

query = 'Tell me about Virat Kolhi'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(documents[index])
print("similarity score is:", score)



