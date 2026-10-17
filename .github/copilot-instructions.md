# Copilot instructions

## Repository workflow

This is the Python starter repository for the shipthatcode **Build a Transformer
(GPT-style)** course. The active solution is always `main.py`; lessons are
separate exercises, so later lesson requirements may intentionally replace
earlier behavior. Do not try to make one implementation satisfy every lesson.
Use git history to recover an earlier solution if needed.

The grader is configured by `.shipthatcode.json` with `main.py` as the
entrypoint. Keep that file and the `tests/` fixtures intact. Each lesson has
numbered `.in` files and byte-exact `.out` files under a zero-padded directory
such as `tests/01-what-is-transformer/`.

## Commands

The repository requires Python 3.10 or newer and has no third-party
dependencies or configured linter.

```sh
# Run every lesson fixture (usually only useful when the implementation covers
# all lessons).
./run_tests.sh

# Run one lesson; both forms select the same zero-padded directory.
./run_tests.sh 01
./run_tests.sh 1

# Run one fixture directly while iterating.
python3 main.py < tests/01-what-is-transformer/1.in

# Compare one fixture's output exactly.
python3 main.py < tests/01-what-is-transformer/1.in \
  | diff -u tests/01-what-is-transformer/1.out -
```

The local runner executes `main.py` once per input fixture and compares stdout
exactly. Avoid diagnostic output on stdout; use the lesson's required output
format only. The course website's **Check my solution** is the authoritative
grader and also runs hidden tests.

## Architecture and data flow

`main.py` is a small stdin/stdout command processor:

1. `read_lines()` reads non-empty input lines and removes carriage returns.
2. The top-level loop splits each line into a command and the remainder payload.
3. The command updates state or calls a pure helper, then prints the result.
4. `run_tests.sh` feeds each fixture to the program and compares its stdout
   with the paired expected file.

The current lesson (`01-what-is-transformer`) builds a character vocabulary
from a `CORPUS` command, then handles `ENCODE` and `DECODE` commands using that
vocabulary. `build_vocab`, `encode`, and `decode` contain the lesson logic;
the input loop already provides the protocol and output framing. For later
lessons, the same single-file/protocol model remains, but the command formats
and numerical helpers change according to that lesson's specification.

## Codebase-specific conventions

- Follow the active lesson's input and output contract exactly; do not infer
  behavior from another lesson's fixtures.
- Preserve the existing stdin loop and keep helper functions independently
  testable. State that must persist across commands belongs in the top-level
  vocabulary/model variable, as established by the starter.
- For the current vocabulary exercise, the vocabulary is a string of distinct
  corpus characters in sorted order. Encoding uses each character's zero-based
  vocabulary index and `-1` for an unknown character; decoding uses `?` for an
  invalid id.
- Outputs are deliberately compact and exact: encoded ids are comma-separated
  with no extra spaces, and decoded text is printed as one line.
- Numeric lessons use the existing `f4()` and `join_row()` formatting helpers:
  four decimal places, comma-separated rows, and `-0.0000` normalized to
  `0.0000`. Preserve these conventions unless the active lesson explicitly
  specifies another format.
- Keep changes focused in `main.py`. Do not add dependencies or generated
  artifacts; `.prog`, bytecode caches, workspace files, and other temporary
  outputs are ignored already.
