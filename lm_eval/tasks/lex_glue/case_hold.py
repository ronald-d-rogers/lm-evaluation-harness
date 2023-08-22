newline = "\n"

prompt = (
    lambda context, endings: f"""
Given the legal decision excerpt, which holding best fills in the masked "<HOLDING>"?

Context:
{context}

Holdings:
{newline.join([f"{i}. {endings[i]}" for i in range(len(endings))])}

Answer: """
)


def alphabetical(num):
    letters = []
    for i in range(num):
        letters.append(chr(i + 65))
    return letters


def doc_to_text(doc):
    return prompt(doc["context"], doc["choices"])


def doc_to_choice(doc):
    return alphabetical(len(doc["endings"]))
