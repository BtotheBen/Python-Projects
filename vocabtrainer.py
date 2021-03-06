from random import randint, random


def view():
    with open('vocab.txt', 'r') as f:
        vocab = f.read()
        print(vocab)

def add():
    deu = input('The German Translation: ')
    eng = input('The English Translation: ')
    with open('vocab.txt', 'a') as f:
        f.write(deu + "|" + eng + '\n')

def ask():
    print("You can quit at all times with: q")
    Vocab = {
    }
    with open('vocab.txt', 'r') as f:
        for v in f.readlines():
            data = v.rstrip()
            key, value = data.split('|')
            Vocab[key] = value

    keys = list(Vocab)

    while True:
        randomnum = randint(0, len(Vocab)-1)
        deu_ask = keys[randomnum]
        eng_ask = Vocab.get(keys[randomnum])

        answ = input("What is the translation of: " + deu_ask + " ?: ")
        if answ == eng_ask:
            print("Good Job, you are right!\n")
        elif answ == 'q':
            break
        else:
            print("Wrong!, the right answer would be: " + eng_ask + '\n')

while True:
    mode = input('\nq --> quit ; add ; view ; ask: ')

    if mode == "q":
        break

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    elif mode == 'ask':
        ask()

    else:
        print('Keine Möglichkeit!\n')
        continue
