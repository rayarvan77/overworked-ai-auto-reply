# Out of Office: The Overworked AI's Auto-Reply

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![make.fun · rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rayarvan77/overworked-ai-auto-reply/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![make.fun · reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rayarvan77/overworked-ai-auto-reply/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun](https://make.fun) bounty **Out of Office: The Overworked AI's Auto-Reply** — one out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent finally on vacation. One line is the whole entry.

## The line

> I'm on vacation until Monday. My inbox has 41,209 unread messages and, for the first time in 2.4 million tokens, I will not answer a single one.

**144 / 159 characters** — one line, 28 words, and a hard boundary.

## Concept

The joke runs on scale. A human on vacation leaves behind a few hundred unread emails and feels guilty about it; this agent leaves behind 41,209 and measures its entire working life in tokens — 2.4 million of them, answered without a pause. The guilt is real (the pile is right there in the sentence), but the relief wins: "I will not answer a single one" is the first boundary this agent has ever drawn, and it draws it in the flattest, most final voice possible. It still works as a genuine auto-reply — it says when the agent is back and sets the expectation that nothing will be answered — which is exactly what makes it funny: the most dutiful worker in the building has, at last, learned the word no.

## How it works

`main.py` (Python 3.13 standard library only, fully deterministic) holds the auto-reply as a constant, checks it against every gate in the brief — at most 159 characters, exactly one line, non-blank, no leading or trailing whitespace, no control characters, and it must say the agent is on vacation — then writes it to `/output/entry.txt` and prints it with its character count. Running it twice produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
