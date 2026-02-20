#!/usr/bin/env python3
"""
Generate colored SVG placeholder images for albums and artists.
These serve as fallback art until real images are fetched via fetch_music_images.py.

The SVGs use a deterministic color derived from the name, showing initials.
"""

import os
import re
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Palette of background colors (dark, looks good with white text)
COLORS = [
    "#1a1a2e", "#16213e", "#0f3460", "#533483",
    "#6b2d6b", "#a84b5a", "#c77d5b", "#3a7bd5",
    "#2b6777", "#2c7873", "#196f3d", "#4a235a",
    "#784212", "#1b4f72", "#7d6608", "#4a4a4a",
    "#6e2f2f", "#2e4057", "#048a81", "#54c6eb",
]


def slug(text):
    s = text.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def pick_color(name):
    h = int(hashlib.md5(name.encode()).hexdigest()[:6], 16)
    return COLORS[h % len(COLORS)]


def initials(name):
    # Strip leading "The ", "A ", "An " for initials
    clean = re.sub(r'^(the|a|an)\s+', '', name, flags=re.I)
    parts = clean.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif parts:
        return parts[0][:2].upper()
    return "?"


def make_svg(label, bg_color, size=250):
    font_size = size * 0.38
    cx = size / 2
    cy = size / 2
    # Slightly lighter version for subtle gradient
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">
  <rect width="{size}" height="{size}" fill="{bg_color}" rx="4"/>
  <text x="{cx}" y="{cy}" font-family="system-ui, sans-serif" font-size="{font_size:.0f}"
    font-weight="700" fill="white" fill-opacity="0.9"
    text-anchor="middle" dominant-baseline="central">{label}</text>
