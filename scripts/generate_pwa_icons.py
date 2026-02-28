#!/usr/bin/env python3
"""PWA için 192x192 ve 512x512 PNG üretir (Norya teal #0d9488). Proje kökünden: python3 scripts/generate_pwa_icons.py
   İsterseniz icon.svg'yi PNG'ye çevirmek için: pip install cairosvg && cairosvg static/icon.svg -o static/icon-512.png -W 512 -H 512"""
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"
# Norya teal
R, G, B = 0x0D, 0x94, 0x88


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    chunk = chunk_type + data
    return struct.pack(">I", len(data)) + chunk + struct.pack(">I", zlib.crc32(chunk) & 0xFFFFFFFF)


def make_solid_png(w: int, h: int) -> bytes:
    raw = b""
    for _ in range(h):
        raw += b"\x00"  # filter byte
        for _ in range(w):
            raw += bytes((R, G, B))
    z = zlib.compress(raw, 9)
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)
    header = b"\x89PNG\r\n\x1a\n"
    return header + png_chunk(b"IHDR", ihdr) + png_chunk(b"IDAT", z) + png_chunk(b"IEND", b"")


def main():
    for size in (192, 512):
        out = STATIC / f"icon-{size}.png"
        out.write_bytes(make_solid_png(size, size))
        print(f"Yazıldı: {out} ({size}x{size})")
    print("PWA ikonları hazır. (Özelleştirmek için icon.svg'den cairosvg ile PNG üretebilirsiniz.)")


if __name__ == "__main__":
    main()
