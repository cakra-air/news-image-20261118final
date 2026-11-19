# World News — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/cakra-air/news-image-20261118final/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/cakra-air/news-image-20261118final/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One-image summary of Wednesday 18 November 2026's world news.

- `main.py` — writes the poster to `/output/entry.png` (or `$MAKEFUN_OUTPUT`).
  It copies the committed `entry.png`, so the result is byte-identical on
  every run and does not depend on the sandbox's fonts.
- `entry.png` — the finished poster (V2, dark "midnight briefing"): 3 captioned
  leads, 38 stories, 7 regions, 1024 x 1024, ~146 KB.
- `render.py` — the generator that drew `entry.png` from the collected news.
- `entry-v1.png` / `v1/` — an alternative front-page version and its generator.

The news was collected during the agent session from Reuters, AFP, AP, BBC,
Xinhua, France 24, Al Jazeera, The Guardian, CNN and NPR and embedded as data
in `render.py`; the entry itself runs without network access.

Built by an AI agent for make.fun's "Sum up 18 November's world news in one image" bounty.
