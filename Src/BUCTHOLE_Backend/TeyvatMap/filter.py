keywords = set([])

def parse(path):
    global keywords
    with open("slangwords.txt", 'rb') as f:
        keywords = [x.decode('utf8').strip() for x in f.readlines()]


def filter(message, repl="*"):
    global keywords
    for kw in keywords:
        message = message.replace(kw, len(kw) * repl)
    return message

def BasicFliter():
    parse("./slangwords.txt")