# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal website (523.life) built as a static site with vanilla HTML, CSS, and JavaScript. The site includes a homepage, about page, notable items page (products, books, tools), and projects showcase. It features a dark/light theme toggle with cross-domain cookie support and a collapsible section system for the notable page.

## Repository Structure

- **Root HTML files**: `index.html`, `about.html`, `notable.html`, `projects.html`
- **Styles**: `style.css` (global), `notable.css` (for notable/about/projects pages)
- **JavaScript**: `script.js` (theme toggle, dropdown functionality, collapsible sections)
- **Images**: `/images/` directory
- **Drafts**: `/drafts/` directory containing blog posts and essays
  - `/drafts/blog/` - Blog post drafts
  - `/drafts/essay/` - Long-form essay drafts
  - `/drafts/samples/` - Sample content
  - `/drafts/WRITING_STYLE_GUIDE.md` - Comprehensive writing guidelines

## Development Workflow

### No Build System
This is a static site with no build step, package manager, or bundler. Files are edited directly and deployed as-is. There is no `package.json`, no npm scripts, no compilation.

### Local Development
Serve the site using any local web server:
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

### Deployment
This is a GitHub Pages site. Changes to the `main` branch automatically deploy to 523.life via the CNAME file configuration.

## Key Architecture Patterns

### Theme System
- CSS custom properties (CSS variables) define light/dark themes in `:root`
- JavaScript in `script.js` manages theme state via cookies with `.523.life` domain
- Cookie persists theme preference across all subdomains
- Theme toggle button in top-right corner of all pages
- Default theme is dark (`data-theme="dark"`)

### Page Structure
All pages share common elements:
- Theme toggle button (`#theme-toggle`)
- Container with breadcrumb navigation (except homepage)
- Footer with back link and copyright
- Deferred script loading (`<script src="script.js" defer>`)

### Notable Page Features
The notable page (`notable.html`) has special collapsible functionality:
- Sections can be collapsed/expanded by clicking title
- Items beyond first row are hidden with "more..." button
- Responsive grid: 3 columns (desktop), 2 columns (tablet), 1 column (mobile)
- Section item counts must be manually updated when adding/removing items
- Comments in HTML remind to update counts: `<!-- UPDATE THIS COUNT when adding/removing items -->`

### JavaScript Architecture
`script.js` contains three main systems:
1. **Theme Management**: Cookie-based theme persistence and toggle
2. **Dropdown System**: Generic dropdown with auto-direction (dropup/dropdown based on viewport space)
3. **Collapsible Sections**: Notable page-specific functionality (checks `document.title.includes('Notable')`)

## Writing Guidelines

When working on content in `/drafts/`, follow the comprehensive style guide at `/drafts/WRITING_STYLE_GUIDE.md`. Key principles:

### Voice & Tone
- Conversational but professional
- Personal reflection, not academic or preachy
- Specific over abstract - use concrete examples and lived experience
- Show through stories, don't tell through instruction

### What to Avoid
- Em-dashes as crutch (4-5 per essay maximum)
- "Just" as minimizer
- Hedging language: "I think," "I believe," "I feel like"
- Repetitive "intentional/intentionality/explicitly"
- "In my opinion," "In my view," "To me," "For me"
- Clinical language in personal contexts ("impacted" → "shaped")
- Telling after showing (delete explanatory sections after narratives)

### What to Embrace
- Three-part lists (Rule of Three)
- Fragment sentences for emphasis
- Memory framing: "I remember," "I heard"
- Emotional texture and specific details
- Acknowledge trade-offs honestly
- Show grace and growth

## Content Management

### Adding Items to Notable Page
When adding items to sections in `notable.html`:
1. Add the new item HTML within the appropriate `<section class="notable-section">`
2. Update the count in `<span class="section-title-count">X</span>` for that section
3. HTML comments remind you: `<!-- IMPORTANT: When adding/removing items, update the count in section-title-count below -->`

### Item Structure
Notable items follow this pattern:
```html
<a href="URL" class="notable-item" target="_blank" rel="noopener">
  <div class="item-content">
    <h3 class="item-title">Title</h3>
    <p class="item-category">Category</p>
    <p class="item-description">Description text</p>
  </div>
</a>
```

Or for items with logos/actions (projects):
```html
<div class="notable-item">
  <div class="item-logo">
    <img src="logo.png" alt="Logo">
  </div>
  <div class="item-content">
    <h3 class="item-title">Title</h3>
    <p class="item-category">Category</p>
    <p class="item-description">Description</p>
  </div>
  <div class="item-actions">
    <a href="URL" class="item-link">Visit</a>
  </div>
</div>
```

## External Projects Referenced

The site links to several related projects on subdomains:
- **timeline.523.life**: Timeline of life events
- **rainflow.523.life**: Ambient audio web app
- **blockdoku.523.life**: Progressive Web App puzzle game
- **mealplanner.523.life**: Meal planning tool
- **zNotch**: macOS utility (github.com/chasemp/znotch)

## Design Philosophy

The site emphasizes:
- **Minimalism**: No frameworks, no build tools, minimal dependencies
- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation
- **Performance**: Lightweight, fast loading, efficient JavaScript
- **Cross-domain consistency**: Theme persistence across all 523.life subdomains
- **Responsive design**: Mobile-first approach with breakpoints for tablet/desktop
