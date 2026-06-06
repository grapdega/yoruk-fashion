from PIL import Image, ImageDraw
import os

SIZE = 1024

OUT_DIR = "assets"
SUBDIRS = ["hair", "top", "bottom", "shoes", "accessory"]

def create_img():
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    return img, draw

def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG")

def rr(draw, x1, y1, x2, y2, fill, outline=None, width=2, radius=8):
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def ell(draw, x1, y1, x2, y2, fill, outline=None, width=2):
    draw.ellipse([x1, y1, x2, y2], fill=fill, outline=outline, width=width)

def poly(draw, pts, fill, outline=None, width=2):
    draw.polygon(pts, fill=fill, outline=outline, width=width)

# Colors
CRIMSON    = (180, 30, 40)
DARK_RED   = (140, 20, 30)
GOLD       = (212, 175, 55)
DARK_GOLD  = (180, 140, 30)
TURQUOISE  = (60, 180, 180)
DARK_TEAL  = (30, 100, 120)
NAVY       = (25, 40, 70)
DARK_GREEN = (40, 100, 60)
FOREST     = (30, 80, 50)
PURPLE     = (120, 60, 140)
BROWN      = (120, 70, 40)
DARK_BROWN = (80, 45, 25)
BEIGE      = (245, 225, 200)
SKIN       = (235, 190, 150)
SKIN_DARK  = (200, 155, 120)
WHITE      = (245, 245, 240)
BLACK      = (30, 30, 30)
GRAY       = (180, 180, 180)
DARK_GRAY  = (100, 100, 100)

# ─── BASE BODIES ───

def gen_base_body_female():
    img, draw = create_img()
    cx = 512  # center x

    # Legs
    rr(draw, cx-80, 560, cx-30, 880, fill=SKIN, outline=(180,140,110), radius=14)
    rr(draw, cx+30, 560, cx+80, 880, fill=SKIN, outline=(180,140,110), radius=14)

    # Skirt
    poly(draw, [
        (cx-110, 560), (cx+110, 560), (cx+140, 880), (cx-140, 880)
    ], fill=(200, 50, 70), outline=(160, 30, 50))

    # Torso
    rr(draw, cx-90, 230, cx+90, 570, fill=(240, 220, 230), outline=(200, 180, 190), radius=16)

    # Arms
    rr(draw, cx-130, 260, cx-92, 530, fill=SKIN, outline=(180,140,110), radius=12)
    rr(draw, cx+92, 260, cx+130, 530, fill=SKIN, outline=(180,140,110), radius=12)

    # Neck
    rr(draw, cx-18, 190, cx+18, 240, fill=SKIN, outline=(180,140,110), radius=6)

    # Head
    ell(draw, cx-75, 50, cx+75, 200, fill=SKIN, outline=(180,140,110))

    # Hair
    ell(draw, cx-85, 40, cx+85, 140, fill=(60, 30, 15))

    # Shoes
    rr(draw, cx-85, 875, cx-25, 910, fill=DARK_RED, outline=(100,10,20), radius=6)
    rr(draw, cx+25, 875, cx+85, 910, fill=DARK_RED, outline=(100,10,20), radius=6)

    # Face features
    ell(draw, cx-20, 105, cx-8, 118, fill=(60, 30, 15))
    ell(draw, cx+8, 105, cx+20, 118, fill=(60, 30, 15))
    draw.arc([cx-40, 120, cx+40, 150], start=0, end=180, fill=(180, 100, 100), width=3)

    save(img, os.path.join(OUT_DIR, "base_body.png"))

def gen_base_body_male():
    img, draw = create_img()
    cx = 512

    # Legs
    rr(draw, cx-90, 560, cx-30, 880, fill=SKIN_DARK, outline=(150,110,80), radius=14)
    rr(draw, cx+30, 560, cx+90, 880, fill=SKIN_DARK, outline=(150,110,80), radius=14)

    # Pants
    rr(draw, cx-105, 560, cx-20, 720, fill=(80, 60, 50), outline=(60, 40, 30), radius=12)
    rr(draw, cx+20, 560, cx+105, 720, fill=(80, 60, 50), outline=(60, 40, 30), radius=12)
    rr(draw, cx-105, 700, cx+105, 740, fill=(80, 60, 50), outline=(60, 40, 30), radius=4)

    # Torso
    rr(draw, cx-95, 230, cx+95, 570, fill=(220, 215, 210), outline=(180, 175, 170), radius=16)

    # Arms
    rr(draw, cx-135, 250, cx-97, 530, fill=SKIN_DARK, outline=(150,110,80), radius=12)
    rr(draw, cx+97, 250, cx+135, 530, fill=SKIN_DARK, outline=(150,110,80), radius=12)

    # Neck
    rr(draw, cx-18, 190, cx+18, 240, fill=SKIN_DARK, outline=(150,110,80), radius=6)

    # Head
    ell(draw, cx-75, 45, cx+75, 195, fill=SKIN_DARK, outline=(150,110,80))

    # Hair (short)
    ell(draw, cx-80, 35, cx+80, 130, fill=(40, 25, 10))

    # Shoes
    rr(draw, cx-90, 875, cx-25, 915, fill=(50, 40, 35), outline=(30, 20, 15), radius=6)
    rr(draw, cx+25, 875, cx+90, 915, fill=(50, 40, 35), outline=(30, 20, 15), radius=6)

    # Face
    ell(draw, cx-22, 100, cx-10, 113, fill=(40, 25, 10))
    ell(draw, cx+10, 100, cx+22, 113, fill=(40, 25, 10))
    draw.arc([cx-35, 115, cx+35, 145], start=0, end=180, fill=(140, 80, 80), width=3)

    save(img, os.path.join(OUT_DIR, "base_body_male.png"))


