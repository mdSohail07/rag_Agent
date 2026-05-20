from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=0.7
)
#
#memory histroy
history = []
while True:
    query = input("User: ")
    history.append({"role":"user", "content":query})
    #print("User: ", query)
    res = llm.invoke(history)
    history.append({"role":"ai", "content": res.content})

    print("AI: ", res.text, "\n")