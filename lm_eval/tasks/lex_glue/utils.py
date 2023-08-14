def num_to_abcs(num):
    letters = []
    for i in range(num):
        letters.append(chr(i + 65))
    return letters


def doc_to_text(doc):
    endings = doc["endings"]
    choices = num_to_abcs(len(endings))

    for i in range(len(endings)):
        choices[i] = choices[i] + ") " + endings[i]

    choices = "\n".join(choices)
    text = f"Given the legal decision excerpt, which holding best fills in the masked \"<HOLDING>\"?\n\nContext:\n{doc['context']}\n\nHoldings:\n{choices}\n\nAnswer:"

    return text


def doc_to_choice(doc):
    endings = doc["endings"]
    choices = num_to_abcs(len(endings))
    return choices
