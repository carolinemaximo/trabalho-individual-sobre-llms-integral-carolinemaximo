import ollamaAI
import chatAI

def main():
    print("Escolha o modelo de IA que deseja usar:")
    print("1) Ollama")
    print("2) Chat GPT (OpenAI)")

    opcao = input("Digite sua opção: ").strip()

    if opcao == "1":
        # Chama a função do Ollama
        ollamaAI.handle_conversation()
    elif opcao == "2":
        # Chama a função da OpenAI
        chatAI.personal_trainer_chat()
    else:
        print("Opção inválida. Finalizando...")

if __name__ == "__main__":
    main()
