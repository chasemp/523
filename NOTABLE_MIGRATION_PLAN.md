# Notable Page Migration Plan

## Overview
This document outlines the plan to complete the migration of the "Notable" page (formerly "likes.html", now "notable.html") with a focus on populating the Books sections with titles and images from Amazon links.

## Current State

### Completed Tasks
1. ✅ Renamed `likes.html` to `notable.html`
2. ✅ Removed the following items from the page:
   - Audible, Keychron K2, Herman Miller Aeron, Vercel, Raycast, Linear, Atomic Habits, The Lean Startup
3. ✅ Added new items:
   - Rainflow to "Music & Media" section
   - Blockdoku to new "Games" section
   - Venty Fan to "Products" section
4. ✅ Restructured the Books section into:
   - Authors
   - Fiction Books
   - Nonfiction Books
   - Book Series
5. ✅ Added initial content:
   - Authors: David & Leigh Eddings, Simon R Green
   - Fiction Books: A Christmas Carol (placeholder)
   - Nonfiction Books: The Pragmatic Programmer (placeholder)
   - Book Series: The Belgariad by David Eddings

### Books Already Processed
The following books have been successfully scraped from Amazon (need to be added to notable.html):

1. **The Spectrum: How to Customize a Way of Eating and Living Just Right for You and Your Family**
   - Authors: Dean Ornish MD and Art Smith
   - Category: Nonfiction (Health & Fitness)
   - URL: https://www.amazon.com/gp/product/B07B77FQPX

2. **The Stranger in the Woods: The Extraordinary Story of the Last True Hermit**
   - Authors: Michael Finkel
   - Category: Nonfiction (History, Americas, United States)
   - URL: https://www.amazon.com/gp/product/B000W96648

3. **Long Walk to Freedom: The Autobiography of Nelson Mandela**
   - Author: Nelson Mandela
   - Category: Nonfiction (Biography/Politics)
   - URL: https://www.amazon.com/gp/product/B0015T6G2G

4. **Switch: How to Change Things When Change Is Hard**
   - Authors: Chip Heath and Dan Heath
   - Category: Nonfiction (Business/Self-Help/Change Management)
   - URL: https://www.amazon.com/gp/product/B0030DHPGQ

5. **Currently loading:** https://www.amazon.com/gp/product/B00LZ7GQJQ

## Remaining Work

### Phase 1: Continue Book Scraping
Use MCP Playwright to visit each remaining Amazon book link and extract:
- Book title
- Author(s)
- Cover image URL
- Category (to determine Fiction vs Nonfiction)

### Phase 2: Categorize Books
Based on the extracted information, categorize each book as either:
- **Fiction**: Novels, stories, literature
- **Nonfiction**: Biographies, business, self-help, history, technical books, etc.

### Remaining Amazon Book URLs to Process

```
https://www.amazon.com/gp/product/B00LZ7GQJQ (currently in progress)
https://www.amazon.com/gp/product/B00N9YPW5C
https://www.amazon.com/gp/product/B002XHNMW6
https://www.amazon.com/gp/product/B006TIPA02
https://www.amazon.com/gp/product/B00C2WDD5I
https://www.amazon.com/gp/product/B000FCKPHG
https://www.amazon.com/gp/product/B000QEOVG4
https://www.amazon.com/gp/product/B005FFPMWG
https://www.amazon.com/gp/product/B004J4WKEC
https://www.amazon.com/gp/product/B003062GEE
https://www.amazon.com/gp/product/B00DQ845EA
https://www.amazon.com/gp/product/B0042AMGDI
https://www.amazon.com/gp/product/B00985E3UG
https://www.amazon.com/gp/product/B01N6Z44OZ
https://www.amazon.com/gp/product/B07BF6BVWK
https://www.amazon.com/gp/product/B078M1TL92
https://www.amazon.com/gp/product/B006DVPWX0
https://www.amazon.com/gp/product/B00ACC5Z1U
https://www.amazon.com/gp/product/B09QHC1LMW
https://www.amazon.com/gp/product/B00FUZQYBO
https://www.amazon.com/gp/product/B004DI7HZ6
https://www.amazon.com/gp/product/B0BPN31YLB
https://www.amazon.com/gp/product/B07DH1QYJK
https://www.amazon.com/gp/product/B004GTLSJS
https://www.amazon.com/gp/product/B0B3755RV9
https://www.amazon.com/gp/product/B00IHGVQ9I
https://www.amazon.com/gp/product/B01IKSX8H0
https://www.amazon.com/gp/product/B0824B49LS
https://www.amazon.com/gp/product/B0DFV1HS1R
https://www.amazon.com/gp/product/B0D1872KMV
https://www.amazon.com/gp/product/B0CQHLFX6Y
https://www.amazon.com/gp/product/B0B1QV6NF7
https://www.amazon.com/gp/product/B01G1K1GAE
https://www.amazon.com/gp/product/B09WVF6Q2W
https://www.amazon.com/gp/product/B00SXHFVLG
```