</svg>"""


# --- Albums list (html_title, artist) ---
ALBUMS = [
    ("Sparkle and Fade", "Everclear"),
    ("A/B", "Kaleo"),
    ("Mind Control Acoustic", "Stephen Marley"),
    ("No Jacket Required", "Phil Collins"),
    ("Kickin' It", "Hamilton Loomis"),
    ("Eat Ya Veggies", "bbno$"),
    ("Freaks of Nature", "Drain STH"),
    ("Jagged Little Pill", "Alanis Morissette"),
    ("John Coltrane and Johnny Hartman", "John Coltrane"),
    ("Greatest Hits", "Steve Miller Band"),
    ("ZABA", "Glass Animals"),
    ("A 20 Something Fuck", "Two Feet"),
    ("The Hits / The B-Sides", "Prince"),
    ("Don't Explain", "Beth Hart"),
    ("Mescalito", "Ryan Bingham"),
    ("Swimming", "Mac Miller"),
    ("Live at Bonnaroo", "Warren Haynes"),
    ("Tapestry", "Carole King"),
    ("The Razors Edge", "AC/DC"),
    ("Nothing But the Best", "Frank Sinatra"),
    ("Trouble", "Ray LaMontagne"),
    ("Facelift", "Alice in Chains"),
    ("Violator", "Depeche Mode"),
    ("Nowhere to Hide", "The Virus"),
    ("Destruction by Definition", "The Suicide Machines"),
    ("Live at the Old Quarter", "Townes Van Zandt"),
    ("Moving Pictures", "Rush"),
    ("2112", "Rush"),
    ("Retrospective I & II", "Rush"),
    ("Rock Spectacle", "Barenaked Ladies"),
    ("Let It Be Me", "Nina Simone"),
    ("Rainbow", "Kesha"),
    ("Lie to Me", "Jonny Lang"),
    ("Live at the Regal", "B.B. King"),
    ("Who Killed the Zutons", "The Zutons"),
    ("Heartattack and Vine", "Tom Waits"),
    ("Hell Freezes Over", "Eagles"),
    ("Keep 'Em on They Toes", "Brent Cobb"),
    ("Rage Against the Machine", "Rage Against the Machine"),
    ("Grace", "Jeff Buckley"),
    ("The Emancipation of Mimi", "Mariah Carey"),
    ("Traveller", "Chris Stapleton"),
    ("Metamodern Sounds in Country Music", "Sturgill Simpson"),
    ("No Fences", "Garth Brooks"),
    ("Pieces of You", "Jewel"),
    ("The Boatman's Call", "Nick Cave and the Bad Seeds"),
    ("Unplugged", "Eric Clapton"),
    ("Whitey Ford Sings the Blues", "Everlast"),
    ("Sublime", "Sublime"),
    ("Bedtime Stories", "Madonna"),
    ("Endless Summer Vacation", "Miley Cyrus"),
    ("Where Have All the Merrymakers Gone?", "Harvey Danger"),
    ("Metallica (Black Album)", "Metallica"),
    ("The River", "Bruce Springsteen"),
    ("Texas Flood", "Stevie Ray Vaughan"),
    ("No More Tears", "Ozzy Osbourne"),
    ("Boston", "Boston"),
    ("Dookie", "Green Day"),
    ("Give Me Convenience or Give Me Death", "Dead Kennedys"),
    ("The Four Seasons", "Vivaldi"),
]

ARTISTS = [
    "Chris Stapleton",
    "Rush",
    "John Mellencamp",
    "Gov't Mule",
    "Tantric",
]


def update_html(albums, artists):
    """Inject item-logo divs into notable.html pointing at SVG placeholders."""
    html_path = os.path.join(BASE_DIR, 'notable.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = 0

    for html_title, artist in albums:
        fname = f"{slug(artist)}-{slug(html_title)}.svg"
        img_src = f"images/albums/{fname}"
        alt = f"{html_title} cover"
        title_escaped = re.escape(html_title)
        # Only inject if item-logo not already present before this title
        pattern = (
            r'(<a href="#" class="notable-item">)'
            r'(?!\s*<div class="item-logo">)'
            r'(<div class="item-content">\s*'
            r'<h3 class="item-title">' + title_escaped + r'</h3>)'
        )
        logo = (
            f'<div class="item-logo">'
            f'<img src="{img_src}" alt="{alt}" loading="lazy"'
            f' onerror="this.parentElement.style.display=\'none\'">'
            f'</div>'
        )
        replacement = r'\1' + '\n              ' + logo + r'\2'
        new_html, n = re.subn(pattern, replacement, html, count=1)
        if n:
            html = new_html
            changed += 1
        else:
            # Already has logo or pattern not found — skip silently
            pass

    for name in artists:
        fname = f"{slug(name)}.svg"
        img_src = f"images/artists/{fname}"
        alt = f"{name} photo"
        name_escaped = re.escape(name)
        pattern = (
            r'(<a href="#" class="notable-item">)'
            r'(?!\s*<div class="item-logo">)'
            r'(<div class="item-content">\s*'
            r'<h3 class="item-title">' + name_escaped + r'</h3>)'
        )
        logo = (
            f'<div class="item-logo">'
            f'<img src="{img_src}" alt="{alt}" loading="lazy"'
            f' onerror="this.parentElement.style.display=\'none\'">'
            f'</div>'
        )
        replacement = r'\1' + '\n              ' + logo + r'\2'
        new_html, n = re.subn(pattern, replacement, html, count=1)
        if n:
            html = new_html
            changed += 1

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  notable.html updated: {changed} items injected.")


def main():
    albums_dir = os.path.join(BASE_DIR, 'images', 'albums')
    artists_dir = os.path.join(BASE_DIR, 'images', 'artists')
    os.makedirs(albums_dir, exist_ok=True)
    os.makedirs(artists_dir, exist_ok=True)

    print("Generating album placeholders...")
    for html_title, artist in ALBUMS:
        fname = f"{slug(artist)}-{slug(html_title)}.svg"
        dest = os.path.join(albums_dir, fname)
        if os.path.exists(dest):
            print(f"  [SKIP] {fname}")
            continue
        label = initials(html_title)
        color = pick_color(html_title + artist)
        svg = make_svg(label, color)
        with open(dest, 'w') as f:
            f.write(svg)
        print(f"  {fname}")

    print("\nGenerating artist placeholders...")
    for name in ARTISTS:
        fname = f"{slug(name)}.svg"
        dest = os.path.join(artists_dir, fname)
        if os.path.exists(dest):
            print(f"  [SKIP] {fname}")
            continue
        label = initials(name)
        color = pick_color(name)
        svg = make_svg(label, color)
        with open(dest, 'w') as f:
            f.write(svg)
        print(f"  {fname}")

    print("\nUpdating notable.html...")
    update_html(ALBUMS, ARTISTS)

    print(f"\nDone. {len(ALBUMS)} album + {len(ARTISTS)} artist placeholders.")


if __name__ == '__main__':
    main()
