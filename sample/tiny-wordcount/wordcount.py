#!/usr/bin/env python3
"""Count the words in a text file and list the most common ones."""
import argparse
import collections
import re
import sys


def count_words(text):
    return collections.Counter(re.findall(r"[a-z']+", text.lower()))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file")
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args(argv)
    try:
        with open(args.file, encoding="utf-8") as handle:
            counts = count_words(handle.read())
    except OSError as exc:
        sys.stderr.write("wordcount: cannot read the file: %s\n" % exc.strerror)
        return 2
    print("%d words, %d different" % (sum(counts.values()), len(counts)))
    for word, number in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[:args.top]:
        print("%4d  %s" % (number, word))
    return 0


if __name__ == "__main__":
    sys.exit(main())
