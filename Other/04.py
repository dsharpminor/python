import random

machen = ["machen", "mache", "machst", "macht", "machen", "macht", "machen"]
sein = ["sein", "bin", "bist", "ist", "sind", "seid", "sind"]


def ask_questions(values):
    pronouns = ["Infinitiv", "ich", "du", "er, sie, es", "wir", "ihr", "sie, Sie"]
    questions = dict(zip(pronouns, values))
    ran = random.choice(pronouns[1:])
    # the first value next(iter(values)) is always the verb in infinitive
    answer = input(f"{ran} [{next(iter(values))}] - {ran} ")

    if answer == questions.get(ran):
        print("Gut! Das ist richtig.")
        ask_questions(values)
    else:
        print("Leider ist die Antwort falsch... :(")
        ask_questions(values)

#
# verbs = [ask_questions(machen), ask_questions(sein)]
# random.choice(verbs)()

ask_questions(machen)