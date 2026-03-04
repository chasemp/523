# 523
523 homepage — [523.life](https://523.life)

## Analytics

This site uses [Umami](https://umami.is) for visitor tracking. Umami is open source ([GitHub](https://github.com/umami-software/umami)) and privacy-focused:

- No cookies, no personal data collected
- GDPR/CCPA compliant by design
- Data is not sold or shared with third parties
- All data is automatically purged after **6 months**
- Hosted on Umami Cloud (`cloud.umami.is`)

The tracking script is included in the `<head>` of every HTML page:

```html
<script defer src="https://cloud.umami.is/script.js" data-website-id="ee320cd6-44bc-4ecc-9da8-3dcd4c413edd"></script>
```

### For future agents: keeping tracking complete

Every `.html` file at the root of this repo must include the Umami script above in its `<head>` section. When adding a new page:

1. Confirm all root-level HTML files have the script:
   ```bash
   grep -L 'umami.is/script.js' *.html
   ```
   Any files printed by that command are missing the tracker — add it.

2. Place the script tag as the last element before `</head>`, after any stylesheet `<link>` tags.

3. Use the **same `data-website-id`** shown above — do not create a new Umami site.
