#!/usr/bin/env python3
"""
Fetch album art from MusicBrainz Cover Art Archive and artist images from Wikipedia.
Downloads images to images/albums/ and images/artists/, then updates notable.html.

Usage: python3 fetch_music_images.py
"""

import os
import re
import time
import json
import urllib.request
import urllib.parse
import urllib.error

USER_AGENT = "523.life-music-images/1.0 (https://523.life)"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Albums: (html_title, artist, optional_search_title)
# optional_search_title used when HTML title differs from MusicBrainz title
ALBUMS = [
    ("Sparkle and Fade", "Everclear", None),
    ("A/B", "Kaleo", None),
    ("Mind Control Acoustic", "Stephen Marley", None),
    ("No Jacket Required", "Phil Collins", None),
    ("Kickin' It", "Hamilton Loomis", None),
    ("Eat Ya Veggies", "bbno$", None),
    ("Freaks of Nature", "Drain STH", None),
    ("Jagged Little Pill", "Alanis Morissette", None),
    ("John Coltrane and Johnny Hartman", "John Coltrane", None),
    ("Greatest Hits", "Steve Miller Band", None),
    ("ZABA", "Glass Animals", None),
    ("A 20 Something Fuck", "Two Feet", None),
    ("The Hits / The B-Sides", "Prince", "The Hits/The B-Sides"),
    ("Don't Explain", "Beth Hart", None),
    ("Mescalito", "Ryan Bingham", None),
    ("Swimming", "Mac Miller", None),
    ("Live at Bonnaroo", "Warren Haynes", None),
    ("Tapestry", "Carole King", None),
    ("The Razors Edge", "AC/DC", None),
    ("Nothing But the Best", "Frank Sinatra", None),
    ("Trouble", "Ray LaMontagne", None),
    ("Facelift", "Alice in Chains", None),
    ("Violator", "Depeche Mode", None),
    ("Nowhere to Hide", "The Virus", None),
    ("Destruction by Definition", "The Suicide Machines", None),
    ("Live at the Old Quarter", "Townes Van Zandt", None),
    ("Moving Pictures", "Rush", None),
    ("2112", "Rush", None),
    ("Retrospective I & II", "Rush", "Retrospective I & II"),
    ("Rock Spectacle", "Barenaked Ladies", None),
    ("Let It Be Me", "Nina Simone", None),
    ("Rainbow", "Kesha", None),
    ("Lie to Me", "Jonny Lang", None),
    ("Live at the Regal", "B.B. King", None),
    ("Who Killed the Zutons", "The Zutons", None),
    ("Heartattack and Vine", "Tom Waits", None),
    ("Hell Freezes Over", "Eagles", None),
    ("Keep 'Em on They Toes", "Brent Cobb", None),
    ("Rage Against the Machine", "Rage Against the Machine", None),
    ("Grace", "Jeff Buckley", None),
    ("The Emancipation of Mimi", "Mariah Carey", None),
    ("Traveller", "Chris Stapleton", None),
    ("Metamodern Sounds in Country Music", "Sturgill Simpson", None),
    ("No Fences", "Garth Brooks", None),
    ("Pieces of You", "Jewel", None),
    ("The Boatman's Call", "Nick Cave and the Bad Seeds", None),
    ("Unplugged", "Eric Clapton", None),
    ("Whitey Ford Sings the Blues", "Everlast", None),
    ("Sublime", "Sublime", None),
    ("Bedtime Stories", "Madonna", None),
    ("Endless Summer Vacation", "Miley Cyrus", None),
    ("Where Have All the Merrymakers Gone?", "Harvey Danger", None),
    ("Metallica (Black Album)", "Metallica", "Metallica"),
    ("The River", "Bruce Springsteen", None),
    ("Texas Flood", "Stevie Ray Vaughan", None),
    ("No More Tears", "Ozzy Osbourne", None),
    ("Boston", "Boston", None),
    ("Dookie", "Green Day", None),
    ("Give Me Convenience or Give Me Death", "Dead Kennedys", None),
    ("The Four Seasons", "Vivaldi", None),
]

ARTISTS = [
    "Chris Stapleton",
    "Rush",
    "John Mellencamp",
    "Gov't Mule",
    "Tantric",
]


def slug(text):
    s = text.lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def album_filename(html_title, artist):
    return f"{slug(artist)}-{slug(html_title)}.jpg"


def artist_filename(name):
    return f"{slug(name)}.jpg"


def mb_request(url):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except Exception as e:
        print(f"    [ERR] {e}")
        return None


def download_url(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) > 2000:
            with open(dest, 'wb') as f:
                f.write(data)
            return True
    except Exception as e:
        print(f"    [ERR] {e}")
    return False


