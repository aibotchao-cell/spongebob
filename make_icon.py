# -*- coding: utf-8 -*-
"""產生《海綿寶寶俄羅斯方塊》PWA 圖示：海底藍底＋黃色海綿方塊（有洞＋笑臉）＋主題小方塊"""
from PIL import Image, ImageDraw
import math

S = 1024

def draw_icon(size):
    img = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # 海底漸層
    for y in range(S):
        t = y / S
        r = int(0x0a + (0x03 - 0x0a) * t)
        g = int(0x5a + (0x1c - 0x5a) * t)
        b = int(0x80 + (0x2e - 0x80) * t)
        d.line([(0, y), (S, y)], fill=(r, g, b, 255))
    # 光柱
    ray = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    rd = ImageDraw.Draw(ray)
    for i in range(3):
        bx = S * (0.18 + i * 0.30)
        rd.polygon([(bx - S * 0.06, 0), (bx + S * 0.06, 0), (bx + S * 0.20, S), (bx - S * 0.10, S)],
                   fill=(150, 230, 255, 34))
    img.alpha_composite(ray)
    d = ImageDraw.Draw(img)
    # 泡泡
    for (bx, by, br) in [(0.14, 0.20, 0.030), (0.86, 0.16, 0.022), (0.80, 0.46, 0.016),
                         (0.12, 0.60, 0.019), (0.90, 0.74, 0.014)]:
        x, y, r = S * bx, S * by, S * br
        d.ellipse([x - r, y - r, x + r, y + r], outline=(200, 245, 255, 150), width=max(2, int(S * 0.005)))
        d.ellipse([x - r * 0.7, y - r * 0.7, x + r * 0.7, y + r * 0.7], fill=(255, 255, 255, 26))
    # 底部主題小方塊（蟹堡／星星／鳳梨色）
    bw = S * 0.155
    by = S * 0.815
    for i, col in enumerate([(0xe6, 0xb1, 0x55), (0xf5, 0xa3, 0xbd), (0xea, 0xa6, 0x3f)]):
        bx = S * 0.175 + i * bw * 1.05
        d.rounded_rectangle([bx, by, bx + bw, by + bw], radius=bw * 0.24,
                            fill=col + (255,), outline=(10, 40, 55, 200), width=max(2, int(S * 0.006)))
    # 主體：黃色海綿方塊
    m = S * 0.205
    d.rounded_rectangle([m, m, S - m, S - m], radius=S * 0.085,
                        fill=(0xf2, 0xd5, 0x44, 255), outline=(0x9c, 0x82, 0x16, 255), width=int(S * 0.014))
    # 上緣高光
    d.rounded_rectangle([m + S * 0.02, m + S * 0.02, S - m - S * 0.02, m + S * 0.075],
                        radius=S * 0.028, fill=(255, 245, 160, 90))
    # 海綿洞
    for (hx, hy, hr) in [(0.30, 0.30, 0.042), (0.68, 0.27, 0.033), (0.76, 0.55, 0.038),
                         (0.26, 0.63, 0.036), (0.50, 0.40, 0.022), (0.44, 0.76, 0.026)]:
        x, y, r = S * hx, S * hy, S * hr
        d.ellipse([x - r, y - r * 0.82, x + r, y + r * 0.82], fill=(0xb9, 0x9c, 0x22, 120))
    # 眼睛
    for ex in (0.415, 0.585):
        x, y = S * ex, S * 0.455
        r = S * 0.072
        d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255, 255), outline=(90, 80, 20, 200), width=max(2, int(S * 0.005)))
        pr = r * 0.44
        d.ellipse([x - pr, y - pr * 0.9, x + pr, y + pr * 1.1], fill=(0x20, 0x30, 0x3a, 255))
        d.ellipse([x - pr * 0.5, y - pr * 0.9, x - pr * 0.05, y - pr * 0.35], fill=(255, 255, 255, 230))
    # 微笑
    d.arc([S * 0.40, S * 0.50, S * 0.60, S * 0.70], start=20, end=160,
          fill=(0x7a, 0x5c, 0x12, 255), width=max(3, int(S * 0.016)))
    return img.resize((size, size), Image.LANCZOS)

for sz in (512, 192, 180):
    draw_icon(sz).save('sb-icon-%d.png' % sz)
    print('wrote sb-icon-%d.png' % sz)
