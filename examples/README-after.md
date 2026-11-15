# tiny-wordcount

Counts the words in a text file and lists the most common ones.

## New to this? Start here

**Who it is for:** Anyone with a plain text file who wants to see which words show up most, no programming needed.

**The problem it solves:** You have notes or a draft and want to know how long it is and which words you repeat, without counting by hand.

**Four steps** (in Claude Desktop, Code tab):

1. Download this project (the `tiny-wordcount` folder) onto your computer.
2. Open the folder in the Code tab.
3. Type the sentence below.
4. Read the result in Claude's reply.

**Type this to Claude:**

    Count the words in sample/notes.txt and show me the most common ones.

**What you get back** (real output, run on 2026-11-12 on the sample in `sample/notes.txt`):

    46 words, 32 different
       8  the
       4  planner
       3  boxes
       2  goal
       2  sold

## Usage

```
python wordcount.py FILE [--top N]
```

`--top N` sets how many words to list (default 5). Words are compared without regard to case. The script uses only the Python standard library.

## Files

- `wordcount.py`: the script.
- `sample/notes.txt`: a short text to try it on.
