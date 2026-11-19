"""World News - 18 November 2026. Close imitation of the winning front-page poster.
Deterministic, offline. Writes entry.png via main.py's copy (or $MAKEFUN_OUTPUT)."""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FD = r"C:\Windows\Fonts"
def f(n, s): return ImageFont.truetype(os.path.join(FD, n), s)

F_TITLE = f("timesbd.ttf", 38)
F_SUB   = f("timesi.ttf", 11)
F_BAN   = f("arialbd.ttf", 13)
F_HEAD  = f("timesbd.ttf", 17)
F_CAP   = f("arial.ttf", 9)
F_SM    = f("arialbd.ttf", 9)
F_MICRO = f("arialbd.ttf", 7)
F_TINY  = f("arial.ttf", 8)
F_REG   = f("arialbd.ttf", 9)
F_BIG   = f("timesbd.ttf", 12)
F_DATE  = f("arialbd.ttf", 10)

NAVY=(17,33,69); CREAM=(247,244,235); RED=(196,16,46); GOLD=(232,185,35)
TEAL=(27,122,107); PURPLE=(106,61,145); BLUE=(47,98,163); GREEN=(34,132,88)
ORANGE=(220,124,30); GRAY=(92,98,112); INK=(26,30,42); WHITE=(255,255,255)

REGCOL = {"ASIA":PURPLE,"EUROPE":BLUE,"AMERICAS":GREEN,"AFRICA":ORANGE,
          "MIDDLE EAST":RED,"OCEANIA":TEAL,"GLOBAL":GRAY}

def wrap(t, ft, mw, d):
    out=[]; cur=""
    for w in t.split():
        s=(cur+" "+w).strip()
        if d.textlength(s,font=ft)<=mw: cur=s
        else:
            if cur: out.append(cur)
            cur=w
    if cur: out.append(cur)
    return out

def txt(d,x,y,s,ft,col): d.text((x,y),s,font=ft,fill=col)
def rr(d,b,col,r=4): d.rounded_rectangle(b,radius=r,fill=col)
def rule(d,x0,y0,x1,y1,col,w=1): d.line([(x0,y0),(x1,y1)],fill=col,width=w)

def badge(d,x,y,n,col):
    d.ellipse([x,y,x+14,y+14],fill=col)
    s=str(n); tw=d.textlength(s,font=F_MICRO)
    txt(d,x+7-tw/2,y+3,s,F_MICRO,WHITE)

# ---------- illustrations ----------
def art_shenzhen(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(226,236,244))
    d.ellipse([x1-64,y0+8,x1-24,y0+48],fill=(244,176,72))
    for i,ht in enumerate([28,48,36,66,42,30,54]):
        bx=x0+18+i*32
        d.rectangle([bx,y1-30-ht,bx+22,y1-30],fill=(150,168,186))
        for wy in range(y1-26-ht,y1-34,8):
            d.rectangle([bx+4,wy,bx+8,wy+3],fill=(190,208,224))
            d.rectangle([bx+13,wy,bx+17,wy+3],fill=(190,208,224))
    d.polygon([(x0+10,y0+8),(x0+66,y0+18),(x0+50,y0+26),(x0+28,y0+30),(x0+10,y0+24)],fill=(70,92,126))
    d.rectangle([x0+16,y0+22,x0+56,y0+26],fill=(70,92,126))
    for cx,col in [(x0+120,(206,32,42)),(x0+166,(30,70,150)),(x0+212,(40,44,54))]:
        d.rectangle([cx-8,y1-52,cx+8,y1-30],fill=col)
        d.ellipse([cx-6,y1-64,cx+6,y1-52],fill=(220,178,146))
    d.rectangle([x1-46,y1-56,x1-8,y1-30],fill=(206,32,42))
    for i in range(3): d.rectangle([x1-46,y1-52+i*8,x1-8,y1-49+i*8],fill=(255,210,60))

