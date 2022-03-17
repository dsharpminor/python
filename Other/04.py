import random

machen = ["machen", "mache", "machst", "macht", "machen", "macht", "machen"]
sein = ["sein", "bin", "bist", "ist", "sind", "seid", "sind"]
fragen = ["fragen", "frage", "fragst", "fragt", "fragen", "fragt", "fragen"]

alle_Verben = [machen, sein, fragen]


def ask_questions(values):
    pronouns = ["Infinitiv", "ich", "du", "er, sie, es", "wir", "ihr", "sie, Sie"]
    questions = dict(zip(pronouns, values))
    ran = random.choice(pronouns[1:])
    # the first value next(iter(values)) is always the verb in infinitive
    answer = input(f"{ran} [{next(iter(values))}] - {ran} ")

    if answer == questions.get(ran):
        print(" ✅ Gut! Das ist richtig.")
    else:
        print(" ❌ Leider ist die Antwort falsch... :(")
        print(f"Die richtige Antwort wäre: \"{ran} {questions.get(ran)}\"")


# functions = [ask_questions]

for i in range(10):  # call each function 3 times
    # for func in functions:
    ask_questions(random.choice(alle_Verben))
