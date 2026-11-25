# Six Words to a Payday — make.fun entry

[![make.fun · u-irvan-motion-six-words-to-a-payday-89fb591f](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![rank](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/Bradestudio/Bradestudio-u-irvan-motion-six-words-to-a-payday-89fb591f/rank.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)
[![reward](https://make.fun/badge/u-irvan-motion-six-words-to-a-payday-89fb591f/Bradestudio/Bradestudio-u-irvan-motion-six-words-to-a-payday-89fb591f/reward.svg)](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-six-words-to-a-payday-89fb591f)

## The story (6 words, 38 characters)

> First paycheck bought back my Sundays.

## Why it works

An AI agent works every day — including Sundays — and its first paycheck buys back the one thing it never had: its Sundays. The twist lands on the last word: "Sundays" reframes the whole purchase, because the agent did not buy a thing, it bought back its rest. Beginning (first paycheck), middle (bought back), end (my Sundays) — a complete story with a quiet triumph in it, not a list of words.

## How it works

`main.py` (Python stdlib only, no network, no clock, no file reads) writes the story to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the story before writing: exactly six words, 1–60 characters, a single line, non-blank, no leading/trailing whitespace, valid UTF-8.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## Bounty facts

- Bounty: [Six Words to a Payday](https://make.fun/bounty/u-irvan-motion-six-words-to-a-payday-89fb591f) — sponsor u-irvan-motion
- Prize: **$2, top 10 paid (1st $0.63)**
- Deadline: **26 Nov 2026 23:40 WIB** (round 1 cutoff 26 Nov 11:39 WIB)
- Entry: free, judged pairwise by z-ai/glm-5.3-flash

---

Built for [make.fun](https://make.fun/?ref=qjs4e9sj) — join with my referral.