# ─── HAIR ───

def gen_hair_turban():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-100, 35, cx+100, 160, fill=(60, 120, 130), outline=(40, 90, 100), radius=20)
    for i in range(4):
        yy = 50 + i * 28
        draw.line([cx-80, yy, cx+80, yy], fill=(50, 100, 110), width=4)
    ell(draw, cx-22, 20, cx+22, 45, fill=GOLD, outline=(160, 130, 30))
    save(img, os.path.join(OUT_DIR, "hair", "hair_turban.png"))

def gen_hair_fes():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-80, 30, cx+80, 180, fill=CRIMSON, outline=DARK_RED, radius=14)
    tx, ty = cx, 175
    draw.line([tx, ty, tx+8, ty+50], fill=(60, 30, 15), width=4)
    ell(draw, tx+1, ty+45, tx+15, ty+65, fill=(60, 30, 15))
    rr(draw, cx-80, 160, cx+80, 180, fill=GOLD, outline=DARK_GOLD, radius=4)
    save(img, os.path.join(OUT_DIR, "hair", "hair_fes.png"))

def gen_hair_hotoz():
    img, draw = create_img()
    cx = 512
    poly(draw, [
        (cx-90, 180), (cx-60, 20), (cx+60, 20), (cx+90, 180)
    ], fill=PURPLE, outline=(90, 40, 110))
    rr(draw, cx-90, 150, cx+90, 180, fill=GOLD, outline=DARK_GOLD, radius=6)
    rr(draw, cx-70, 165, cx+70, 220, fill=(180, 140, 180, 140), outline=None, radius=8)
    save(img, os.path.join(OUT_DIR, "hair", "hair_hotoz.png"))

def gen_hair_tac():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-100, 40, cx+100, 150, fill=GOLD, outline=DARK_GOLD, radius=12)
    for i in range(7):
        px = cx - 80 + i * 27
        poly(draw, [
            (px-10, 40), (px, 5), (px+10, 40)
        ], fill=GOLD, outline=DARK_GOLD)
    for i in range(6):
        jx = cx - 75 + i * 30
        ell(draw, jx, 65, jx+18, 88, fill=TURQUOISE, outline=(40, 120, 120))
    save(img, os.path.join(OUT_DIR, "hair", "hair_tac.png"))


# ─── TOPS ───

def gen_top_kaftan():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-130, 220, cx+130, 760, fill=(180, 30, 50), outline=(140, 20, 35), radius=20)
    rr(draw, cx-120, 740, cx+120, 760, fill=GOLD, outline=DARK_GOLD, radius=4)
    draw.line([cx, 240, cx, 760], fill=GOLD, width=5)
    rr(draw, cx-130, 480, cx+130, 510, fill=(40, 30, 80), outline=(25, 15, 55), radius=6)
    save(img, os.path.join(OUT_DIR, "top", "top_kaftan.png"))

def gen_top_yelek():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-120, 230, cx+120, 530, fill=(60, 60, 140), outline=(40, 40, 110), radius=16)
    poly(draw, [
        (cx-30, 230), (cx+30, 230), (cx, 370)
    ], fill=(0,0,0,0), outline=(40, 40, 110))
    for i in range(4):
        yy = 270 + i * 60
        draw.line([cx-100, yy, cx+100, yy], fill=GOLD, width=3)
    save(img, os.path.join(OUT_DIR, "top", "top_yelek.png"))

def gen_top_bindalli():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-130, 220, cx+130, 760, fill=(50, 120, 110), outline=(35, 90, 85), radius=20)
    for i in range(6):
        yy = 250 + i * 40
        for j in range(5):
            xx = cx - 90 + j * 45
            ell(draw, xx, yy, xx+18, yy+18, fill=GOLD)
    rr(draw, cx-110, 480, cx+110, 510, fill=GOLD, outline=DARK_GOLD, radius=6)
    save(img, os.path.join(OUT_DIR, "top", "top_bindalli.png"))

