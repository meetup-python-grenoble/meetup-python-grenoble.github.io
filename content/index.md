---
title: Home
hide:
  - footer
---

# 🐍 Meetup Python Grenoble

<!-- ![Logo](static/python-logo-generic.svg) -->

![Banner](static/banner.jpeg)

Python user group from [Grenoble (France)](https://www.grenoble.fr) discussing
everything related to the [Python programming language](https://www.python.org),
while still being open to every other languages and technologies!

!!! tip
    Whatever your relationship and expertise with Python, you are more than
    welcome to attend future events! Simply register to events in advance then
    bring a good dose of cusiosity and a big smile!

## Links

You can find us on the following platforms:

[:fontawesome-brands-meetup: Meetup](https://www.meetup.com/fr-FR/groupe-dutilisateurs-python-grenoble/)

[:fontawesome-brands-github: GitHub](https://github.com/meetup-python-grenoble)

## Submissions

Want to share your experience about something Python-related to the Grenoble
crowd? Please submit your event idea by filling the issue form on GitHub!

[Submit an event](https://github.com/meetup-python-grenoble/meetup-python-grenoble.github.io/issues/new?assignees=&labels=submission&template=submission.yml&title=New+Event+Submission){ .md-button }

### Latest Submissions

<div id="gh-submission-list"></div>

<template id="gh-submission-template">
  <article class="gh-submission-item">
    <h4><a class="gh-submission-url" href="">Title</a></h4>
    <small>Submitted by <a class="gh-submission-author" href="">username</span></small>
  </article>
</template>

<script>
function addSubmissionItem(submission) {
  const submissionList = document.querySelector('#gh-submission-list')
  const submissionTemplate = document.querySelector('#gh-submission-template')
  const submissionItem = submissionTemplate.content.cloneNode(true)
  const link = submissionItem.querySelector('.gh-submission-url')
  const author = submissionItem.querySelector('.gh-submission-author')

  link.setAttribute('href', submission.html_url)
  link.text = submission.title

  author.setAttribute('href', submission.user.html_url)
  author.text = submission.user.login

  submissionList.appendChild(submissionItem)
}

async function getLatestSubmissions(repository) {
  const response = await fetch(`https://api.github.com/repos/${repository}/issues?state=open&labels=submission`)
  const submissions = await response.json()
  submissions.forEach(addSubmissionItem)
}

getLatestSubmissions('meetup-python-grenoble/meetup-python-grenoble.github.io')
</script>

## Discussions

If you want to:

- Interact with the Meetup organizers
- Interact with the Meetup community
- Share your ideas
- Checkout the latest announcements
- ...or anything else?

Let's talk on GitHub Discussions!

[Discussions](https://github.com/meetup-python-grenoble/meetup-python-grenoble.github.io/discussions){ .md-button }

## Hosts

[![mjbright](https://avatars.githubusercontent.com/u/1880109){ width=100 }](https://github.com/mjbright "Michael J Bright")
[![rclement](https://avatars.githubusercontent.com/u/1238873){ width=100 }](https://github.com/rclement "Romain Clement")
[![plbayart](https://avatars.githubusercontent.com/u/37104025){ width=100 }](https://github.com/Pierre-Loic "Pierre-Loïc Bayart")

## Partners

Thanks to all our wonderful partners!

[![La Turbine.coop](static/laturbine.png){ width=200 }](https://turbine.coop "La Turbine.coop Website")

!!! info "Want to be come a partner?"

    Here is what you could do:

    - Hosting events
    - Providing food and drinks
    - Anything that can benefit the community

    In exchange, you get your logo on this page and a 5 minutes pitch at the
    beginning of sponsored events.

    [Become a partner](https://github.com/meetup-python-grenoble/meetup-python-grenoble.github.io/discussions){ .md-button }
