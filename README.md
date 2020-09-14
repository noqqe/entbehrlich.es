# Install

In order to write new entbehrlich.es articles you need to do the following

```
git clone git@github.com:noqqe/entbehrlich.es.git entbehrlich.es
cd entbehrlich.es
pip install -r requirements.txt
```

After that you can try `./articles queue`

# Usage

Add new article

```
$ ./articles new --thanks <twitter handle> https://de.wikipedia.org/wiki/Schlacht_in_der_Javasee
```

See queued articles

```
$ ./articles queue
10:34:43 All unpublished posts:
10:34:43  * ORGAN²ASLSP.md
10:34:43  * Postbeutel.md
10:34:43  * Kenneth-Parks.md
```

Or get an general overview of the `./articles` tool

```
> ./articles --help
Usage: articles [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  inspiration  Live recently update articles from Wikipedia
  new          Create a new post
  podcast      Add link to podcast to article
  queue        Show current drafts
  random       Get 20 random articles from Wikipedia
  reedit       Edit an already written article
  release      Publish a post
  tweet        Tweet latest blogpost from rss feed
  unpodcasted  Show all posts that are not podcasted, yet!
```

# Deployment & Hosting

[entbehrlich.es](https://entbehrlich.es) is running on a private server of noqqe.

Its build and deployed using travis-ci. If you made markdown/syntax errors the blog will
not be published. Every time someone commits something to the repo, the blog gets built and deployed.

Current build status:

[![Build Status](https://travis-ci.org/noqqe/entbehrlich.es.svg?branch=master)](https://travis-ci.org/noqqe/entbehrlich.es)

# Requirements

These are the requirements to get ./articles running

* Python 3
* All requirements installed from requirements.txt
* A working editor under $EDITOR
* Install `libjpeg-dev` when you are on debian
* `hugo` in your $PATH
