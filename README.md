# mdst.eecs.umich.edu

This repository holds the files for MDST's github pages website.

## Contributing


### Prerequisites
This website uses [`jekyll`](https://jekyllrb.com/), and is hosted on Amazon S3. Here are a list of things which must be installed in order for you to test this website locally and push your changes to the live site.

* `s3cmd`: Can be installed via `brew` and `apt-get`.
* `jekyll`: Can be installed using RubyGems, which comes with an installation of `ruby`, which is pre-installed on MacOS. Install with `$ gem install jekyll bundler`
* `git`: If you haven't used git before, I'm sorry, but you were gonna have to learn it at some point.

### Writing Posts

The MDST website has the nice feature of supporting blog posts. Here's how you do it. If you don't want to think about any of this that hard, the easiest thing to do will be to look for a post similar to the one you want to write, copy it, and change the file name.

### Quick Start

If you just want to write a post as fast as possible, here's the quickest way to do that.

1. Make sure you download and install the pre-requisite programs listed above.
1. Clone this repository. If you have already cloned it and haven't updated recently, run `git pull` in the folder to update.
    1. `$ git clone https://github.com/MichiganDataScienceTeam/MichiganDataScienceTeam.github.io.git`
1. Copy a post from `_posts/` and change the filename according to the pattern of the other files.
1. Make your own branch and push it to the repo.
    1. `$ git checkout -b my-new-post`
1. Change the variables at the top of the post between the two `---` dashes.
1. Preview your post.
    1. `$ jekyll serve`
    1. Use your browser to navigate to `localhost:4000`
1. Add your changes, commit your changes locally, and push your changes to GitHub.
    1. `$ git add _posts/the-post-that-you-made.md`
    1. `$ git commit`
    1. `$ git push -u origin my-new-post`
1. Go to GitHub and create a pull-request. If you have successfully pushed your branch and it contains changes, there should be a button under the name of the repository towards the top left corner of the screen.
1. Add some details and I'll merge the branch into master if it all looks good.
1. After the branch is merged into master, you may run `$ ./update-live-site` if you have the password. Otherwise, someone with the password will update. All this said, you can actually run that script at any point, but until I move the script to an AWS Lambda function it will remain in the project repo.

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

