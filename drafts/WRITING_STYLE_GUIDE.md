# Writing Style Guide for LLM Assistance
*Based on collaborative essay writing experience*

## Core Principles

### Voice & Tone
- **Conversational but professional** - Personal reflection, not academic or preachy
- **Earnest and honest** - Acknowledge trade-offs, don't oversell
- **Specific over abstract** - Concrete examples, lived experience, named moments
- **Show, don't tell** - Stories demonstrate principles; avoid repetitive instruction

### Key Mantras
1. **The essay is the opinion** - Don't need "in my opinion" throughout when the whole piece is personal
2. **Stories carry authority** - Don't undercut with hedging language ("I think," "I believe")
3. **Emotional texture over clinical distance** - "Shaped" not "impacted," "misty-eyed" not "emotional"
4. **Intentionality without repetition** - Demonstrate through structure, don't hammer it verbally

---

## What to Avoid

### 1. Stylistic Tics to Watch

#### **Em-dashes (—)**
- **Issue:** Can become a crutch; 27 uses becomes distracting
- **Solution:** Vary with commas, periods, colons, parentheses
- **Keep for:** True dramatic pause or strong contrast (4-5 per essay is fine)
- **Example fixes:**
  - `line, one of those "birds"` not `line—one of those "birds"`
  - `(around service-oriented architecture)` not `—around service-oriented architecture—`

#### **"Just" as minimizer**
- **Issue:** Weakens statements, adds no meaning (found 9 times initially)
- **Cut where possible:**
  - ❌ `just look at open source` → ✅ `look at open source`
  - ❌ `You're just processing data` → ✅ `You're processing data`
  - ❌ `just as deep, work just as effective` → ✅ `as deep, work as effective`
- **Keep when it adds casualness:** "just chatting over tea" (works with the tone)

#### **Hedging language: "I think," "I believe," "I feel like"**
- **Issue:** Undercuts authority when speaking from 15 years experience
- **Cut where you're stating from experience:**
  - ❌ `I think part of it goes back` → ✅ `Part of it goes back`
  - ❌ `I think that experience normalized` → ✅ `That experience normalized`
- **Keep when genuinely speculating or being diplomatic**

#### **"Intentional/intentionality/explicitly"**
- **Issue:** Found 10+ times; becomes preachy telling vs. showing
- **Solution:** Say it once or twice, demonstrate through structure/examples
- **Delete entire sections** that just repeat "you have to be intentional" after stories already showed it

#### **"In my opinion," "In my view," "To me," "For me"**
- **Issue:** The entire essay is personal perspective; these become redundant
- **Cut 50-75% of these:**
  - ❌ `In my opinion, it's not cheaper` → ✅ `It's not cheaper`
  - ❌ `In my view, remote work is` → ✅ `Remote work is`
- **Keep 1-2 for critical framings:** "Here's my opinion: you're never going to have everyone..."

---

### 2. Word Choice Preferences

#### Choose Warm Over Clinical
- **Shaped** > impacted (when talking about personal life)
- **Connection** > collaboration (in personal contexts)
- **Paused** > stopped (more deliberate)
- **Get-togethers** > meetings (when informal)

#### Choose Active Over Passive
- **They saw** > They believed (more direct)
- **Bolstered by** > required (softer when not absolute)
- **Distributed realities** > distributed work (more human)

#### Choose Concrete Over Abstract
- ✅ "Eating lunch with my daughters at the table for half an hour"
- ❌ "Spending quality family time"

---

### 3. Structural Patterns to Avoid

#### Repetitive "Remote work" sentence starts
- **Found:** 7 paragraphs starting with "Remote work..."
- **Solution:** Vary sentence structures naturally
- **User preference:** "For now I'm ok with it considering the topic"

#### Telling after showing
- **Problem:** Section that explains "you need to be explicit" after stories already demonstrated it
- **Solution:** Delete explanatory sections that repeat what narratives proved
- **Example:** Deleted entire "Intentionality in Any Context" section - redundant

#### Trendy jargon
- ❌ "overwhelm" (as a noun)
- ❌ "non-office" without quotes (mark wordplay clearly)
- ✅ Use sparingly, signal intentional playfulness

---

## What to Embrace

### 1. Rhetorical Devices That Work

#### Three-part lists (Rule of Three)
- **Use freely** - Strong, memorable, satisfying rhythm
- **Examples:**
  - "build trust, share ideas, solve problems"
  - "building trust, building rapport, understanding what other people care about"
  - "do good work, build good teams, and progress the mission"

#### Fragment sentences for emphasis
- **Use sparingly** - Creates impact through rhythm break
- **Examples that work:**
  - "That hit home."
  - "Remote or not."
  - "This is all fine."

#### Memory framing: "I remember," "I heard"
- **Use liberally** - Signals transition into specific story
- **Works well** - Sets up anecdotes naturally without pretension

---

### 2. Emotional and Personal Details

#### Add texture through specifics
- ✅ "He was misty-eyed as he said it, and I felt the same"
- ✅ "Eating lunch with my daughters at the table"
- ✅ "Black Friday in the whirlwind of a datacenter"
- ✅ "Pulled over on the side of the road with my family in the car"