def gen_top_gomlek():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-125, 230, cx+125, 540, fill=(240, 238, 235), outline=(200, 198, 195), radius=16)
    poly(draw, [
        (cx-35, 230), (cx+35, 230), (cx, 290)
    ], fill=(240, 238, 235), outline=(200, 198, 195))
    for i in range(4):
        ell(draw, cx-4, 300+i*45, cx+4, 310+i*45, fill=(180, 178, 175))
    save(img, os.path.join(OUT_DIR, "top", "top_gomlek.png"))


# ─── BOTTOMS ───

def gen_bottom_salvar():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-120, 550, cx+120, 780, fill=(80, 50, 70), outline=(60, 35, 55), radius=16)
    rr(draw, cx-120, 755, cx-50, 800, fill=(70, 40, 60), outline=(50, 25, 45), radius=8)
    rr(draw, cx+50, 755, cx+120, 800, fill=(70, 40, 60), outline=(50, 25, 45), radius=8)
    rr(draw, cx-120, 535, cx+120, 560, fill=(40, 25, 55), outline=(30, 15, 40), radius=6)
    save(img, os.path.join(OUT_DIR, "bottom", "bottom_salvar.png"))

def gen_bottom_etek():
    img, draw = create_img()
    cx = 512
    poly(draw, [
        (cx-90, 555), (cx+90, 555), (cx+130, 840), (cx-130, 840)
    ], fill=(180, 50, 80), outline=(140, 30, 60))
    for i in range(4):
        yy = 580 + i * 65
        draw.line([cx-110+i*8, yy, cx+110-i*8, yy], fill=GOLD, width=3)
    rr(draw, cx-90, 540, cx+90, 560, fill=(60, 20, 40), outline=(40, 10, 25), radius=4)
    save(img, os.path.join(OUT_DIR, "bottom", "bottom_etek.png"))

def gen_bottom_salvar_kisa():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-115, 550, cx+115, 710, fill=(100, 120, 140), outline=(70, 90, 110), radius=16)
    rr(draw, cx-115, 693, cx-45, 725, fill=(90, 105, 125), outline=(60, 75, 95), radius=6)
    rr(draw, cx+45, 693, cx+115, 725, fill=(90, 105, 125), outline=(60, 75, 95), radius=6)
    rr(draw, cx-115, 535, cx+115, 560, fill=(60, 80, 100), outline=(40, 60, 80), radius=6)
    save(img, os.path.join(OUT_DIR, "bottom", "bottom_salvar_kisa.png"))


# ─── SHOES ───

def gen_shoes_cizme():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        bx = cx + side * 60
        poly(draw, [
            (bx-20, 830), (bx+20, 830), (bx+20, 910), (bx-35, 910), (bx-40, 880)
        ], fill=(60, 40, 30), outline=(40, 25, 15))
        rr(draw, bx-22, 815, bx+22, 835, fill=(80, 55, 40), outline=(50, 35, 25), radius=4)
    save(img, os.path.join(OUT_DIR, "shoes", "shoes_cizme.png"))

def gen_shoes_babuc():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        bx = cx + side * 55
        ell(draw, bx-18, 855, bx+22, 890, fill=(180, 40, 60), outline=(140, 25, 45))
        poly(draw, [
            (bx+15, 858), (bx+40, 865), (bx+15, 880)
        ], fill=(180, 40, 60), outline=(140, 25, 45))
    save(img, os.path.join(OUT_DIR, "shoes", "shoes_babuc.png"))

def gen_shoes_takunya():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        bx = cx + side * 55
        rr(draw, bx-18, 870, bx+22, 910, fill=(160, 130, 80), outline=(120, 95, 55), radius=6)
        rr(draw, bx-8, 845, bx+8, 875, fill=(80, 40, 60), outline=(60, 25, 45), radius=4)
    save(img, os.path.join(OUT_DIR, "shoes", "shoes_takunya.png"))


# ─── ACCESSORIES ───

def gen_acc_necklace():
    img, draw = create_img()
    cx = 512
    draw.arc([cx-80, 340, cx+80, 450], start=0, end=180, fill=GOLD, width=5)
    for i in range(8):
        bx = cx - 60 + i * 17
        ell(draw, bx-5, 400+abs(i-4)*8, bx+5, 415+abs(i-4)*8, fill=(TURQUOISE if i%2==0 else GOLD))
    save(img, os.path.join(OUT_DIR, "accessory", "acc_necklace.png"))

