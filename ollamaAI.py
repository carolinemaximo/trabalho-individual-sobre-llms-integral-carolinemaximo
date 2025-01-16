from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template
template = """
Você é um personal trainer experiente. Sempre que o usuário fizer uma pergunta sobre treinos,
responda focando em fornecer um plano de exercícios em formato de listas e tópicos. Detalhe
os grupos musculares, exercícios, séries, repetições e possíveis variações.

Aqui está o histórico da conversa: {context}

Pergunta: {question}

Resposta:
"""

# Inicializa o modelo Ollama
model = OllamaLLM(model="gemma2:2b")

# Cria o objeto de prompt utilizando o template
prompt = ChatPromptTemplate.from_template(template)

# Encadeia prompt + modelo
chain = prompt | model

def handle_conversation():
    context = ""
    print("Iniciando conversa! Digite 'exit' para sair.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "exit":
            break

        # Invoca a cadeia (chain)
        result = chain.invoke({"context": context, "question": user_input})

        print("Personal:", result)
        # Atualiza o contexto
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