#### Show grace and growth
- ✅ "We stayed in touch and have since gone to events together. I'm not bitter or indignant"
- ✅ Acknowledging former colleagues changed their minds shows maturity

#### Acknowledge trade-offs honestly
- ✅ "Not lovable, yet I knew what I was getting into"
- ✅ "It's not punitive against them"

---

### 3. Structure & Flow

#### Show before tell
1. **Open with concrete story** (5:30 AM shuffle, Red Hat father)
2. **Build proof** (maintenance window, bricklayer, telegraph history, open source)
3. **Share strategies** (IRC background, face time value, boundaries)
4. **Address challenges last** (managing remote, pandemic, not for everyone)

#### Group related themes
- **Keep challenges together** near end:
  - Managing Remote Teams
  - Pandemic Remote Was Different
  - Not For Everyone
- **User preference:** Pandemic section moved from early to late was better flow

#### Let conclusions breathe
- ✅ Final strong statements work: "Trust is necessary for change, and change is the only constant"
- ❌ Don't repeat main thesis 3+ times in conclusion

---

## Technical Preferences

### Format
- **YAML front matter** must be proper YAML, not markdown with escaped characters
- **Hyphenate compound adjectives:** "remote-first teams" not "remote first teams"
- **Quotes for wordplay:** "non-office" needs quotes to signal intentional coinage

### Grammar & Style
- **Commas for clarity:** "because X requires Y, knowledge workers..." (add comma after dependent clause)
- **Consistency:** If using contractions, use throughout; don't mix formal/informal tone
- **Avoid clinical passive:** "families" not "family" when inclusive of multiple families impacted

---

## Coverage Checklist
*For essay completeness - all points from discussion transcripts*

### ✅ Must Include:
- Personal motivation (family time)
- Concrete work examples (maintenance windows, on-call stories)
- Historical context (telegraph, open source)
- Boundaries and structure (closed door rule, daily rhythms)
- Social connection needs (IRC background, sitcom fallacy, face-time value)
- Management considerations (outcomes vs. time-in-seat)
- Pandemic differentiation (atypical, isolation vs. intentional)
- Practical alternatives (co-working spaces)
- Honest caveats (personality fit, trade-offs)

---

## Red Flags for LLM Assistance

### When reviewing LLM-generated content, flag:
1. **Repetition of key phrases** (count "intentional," "explicitly," etc.)
2. **Hedging when stating facts/experience** ("I think," "I believe" overuse)
3. **Clinical language in personal contexts** ("impacted" vs "shaped")
4. **Telling after showing** (explanatory section after narrative proved the point)
5. **Trendy jargon** without purpose ("overwhelm" as noun, "learnings")
6. **Stylistic tics** (em-dash count, "just" count)
7. **Missing emotional texture** (no specific details, generic descriptions)
8. **Defensive tone** where confidence is warranted (15 years experience needs no hedging)

---

## Revision Priorities

### HIGH: Must fix
- Technical errors (YAML, typos, grammar)
- Repetitive "intentional" language (10+ uses → 3-4)
- Weak "just" overuse (9 uses → 3-4)
- Telling after showing (delete redundant sections)

### MEDIUM: Should consider
- Hedging language (6 "I think" → 2-3)
- Personal qualifiers (7 "to me/for me" → 3-4)
- Em-dash overuse (27 → 5-6)
- Awkward phrasings

### LOW: User preference
- Remote work sentence starts (acceptable for topic-focused essay)
- "Yet" vs "but" (keep user's voice)
- Wordplay like "non-office" (keep but mark with quotes)
- "Overwhelm" as noun (keep if user likes it)

---

## Example Transformations

### Before & After (Voice)
❌ **Before:** "This isn't a manifesto or how-to guide. It's a personal reflection on defining remote work as a lifestyle that has impacted myself and my family."

✅ **After:** "This is a personal reflection on remote work as a lifestyle that has shaped my life and families."

*Why: Removed unnecessary hedge ("isn't a..."), simplified "defining...as," warmed "impacted" to "shaped," corrected "myself" to "my life," made inclusive "families"*

---

### Before & After (Showing vs Telling)
❌ **Before:** 
```
Team building and teamwork are foundational, whether you're remote or not. 
My feeling is you want to be explicit about it in either case. 
Remote is just one flavor of that.
```

✅ **After:** *Delete section entirely*

*Why: Wikimedia leadership training story, MediaWiki summit story, and Sitcom Fallacy section already demonstrated these points through narrative*

---

### Before & After (Stylistic Tics)
❌ **Before:** "The connections can be just as deep, the work just as effective—"

✅ **After:** "The connections can be as deep, the work as effective"

*Why: Removed both weak "just"s and unnecessary em-dash*

---

## Notes for Iteration

- **User trusts their instincts** - When they keep something, they're usually right about their voice
- **Concrete > abstract always** - Black Friday datacenter beats "worked weekends"
- **Grace over grievance** - Showing growth (staying friends with former colleagues) > bitterness
- **Let personality through** - "Non-office" wordplay, "This is all fine" declarative, casual asides
- **Technical polish matters** - YAML errors and typos undercut otherwise strong content

---

*Version: 1.0 | Created: 2026-01-09 | Based on: Remote work essay collaboration*
