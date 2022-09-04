import json
import re
import sys


def transform(book):
    for i in range(len(book["sections"])):
        # Separator case
        if type(book["sections"][i]) != dict or "Chapter" not in book["sections"][i]:
            continue
        book["sections"][i]["Chapter"]["content"] = re.sub(
            r'\$(.*?)\$', r'\\\\(\1\\\\)', book["sections"][i]["Chapter"]["content"])

        book["sections"][i]["Chapter"]["sub_items"] = transform_sub(
            book["sections"][i]["Chapter"]["sub_items"]
        )

    return book


def transform_sub(sub):
    for i in range(len(sub)):
        if type(sub[i]) != dict or "Chapter" not in sub[i]:
            continue
        sub[i]["Chapter"]["content"] = re.sub(
            r'\$(.*?)\$', r'\\\\(\1\\\\)', sub[i]["Chapter"]["content"])

        sub[i]["Chapter"]["sub_items"] = transform_sub(
            sub[i]["Chapter"]["sub_items"]
        )
    return sub


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == "supports":
            sys.exit(0)

    context, book = json.load(sys.stdin)
    sys.stderr.write(json.dumps(book, indent=2))
    book = transform(book)
    sys.stderr.write(json.dumps(book, indent=2))
    print(json.dumps(book))
