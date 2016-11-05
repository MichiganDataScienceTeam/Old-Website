# mdst.eecs.umich.edu

This repository holds the files for MDST's github pages website.

## Contributing


### Prerequisites
This website uses jekyll, and is hosted on amazon s3. Here are a list of things which must be installed in order for you to test this website locally and push your changes to the live site.


### Writing Posts

The MDST website has the nice feature of supporting blog posts. Here's how you do it.

#### Jekyll

Notice the `/_posts/` directory. Inside, you will find files with the format `YYYY-m-d-unique-title.md`. These are our blog posts, written in a markup language called `markdown`. Markdown files in our repository have the extension `.md`. Let's take a look at `/_posts/2016-5-20-new-website.md`.

```markdown
---
layout: post
title: "This is our New Website!"
excerpt: "... It's still a work in progress."
share: false
author: alex
image:
    feature: construction.png
tags: [website, news]
---

If you are reading this, then ...
```

Alright, don't be afraid, but there's a bit to unpack here. At the top of the file, we see a bunch of key-value pairs between two sets of three dashes `---`, one on line `1` and the other on line `10`. The syntax of these configuration options is `yaml` _(Yet Another Markdown Language)_, which is similar to `json` and `xml` in the way that it is merely a way of organizing data that humans can read quite easily. `yaml`.

Many of these options are pretty self explanatory, but I'll explain a few that aren't.

* __`tags` ::__ This is for search engine optimization. Think of them as keywords for a research paper.
* __`image` ::__ Here, I am using the `feature:` child value, and setting it equal to an image called `construction.png`. This adds a really wide picture to the top of the page. Replacing `feature:` with `heading:` will add the photo to the top of the post in a way which doesn't stretch across the top of the article. Try both out and pick which one you like. Be sure that the image you wish to display is located in `/images/`.
* __`author` ::__ This is a cool one. If you add your information to the `/_data/authors.yml` file, you will be able to specify your name in the `name:` variable and see that the post is credited to you.
* __`share` ::__ This should be set to `false` until further notice. We haven't configured these properly yet. Maybe one day.
* __`layout` ::__ This should always be `post`.
