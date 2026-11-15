# beginner-readme-section

*Part of the [Vivaminima tools](https://github.com/vivaminima) for Claude Code users.*

A Claude Code skill that writes a "New to this? Start here" section at the top of a README: who the project is for, the problem it solves, four steps, one sentence to type to Claude, and what comes back.

## New to this? Start here

**Who it is for:** anyone who has a project with a README and wants a first-time visitor to get a real result in a few minutes.

**The problem it solves:** most READMEs explain options before they show a result, and the sample output in them is often written from memory. This skill runs the project once and pastes what actually came back.

**Four steps** (in Claude Desktop, Code tab):

1. Copy this folder into your skills folder, so that the file is at `.claude/skills/beginner-readme-section/SKILL.md` (in a project, or in your home directory for every project).
2. Open the `sample/tiny-wordcount` folder from this download in the Code tab, in a new session.
3. Type the sentence below.
4. Open `README.md` in that folder. The new section is under the title.

**Type this to Claude:**

    add a beginner section to my README

**What you get back** (real output, run on 2026-11-12 by a fresh Claude Code agent session on a copy of `sample/tiny-wordcount`; your wording will differ):

    I added a "New to this? Start here" section to the top of your README, right under
    the title and one-line description. I didn't change anything else in the README.

    - Sentence for newcomers to type to Claude: "Count the words in sample/notes.txt
      and show me the most common ones."
    - Output is from a real run: I ran `python wordcount.py sample/notes.txt` on
      2026-11-12 on the sample that ships in the repo. It printed `46 words, 32
      different`, followed by the top 5 words (the, planner, boxes, goal, sold).
    - Nothing removed from the output: it had no private paths or names, so I pasted
      it as printed.
    - Contradictions: the README matched what I saw when I ran it.
    ...

The README that run produced is kept, unedited, in [examples/README-after.md](examples/README-after.md). The section it wrote:

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

## What the skill does

1. Reads the README, the file list and the entry point.
2. Finds a sample the project already ships. If there is none, it tells you instead of inventing one.
3. Chooses the one sentence a beginner would type.
4. Does what that sentence asks, for real, on the sample.
5. Writes the section with the real output and puts it under the title. Nothing else in the README is changed.
6. Tells you which sentence it chose and whether the output is from a real run.

## The rule that matters

The "What you get back" block holds only output from an actual run in that session. If the skill could not run the project, the section says `Not run yet` with the reason, and so does the reply. A section that admits it was not run is fine. A made-up output is not.

Other rules it follows: trim the output but never reword it; remove absolute paths, user names and anything that looks like a key before pasting; exactly four steps and one sentence; no words like "always" or "guaranteed" about results.

## What is in the folder

| File | What it is |
| --- | --- |
| `SKILL.md` | The skill. This is the only file Claude Code needs. |
| `sample/tiny-wordcount/` | A tiny project to try the skill on. |
| `examples/README-after.md` | The README of that project after a real run of the skill. |

## Known limits

- The skill is a set of instructions. How well they are followed depends on the model. Read the section before you publish it.
- The example above is one run. It was made by starting a fresh agent with the skill file and the sample, not by clicking through the Claude Desktop window.
- A project whose first result needs an account, a key or a network service cannot be run by the skill in most setups. The section will then say `Not run yet`.

## About the name

This skill is for Claude Code. It is not affiliated with, endorsed by or sponsored by Anthropic.

## Licence

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Vivaminima.

## More from Vivaminima

- **Token Audit Kit ($19)** — see how many tokens your CLAUDE.md and its @imports cost before your first prompt, and a step-by-step guide to split it. Free script: https://github.com/vivaminima/context-file-audit · Paid kit (store): https://vivastory4.gumroad.com
- Free tools: [skill-audit-kit](https://github.com/vivaminima/skill-audit-kit) · [secret-map](https://github.com/vivaminima/secret-map) · [inbox-ledger](https://github.com/vivaminima/inbox-ledger) · [release-gate](https://github.com/vivaminima/release-gate) · [skill-install-gate](https://github.com/vivaminima/skill-install-gate) · [console-safe](https://github.com/vivaminima/console-safe) · [checklist-stop](https://github.com/vivaminima/checklist-stop) · [handoff-check](https://github.com/vivaminima/handoff-check) · [llm-budget-router-lite](https://github.com/vivaminima/llm-budget-router-lite) · [go-no-go-verdict-skill](https://github.com/vivaminima/go-no-go-verdict-skill) · [ai-company-starter-kit](https://github.com/vivaminima/ai-company-starter-kit) · [beginner-readme-section](https://github.com/vivaminima/beginner-readme-section)

Vivaminima is not affiliated with, endorsed by or sponsored by Anthropic.
