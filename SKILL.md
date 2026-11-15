---
name: beginner-readme-section
description: Adds a "New to this? Start here" section to the top of a project's README, written for someone who has never used the project - who it is for, the problem it solves, four steps, one sentence to type to Claude, and what comes back. The "what you get back" part is only ever real output from actually running that sentence; if it could not be run, the section says so. Use when the user asks to add a beginner section, a start-here section or a quick start for newcomers to a README, for example "add a beginner section to my README", "README에 초보용 칸 만들어 줘", "make my README beginner friendly".
---

# Beginner README Section

Write one short section at the top of the README that gets a first-time reader from "what is this" to a real result. Change nothing else in the README.

## When to use

- The user asks for a beginner section, a "start here" section, or a newcomer quick start in a README.
- The user says the README is hard for new people to follow.

Do not use it to rewrite or restructure the whole README, and do not use it for API reference or contributor docs.

## Steps

1. **Read the project.** Read the README, the top-level file list, and the entry point (the main script, the skill file, or the command the README tells people to run). Find out what a person actually does with this project and what they get.
2. **Find the sample.** Look for a sample or example folder the project ships (`examples/`, `sample/`, `demo/`, test fixtures). The beginner steps must work on something that is already in the repository. If there is nothing to run the project on, tell the user and ask whether to add a small sample; do not invent one silently.
3. **Choose the one sentence.** Write the single sentence a beginner would type to Claude to get the project's main result on the sample. Use the user's own words where the README has them. One sentence, no options, no flags.
4. **Run it for real.** Do exactly what that sentence asks, on the sample, the way a newcomer's Claude would: run the command or follow the skill. Capture what comes back. Work on a copy if running it changes files.
5. **Write the section** in the format below, with the real output from step 4.
6. **Put it in the README** directly under the title and any one-line description, above everything else. If a "New to this? Start here" section is already there, replace that section only.
7. **Tell the user** what you added, which sentence you chose, and whether the output is from a real run.

## The section

Use this shape. Keep it under about 30 lines, not counting the output block.

```markdown
## New to this? Start here

**Who it is for:** (one sentence: the kind of person, in plain words)

**The problem it solves:** (one or two sentences, from the reader's side)

**Four steps** (in Claude Desktop, Code tab):

1. (get the project onto the computer)
2. (open the folder in the Code tab)
3. (type the sentence below)
4. (where to look for the result)

**Type this to Claude:**

    (the one sentence)

**What you get back** (real output, run on (date) on the sample in `(sample path)`):

    (the output, trimmed to the lines that matter)
```

## Rules

- **Real output only.** The "What you get back" block holds only output you got by actually running the sentence in this session. Do not write what the output "should" look like. Do not copy an output block from elsewhere in the README without running it again.
- **If you could not run it, say so in the section.** Replace the output block with one line: `Not run yet: (reason). Run the sentence above and paste the result here.` Tell the user the same thing in your reply. A section that admits it was not run is fine; a made-up output is not.
- **Trim, do not edit.** You may cut the output down to the lines that matter and mark the cut with `...`. Do not reword, tidy or "fix" what the tool printed.
- **No private details in the output.** Before pasting, remove absolute paths, user names and anything that looks like a key or token. Replace each with a short placeholder such as `<your folder>`.
- **Plain words.** No jargon the reader would need the project to understand. If a term is unavoidable, explain it in the same sentence.
- **Exactly four steps and exactly one sentence.** If the project needs more than that to get a first result, say so to the user: that is a problem with the project's first run, not something to hide in the README.
- **Do not promise.** Describe what happened in the run. Do not write "always", "guaranteed" or "automatically" about results.
- **Touch nothing else.** Do not reorder, reword or delete other parts of the README. If something else in it is wrong, tell the user; do not fix it unasked.

## When you are done, report

- The sentence you chose.
- Whether the output block is from a real run, and on which sample.
- Anything you removed from the output (paths, names).
- Anything in the README that contradicts what you saw when you ran it.
