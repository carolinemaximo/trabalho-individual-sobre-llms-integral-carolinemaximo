from openai import OpenAI

def personal_trainer_chat():

    client = OpenAI(
        api_key="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"
    )

    print("Bem-vindo(a) ao Personal Trainer Virtual!")
    print("Digite 'exit' para sair.\n")

    context = ""

    while True:
        user_input = input("Você: ")
        if user_input.strip().lower() == "exit":
            print("Encerrando o chat. Bons treinos!")
            break

        # Define mensagens
        messages = [
            {
                "role": "developer",
                "content": (
                    "Você é um personal trainer experiente. Sempre que o usuário pedir um treino, "
                    "responda fornecendo um plano de exercícios em formato de listas. "
                    "Detalhe grupos musculares, exercícios, séries e repetições, mantendo um tom motivador."
                )
            },
            {
                "role": "user",
                "content": f"Histórico:\n{context}\n\nPergunta: {user_input}"
            }
        ]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # Extrai a resposta
        response = completion.choices[0].message

        # Print resposta
        print("\n[Personal]:")
        print(response["content"])
        print("-" * 50)

        # Atualiza o contexto da conversa (histórico)
        context += f"Você: {user_input}\nPersonal Trainer: {response['content']}\n"

if __name__ == "__main__":
    personal_trainer_chat()
