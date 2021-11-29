---
title: Team
---

<!-- section dark -->
<!-- section background images/banner.jpg -->

{% include figure.html image="images/2021_arcadelab_cropped.jpeg" width="80%" %}

We are looking for motivated students interested in the intersection of computer science, vision,
and health.

PhD applicants may apply through Johns Hopkins graduate admissions, being sure to note Mathias
Unberath as their primary faculty member of interest.

Postdoctoral applicants, masters students, and undergraduates should reach out to Prof. Unberath
directly, being sure to include area of interest, time frame, and the type of work (Masters thesis,
general research, etc). Applicants may wish to identify a PhD student whose interests align with
theirs, who could supervise.

{%
  include big-link.html
  icon="fas user-graduate"
  text="PhD Applicants"
  link="https://applygrad.jhu.edu/apply/"
  button=true
%}{%
  include big-link.html
  icon="fas envelope"
  text="Other Applicants"
  link="mailto:unberath@jhu.edu"
  button=true
%}{:.center}

<!-- section break -->

# <i class="fas fa-users"></i>Team Members

Our team consists of full-time PhD students, Masters students, and undergrads, led by Prof. Mathias Unberath. For up-to-date info on our members, check out their personal websites, Google Scholar profiles, or social media by clicking through below.

<!-- section break -->

{% capture contents %}
{% include team-list.html group="" role="pi" %}
{% include team-list.html group="" role="postdoc" %}
{% include team-list.html group="" role="phd" %}
{% include team-list.html group="" role="masters" %}
{% include team-list.html group="" role="undergrad" %}
{% include team-list.html group="" role="mascot" %}
{% endcapture %}

{% include centerer.html contents=contents %}

<!-- section break -->

## Alumni

{% capture contents %}
{% include team-list.html group="alum" role="pi" %}
{% include team-list.html group="alum" role="postdoc" %}
{% include team-list.html group="alum" role="phd" %}
{% include team-list.html group="alum" role="masters" %}
{% include team-list.html group="alum" role="undergrad" %}
{% endcapture %}

{% include centerer.html contents=contents %}
