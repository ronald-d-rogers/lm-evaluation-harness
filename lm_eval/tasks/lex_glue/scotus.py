newline = "\n"

scotus_classes = [
    "Criminal Procedure",
    "Civil Rights",
    "First Amendment",
    "Due Process",
    "Privacy",
    "Attorneys",
    "Unions",
    "Economic Activity",
    "Judicial Power",
    "Federalism",
    "Interstate Relations",
    "Federal Taxation",
    "Miscellaneous",
    "Private Action",
]

prompt = (
    lambda text: f"""
Which issue area best describes the given the legal opinion excerpt?

Context:
{text}

Issue areas:
{newline.join(scotus_classes)}

Answer: """
)


def doc_to_text(doc):
    return prompt(doc["text"])


def doc_to_choice(doc):
    return scotus_classes