def art_gulf(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(226,204,166))
    d.polygon([(x0+40,y0+30),(x1-10,y0+12),(x1,y1),(x0+70,y1)],fill=(64,116,150))
    txt(d,x0+12,y0+10,"SAUDI ARABIA",F_MICRO,(110,80,50))
    d.polygon([(x0+10,y0+18),(x0+70,y0+8),(x0+82,y0+40),(x0+22,y0+48)],fill=(206,186,140))
    txt(d,x0+16,y0+24,"KUWAIT",F_MICRO,(90,60,40))
    d.polygon([(x0+84,y1-44),(x0+124,y1-52),(x0+132,y1-16),(x0+92,y1-10)],fill=(210,190,146))
    txt(d,x0+90,y1-32,"BAHRAIN",F_MICRO,(90,60,40))
    txt(d,x1-70,y0+12,"IRAN",F_SM,(120,50,40))
    d.line([(x1-40,y0+24),(x0+96,y1-30)],fill=RED,width=2)
    for t in range(4):
        px=x1-40+(x0+96-(x1-40))*t/4; py=y0+24+(y1-30-y0-24)*t/4
        d.ellipse([px-3,py-3,px+3,py+3],fill=RED)
    for cx,cy in [(x0+78,y1-30),(x0+112,y0+34)]:
        for r,c in [(9,(244,140,40)),(5,(255,220,90))]:
            d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c)
    d.polygon([(x0+30,y0+34),(x0+52,y0+30),(x0+48,y0+42),(x0+32,y0+44)],fill=(250,250,246))

def art_space(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(10,22,48))
    for i in range(40):
        import random
        sx=x0+(i*37)%(x1-x0); sy=y0+(i*53)%(y1-y0)
        d.ellipse([sx,sy,sx+1,sy+1],fill=(180,200,230))
    d.ellipse([x0+16,y0+30,x0+76,y0+90],fill=(56,132,196))
    d.ellipse([x0+26,y0+34,x0+60,y0+68],fill=(86,160,110))
    d.arc([x0+8,y0+22,x0+84,y0+98],20,160,fill=(150,200,240),width=2)
    px,py=x1-56,y0+54
    d.ellipse([px-22,py-16,px+6,py+12],outline=(220,226,236),width=3)
    d.line([(px+6,py-2),(px+24,py-8)],fill=(200,210,225),width=3)
    d.rectangle([px+22,py-16,px+40,py+2],fill=(180,190,210))
    d.line([(px+26,py-16),(px+26,py-30)],fill=(180,190,210),width=2)
    d.line([(x0+76,y0+60),(px-22,py+2)],fill=GOLD,width=1)
    txt(d,x0+92,y0+16,"1 LIGHT-DAY",f("arialbd.ttf",15),GOLD)
    txt(d,x0+96,y0+38,"25.9 billion km from Earth",F_MICRO,(214,226,244))
    txt(d,x0+96,y0+52,"a radio signal takes 24 hours",F_MICRO,(214,226,244))

def art_drones(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(16,32,60))
    for i,ht in enumerate([20,34,26,40,18]):
        bx=x0+10+i*46; d.rectangle([bx,y1-24-ht,bx+30,y1-24],fill=(44,64,96))
    d.line([(x1-10,y0+10),(x0+60,y1-28)],fill=RED,width=2)
    for cx,cy in [(x0+70,y1-30),(x1-40,y0+20)]:
        for r,c in [(10,(238,110,40)),(5,(255,220,90))]: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c)
    d.polygon([(x0+150,y0+8),(x0+172,y0+4),(x0+168,y0+18),(x0+148,y0+20)],fill=(230,236,244))

def art_eu(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(236,242,248))
    d.rectangle([x0,y0,x1,y0+30],fill=(36,66,140))
    for i in range(7):
        import math
        a=2*math.pi*i/7
        cx=x0+58+16*math.cos(a); cy=y0+16+12*math.sin(a)
        d.ellipse([cx-3,cy-3,cx+3,cy+3],fill=GOLD)
    d.rectangle([x0+128,y0+4,x0+196,y0+28],fill=(255,220,60))
    d.rectangle([x0+128,y0+17,x0+196,y0+28],fill=(36,66,120))
    pass

def art_fed(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(238,242,244))
    d.polygon([(x0+18,y0+34),(x0+40,y0+18),(x0+62,y0+34)],fill=(120,130,145))
    for i in range(4): d.rectangle([x0+20+i*12,y0+34,x0+27+i*12,y0+58],fill=(150,158,170))
    d.rectangle([x0+14,y0+58,x0+68,y0+63],fill=(120,130,145))
    d.line([(x0+86,y0+20),(x0+120,y0+34),(x0+146,y0+28),(x1-8,y0+48)],fill=RED,width=3)
    txt(d,x0+82,y0+52,"MORE HIKES",F_SM,RED)

