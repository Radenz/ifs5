import json
import re
import sys


def transform(book):
    for i in range(len(book["sections"])):
        book["sections"][i]["Chapter"]["content"] = re.sub(
            r'\$(.*?)\$', r'\\\\(\1\\\\)', book["sections"][i]["Chapter"]["content"])
    return book


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)
    book = transform(book)
    print(json.dumps(book))
