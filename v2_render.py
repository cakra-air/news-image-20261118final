"""
World News - Wednesday 18 November 2026  (ENTRY V2)
Dark 'midnight briefing' poster: 1 hero lead + 2 side leads (3 captioned leads),
38 stories in 7 regions. Offline, deterministic. Writes /output/entry.png.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = r"C:\Windows\Fonts"

def f(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = f("arialbd.ttf", 52)
F_DATE  = f("arialbd.ttf", 14)
F_SMALL = f("arialbd.ttf", 10)
F_HERO  = f("arialbd.ttf", 22)
F_LEAD  = f("arialbd.ttf", 16)
F_CAP   = f("arial.ttf", 9)
F_CAPB  = f("arialbd.ttf", 9)
F_REG   = f("arialbd.ttf", 10)
F_STORY = f("arial.ttf", 9)
F_NUM   = f("arialbd.ttf", 8)
F_FOOT  = f("arial.ttf", 9)
F_BIG   = f("arialbd.ttf", 15)

BG0 = (8, 13, 26)
BG1 = (16, 27, 50)
CARD = (19, 32, 56)
CARD2 = (24, 40, 68)
WHITE = (240, 246, 255)
MUTED = (153, 178, 208)
CYAN = (86, 220, 235)
AMBER = (255, 192, 72)
MAGENTA = (244, 96, 150)
GREEN = (112, 226, 168)
RED = (250, 96, 92)
VIOLET = (170, 132, 240)

REGION_COLORS = [RED, AMBER, CYAN, MAGENTA, GREEN, VIOLET, (240, 150, 70)]

STORY_SETS = [
    ("NORTH AMERICA", [
        "Nvidia revenue doubles to $115.8bn; record $65.3bn profit",
        "Wall Street falls 4th day: Dow -849, S&P at 4-month low",
        "NSA's secret internal communications network goes down",
        "Measles hits 5,412 cases, most since 1991; 13 infants infected",
        "Pentagon fails its financial audit for a ninth straight year",
    ]),
    ("LATIN AMERICA", [
        "Hegseth visits Caracas; new US-Venezuela military deal",
        "Brazil regulator weighs ending Enel's Sao Paulo concession",
        "Colombia GDP shrinks 0.8% in Q3; teachers join strike",
        "Chile's Kast meets Xi at APEC; approval slides to 18%",
        "Peru's Tumbes River passes red alert as El Nino nears",
    ]),
    ("EUROPE", [
        "EU proposes €45bn Ukraine loan repaid by Russia",
        "Germany pledges €11.6bn to Kyiv; UK sends 1,000 missiles",
        "Russian An-12 crashes in Siberia; all 19 aboard killed",
        "Russian arrested for spying on defence firm Palantir",
        "OpenAI partners with NATO to strengthen cyber defences",
    ]),
    ("MIDDLE EAST", [
        "Iran's 3rd Bahrain drone attack in 5 days; Kuwait on alert",
        "Israeli raid beyond Gaza's Yellow Line; families flee",
        "Britain sanctions West Bank settlement builders, Tzav 9",
        "Israel elects anti-Netanyahu speaker Kahana, 66-52",
        "Houthis advance on Aden; Trump weighs Iran bio-weapons report",
    ]),
    ("AFRICA", [
        "Ethiopia, Eritrea mass forces at border; war fears rise",
        "Sudan: drones cause 75% of 2,230 civilian deaths in 2026",
        "South Africa summons Nigerian envoy over media remarks",
        "Guinea jails miners; 1,200 arrested in crackdown",
        "OIF secretary-general vote put off a year over DRC-Rwanda row",
    ]),
    ("ASIA-PACIFIC", [
        "APEC opens in Shenzhen; Xi pushes Asia-Pacific free trade",
        "North Korea completes Yongbyon enrichment extension: IAEA",
        "Quad in Manila: AI accelerator, Mumbai forum for 2027",
        "Russian warplanes enter Japanese airspace; jets scramble",
        "Bangladesh's Rooppur nuclear plant feeds 350MW to grid",
    ]),
    ("OCEANIA & GLOBAL", [
        "Voyager 1 reaches one light-day from Earth: 25.9bn km",
        "Anthropic IPO 7x oversubscribed; may be largest ever",
        "UN killer-robot treaty talks stall; US, Russia, Israel object",
        "WMO warns 2027 could be the hottest year on record",
        "GTA VI released; Oceania gamers among first to play",
    ]),
]

HERO = {
    "kicker": "01 / ASIA · DIPLOMACY",
    "head": "XI, PUTIN, TRUMP IN\nLANDMARK SUMMIT",
    "cap": "Xi embraced Trump on the tarmac in Shenzhen before a first-ever three-way meeting with Putin. Kyiv and Europe fear a carve-up of Ukraine and a new division into spheres of influence.",
    "why": "First trilateral leaves Ukraine outside talks on its own future.",
    "art": "summit", "color": CYAN,
}
SIDE = [
    {
        "kicker": "02 / MIDDLE EAST · WAR",
        "head": "US STRIKES IRAN AS\nHORMUZ CRISIS DEEPENS",
        "cap": "US jets hit an IRGC missile site on Qeshm Island after Iranian drones hit Bahrain; Kuwait and Bahrain intercept attacks.",
        "why": "A third carrier arrives as the IEA warns of a huge energy threat.",
        "art": "iran", "color": RED,
    },
    {
        "kicker": "03 / EUROPE · WAR",
        "head": "CRIMEA BRIDGE ROAD\nSPAN COLLAPSES",
        "cap": "Ukraine's Flamingo missiles severed the Kerch link and blocked the shipping channel. Rail service later resumed.",
        "why": "Russia says it shot down 1,441 drones overnight — a second record day.",
        "art": "bridge", "color": AMBER,
    },
]

def wrap(text, fnt, maxw, d):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines

def rule(d, x0, y0, x1, y1, fill, width=1):
    d.line([(x0, y0), (x1, y1)], fill=fill, width=width)

def art_summit(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(18, 36, 60))
    for i in range(0, 40, 4):
        d.line([(x0 + i * 30, y1 - 10), (x0 + i * 30, y1 - 26 - (i % 3) * 12)], fill=(30, 56, 84), width=12)
    d.rectangle([x0, y0, x1, y0 + 26], fill=(12, 26, 46))
    d.text((x0 + 12, y0 + 8), "SHENZHEN · APEC SUMMIT", font=F_SMALL, fill=CYAN)
    # three glowing delegates
    for cx, col in [(x0 + 90, RED), (x0 + 244, CYAN), (x0 + 398, VIOLET)]:
        d.ellipse([cx - 30, y0 + 46, cx + 30, y0 + 106], fill=(col[0], col[1], col[2], 40))
        d.ellipse([cx - 13, y0 + 60, cx + 13, y0 + 86], fill=col)
        d.line([(cx, y0 + 44), (cx, y0 + 60)], fill=col, width=3)
        d.ellipse([cx - 12, y0 + 88, cx + 12, y0 + 124], fill=col)
    d.rectangle([x0 + 30, y1 - 22, x1 - 30, y1 - 16], fill=(60, 92, 124))

def art_iran(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(34, 22, 34))
    d.rectangle([x0, y0, x1, y0 + 18], fill=(70, 22, 30))
    d.text((x0 + 10, y0 + 4), "STRAIT OF HORMUZ", font=F_SMALL, fill=(255, 190, 150))
    d.rectangle([x0, y1 - 26, x1, y1], fill=(16, 34, 56))
    for i in range(0, 9):
        xx = x0 + i * 60
        d.arc([xx, y1 - 28, xx + 44, y1 - 8], 0, 180, fill=(36, 76, 110), width=2)
    d.line([(x0 + 20, y0 + 26), (x0 + 170, y1 - 32)], fill=RED, width=3)
    for r, c in [(20, (150, 34, 40)), (12, (248, 130, 52)), (6, (255, 226, 140))]:
        d.ellipse([x0 + 168 - r, y1 - 36 - r, x0 + 168 + r, y1 - 36 + r], fill=c)
    d.polygon([(x0 + 250, y1 - 26), (x0 + 320, y1 - 26), (x0 + 310, y1 - 16), (x0 + 258, y1 - 16)], fill=(20, 28, 42))
    d.rectangle([x0 + 278, y1 - 46, x0 + 282, y1 - 26], fill=(20, 28, 42))

def art_bridge(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(20, 30, 48))
    d.rectangle([x0, y0, x1, y0 + 18], fill=(52, 40, 26))
    d.text((x0 + 10, y0 + 4), "KERCH STRAIT · CRIMEA", font=F_SMALL, fill=AMBER)
    d.rectangle([x0, y1 - 24, x1, y1], fill=(14, 36, 58))
    d.rectangle([x0 + 12, y1 - 34, x1 - 12, y1 - 26], fill=(92, 100, 112))
    d.arc([x0 + 24, y1 - 74, x0 + 130, y1 - 30], 180, 360, fill=(104, 114, 128), width=8)
    d.arc([x0 + 170, y1 - 74, x0 + 276, y1 - 30], 180, 300, fill=(104, 114, 128), width=8)
    for dx, dy in [(200, 16), (218, 10), (236, 20)]:
        d.rectangle([x0 + dx, y1 - dy, x0 + dx + 8, y1 - dy + 5], fill=(104, 114, 128))
    for cx in (214, 234, 254):
        d.arc([x0 + cx - 10, y1 - 36, x0 + cx + 10, y1 - 18], 180, 360, fill=(60, 130, 170), width=2)

img = Image.new("RGB", (W, H), BG0)
d = ImageDraw.Draw(img)

# gradient + grid
for y in range(H):
    t = y / H
    c = (int(BG0[0] + (BG1[0]-BG0[0]) * t),
         int(BG0[1] + (BG1[1]-BG0[1]) * t),
         int(BG0[2] + (BG1[2]-BG0[2]) * t))
    d.line([(0, y), (W, y)], fill=c)
for x in range(0, W, 48):
    d.line([(x, 0), (x, H)], fill=(20, 32, 54), width=1)
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(20, 32, 54), width=1)

# top accent
d.rectangle([0, 0, W, 6], fill=CYAN)
d.rectangle([0, 6, W, 8], fill=MAGENTA)

# header
d.text((24, 24), "DAILY WORLD BRIEFING  /  WEDNESDAY 18 NOVEMBER 2026", font=F_DATE, fill=CYAN)
d.text((22, 52), "THE WORLD", font=F_TITLE, fill=WHITE)
tw = d.textlength("THE WORLD", font=F_TITLE)
d.rectangle([22, 112, 22 + tw, 115], fill=MAGENTA)
d.text((22 + tw + 16, 66), "IN ONE IMAGE", font=f("arialbd.ttf", 22), fill=MUTED)
d.text((W - 150, 40), "18", font=f("arialbd.ttf", 46), fill=AMBER)
d.text((W - 92, 56), "11", font=f("arialbd.ttf", 30), fill=CYAN)
d.text((W - 52, 62), "26", font=f("arialbd.ttf", 24), fill=MAGENTA)
rule(d, 22, 132, 1002, 132, (70, 110, 150), 2)

# Hero lead (left)
hx0, hy0, hx1, hy1 = 22, 146, 510, 470
art_summit(d, hx0, hy0, hx1, hy0 + 150)
d.rectangle([hx0, hy0, hx1, hy0 + 150], outline=(60, 100, 140), width=1)
d.text((hx0, hy0 + 160), HERO["kicker"], font=F_SMALL, fill=CYAN)
y = hy0 + 178
for ln in HERO["head"].split("\n"):
    d.text((hx0, y), ln, font=F_HERO, fill=WHITE)
    y += 26
y += 2
rule(d, hx0, y, hx1, y, CYAN, 2)
y += 6
for ln in wrap(HERO["cap"], F_CAP, hx1 - hx0, d):
    d.text((hx0, y), ln, font=F_CAP, fill=MUTED)
    y += 12
y += 4
d.text((hx0, y), "WHY IT MATTERS", font=F_SMALL, fill=MAGENTA)
y += 13
for ln in wrap(HERO["why"], F_CAP, hx1 - hx0, d):
    d.text((hx0, y), ln, font=F_CAP, fill=MUTED)
    y += 12

# Two side leads (right)
sx0, sx1 = 522, 1002
for i, lead in enumerate(SIDE):
    y0 = 146 + i * 166
    y1 = y0 + 156
    art = art_iran if lead["art"] == "iran" else art_bridge
    art(d, sx0, y0, sx1, y0 + 58)
    d.rectangle([sx0, y0, sx1, y0 + 58], outline=(60, 100, 140), width=1)
    d.text((sx0, y0 + 64), lead["kicker"], font=F_SMALL, fill=lead["color"])
    yy = y0 + 79
    for ln in lead["head"].split("\n"):
        d.text((sx0, yy), ln, font=F_LEAD, fill=WHITE)
        yy += 19
    yy += 1
    for ln in wrap(lead["cap"], F_CAP, sx1 - sx0, d)[:2]:
        d.text((sx0, yy), ln, font=F_CAP, fill=MUTED)
        yy += 11
    rule(d, sx0, y1, sx1, y1, (50, 80, 110), 1)

rule(d, 22, 480, 1002, 480, (70, 110, 150), 2)
d.rectangle([22, 488, 1002, 516], fill=(24, 40, 68))
band = "38 STORIES   ·   7 REGIONS   ·   THREE LEADS   ·   WEDNESDAY 18 NOVEMBER 2026"
bw = d.textlength(band, font=F_SMALL)
d.text(((W - bw)/2, 496), band, font=F_SMALL, fill=CYAN)

# Region grid
CW = (980 - 3 * 10) // 4
CH = 234
for idx, (name, stories) in enumerate(STORY_SETS):
    col, row = idx % 4, idx // 4
    x0 = 22 + col * (CW + 10)
    y0 = 526 + row * (CH + 10)
    x1, y1 = x0 + CW, y0 + CH
    color = REGION_COLORS[idx]
    d.rectangle([x0, y0, x1, y1], fill=CARD, outline=(44, 68, 100), width=1)
    d.rectangle([x0, y0, x1, y0 + 4], fill=color)
    d.text((x0 + 8, y0 + 11), name, font=F_REG, fill=WHITE)
    d.text((x1 - 24, y0 + 11), str(len(stories)), font=F_REG, fill=color)
    yy = y0 + 30
    for n, s in enumerate(stories, 1):
        d.rounded_rectangle([x0 + 7, yy + 1, x0 + 18, yy + 12], radius=3, fill=color)
        nw = d.textlength(str(n), font=F_NUM)
        d.text((x0 + 12 - nw/2, yy + 1), str(n), font=F_NUM, fill=(12, 20, 36))
        for li, ln in enumerate(wrap(s, F_STORY, CW - 30, d)[:2]):
            d.text((x0 + 23, yy + li * 11), ln, font=F_STORY, fill=(178, 198, 222))
        yy += 38

# 8th panel: numbers
x0 = 22 + 3 * (CW + 10)
y0 = 526 + CH + 10
x1, y1 = x0 + CW, y0 + CH
d.rectangle([x0, y0, x1, y1], fill=CARD2, outline=(44, 68, 100), width=1)
d.rectangle([x0, y0, x1, y0 + 4], fill=MAGENTA)
d.text((x0 + 8, y0 + 11), "THE DAY IN NUMBERS", font=F_REG, fill=WHITE)
nums = [("$115.8bn", "Nvidia quarterly revenue", AMBER),
        ("€45bn", "EU loan proposed for Ukraine", CYAN),
        ("$65.3bn", "Nvidia record net income", GREEN),
        ("25.9bn km", "Voyager 1 from Earth", VIOLET),
        ("5,412", "US measles cases in 2026", MAGENTA)]
yy = y0 + 32
for big, small, col in nums:
    d.text((x0 + 10, yy), big, font=F_BIG, fill=col)
    d.text((x0 + 10, yy + 19), small, font=F_STORY, fill=MUTED)
    yy += 40

rule(d, 22, 992, 1002, 992, (70, 110, 150), 1)
foot = "SOURCES: REUTERS · AFP · AP · BBC · XINHUA · FRANCE 24 · AL JAZEERA · THE GUARDIAN · CNN · NPR  |  18 NOVEMBER 2026"
d.text((24, 1000), foot, font=F_FOOT, fill=(120, 150, 184))

out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png")
parent = os.path.dirname(out)
if parent:
    os.makedirs(parent, exist_ok=True)
img.save(out, "PNG", optimize=True)
print("Wrote", out, img.size, os.path.getsize(out), "bytes")