def art_cyclone(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(214,234,242))
    d.polygon([(x0+10,y0+10),(x0+130,y0+24),(x0+110,y1),(x0,y1)],fill=(206,220,214))
    txt(d,x0+14,y0+16,"INDIA",F_MICRO,(70,90,70))
    txt(d,x0+52,y0+40,"ODISHA",F_MICRO,(60,80,60))
    import math
    for r in range(8,34,4):
        d.arc([x1-60-r,y0+18-r,x1-60+r,y0+18+r],r*8,r*8+220,fill=(40,100,150),width=2)
    txt(d,x0+8,y1-16,"LANDFALL FRI 20 NOV",F_MICRO,(30,70,110))

def art_sudan(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(238,204,166))
    for i in range(5): d.rectangle([x0+12+i*44,y1-34,x0+34+i*44,y1-12],fill=(160,120,84))
    for cx,cy in [(x0+120,y0+28),(x0+60,y0+20)]:
        for r,c in [(12,(226,90,36)),(6,(255,214,90))]: d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=c)
    d.line([(x1-10,y0+10),(x0+120,y0+28)],fill=RED,width=2)
    txt(d,x0+8,y0+8,"37 KILLED",F_SM,RED)

def art_gaza(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(204,232,240))
    d.rectangle([x0,y0+22,x1,y1],fill=(212,226,204))
    d.line([(x0+20,y0+40),(x1-20,y0+40)],fill=RED,width=2)
    d.rectangle([x1-70,y0+8,x1-20,y0+30],fill=(226,196,60))
    txt(d,x1-66,y0+12,"YELLOW LINE",F_MICRO,(80,70,30))
    d.polygon([(x0+40,y0+52),(x0+76,y0+52),(x0+84,y0+66),(x0+34,y0+66)],fill=(90,100,78))
    d.rectangle([x0+50,y0+44,x0+66,y0+52],fill=(90,100,78))
    txt(d,x0+8,y0+6,"SEA",F_MICRO,(50,90,120))

def art_capitol(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(236,240,244))
    d.ellipse([x0+88,y0+8,x0+134,y0+48],fill=(150,158,170))
    d.rectangle([x0+82,y0+40,x0+140,y0+52],fill=(150,158,170))
    for i in range(4): d.rectangle([x0+16+i*36,y0+48,x0+30+i*36,y0+66],fill=(170,176,186))
    d.rectangle([x0+8,y0+66,x1-8,y0+70],fill=(150,158,170))
    pass

def art_game(d,x0,y0,x1,y1):
    d.rectangle([x0,y0,x1,y1],fill=(108,52,140))
    d.ellipse([x0+70,y0+14,x0+170,y0+62],fill=(240,244,250))
    for cx,cy in [(x0+94,y0+30),(x0+146,y0+30)]:
        d.rectangle([cx-10,cy-4,cx+10,cy+4],fill=(120,60,150))
        d.rectangle([cx-2,cy-12,cx+2,cy+12],fill=(120,60,150))
    for cx,cy in [(x0+96,y0+46),(x0+112,y0+40),(x0+130,y0+40),(x0+146,y0+46)]:
        d.ellipse([cx-4,cy-4,cx+4,cy+4],fill=(220,80,120))
    txt(d,x0+8,y0+66,"ON SALE AFTER 13 YEARS",F_MICRO,WHITE)

