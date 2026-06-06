#!/usr/bin/env python3
"""High-quality Turkic traditional clothing assets at 512x1024."""
from PIL import Image, ImageDraw
import math

W, H = 512, 1024
GOLD = (255, 215, 0)
DARK_GOLD = (200, 170, 0)

def embroider(d, points, color=GOLD, spacing=18, dot_r=3):
    """Add embroidery dots along a path."""
    for i in range(0, len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        dist = math.hypot(dx, dy)
        steps = max(2, int(dist / spacing))
        for s in range(steps):
            t = s / steps
            x = p1[0] + dx * t
            y = p1[1] + dy * t
            d.ellipse([x-dot_r, y-dot_r, x+dot_r, y+dot_r], color)

def draw_pattern(d, x, y, w, h, color, size=12):
    """Draw a repeating diamond pattern."""
    for py in range(y, y + h, size * 2):
        for px in range(x, x + w, size * 2):
            cx, cy = px + size // 2, py + size // 2
            d.polygon([(cx, cy-size//2), (cx+size//2, cy), (cx, cy+size//2), (cx-size//2, cy)], color)

def base_body():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    skin = (242, 210, 192)
    shadow = (215, 185, 168)
    cx = W // 2

    # Legs
    d.rounded_rectangle([440, 380, 498, 480], 12, skin)
    d.rounded_rectangle([526, 380, 584, 480], 12, skin)
    d.rounded_rectangle([430, 480, 508, 500], 8, shadow)
    d.rounded_rectangle([516, 480, 594, 500], 8, shadow)

    # Arms
    for rx in (385, 609):
        d.rounded_rectangle([rx, 232, rx + 30, 370], 10, skin)
        # Hand
        d.rounded_rectangle([rx + 2, 365, rx + 28, 390], 6, skin)

    # Body
    d.rounded_rectangle([420, 228, 604, 385], 14, skin)
    d.rounded_rectangle([422, 230, 602, 383], 14, outline=shadow, width=2)

    # Neck
    d.rectangle([482, 195, 542, 230], skin)

    # Head
    d.ellipse([432, 55, 592, 225], skin)
    d.ellipse([432, 56, 592, 226], outline=shadow, width=2)

    # Eyes
    for ex in (480, 536):
        d.ellipse([ex, 126, ex + 18, 144], (55, 45, 35))
        d.ellipse([ex + 3, 130, ex + 10, 137], (255, 255, 255))

    # Eyebrows
    d.arc([478, 116, 500, 130], 180, 360, (80, 65, 50), 3)
    d.arc([524, 116, 546, 130], 180, 360, (80, 65, 50), 3)

    # Mouth
    d.arc([498, 162, 526, 176], 10, 170, (195, 115, 115), 3)

    # Blush
    d.ellipse([455, 148, 472, 165], (235, 195, 190, 80))
    d.ellipse([552, 148, 569, 165], (235, 195, 190, 80))

    img.save("assets/base_body.png")

def head_turban():
    """Traditional white turban with gold trim."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Turban wraps
    d.ellipse([410, 20, 614, 170], (235, 225, 210))
    d.ellipse([420, 30, 604, 160], (245, 238, 225))
    # Wrap folds
    for wy in range(50, 120, 20):
        d.arc([422, wy, 602, wy + 40], 0, 180, (220, 210, 195), 2)
    # Gold band
    d.ellipse([412, 115, 612, 135], GOLD)
    d.ellipse([412, 118, 612, 132], DARK_GOLD)
    # Jewel on front
    d.ellipse([502, 110, 522, 130], (220, 30, 30))
    d.ellipse([506, 114, 518, 126], (255, 80, 80))
    img.save("assets/hair/hair_turban.png")

def head_fes():
    """Red fez with gold tassel."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Fez body
    d.rounded_rectangle([464, 25, 560, 140], 18, (180, 30, 30))
    d.rounded_rectangle([466, 27, 558, 138], 16, (200, 40, 40))
    # Gold band
    d.rounded_rectangle([462, 115, 562, 130], 6, GOLD)
    d.rounded_rectangle([464, 117, 560, 128], 4, DARK_GOLD)
    # Tassel
    d.line([512, 130, 512, 190], GOLD, 3)
    d.ellipse([506, 185, 518, 200], GOLD)
    # Top
    d.ellipse([464, 20, 560, 40], (190, 35, 35))
    img.save("assets/hair/hair_fes.png")

def head_hotoz():
    """Traditional women's headdress with gold embroidery."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Main headdress
    d.ellipse([400, 10, 624, 180], (120, 20, 60))
    d.ellipse([408, 18, 616, 170], (140, 25, 70))
    # Gold embroidery border
    d.ellipse([410, 16, 614, 172], outline=GOLD, width=3)
    # Pattern
    for px in range(440, 584, 30):
        d.ellipse([px-3, 60, px+3, 66], GOLD)
        d.ellipse([px-3, 80, px+3, 86], GOLD)
        d.ellipse([px-3, 100, px+3, 106], GOLD)
    # Side ornaments
    for sx in (420, 604):
        d.ellipse([sx-8, 70, sx+8, 100], GOLD)
        d.line([sx, 100, sx, 135], GOLD, 2)
        d.ellipse([sx-4, 130, sx+4, 142], GOLD)
    img.save("assets/hair/hair_hotoz.png")

def head_tac():
    """Ornamental crown/tac."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Crown base
    d.rounded_rectangle([474, 50, 550, 120], 8, GOLD)
    d.rounded_rectangle([476, 52, 548, 118], 6, DARK_GOLD)
    # Points
    pts = [(474,120),(474,90),(488,108),(500,80),(512,102),
           (524,80),(536,108),(550,90),(550,120)]
    d.polygon(pts, GOLD)
    d.polygon(pts, outline=DARK_GOLD, width=2)
    # Jewels
    for jx in (488, 512, 536):
        d.ellipse([jx-5, 70, jx+5, 80], (220, 30, 30))
    # Center jewel large
    d.ellipse([506, 62, 518, 78], (30, 100, 220))
    d.ellipse([509, 65, 515, 75], (100, 170, 255))
    img.save("assets/hair/hair_tac.png")

def top_kaftan():
    """Long traditional kaftan with rich pattern."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Main kaftan body
    d.rounded_rectangle([405, 215, 619, 400], 18, (140, 30, 50))
    d.rounded_rectangle([408, 218, 616, 397], 16, (160, 35, 55))
    # V-neck opening
    d.polygon([(482,218),(512,300),(542,218)], (242, 210, 192))
    d.polygon([(484,220),(512,298),(540,220)], (222, 190, 175), width=2)
    # Gold trim along V-neck
    d.line([482, 218, 512, 300], GOLD, 3)
    d.line([542, 218, 512, 300], GOLD, 3)
    # Sleeves
    d.rounded_rectangle([378, 230, 408, 370], 10, (140, 30, 50))
    d.rounded_rectangle([616, 230, 646, 370], 10, (140, 30, 50))
    # Sleeve trim
    d.line([378, 230, 378, 370], GOLD, 3)
    d.line([646, 230, 646, 370], GOLD, 3)
    # Belt/sash
    d.rounded_rectangle([418, 360, 606, 385], 6, (30, 100, 160))
    d.line([418, 370, 606, 370], GOLD, 3)
    # Embroidery pattern on body
    for px in range(430, 594, 35):
        d.ellipse([px-2, 250, px+2, 254], GOLD)
        d.ellipse([px-2, 290, px+2, 294], GOLD)
        d.ellipse([px-2, 330, px+2, 334], GOLD)
    # Gold border at bottom
    d.line([405, 398, 619, 398], GOLD, 4)
    img.save("assets/top/top_kaftan.png")

def top_yelek():
    """Embroidered velvet vest."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Vest body
    d.rounded_rectangle([412, 215, 612, 395], 14, (30, 60, 120))
    d.rounded_rectangle([415, 218, 609, 392], 12, (35, 70, 135))
    # V-neck
    d.polygon([(480,218),(512,270),(544,218)], (242, 210, 192))
    # Gold embroidery along edges
    d.line([410, 218, 410, 395], GOLD, 2)
    d.line([614, 218, 614, 395], GOLD, 2)
    d.line([480, 218, 512, 270], GOLD, 2)
    d.line([544, 218, 512, 270], GOLD, 2)
    # Diamond pattern on vest
    draw_pattern(d, 425, 270, 175, 100, GOLD, 10)
    # Bottom gold trim
    d.rounded_rectangle([410, 380, 614, 395], 6, GOLD)
    img.save("assets/top/top_yelek.png")

def top_bindalli():
    """Gold-embroidered velvet dress."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Dress top
    d.rounded_rectangle([410, 215, 614, 370], 14, (90, 20, 45))
    d.rounded_rectangle([413, 218, 611, 367], 12, (105, 25, 50))
    # Flowing skirt
    d.polygon([(410,370),(614,370),(658,480),(366,480)], (105, 25, 50))
    d.polygon([(413,370),(611,370),(652,477),(372,477)], (120, 30, 55))
    # Gold embroidery on bodice
    for px in range(440, 584, 25):
        for py in range(250, 350, 30):
            d.ellipse([px-2, py-2, px+2, py+2], GOLD)
    # Gold trim at neckline
    d.arc([480, 215, 544, 240], 180, 360, GOLD, 3)
    # Gold belt line
    d.line([410, 370, 614, 370], GOLD, 3)
    # Hem embroidery
    embroider(d, [(366,480),(512,498),(658,480)], GOLD, 12, 4)
    # Sleeves
    for rx in (380, 634):
        d.rounded_rectangle([rx, 232, rx+28, 310], 8, (90, 20, 45))
        d.line([rx, 310, rx+28, 310], GOLD, 2)
    img.save("assets/top/top_bindalli.png")

def top_gomlek():
    """Traditional shirt with embroidered details."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Shirt
    d.rounded_rectangle([415, 218, 609, 385], 12, (230, 220, 210))
    d.rounded_rectangle([418, 221, 606, 382], 10, (245, 238, 228))
    # Collar opening
    d.polygon([(492,218),(512,280),(532,218)], (242, 210, 192))
    # Collar embroidery
    d.line([492, 218, 512, 280], (180, 50, 60), 2)
    d.line([532, 218, 512, 280], (180, 50, 60), 2)
    # Cuff embroidery
    for rx in (415, 605):
        d.line([rx, 360, rx+10, 360], (180, 50, 60), 2)
        d.line([rx, 370, rx+10, 370], (180, 50, 60), 2)
    # Front embroidery
    for px in range(440, 584, 30):
        d.ellipse([px-1, 300, px+1, 304], (180, 50, 60))
    img.save("assets/top/top_gomlek.png")

def bottom_salvar():
    """Traditional baggy shalwar pants."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Baggy legs
    d.rounded_rectangle([400, 375, 520, 480], 14, (40, 40, 80))
    d.rounded_rectangle([504, 375, 624, 480], 14, (40, 40, 80))
    # Gather at ankles
    d.rounded_rectangle([435, 470, 500, 488], 6, (50, 50, 95))
    d.rounded_rectangle([524, 470, 589, 488], 6, (50, 50, 95))
    # Ankle embroidery
    d.line([435, 486, 500, 486], GOLD, 3)
    d.line([524, 486, 589, 486], GOLD, 3)
    # Waistband
    d.rounded_rectangle([430, 372, 594, 385], 4, (60, 60, 110))
    d.line([430, 378, 594, 378], GOLD, 2)
    img.save("assets/bottom/bottom_salvar.png")

def bottom_etek():
    """Traditional patterned skirt."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Skirt - flared
    d.polygon([(414,376),(610,376),(570,490),(454,490)], (60, 120, 70))
    d.polygon([(418,378),(606,378),(567,488),(457,488)], (70, 135, 80))
    # Pattern stripes
    for px in range(440, 584, 24):
        d.line([px, 376, px-8, 490], (90, 155, 100), 2)
    # Waistband
    d.rounded_rectangle([430, 373, 594, 382], 4, GOLD)
    # Hem embroidery
    embroider(d, [(454,490),(512,496),(570,490)], GOLD, 10, 3)
    img.save("assets/bottom/bottom_etek.png")

def bottom_salvar_kisa():
    """Short shalwar (bloomers)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Puff legs
    d.rounded_rectangle([420, 376, 508, 430], 12, (160, 60, 60))
    d.rounded_rectangle([516, 376, 604, 430], 12, (160, 60, 60))
    # Hem at knee
    d.rounded_rectangle([422, 420, 506, 434], 6, (140, 50, 50))
    d.rounded_rectangle([518, 420, 602, 434], 6, (140, 50, 50))
    # Gold trim
    d.line([422, 432, 506, 432], GOLD, 2)
    d.line([518, 432, 602, 432], GOLD, 2)
    # Waist
    d.rounded_rectangle([430, 372, 594, 382], 4, (100, 35, 35))
    img.save("assets/bottom/bottom_salvar_kisa.png")

def shoes_cizme():
    """Traditional leather boots."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Boot shafts
    d.rounded_rectangle([434, 454, 502, 486], 8, (80, 50, 40))
    d.rounded_rectangle([522, 454, 590, 486], 8, (80, 50, 40))
    # Boot feet
    d.rounded_rectangle([428, 484, 508, 508], 10, (90, 55, 45))
    d.rounded_rectangle([516, 484, 596, 508], 10, (90, 55, 45))
    # Top trim
    d.rounded_rectangle([432, 452, 504, 462], 4, (180, 150, 100))
    d.rounded_rectangle([520, 452, 592, 462], 4, (180, 150, 100))
    # Sole
    d.rounded_rectangle([428, 504, 508, 510], 2, (40, 25, 20))
    d.rounded_rectangle([516, 504, 596, 510], 2, (40, 25, 20))
    img.save("assets/shoes/shoes_cizme.png")

def shoes_babuc():
    """Traditional curved slippers."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Slipper body
    d.rounded_rectangle([430, 486, 508, 504], 8, (180, 50, 70))
    d.rounded_rectangle([516, 486, 594, 504], 8, (180, 50, 70))
    # Curved toe
    d.ellipse([428, 483, 508, 500], (180, 50, 70))
    d.ellipse([516, 483, 596, 500], (180, 50, 70))
    # Gold decoration
    d.ellipse([455, 488, 470, 498], GOLD)
    d.ellipse([554, 488, 569, 498], GOLD)
    img.save("assets/shoes/shoes_babuc.png")

def shoes_takunya():
    """Traditional sandals."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Sole
    d.rounded_rectangle([428, 488, 510, 504], 6, (120, 80, 50))
    d.rounded_rectangle([514, 488, 596, 504], 6, (120, 80, 50))
    # Leather straps
    d.line([440, 488, 470, 488], (160, 110, 70), 4)
    d.line([440, 496, 470, 496], (160, 110, 70), 4)
    d.line([470, 488, 470, 504], (160, 110, 70), 4)
    d.line([470, 488, 440, 504], (160, 110, 70), 4)
    d.line([554, 488, 584, 488], (160, 110, 70), 4)
    d.line([554, 496, 584, 496], (160, 110, 70), 4)
    d.line([554, 488, 554, 504], (160, 110, 70), 4)
    d.line([584, 488, 554, 504], (160, 110, 70), 4)
    img.save("assets/shoes/shoes_takunya.png")

def acc_kusak():
    """Embroidered sash/belt."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Sash
    d.rounded_rectangle([410, 358, 614, 388], 10, (200, 50, 70))
    d.rounded_rectangle([410, 368, 614, 382], 8, (220, 60, 80))
    # Gold embroidery band
    d.rounded_rectangle([410, 362, 614, 372], 4, GOLD)
    # Pattern
    for px in range(420, 604, 20):
        d.ellipse([px-2, 364, px+2, 368], DARK_GOLD)
    # Buckle/center ornament
    d.ellipse([506, 360, 518, 375], GOLD)
    d.ellipse([509, 363, 515, 372], (220, 30, 30))
    img.save("assets/accessory/acc_kusak.png")

def acc_kolye():
    """Traditional gold coin necklace."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Necklace chain
    d.arc([448, 192, 576, 250], 200, 340, GOLD, 2)
    # Coins along necklace
    pos = [(470,216),(490,222),(512,226),(534,222),(554,216)]
    for px, py in pos:
        d.ellipse([px-8, py-8, px+8, py+8], GOLD)
        d.ellipse([px-6, py-6, px+6, py+6], DARK_GOLD)
        d.ellipse([px-2, py-2, px+2, py+2], GOLD)
    # Center pendant
    d.ellipse([504, 228, 520, 248], GOLD)
    d.ellipse([507, 231, 517, 245], (220, 30, 30))
    d.ellipse([510, 234, 514, 242], (255, 80, 80))
    img.save("assets/accessory/acc_kolye.png")

def acc_kupe():
    """Traditional gold earrings."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Earrings
    for ex in (455, 569):
        # Hoop
        d.ellipse([ex-10, 140, ex+10, 170], outline=GOLD, width=3)
        # Coin drop
        d.ellipse([ex-6, 168, ex+6, 182], GOLD)
        d.ellipse([ex-3, 171, ex+3, 179], DARK_GOLD)
        # Connection
        d.line([ex, 155, ex, 168], GOLD, 2)
    img.save("assets/accessory/acc_kupe.png")

def acc_bilezik():
    """Traditional gold bracelets."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx = W // 2
    # Left arm bracelets
    for by in range(360, 381, 8):
        d.ellipse([386, by, 412, by+6], outline=GOLD, width=3)
    # Right arm bracelets
    for by in range(360, 381, 8):
        d.ellipse([610, by, 636, by+6], outline=GOLD, width=3)
    img.save("assets/accessory/acc_bilezik.png")

def base_body_male():
    """Male base body — broader shoulders, square jaw, no blush."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    skin = (235, 200, 180)
    shadow = (205, 175, 158)
    cx = W // 2

    # Legs (slightly wider stance)
    d.rounded_rectangle([435, 380, 498, 480], 12, skin)
    d.rounded_rectangle([526, 380, 589, 480], 12, skin)
    d.rounded_rectangle([425, 480, 508, 500], 8, shadow)
    d.rounded_rectangle([516, 480, 599, 500], 8, shadow)

    # Arms (broader)
    for rx in (372, 622):
        d.rounded_rectangle([rx, 225, rx + 34, 370], 10, skin)
        d.rounded_rectangle([rx + 2, 365, rx + 32, 395], 6, skin)

    # Body / torso (wider shoulders)
    d.rounded_rectangle([415, 220, 609, 385], 14, skin)
    d.rounded_rectangle([417, 222, 607, 383], 14, outline=shadow, width=2)

    # Neck (wider)
    d.rectangle([478, 190, 546, 222], skin)

    # Head — slightly squarer jaw
    d.ellipse([432, 55, 592, 225], skin)
    # Jaw line
    d.rounded_rectangle([437, 168, 587, 225], 10, skin)
    d.ellipse([432, 56, 592, 226], outline=shadow, width=2)

    # Eyes (slightly narrower)
    for ex in (480, 536):
        d.ellipse([ex, 126, ex + 16, 142], (55, 45, 35))
        d.ellipse([ex + 3, 130, ex + 8, 136], (255, 255, 255))

    # Eyebrows (straighter, thicker)
    d.line([478, 118, 502, 120], (70, 55, 40), 4)
    d.line([522, 120, 546, 118], (70, 55, 40), 4)

    # Mouth (straight line)
    d.line([500, 168, 524, 168], (170, 110, 100), 3)

    # No blush — male version

    img.save("assets/base_body_male.png")

if __name__ == "__main__":
    base_body()
    base_body_male()
    head_turban()
    head_fes()
    head_hotoz()
    head_tac()
    top_kaftan()
    top_yelek()
    top_bindalli()
    top_gomlek()
    bottom_salvar()
    bottom_etek()
    bottom_salvar_kisa()
    shoes_cizme()
    shoes_babuc()
    shoes_takunya()
    acc_kusak()
    acc_kolye()
    acc_kupe()
    acc_bilezik()
    print("All Turkic clothing assets generated at 1024x512.")