### Phase 3: Update notable.html Structure
The `notable.html` file needs to be updated with the following structure:

```html
<section class="likes-section">
    <h2>Authors</h2>
    <div class="likes-grid">
        <!-- Existing: David & Leigh Eddings -->
        <!-- Existing: Simon R Green -->
    </div>
</section>

<section class="likes-section">
    <h2>Fiction Books</h2>
    <div class="likes-grid">
        <!-- Existing: A Christmas Carol -->
        <!-- Add fiction books from the list -->
    </div>
</section>

<section class="likes-section">
    <h2>Nonfiction Books</h2>
    <div class="likes-grid">
        <!-- Existing: The Pragmatic Programmer -->
        <!-- Add: The Spectrum -->
        <!-- Add: The Stranger in the Woods -->
        <!-- Add: Long Walk to Freedom -->
        <!-- Add: Switch -->
        <!-- Add all other nonfiction books -->
    </div>
</section>

<section class="likes-section">
    <h2>Book Series</h2>
    <div class="likes-grid">
        <!-- Existing: The Belgariad -->
        <!-- Could add more series from Goodreads if desired -->
    </div>
</section>
```

### Phase 4: HTML Entry Format
Each book entry should follow this format:

```html
<div class="likes-item">
    <div class="item-logo">
        <img src="BOOK_COVER_IMAGE_URL" alt="BOOK_TITLE cover">
    </div>
    <div class="item-content">
        <h3><a href="AMAZON_URL" target="_blank">BOOK_TITLE</a></h3>
        <p>by AUTHOR_NAME(S)</p>
    </div>
</div>
```

## Technical Details

### Using MCP Playwright for Book Scraping
1. Navigate to each Amazon book URL
2. Wait for the page to load
3. Take a snapshot to identify the book details
4. Extract:
   - Title from the product title element
   - Author from the author link/byline
   - Cover image from the book cover image element
   - Category from breadcrumb or product details

### Handling Amazon Bot Detection
- Amazon may occasionally show bot detection pages
- If this happens, try:
  1. Clicking the "Continue shopping" button if available
  2. Waiting a few seconds between requests
  3. Taking screenshots to see the actual page state

### CSS Styling
The existing `likes.css` file already has the necessary styling:
- `.likes-item` for the container
- `.item-logo` for the book cover image (64x64px on desktop, 48x48px on mobile)
- `.item-content` for the text content
- Responsive design for mobile screens

## Step-by-Step Execution Plan

1. **Continue Playwright scraping** for all remaining URLs
   - Navigate to each URL
   - Extract book information
   - Store results in a structured format (array/JSON)

2. **Categorize all books** into Fiction vs Nonfiction
   - Review category information from Amazon
   - Make manual adjustments if needed

3. **Update notable.html** with all book entries
   - Add books to appropriate sections (Fiction/Nonfiction)
   - Use the proper HTML structure with book cover images
   - Include proper links to Amazon pages

4. **Test the page**
   - Check that all images load correctly
   - Verify all links work
   - Test responsive design on mobile

5. **Commit and push changes**
   ```bash
   git add notable.html
   git commit -m "Add complete book listings to Notable page"
   git push
   ```

## Notes
- The file `likes.html` should be renamed to `notable.html` (if not already done)
- Navigation links in other pages (index.html, etc.) may need to be updated to point to `notable.html` instead of `likes.html`
- Consider adding a description or category tag to books if desired
- Book cover images should be Amazon's CDN URLs (they're reliable and fast)

## Current Playwright Session
There's an active Playwright browser session that has successfully navigated to 5 Amazon book pages. You can continue from where it left off or restart fresh.

## Fallback Options
If Amazon bot detection becomes a persistent issue:
1. Use a different tool/method to get book data (e.g., Goodreads API, manual entry)
2. Add delays between requests
3. Consider using book ISBNs to look up data from other sources
4. Manually curate a smaller subset of the most important books

## Success Criteria
- ✅ All books from the provided URLs are added to notable.html
- ✅ Books are correctly categorized as Fiction or Nonfiction
- ✅ All book entries have cover images displayed
- ✅ All links work correctly
- ✅ Page is responsive and looks good on mobile
- ✅ Changes are committed and pushed to git

