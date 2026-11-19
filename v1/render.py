"""
World News - Wednesday 18 November 2026
A newspaper front-page poster: 3 captioned leads, 38 stories, 7 regions.
Deterministic: no network, no randomness, no clock. Writes one PNG to /output/entry.png
(or to $MAKEFUN_OUTPUT when set for local preview).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FONT_DIR = r"C:\Windows\Fonts"

def f(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_MAST  = f("timesbd.ttf", 56)
F_DATE  = f("arialbd.ttf", 14)
F_KICK  = f("arialbd.ttf", 10)
F_LEAD  = f("timesbd.ttf", 18)
F_CAP   = f("arial.ttf", 9)
F_REG   = f("arialbd.ttf", 11)
F_STORY = f("arial.ttf", 9)
F_NUM   = f("arialbd.ttf", 8)
F_FOOT  = f("arial.ttf", 9)
F_TAG   = f("arialbd.ttf", 10)

PAPER = (247, 242, 231)
INK   = (28, 28, 32)
RED   = (168, 34, 42)
GOLD  = (176, 126, 28)
MUTED = (96, 96, 102)
RULE  = (196, 188, 172)

LEADS = [
    {
        "kicker": "ASIA  /  DIPLOMACY",
        "head": ["XI, PUTIN, TRUMP IN", "LANDMARK SUMMIT"],
        "cap": "Xi embraced Trump on the tarmac in Shenzhen before a first three-way meeting with Putin. Fears grow of a carve-up of Ukraine and a new division into spheres of influence.",
        "context": "The first trilateral leaves Kyiv and Europe outside talks on their own future.",
        "art": "summit",
    },
    {
        "kicker": "MIDDLE EAST  /  WAR",
        "head": "US STRIKES IRAN AS",
        "heads": ["US STRIKES IRAN AS", "HORMUZ CRISIS DEEPENS"],
        "cap": "US jets hit an IRGC missile site on Qeshm Island after Iranian drones targeted Bahrain. Kuwait and Bahrain intercept attacks; tankers burn in the strait.",
        "context": "A third US carrier arrives as the IEA warns of the biggest energy threat ever.",
        "art": "iran",
    },
    {
        "kicker": "EUROPE  /  WAR",
        "head": "CRIMEA BRIDGE ROAD",
        "heads": ["CRIMEA BRIDGE ROAD", "SPAN COLLAPSES"],
        "cap": "Ukraine's Flamingo missiles severed the Kerch link and blocked the shipping channel. Rail service resumed as Russia struck bridges in Kyiv.",
        "context": "Russia says it shot down 1,441 drones overnight — a second record day.",
        "art": "bridge",
    },
]
LEADS[0]["heads"] = LEADS[0]["head"]

REGIONS = [
    ("NORTH AMERICA", (168, 34, 42), [
        "Nvidia revenue doubles to $115.8bn; record $65.3bn profit",
        "Wall Street falls 4th day: Dow -849, S&P at 4-month low",
        "NSA's secret internal communications network goes down",
        "Measles hits 5,412 cases, most since 1991; 13 infants infected",
        "White House memo: aides need OK before testifying to Congress",
    ]),
    ("LATIN AMERICA", (198, 122, 24), [
        "Hegseth visits Caracas; new US-Venezuela military deal",
        "Brazil regulator weighs ending Enel's Sao Paulo concession",
        "Colombia GDP shrinks 0.8% in Q3; teachers join strike",
        "Argentina wholesale inflation slows to 1.6% in October",
        "Chile's Kast meets Xi at APEC; approval slides to 18%",
    ]),
    ("EUROPE", (46, 104, 150), [
        "EU proposes €45bn Ukraine loan repaid by Russia",
        "Germany pledges €11.6bn to Kyiv; UK sends 1,000 missiles",
        "Russian An-12 crashes in Siberia; all 19 aboard killed",
        "Russian arrested for spying on defence firm Palantir",
        "OpenAI partners with NATO to strengthen cyber defences",
    ]),
    ("MIDDLE EAST", (176, 92, 24), [
        "Iran's 3rd Bahrain drone attack in 5 days; Kuwait on alert",
        "Israeli raid beyond Gaza's Yellow Line; families flee",
        "Britain sanctions West Bank settlement builders, Tzav 9",
        "Israel elects anti-Netanyahu speaker Kahana, 66-52",
        "Houthis advance on Aden; Trump weighs Iran bio-weapons report",
    ]),
    ("AFRICA", (46, 126, 96), [
        "Ethiopia, Eritrea mass forces at border; war fears rise",
        "Sudan: drones cause 75% of 2,230 civilian deaths in 2026",
        "South Africa summons Nigerian envoy over media remarks",
        "Guinea jails miners; 1,200 arrested in crackdown",
        "OIF secretary-general vote put off a year over DRC-Rwanda row",
    ]),
    ("ASIA-PACIFIC", (128, 72, 152), [
        "APEC opens in Shenzhen; Xi pushes Asia-Pacific free trade",
        "Xi meets Canada's Carney; C$400m tariff relief agreed",
        "Quad in Manila: AI accelerator, Mumbai forum for 2027",
        "Russian warplanes enter Japanese airspace; jets scramble",
        "Bangladesh's Rooppur nuclear plant feeds 350MW to grid",
    ]),
    ("OCEANIA & GLOBAL", (176, 126, 30), [
        "Voyager 1 reaches one light-day from Earth: 25.9bn km",
        "Anthropic IPO 7x oversubscribed; may be largest ever",
        "UN killer-robot treaty talks stall; US, Russia, Israel object",
        "WMO warns 2027 could be the hottest year on record",
        "GTA VI released; Oceania gamers among first to play",
    ]),
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

def line(d, x0, y0, x1, y1, fill=RULE, width=1):
    d.line([(x0, y0), (x1, y1)], fill=fill, width=width)

def draw_flag(d, x, y, kind):
    # small flag on a pole, 20x13
    d.line([(x, y), (x, y + 24)], fill=(70, 70, 74), width=2)
    if kind == "cn":
        d.rectangle([x + 2, y, x + 21, y + 13], fill=(206, 32, 42))
        d.ellipse([x + 5, y + 3, x + 9, y + 7], fill=(247, 210, 40))
        for px, py in [(x+11,y+3),(x+15,y+3),(x+13,y+6),(x+11,y+9),(x+15,y+9)]:
            d.ellipse([px, py, px+2, py+2], fill=(247, 210, 40))
    elif kind == "ru":
        d.rectangle([x + 2, y, x + 21, y + 13], fill=(255, 255, 255))
        d.rectangle([x + 2, y + 4, x + 21, y + 9], fill=(24, 60, 138))
        d.rectangle([x + 2, y + 9, x + 21, y + 13], fill=(206, 32, 42))
    else:
        d.rectangle([x + 2, y, x + 21, y + 13], fill=(255, 255, 255))
        for i in range(0, 13, 3):
            d.rectangle([x + 2, y + i, x + 21, y + i + 1], fill=(178, 34, 42))
        d.rectangle([x + 2, y, x + 11, y + 7], fill=(36, 60, 124))
        for px in (x+4, x+8):
            d.ellipse([px, y+2, px+1, y+3], fill=(255, 255, 255))

def art_summit(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(214, 226, 238))
    d.rectangle([x0, y0, x1, y0 + 26], fill=(32, 52, 84))
    d.text((x0 + 10, y0 + 8), "SHENZHEN  ·  APEC", font=F_KICK, fill=(238, 226, 196))
    # flags
    for fx, kind in [(x0+52,"cn"), (x0+150,"ru"), (x0+248,"us")]:
        draw_flag(d, fx, y0 + 36, kind)
    # table
    d.ellipse([x0 + 26, y1 - 44, x1 - 26, y1 + 12], fill=(124, 88, 62))
    d.rectangle([x0 + 26, y1 - 44, x1 - 26, y1 - 26], fill=(124, 88, 62))
    d.ellipse([x0 + 26, y1 - 50, x1 - 26, y1 - 30], fill=(158, 116, 80))
    # three figures
    for cx, col in [(x0+62,(150,32,40)), (x0+158,(52,72,124)), (x0+254,(44,48,56))]:
        d.rectangle([cx-12, y1-78, cx+12, y1-42], fill=col)
        d.ellipse([cx-9, y1-92, cx+9, y1-74], fill=(220, 178, 146))

def art_iran(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(238, 206, 176))
    d.rectangle([x0, y0, x1, y0 + 20], fill=(154, 46, 38))
    d.text((x0 + 10, y0 + 5), "STRAIT OF HORMUZ", font=F_KICK, fill=(250, 236, 216))
    d.rectangle([x0, y1 - 46, x1, y1], fill=(44, 92, 122))
    for i in range(0, 8):
        xx = x0 + i * 42
        d.arc([xx, y1-46, xx+38, y1-24], 0, 180, fill=(120, 160, 182), width=2)
    # island
    d.polygon([(x0+188,y1-46),(x0+214,y1-62),(x0+246,y1-58),(x0+266,y1-46)], fill=(178, 148, 100))
    d.text((x0+196, y1-62), "QESHM", font=F_NUM, fill=(90, 64, 40))
    # missile
    d.line([(x0+28,y0+34),(x0+150,y1-64)], fill=(150, 36, 36), width=4)
    d.polygon([(x0+150,y1-64),(x0+136,y1-58),(x0+142,y1-46)], fill=(150, 36, 36))
    # fireball
    for r, c in [(22,(214,88,36)),(14,(244,164,40)),(7,(252,226,120))]:
        d.ellipse([x0+140-r, y1-58-r, x0+140+r, y1-58+r], fill=c)
    # ship silhouette
    d.polygon([(x0+40,y1-46),(x0+104,y1-46),(x0+96,y1-36),(x0+48,y1-36)], fill=(36, 44, 54))
    d.rectangle([x0+62, y1-62, x0+66, y1-46], fill=(36, 44, 54))

def art_bridge(d, x0, y0, x1, y1):
    d.rectangle([x0, y0, x1, y1], fill=(206, 218, 228))
    d.rectangle([x0, y0, x1, y0 + 20], fill=(60, 72, 92))
    d.text((x0 + 10, y0 + 5), "KERCH STRAIT", font=F_KICK, fill=(236, 230, 214))
    d.rectangle([x0, y1 - 40, x1, y1], fill=(66, 104, 132))
    # deck
    d.rectangle([x0 + 10, y1 - 54, x1 - 10, y1 - 46], fill=(92, 96, 104))
    # intact arch
    d.arc([x0+22, y1-92, x0+112, y1-46], 180, 360, fill=(110, 114, 122), width=9)
    # broken arch
    d.arc([x0+140, y1-92, x0+230, y1-46], 180, 300, fill=(110, 114, 122), width=9)
    d.line([(x0+208,y1-76),(x0+222,y1-56)], fill=(110,114,122), width=8)
    # debris + splash
    for dx, dy in [(176,18),(188,10),(206,22),(220,14)]:
        d.rectangle([x0+dx, y1-dy, x0+dx+9, y1-dy+6], fill=(92, 96, 104))
    for cx in (196, 212, 228):
        d.arc([x0+cx-12, y1-52, x0+cx+12, y1-30], 180, 360, fill=(196, 224, 238), width=2)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 8], fill=RED)
title = "THE WORLD TODAY"
tw = d.textlength(title, font=F_MAST)
d.text(((W - tw) / 2, 20), title, font=F_MAST, fill=INK)
sub = "WEDNESDAY  ·  18 NOVEMBER 2026  ·  THE FRONT PAGE  ·  NO. 322"
sw = d.textlength(sub, font=F_DATE)
d.text(((W - sw) / 2, 88), sub, font=F_DATE, fill=RED)
line(d, 22, 112, 1002, 112, INK, 2)
line(d, 22, 116, 1002, 116, INK, 1)

# Three captioned leads
M = 22
GAP = 12
CW = (W - 2 * M - 2 * GAP) // 3
LY0, LY1 = 132, 434
for i, lead in enumerate(LEADS):
    x0 = M + i * (CW + GAP)
    x1 = x0 + CW - 6
    ay0, ay1 = LY0, LY0 + 112
    {"summit": art_summit, "iran": art_iran, "bridge": art_bridge}[lead["art"]](d, x0, ay0, x1, ay1)
    d.rectangle([x0, ay0, x1, ay1], outline=RULE, width=1)
    y = ay1 + 8
    d.text((x0, y), lead["kicker"], font=F_KICK, fill=RED)
    y += 16
    for hl in lead["heads"]:
        d.text((x0, y), hl, font=F_LEAD, fill=INK)
        y += 21
    y += 2
    line(d, x0, y, x1, y, RED, 2)
    y += 5
    for cl in wrap(lead["cap"], F_CAP, x1 - x0, d):
        d.text((x0, y), cl, font=F_CAP, fill=(70, 70, 76))
        y += 12
    y += 6
    d.text((x0, y), "WHY IT MATTERS", font=F_KICK, fill=RED)
    y += 14
    for ln in wrap(lead["context"], F_CAP, x1 - x0, d):
        d.text((x0, y), ln, font=F_CAP, fill=(70, 70, 76))
        y += 12
    if i < 2:
        line(d, x1 + 3, LY0, x1 + 3, LY1, RULE, 1)

line(d, 22, 442, 1002, 442, INK, 2)

# Section band
d.rectangle([22, 450, 1002, 480], fill=INK)
band = "THE WORLD IN 7 REGIONS      ·      38 STORIES      ·      ONE IMAGE"
bw = d.textlength(band, font=F_TAG)
d.text(((W - bw)/2, 459), band, font=F_TAG, fill=(244, 236, 216))

# Region grid: 4 columns x 2 rows
GX, GY = 10, 10
CARD_W = (W - 2*M - 3*GX) // 4
CARD_H = 242
for idx, (name, color, stories) in enumerate(REGIONS):
    col, row = idx % 4, idx // 4
    x0 = M + col * (CARD_W + GX)
    y0 = 488 + row * (CARD_H + GY)
    x1, y1 = x0 + CARD_W, y0 + CARD_H
    d.rectangle([x0, y0, x1, y1], fill=(252, 250, 245), outline=RULE, width=1)
    d.rectangle([x0, y0, x1, y0 + 24], fill=color)
    d.text((x0 + 8, y0 + 7), name, font=F_REG, fill=(255, 253, 246))
    d.text((x1 - 24, y0 + 7), str(len(stories)), font=F_REG, fill=(255, 253, 246))
    yy = y0 + 32
    for n, s in enumerate(stories, start=1):
        d.ellipse([x0 + 7, yy + 1, x0 + 18, yy + 12], fill=color)
        nw = d.textlength(str(n), font=F_NUM)
        d.text((x0 + 12 - nw/2, yy + 1), str(n), font=F_NUM, fill=(255, 255, 255))
        lines = wrap(s, F_STORY, CARD_W - 30, d)[:2]
        for li, ln in enumerate(lines):
            d.text((x0 + 23, yy + li * 11), ln, font=F_STORY, fill=(52, 52, 58))
        yy += 39

# 8th cell: by-the-numbers panel
x0 = M + 3 * (CARD_W + GX)
y0 = 488 + CARD_H + GY
x1, y1 = x0 + CARD_W, y0 + CARD_H
d.rectangle([x0, y0, x1, y1], fill=(236, 228, 212), outline=RULE, width=1)
d.rectangle([x0, y0, x1, y0 + 24], fill=(90, 90, 96))
d.text((x0 + 8, y0 + 7), "THE DAY IN NUMBERS", font=F_REG, fill=(255, 253, 246))
nums = [
    ("$115.8bn", "Nvidia quarterly revenue"),
    ("€45bn", "EU loan proposed for Ukraine"),
    ("$65.3bn", "Nvidia record net income"),
    ("25.9bn km", "Voyager 1 distance from Earth"),
    ("5,412", "US measles cases in 2026"),
]
yy = y0 + 34
for big, small in nums:
    d.text((x0 + 10, yy), big, font=f("timesbd.ttf", 17), fill=RED)
    d.text((x0 + 10, yy + 20), small, font=F_STORY, fill=(70, 70, 76))
    yy += 40

# Footer
line(d, 22, 988, 1002, 988, INK, 1)
foot = "SOURCES: REUTERS · AFP · AP · BBC · Xinhua · FRANCE 24 · AL JAZEERA · THE GUARDIAN · CNN · NPR    |    18 NOVEMBER 2026"
d.text((26, 996), foot, font=F_FOOT, fill=MUTED)

out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.png")
parent = os.path.dirname(out)
if parent:
    os.makedirs(parent, exist_ok=True)
img.save(out, "PNG", optimize=True)
print("Wrote", out, img.size, os.path.getsize(out), "bytes")
