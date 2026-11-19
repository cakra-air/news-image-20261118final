# World News — 18 November 2026

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
