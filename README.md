# Bristol Paleo Modelling Group website

The group's website, built with [Jekyll](https://jekyllrb.com/) and hosted on GitHub Pages.

**Live site:** https://paleo-modelling-bristol.github.io/website/

## Site structure

- `_pages/` — the 7 top-level pages: Home, Publications, Model Outputs, People, Group Socials, Group Meetings, Join Us.
- `_data/` — the content behind most pages, as plain YAML: `publications.yml`, `model_outputs.yml`, `positions.yml`, `seminars.yml`, `socials.yml`, `news.yml`, `navigation.yml`. Edit these to update text/lists without touching any page's markup.
- `_people/` — one file per person on the People page (see below).
- `_layouts/` + `_includes/` — the page templates (default page shell, person profile, nav, footer). Usually don't need touching unless you're changing the site's structure/design, not just its content.
- `assets/css/main.css` — all of the site's styling in one file.

## Editing content

Two ways to make changes, pick whichever suits the edit:

- **On GitHub.com** — open the file, click the pencil icon, edit, commit. No install needed, good for text/data changes.
- **Locally** — clone the repo, edit with any text editor, `git commit` + `git push`. Better when changing several files at once, or when you want to preview locally first (see "Testing locally" below).

Either way, pushing to `main` triggers GitHub Pages to rebuild automatically — changes go live within a minute or two.

## Adding/editing a person

Copy an existing file in `_people/` (e.g. `_people/yixuan.md`) as a starting point. Each file has two ways to show a profile — the comment block at the top of the file explains both:

1. **External link** — set `external_profile` to a URL (e.g. a University research portal page, Google Scholar). Only `name` and `role` matter; the card on `/people/` links straight out, and this file's own page just shows a "view profile" button.
2. **Internal page** — leave `external_profile` as `""` and fill in the rest of the fields, plus write a bio using Markdown headings (`## About`, `## Education`, `## Publications`, ...) below the front matter.

`section:` must be one of the five values defined in `_pages/people.md` (`pi` / `postdoc` / `pgr` / `visitor` / `old_friends`) — anything else silently won't appear on the People page.

`photo:` accepts either a full image URL (e.g. a Google Drive share link) or a local path starting with `/assets/images/...` (put the image file there first).

## Adding a new page

1. Create a new file in `_pages/`, e.g. `_pages/resources.md`, with front matter:
   ```yaml
   ---
   layout: default
   title: "Resources"
   permalink: /resources/
   ---
   ```
2. Add it to the nav bar by adding an entry to `_data/navigation.yml`:
   ```yaml
   - title: "Resources"
     url: /resources/
   ```

## Getting write access

Content changes require push access to this repo. Ask whoever currently maintains it to add you as a collaborator (Settings → Collaborators and teams), or fork the repo and open a Pull Request if you'd rather have your changes reviewed first.

> NB: This is maintained on a best-effort basis by group members. If something looks broken, check recent commits first, or reach out to whoever last touched the relevant file.

## Testing locally

Install Ruby dependencies:

```
bundle install
```

Build and serve the site locally:

```
bundle exec jekyll serve
```

The site will be available at http://localhost:4000

To build for production (output goes to `_site/`):

```
bundle exec jekyll build
```