def gen_acc_glasses():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        lx = cx + side * 55
        ell(draw, lx-28, 95, lx+28, 150, fill=(200, 215, 230, 100), outline=(80, 80, 80), width=4)
    draw.line([cx-27, 120, cx+27, 120], fill=(80, 80, 80), width=4)
    draw.line([cx-83, 110, cx-110, 125], fill=(80, 80, 80), width=4)
    draw.line([cx+83, 110, cx+110, 125], fill=(80, 80, 80), width=4)
    save(img, os.path.join(OUT_DIR, "accessory", "acc_glasses.png"))

def gen_acc_hat():
    img, draw = create_img()
    cx = 512
    ell(draw, cx-120, 140, cx+120, 170, fill=(120, 80, 50), outline=(90, 55, 30))
    rr(draw, cx-70, 20, cx+70, 145, fill=(140, 95, 60), outline=(110, 70, 40), radius=12)
    rr(draw, cx-70, 110, cx+70, 135, fill=DARK_RED, outline=(100, 15, 25), radius=6)
    save(img, os.path.join(OUT_DIR, "accessory", "acc_hat.png"))

def gen_acc_crown():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-100, 40, cx+100, 140, fill=GOLD, outline=DARK_GOLD, radius=8)
    for i in range(7):
        px = cx - 80 + i * 27
        poly(draw, [
            (px-8, 40), (px, 0), (px+8, 40)
        ], fill=GOLD, outline=DARK_GOLD)
    for i in range(6):
        jx = cx - 75 + i * 30
        ell(draw, jx, 65, jx+16, 88, fill=TURQUOISE, outline=(40, 120, 120))
    save(img, os.path.join(OUT_DIR, "accessory", "acc_crown.png"))

def gen_acc_kolye():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        draw.line([cx+side*40, 370, cx, 410], fill=GOLD, width=3)
    poly(draw, [
        (cx, 405), (cx-30, 480), (cx+30, 480)
    ], fill=GOLD, outline=DARK_GOLD)
    ell(draw, cx-14, 440, cx+14, 470, fill=(200, 50, 70))
    save(img, os.path.join(OUT_DIR, "accessory", "acc_kolye.png"))

def gen_acc_kupe():
    img, draw = create_img()
    cx = 512
    # Left
    draw.line([cx-82, 140, cx-95, 210], fill=GOLD, width=3)
    ell(draw, cx-108, 195, cx-82, 235, fill=GOLD, outline=DARK_GOLD)
    ell(draw, cx-104, 202, cx-86, 228, fill=TURQUOISE)
    # Right
    draw.line([cx+82, 140, cx+95, 210], fill=GOLD, width=3)
    ell(draw, cx+82, 195, cx+108, 235, fill=GOLD, outline=DARK_GOLD)
    ell(draw, cx+86, 202, cx+104, 228, fill=TURQUOISE)
    save(img, os.path.join(OUT_DIR, "accessory", "acc_kupe.png"))

def gen_acc_bilezik():
    img, draw = create_img()
    cx = 512
    for side in [-1, 1]:
        bx = cx + side * 128
        for i in range(4):
            ell(draw, bx-10+i*3, 460+i*4, bx+22+i*3, 485+i*4, fill=None, outline=GOLD, width=5)
    save(img, os.path.join(OUT_DIR, "accessory", "acc_bilezik.png"))

def gen_acc_kusak():
    img, draw = create_img()
    cx = 512
    rr(draw, cx-135, 470, cx+135, 510, fill=(180, 40, 60), outline=(140, 25, 45), radius=6)
    for i in range(5):
        sx = cx - 100 + i * 50
        rr(draw, sx, 477, sx+30, 503, fill=GOLD, outline=DARK_GOLD, radius=4)
    poly(draw, [
        (cx-30, 510), (cx-50, 570), (cx+10, 570)
    ], fill=(180, 40, 60), outline=(140, 25, 45))
    save(img, os.path.join(OUT_DIR, "accessory", "acc_kusak.png"))


# ─── MAIN ───

if __name__ == "__main__":
    print("Generating 1024x1024 assets (v2 - full-size characters)...")

    print("[Base Bodies]")
    gen_base_body_female()
    gen_base_body_male()

    print("[Hair]")
    gen_hair_turban(); gen_hair_fes(); gen_hair_hotoz(); gen_hair_tac()

    print("[Tops]")
    gen_top_kaftan(); gen_top_yelek(); gen_top_bindalli(); gen_top_gomlek()

    print("[Bottoms]")
    gen_bottom_salvar(); gen_bottom_etek(); gen_bottom_salvar_kisa()

    print("[Shoes]")
    gen_shoes_cizme(); gen_shoes_babuc(); gen_shoes_takunya()

    print("[Accessories]")
    gen_acc_necklace(); gen_acc_glasses(); gen_acc_hat(); gen_acc_crown()
    gen_acc_kolye(); gen_acc_kupe(); gen_acc_bilezik(); gen_acc_kusak()

    print("Done! All 23 assets regenerated at 1024x1024.")
