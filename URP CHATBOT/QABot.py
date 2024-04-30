class QABot:
    def __init__(self, database_file):
        self.database = {}
        with open(database_file, 'r') as file:
            for line in file:
                question, answer = line.strip().split('|')
                self.database[question.lower()] = answer

    def answer_question(self, question):
        return self.database.get(question.lower(), "Sorry, I don't understand that question.")
