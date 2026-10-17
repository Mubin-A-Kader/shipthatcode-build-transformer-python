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
    return "".join(sorted(set(corpus)))


def encode(vocab, text):
    ids = []
    for ch in text:
        ids.append(vocab.find(ch))
    return ids


def decode(vocab, ids):
    out = []
    for i in ids:
        out.append(vocab[i] if 0 <= i < len(vocab) else "?")
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
