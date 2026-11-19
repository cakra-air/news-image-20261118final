# World News — 18 November 2026 (V1: front page)

One-image summary of the world's news for Wednesday 18 November 2026.
A newspaper front-page poster with 3 captioned leads (clippings of the day's
main stories) and 38 stories across 7 regions.

- `main.py` — renders the poster offline to `/output/entry.png` (or `$MAKEFUN_OUTPUT`).
- Deterministic: no network, no randomness, no clock. Two runs produce identical bytes.
- Output: PNG, 1024 x 1024, ~138 KB.

News was collected during the agent session from Reuters, AFP, AP, BBC,
Xinhua, France 24, Al Jazeera, The Guardian, CNN and NPR, then embedded as
data in `main.py` (the sandbox has no network).

Sources used: The Hindu (top news of the day), Xinhua Daily World Briefing,
Zhudong daily world news, AllAfrica, Latin American Examiner, Rio Times,
GlobalsConflicts, Saachi Baat, Izvestia.
