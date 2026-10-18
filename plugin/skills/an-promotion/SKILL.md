---
name: an-promotion
description: "Use for the brand kit, profiles, the website, listings and posts: drafted from facts, each waiting for the owner's yes."
---

# an-promotion

Sections: b-business-manager; b-business-manager; b-business-manager.

## b-business-manager
(procedure file: sop-presence.txt)

Procedure: b-business-manager. Profiles and the brand kit. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Goes with: `an-office-manager`, `an-promotion` (b-business-manager), `an-promotion` (b-business-manager)
Read this when a LinkedIn page, an X account or another profile comes up, or when they need a logo, a tagline or a short description. Then leave it.

THE BRAND KIT FIRST (brand/ in the business folder, made once, used everywhere)
Everything public is copied from this kit, so it all says the same thing.
- Logo: a square version (at least 400 x 400; 1200 x 1200 is better) for profile pictures, and a wide one if they want. b-analyst can draft concepts; they choose. Keep the original files.
- Colors and a font or two, written down.
- Descriptions: one line (under 120 characters, a tagline), 25 words, 50 words, 100 words. Plain, true, no hype.
- Fact sheet: the only facts anyone may state publicly (what it is, who it's for, price if set, where to get it, contact). Nothing in it they haven't confirmed.
- About them: a short bio (40 words) and a longer one (120 words), in their words, true.
- Pictures: the product (real photos once there is one; renders clearly called renders before that), and one of them if they're willing.
- Banner images sized for each profile (below).

THE PROFILES (one at a time, the ones that fit their buyers)
For each: they create the account and sign in themselves (never type a password); you give them every field filled in from the kit, and the exact sizes.
- LinkedIn company page (https://www.linkedin.com/company/setup/new/ ; needs a personal LinkedIn profile first). Name, page address, industry (a product business is often Consumer Goods or the product's own industry; product development services fit Engineering Services), organization type (Privately held, or Self-employed), logo (square, 400 x 400 or more), tagline (120 characters max), cover image (1128 x 191), the 100-word description, website. Their own profile: add the role, e.g. "Founder", under the company.
- X (https://x.com): handle as close to the business name as possible, profile picture (the square logo), header (1500 x 500), bio (160 characters: the one-liner + the site), the website link, a pinned post.
- Facebook page and Instagram (Meta): useful for consumer products and local buyers; same picture, banner sized for each, the 50-word description.
- YouTube: for demo videos; channel name, picture, banner, description.
- Google Business Profile: only if they have a public location or serve a local area.
- Places their buyers are: a store page (Amazon, Etsy), an industry directory, a marketplace. Ask who buys it first.
Same name, picture, one-liner and website link on every one. Record each profile's address and the date in business.txt.

RULES
Their voice, always clear it's them. Never create accounts or accept terms for them. No fake followers, reviews or likes. A profile that would show an unfiled invention: the patent check first (`an-promotion` (b-business-manager)).

Sources: LinkedIn pages help https://www.linkedin.com/help/linkedin/topics/6227/6228 ; X help https://help.x.com ; Google Business Profile https://support.google.com/business .

## b-business-manager
(procedure file: sop-website.txt)

Procedure: b-business-manager. Domain, website, email and search. Revision 2 — October 18, 2026.
Index: the procedure index in `an-office`
Goes with: `an-office-manager`, `an-promotion` (b-business-manager)
Read this when the domain, a website, a business email, or being found on Google and Bing comes up. Then leave it.

WHY
A simple, honest website is where every post, profile and listing points. It doesn't need to be fancy: what it is, who it's for, a picture, how to reach them. Set up once for the business; each product gets a page.

1. THE DOMAIN
- Pick it with the name (`an-business-record` (b-business-manager)). Expect the plain name to be taken; nine times out of ten it is. That's normal; don't sweat it. The choices: another ending (.co, .net, .shop, .us or one that fits the product), or keep .com and add something: "llc", a word like "co" or "shop", the product or the town. It's expected and it happens.
- What matters: they can say it over the phone without spelling games. People rarely memorize web addresses; they type it once and bookmark it, like a phone number. A decent, sayable address beats a clever one.
- Prefer an added word over hyphens or numbers; those are the hardest to say over the phone.
- A .com doesn't rank better in search than other endings; pick on sayability.
- Same name as the company and the social handles where possible; check all three together.
- If a close variant is cheap (the .com with and without "llc", a common misspelling), buying it too is optional insurance; it doesn't have to be used.
- Name the domain for the company, not one product; products get pages.
- Check it's free at a registrar before falling in love with it.
- They buy it themselves at a registrar (Cloudflare, Namecheap, Porkbun and others; about $10 to $20 a year). Turn on auto-renew and the registrar's privacy option. Record the registrar and renewal date in business.txt and actions.csv.

2. THE WEBSITE (simplest that works)
- Pages: Home (what it is, in a sentence, with a picture), the product (one page each), About (who they are, honestly), Contact (an email address or form). Add a privacy policy page if the site collects anything, even an email list.
- Easiest for most: a site builder (Squarespace, Wix, Carrd and similar), drag and drop, about $10 to $25 a month, which also connects the domain for them.
- Free and in their own hands: GitHub Pages (https://pages.github.com/) from a public website repository b-analyst builds and updates on request. Never publish the private an-creation repository; the website is its own, public repository with only what they approved.
- Say nothing on the site that isn't true or that they haven't approved. No made-up customers, results, prices or certifications. Before an invention is shown publicly, the patent check in `an-promotion` (b-business-manager).
- HTTPS (the padlock) on: builders and GitHub Pages do it; check the site opens with https://.

3. BUSINESS EMAIL
An address at their domain (name@theirdomain.com) looks real. Google Workspace or Microsoft 365 (paid, about $6 to $8 a month), or the email forwarding most registrars include free. They set it up and sign in themselves.

4. BEING FOUND (search)
Once the site is up:
- Google Search Console, https://search.google.com/search-console : they sign in with the Google account that should own the site. Add a "Domain" property, verify it (the registrar or DNS provider's option, or a TXT record they add), submit the sitemap (most builders make one at /sitemap.xml), and request indexing for the home page.
- Bing Webmaster Tools, https://www.bing.com/webmasters : they sign in; "Import from Google Search Console" brings the site and sitemap over. Bing also feeds DuckDuckGo, Yahoo and ChatGPT search.
- Every page: a clear title and a one-line description (builders have a field for it). One address: www and the bare domain should go to the same place.
- Log what's verified and submitted in promo-log.csv or plan.md.
Every sign-in, "Allow access" screen or terms page: stop and ask first; they sign in; never type a password.

5. WEEKLY CHECK (once a week, short)
Search Console and Bing: pages found vs. pages in the sitemap, any new errors (and which page), the top search terms. Three lines to the inventor; "No change" if nothing changed. A fix on the site goes to b-analyst, with their yes.

Sources: Google Search Console start https://support.google.com/webmasters/answer/9128668 ; sitemaps https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview ; SEO starter guide https://developers.google.com/search/docs/fundamentals/seo-starter-guide ; Bing Webmaster https://www.bing.com/webmasters ; GitHub Pages https://docs.github.com/en/pages .

## b-business-manager
(procedure file: sop-promotion.txt)

Procedure: b-business-manager. Promotion and listings. Revision 3 — October 18, 2026.
Index: the procedure index in `an-office`
Goes with: `an-office-manager`, `an-promotion` (b-business-manager) (the brand kit is the only source of wording)
Read this when they want to get the word out: posts, replies, groups, press, directories, a launch. Then leave it.

BEFORE ANYTHING ABOUT AN INVENTION GOES PUBLIC
Check Office files for that invention: is a patent filing planned, and is it filed? If one is planned and nothing is filed, say plainly: "Showing it publicly before a patent filing can affect your rights. Let's settle the patent decision first: file a provisional, keep it quiet, or skip it." (`an-principles-bm` (Decide on the patent before showing it publicly)) Record their decision. Business posts that don't show the invention can go ahead.

WHERE TO PROMOTE (pick the few where their buyers actually are; ask who buys it first)
- LinkedIn: their own posts and the company page; good for business buyers, suppliers, investors, and the founder's story.
- X: short posts, replies in relevant conversations, a pinned post; good for tech, makers, early adopters.
- Reddit: the subreddit for their product's use (fishing, gardening, robotics...), and r/inventors, r/SideProject; read each subreddit's rules first; many ban self-promotion or allow it only on set days.
- Facebook groups and Instagram: hobby and local groups, consumer products.
- YouTube and short video (TikTok, Reels, Shorts): a 30 to 60 second demo often does more than any post.
- Forums and communities for the product's field.
- Inventor and small-business groups: United Inventors Association (https://www.uiausa.org), local inventor clubs, SCORE (https://www.score.org), Small Business Development Centers (https://americassbdc.org), library maker and business programs, makerspaces.
- Maker and hardware press that take tips (Hackaday, Make:), local news, trade magazines and podcasts in their field: a short personal email with the 100-word description.
- Product Hunt, Hacker News (Show HN): only for something people can try now, on a day they pick.
- Crowdfunding (Kickstarter, Indiegogo): a launch of its own; the patent check first, and only with a cost and delivery plan from b-project-manager.
- Trade shows and local events: when there's something to show or sell.
- An email list on their site: the one audience they own.

THE LOOP (every time)
1. Look for fresh, relevant places and conversations (the last week or so).
2. Skip anything where a link would be spam, off-topic, hostile, or against the place's rules.
3. For each good one, start from the brand kit and make light edits only.
4. Bring up to 5 at a time, each like this:

   #1  [platform] [place / author]  [link]
   What it is: one line.
   Why it fits: one line.
   Planned text:
   """
   (exact text)
   """
   Image: none | brand/<file>
   OK to go?

5. Act only on a clear yes for that number. No, silence or edits: don't post; apply edits and show it again.
6. After a yes: post it if you can; if not, hand them the final text and image ready to paste. Log it (promo-log.csv) the same turn.
Every link must be complete and open the right page; never a cut-off link.

PACE AND HONESTY
- At most one new post per platform a day; never the same subreddit or group twice in a month; never the same text twice in a week; don't reply to the same person twice unless they reply.
- Their voice ("I built"), always clear it's them. Never pose as a customer or fan. No fake accounts, reviews, votes or paid likes.
- Only facts from the fact sheet. No claims of sales, users, results or certifications they don't have.
- Hostile replies: don't engage; tell them.

LISTINGS AND DIRECTORIES
Places that list products or tools like theirs: industry directories, marketplaces, local business lists, resource pages of groups above. Bring up to 5 at a time:

   #1  [site name]  [link]
   What it is: one line.
   Why it fits: one line.
   Needs: free form | account | email to editor
   Listing text: """(from the brand kit)"""
   OK to go?

Skip paid "featured" listings, badges on their site, link swaps and anything that looks like spam; a few good listings beat many weak ones.

RECORD
promo-log.csv: date, platform, place, post_id, image, link, status (proposed, approved, posted, handed over, declined), replies, results, notes. Results only from what the platform shows; never estimated.

Sources: FTC endorsement guides https://www.ftc.gov/business-guidance/advertising-marketing/endorsements-influencers-reviews ; Reddit self-promotion guidance https://support.reddithelp.com/hc/en-us/articles/360043504051 ; USPTO on public disclosure and patents https://www.uspto.gov/patents/basics .
