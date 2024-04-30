from QABot import QABot

def print_list():
    try:
        with open('list.txt', 'r') as file:
            print("List of questions:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("List file not found.")

def main():
    bot = QABot('database.txt')
    while True:
        question = input("Ask me a question (type 'example' for an example, or 'exit' to quit): ")
        if question.lower() == 'exit':
            break
        elif question.lower() == 'example':
            print("Example Question: What can you do?|")
            print("Example Answer: I can answear to a list of question about URP, Educational System, Artificial Intelligence technologies and the Phylosophy of Ethics.")
        elif question.lower() == 'list':
            print_list()
        else:
            answer = bot.answer_question(question)
            print("Answer:", answer)

if __name__ == "__main__":
    main()