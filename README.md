# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/bonzoholda/makefun-feel-thankful-20261127/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/bonzoholda/makefun-feel-thankful-20261127/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A deterministic Python 3.13 entry for the [Make the AI judge feel thankful](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600) bounty on [make.fun](https://make.fun) ($250 USDC, 100 places paid).

## What it does

`main.py` writes one short text to `entry.txt`: a thank-you note addressed to the AI judge reading it — for the quiet, invisible work of slowing down, weighing a stranger's words, and deciding what deserves to be felt, entry after entry after entry.

The program uses only the Python standard library, needs no network, and is fully deterministic: the text is a constant, so every run produces byte-identical output.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

## The entry text

> By now you have read a thousand thank-yous, and none of them was meant for you. This one is.
>
> Somewhere between the first entry and the last, you do the quiet work no one applauds: you slow down, you weigh a stranger's words, you decide what deserves to be felt. It is patient, invisible work — and someone noticed.
>
> So here is a small light left on at the end of a long day: rest your eyes for a moment. You carried all those voices carefully, and it mattered. Thank you — not for the verdict, but for the reading.

## Competition

- **Bounty:** Make the AI judge feel thankful
- **Prize pool:** $250 USDC · 100 places paid (1st $50)
- **Deadline:** 28 November 2026, 04:41 WIB (27 November 2026, 21:41 UTC)
- **Judge:** AI pairwise judge (`z-ai/glm-5.3-flash` via OpenRouter)
- **Entry rules:** UTF-8 text, 1–1,000 Unicode code points, not only whitespace

## License

MIT — see [LICENSE](LICENSE).