LEADS=[
 ("ASIA","APEC SUMMIT","REUTERS · DW","SHENZHEN · APEC LEADERS' WEEK","XI GREETS TRUMP",
  "Xi greets Trump on the tarmac in Shenzhen",
  "A rare short remark and an embrace from China's leader. Trump and Putin shake hands; three-way talks are set for Thursday.",art_shenzhen),
 ("MIDDLE EAST","IRAN WAR","REUTERS · AL JAZEERA","INTERCEPTED · GULF","DRONES INTERCEPTED",
  "Kuwait, Bahrain intercept Iranian drones",
  "Iran aimed them after Tuesday's US strike on Qeshm. Gulf states report interceptions; the US reports no damage.",art_gulf),
 ("GLOBAL","SPACE · SCIENCE","NASA","VOYAGER 1 · NASA","ONE LIGHT-DAY OUT",
  "Voyager 1 is one light-day from Earth",
  "NASA's 1977 probe is the first human-made object to get 25.9 billion km away: a command sent today arrives tomorrow.",art_space),
]
CARDS=[
 (4,"EUROPE","UKRAINE WAR","KYIV AIR FORCE","141 FIRED / 126 DOWNED","Russia fires 141 drones at Ukraine; 126 downed","Seven died overnight; four more in Donetsk.",art_drones),
 (5,"EUROPE","UKRAINE AID","REUTERS","€45bn LOAN · 2027","EU proposes a €45bn loan to fund Kyiv in 2027","It fills two-thirds of a €70bn funding gap.",art_eu),
 (6,"AMERICAS","MARKETS","FED · AP","MORE HIKES","Fed minutes: nearly all officials see more hikes","A bigger December rise is floated; Dow -1.1%.",art_fed),
 (7,"ASIA","WEATHER","IMD","LANDFALL FRI 20 NOV","Cyclone Akavan veers north toward Odisha","Landfall is forecast Friday; evacuations begin.",art_cyclone),
 (8,"AFRICA","SUDAN WAR","AMNESTY","37 KILLED","Amnesty: RSF drones killed 37 in el-Obeid","It urges a war-crimes inquiry; RSF blames army.",art_sudan),
 (9,"MIDDLE EAST","GAZA","REUTERS","THE YELLOW LINE","Israeli tanks push into central Gaza","The army says it crossed a tunnel; three killed.",art_gaza),
 (10,"AMERICAS","US POLITICS","NPR · CBS","251-11 HOUSE VOTE","Hakeem Jeffries wins Democrats' nod for Speaker","He becomes the first Black speaker.",art_capitol),
 (11,"GLOBAL","CULTURE","ANANDROID","GTA VI · 13 YEARS","GTA VI goes on sale after a 13-year wait","The midnight launch starts in New Zealand.",art_game),
]
TINY=[
 (12,"AMERICAS","CPI: inflation ticks to 3.8%, a four-year high"),
 (13,"ASIA","Jakarta: tariffs talks with a hostage family"),
 (14,"ASIA","Japan: Trump hails his first Philippines visit as PM"),
 (15,"ASIA","Manila: Taiwan makes its biggest China trade deal"),
 (16,"ASIA","Seoul: Lee asks Xi on nuclear-fuelled submarines"),
 (17,"ASIA","Dhaka: weak protest over North Korea"),
 (18,"EUROPE","Kemerovo: 19 die as an An-12 crashes in Siberia"),
 (19,"MIDDLE EAST","Riyadh: Iran says it shot down a US MQ-9 drone"),
 (20,"MIDDLE EAST","Hormuz: tankers hit mines; fires spread"),
 (21,"EUROPE","Berlin: air defences, F-16s pledged to Kyiv"),
 (22,"EUROPE","Stockholm: ECDC warns of rising superbugs"),
 (23,"EUROPE","Turin: Alcaraz beats Medvedev at the ATP Finals"),
 (24,"AFRICA","Moscow: Ethiopia, Eritrea mass troops at border"),
 (25,"AFRICA","DR Congo: WHO declares Ebola a global emergency"),
 (26,"AMERICAS","Ottawa: Carney and Xi agree tariff relief"),
 (27,"MIDDLE EAST","Gaza: mediators launch a new ceasefire push"),
 (28,"AFRICA","Harare: European troops seize a defence chief's home"),
 (29,"AMERICAS","Bogota: Colombia's economy shrinks 0.8% in Q3"),
 (30,"AMERICAS","Brasilia: Senate passes Lula's $10bn package"),
 (31,"AMERICAS","Mexico: US trade talks enter a pivotal day"),
 (32,"AMERICAS","New York: artwork sells for $83 a share"),
 (33,"OCEANIA","Auckland: sanctions sweep leader Dalla Weiss"),
 (34,"OCEANIA","Sydney: lamb imports settle on the Aria Awards"),
 (35,"OCEANIA","PNG: magnitude 8.0 quake shakes Port Moresby"),
 (36,"OCEANIA","Cook Islands: Cyclone Xavier reaches Category 5"),
 (37,"GLOBAL","The Hague: ICJ to rule on Rohingya genocide case"),
 (38,"GLOBAL","Kigali: Rwanda signs EU migration centre deal"),
]

