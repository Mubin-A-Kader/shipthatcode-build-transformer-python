import sys

def read_lines():
    return [l.rstrip("\r") for l in sys.stdin.read().split("\n") if l.rstrip("\r") != ""]


def f4(v):
    s = "%.4f" % v
    return "0.0000" if s == "-0.0000" else s


def parse_list(s):
    return [float(t) for t in s.split(",")]


def join_row(v):
    return ",".join(f4(x) for x in v)


def build_vocab(corpus):
    # TODO: the vocabulary is the distinct characters of the corpus, in sorted order (a string)
    return ""


def encode(vocab, text):
    ids = []
    for ch in text:
        # TODO: append the index of ch in vocab, or -1 when it is not there
        ids.append(0)
    return ids


def decode(vocab, ids):
    out = []
    for i in ids:
        # TODO: append the character with id i, or "?" when i is not a valid id
        out.append("?")
    return "".join(out)


vocab = ""
for line in read_lines():
    cmd, _, rest = line.partition(" ")
    if cmd == "CORPUS":
        vocab = build_vocab(rest)
    elif cmd == "ENCODE":
        print(",".join(str(i) for i in encode(vocab, rest)))
    elif cmd == "DECODE":
        print(decode(vocab, [int(t) for t in rest.split(",")]))
