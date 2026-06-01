# Personal website on Academic Pages

This repo is aimed to assist members of the Bristol Glaciology Centre in creating a minimal working personal website, built in Jekyll using the [Minimal Mistakes template](https://github.com/academicpages/academicpages.github.io).

> NB: This works as of July 2026, but is not planned on being maintained. Bristol Glaciology Group members who find this broken in the future can try and contact Tom and Fabien for help, but no guarantees are made!

1. Fork this repository, and rename it in the format `yourusername.github.io` (replacing `yourusername` with your user name).
2. Edit the content, editing pages and adding/deleting images as you desire.
   1. It is desirable to try and do this locally using Git command line workflows, but quick edits using the online GUI will be fine for learning.
3. Make available on GitHub pages via the Settings > Pages tab.


# Testing locally

Install Ruby dependencies:

```
bundle install
```

To build and serve the site locally:

```
bundle exec jekyll serve
```

The site will be available at http://localhost:4000

Building for Production

To build the site for production:

bundle exec jekyll build
The output will be in the _site/ directory.