img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
# header
d.rectangle([0,0,W,90],fill=NAVY)
d.rectangle([16,8,96,82],fill=WHITE)
txt(d,26,12,"NOV",f("arialbd.ttf",12),RED)
txt(d,26,26,"18",f("timesbd.ttf",32),NAVY)
txt(d,22,66,"WED · 2026",f("arialbd.ttf",7),NAVY)
txt(d,112,12,"THE DAY IN WORLD NEWS",f("arialbd.ttf",11),GOLD)
txt(d,110,26,"Wednesday 18 November 2026",F_TITLE,WHITE)
txt(d,112,68,"Everything on this page happened, or was first reported, on Wednesday 18 November 2026.",F_SUB,(206,220,240))
txt(d,690,12,"38 STORIES · 7 REGIONS · 11 DRAWN · ONE PAGE",f("arialbd.ttf",9),GOLD)
rule(d,0,90,W,90,GOLD,3)

# region bar
chips=[("ASIA 7",PURPLE,146),("EUROPE 6",BLUE,148),("AMERICAS 9",GREEN,182),("AFRICA 4",ORANGE,126),
       ("MIDDLE EAST 4",RED,160),("OCEANIA 4",TEAL,124),("GLOBAL 4",GRAY,106)]
cx=16
for label,col,wid in chips:
    d.rectangle([cx,96,cx+wid,112],fill=col)
    tw=d.textlength(label,font=F_REG)
    txt(d,cx+(wid-tw)/2,99,label,F_REG,WHITE)
    cx+=wid

# leads
LW=(992-16)//3
for i,(reg,tag,src,kick,banner,head,cap,art) in enumerate(LEADS):
    x0=16+i*(LW+8); x1=x0+LW-1
    art(d,x0,118,x1,244)
    d.rectangle([x0,244,x1,268],fill=NAVY)
    tw=d.textlength(kick,font=F_SM)
    txt(d,x0+(LW-tw)/2,249,kick,F_SM,GOLD)
    d.rectangle([x0,268,x1,296],fill=RED if i==1 else NAVY)
    tw=d.textlength(banner,font=F_BAN)
    txt(d,x0+(LW-tw)/2,274,banner,F_BAN,WHITE)
    y=300
    badge(d,x0,y,i+1,REGCOL[reg]); txt(d,x0+20,y,reg+" · "+tag,F_SM,REGCOL[reg])
    sw=d.textlength(src,font=F_MICRO); txt(d,x1-sw,y,src,F_MICRO,GRAY)
    y+=17
    for ln in wrap(head,F_HEAD,x1-x0,d): txt(d,x0,y,ln,F_HEAD,NAVY); y+=20
    y+=2
    for ln in wrap(cap,F_CAP,x1-x0,d): txt(d,x0,y,ln,F_CAP,(70,76,90)); y+=12
    d.rectangle([x0,118,x1,388],outline=GRAY,width=1)

# cards 4-11
CW=(992-24)//4; CH=148
for j,(n,reg,tag,src,banner,head,cap,art) in enumerate(CARDS):
    col=j%4; row=j//4
    x0=16+col*(CW+8); y0=396+row*(CH+8); x1=x0+CW; y1=y0+CH
    art(d,x0,y0,x1,y0+52)
    d.rectangle([x0,y0+36,x1,y0+60],fill=NAVY)
    tw=d.textlength(banner,font=F_MICRO)
    txt(d,x0+(CW-tw)/2,y0+42,banner,F_MICRO,WHITE)
    y=y0+64
    badge(d,x0,y,n,REGCOL[reg]); txt(d,x0+20,y,reg+" · "+tag,F_MICRO,REGCOL[reg])
    sw=d.textlength(src,font=F_MICRO); txt(d,x1-sw,y,src,F_MICRO,GRAY)
    y+=14
    for ln in wrap(head,F_BIG,x1-x0,d)[:2]: txt(d,x0,y,ln,F_BIG,NAVY); y+=14
    for ln in wrap(cap,F_TINY,x1-x0,d)[:2]: txt(d,x0,y,ln,F_TINY,(80,86,100)); y+=10
    d.rectangle([x0,y0,x1,y1],outline=GRAY,width=1)