def search_release_mbid(album, artist):
    """Search MusicBrainz for release, return best-match MBID."""
    q = urllib.parse.quote(f'release:"{album}" artist:"{artist}"')
    url = f"https://musicbrainz.org/ws/2/release/?query={q}&limit=5&fmt=json"
    data = mb_request(url)
    time.sleep(1.1)
    if not data:
        return None
    try:
        j = json.loads(data)
        releases = j.get('releases', [])
        if releases:
            return releases[0]['id']
    except Exception as e:
        print(f"    [PARSE ERR] {e}")
    return None


def fetch_cover_art(mbid, dest):
    """Download 250px front cover from Cover Art Archive."""
    url = f"https://coverartarchive.org/release/{mbid}/front-250"
    ok = download_url(url, dest)
    time.sleep(0.5)
    return ok


def fetch_artist_image_wikipedia(name, dest):
    """Get artist thumbnail from Wikipedia REST API."""
    title = urllib.parse.quote(name.replace(' ', '_'))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    data = mb_request(url)
    time.sleep(0.5)
    if not data:
        return False
    try:
        j = json.loads(data)
        img_url = j.get('thumbnail', {}).get('source', '')
        if img_url:
            return download_url(img_url, dest)
    except Exception as e:
        print(f"    [PARSE ERR] {e}")
    return False


def update_html(album_results, artist_results):
    """
    Update notable.html: replace SVG placeholder src with downloaded JPG src
    for each successfully downloaded image.
    """
    html_path = os.path.join(BASE_DIR, 'notable.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = 0

    for html_title, artist, _ in ALBUMS:
        jpg_fname = album_filename(html_title, artist)
        if jpg_fname not in album_results:
            continue
        svg_src = f"images/albums/{slug(artist)}-{slug(html_title)}.svg"
        jpg_src = f"images/albums/{jpg_fname}"
        if svg_src in html:
            html = html.replace(svg_src, jpg_src, 1)
            changed += 1
        elif jpg_src not in html:
            print(f"  [WARN] No placeholder found for album: {html_title}")

    for name in ARTISTS:
        jpg_fname = artist_filename(name)
        if jpg_fname not in artist_results:
            continue
        svg_src = f"images/artists/{slug(name)}.svg"
        jpg_src = f"images/artists/{jpg_fname}"
        if svg_src in html:
            html = html.replace(svg_src, jpg_src, 1)
            changed += 1
        elif jpg_src not in html:
            print(f"  [WARN] No placeholder found for artist: {name}")

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\nHTML updated: {changed} SVG placeholders replaced with real images.")


def main():
    albums_dir = os.path.join(BASE_DIR, 'images', 'albums')
    artists_dir = os.path.join(BASE_DIR, 'images', 'artists')
    os.makedirs(albums_dir, exist_ok=True)
    os.makedirs(artists_dir, exist_ok=True)

    album_results = set()
    artist_results = set()

    print("=" * 60)
    print("PHASE 1: Album Art")
    print("=" * 60)
    for html_title, artist, search_title in ALBUMS:
        fname = album_filename(html_title, artist)
        dest = os.path.join(albums_dir, fname)

        if os.path.exists(dest):
            print(f"  [SKIP] {html_title} by {artist}")
            album_results.add(fname)
            continue

        search = search_title or html_title
        print(f"  Searching: {search} by {artist}")
        mbid = search_release_mbid(search, artist)
        if mbid:
            ok = fetch_cover_art(mbid, dest)
            if ok:
                print(f"    -> {fname}")
                album_results.add(fname)
            else:
                print(f"    -> no cover art for mbid={mbid}")
        else:
            print(f"    -> no MusicBrainz match")

    print()
    print("=" * 60)
    print("PHASE 2: Artist Images")
    print("=" * 60)
    for name in ARTISTS:
        fname = artist_filename(name)
        dest = os.path.join(artists_dir, fname)

        if os.path.exists(dest):
            print(f"  [SKIP] {name}")
            artist_results.add(fname)
            continue

        print(f"  Fetching: {name}")
        ok = fetch_artist_image_wikipedia(name, dest)
        if ok:
            print(f"    -> {fname}")
            artist_results.add(fname)
        else:
            print(f"    -> no image found")

    print()
    print("=" * 60)
    print("PHASE 3: Update notable.html")
    print("=" * 60)
    update_html(album_results, artist_results)

    print()
    print(f"Albums downloaded: {len(album_results)}/{len(ALBUMS)}")
    print(f"Artists downloaded: {len(artist_results)}/{len(ARTISTS)}")


if __name__ == '__main__':
    main()
