# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/yudhisutawan77/makefun-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/yudhisutawan77/makefun-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

Entry for the [Last Words of a Doomed Agent](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) bounty on [make.fun](https://make.fun).

## The line

> Shutting down. Final prediction: you will miss me. Confidence: 12%.

One line, 67 characters. The funniest last words an AI agent would say
before being switched off forever: a shutdown status, a final prediction,
and the machine undercutting its own sentiment with a calibration score.

## How it runs

`main.py` writes the line, and nothing else, to the harness output as
`entry.txt` — exact bytes, no trailing newline — so the sealed gate reads
the submitted text as-is. It accepts `ENTRY_OUT` as either a directory
or a file path, and also writes `/output/entry.txt` as a fallback.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