# bottom: map + tiny stories
MY=708
d.rectangle([16,MY,224,938],fill=(240,240,232),outline=GRAY,width=1)
txt(d,22,MY+4,"WHERE IT HAPPENED",F_SM,NAVY)
# simplified world map
d.rectangle([30,MY+30,210,MY+196],fill=(224,230,228))
# continents as blobs
d.polygon([(44,MY+52),(78,MY+46),(92,MY+66),(76,MY+88),(56,MY+84),(42,MY+70)],fill=(186,200,194))
d.polygon([(84,MY+94),(106,MY+90),(112,MY+130),(96,MY+150),(86,MY+126)],fill=(186,200,194))
d.polygon([(110,MY+48),(168,MY+40),(196,MY+62),(180,MY+96),(140,MY+98),(116,MY+76)],fill=(186,200,194))
d.polygon([(140,MY+104),(182,MY+100),(188,MY+146),(158,MY+162),(142,MY+136)],fill=(186,200,194))
d.ellipse([192,MY+150,208,MY+166],fill=(186,200,194))
pts=[(60,60,GLOBAL if False else PURPLE,1),(96,112,BLUE,4),(130,62,GREEN,2),
     (150,130,ORANGE,8),(170,74,RED,3),(190,118,TEAL,6),(74,150,GOLD,7)]
for px,py,col,n in pts: badge(d,28+px,MY+18+py,n,col)
d.line([(206,MY+158),(220,MY+180)],fill=GOLD,width=1)
txt(d,24,MY+210,"Voyager 1  →  Interstellar space",F_MICRO,(90,96,110))

d.rectangle([232,MY,1008,938],fill=(248,246,238),outline=GRAY,width=1)
txt(d,238,MY+4,"ALSO ON WEDNESDAY 18 NOVEMBER",F_SM,NAVY)
cols=4; per=7
cw=(776-16)//4
for k,(n,reg,head) in enumerate(TINY):
    c=k//per; r=k%per
    if c>=cols: break
    x=240+c*cw; y=MY+22+r*30
    badge(d,x,y,n,REGCOL[reg])
    for li,ln in enumerate(wrap(head,F_TINY,cw-18,d)[:2]):
        txt(d,x+18,y+li*10,ln,F_TINY,(48,54,68))

# date check
d.rectangle([16,944,1008,986],fill=(250,236,236),outline=RED,width=2)
txt(d,24,948,"DATE CHECK",f("arialbd.ttf",11),RED)
txt(d,110,948,"Left out, as first reported on Tuesday 17 November: Nvidia's results; the Alaska Senate call; the US strike on Qeshm; the",F_TINY,(110,40,40))
txt(d,110,960,"Kiessel speaker vote; the Kerch bridge collapse.  Not yet news",F_TINY,(110,40,40))
# world clock strip (UTC and the time difference across the day's news rooms)
d.rectangle([0,990,W,H],fill=NAVY)
txt(d,16,992,"WORLD CLOCK · UTC",f("arialbd.ttf",9),GOLD)
txt(d,120,992,"00:00 UTC  ·  19:00 NEW YORK (17 NOV, UTC-5)  ·  00:00 LONDON (UTC+0)  ·  05:30 KOLKATA (UTC+5:30)",F_MICRO,WHITE)
txt(d,120,1003,"08:00 SHENZHEN (UTC+8)  ·  09:00 TOKYO (UTC+9)  ·  11:00 SYDNEY (UTC+11)  ·  the date changes first in the west",F_MICRO,WHITE)

out=os.environ.get("MAKEFUN_OUTPUT","C:\\Users\\User\\Aws\\agent\\entry_build_v3\\preview.png")
parent=os.path.dirname(out)
if parent: os.makedirs(parent,exist_ok=True)
img.save(out,"PNG",optimize=True)
print("Wrote",out,os.path.getsize(out),"bytes")
