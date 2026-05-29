---
layout: page
title: publications
permalink: /publications/
description: Publications from the ICE Lab at Drexel University.
nav: true
nav_order: 5
publications_compact: true
---

<p class="publications-lead">
  <strong>Google Scholar Profile:</strong>
  <a href="https://scholar.google.com/citations?user=qe9QgMZUjAMC" target="_blank" rel="noopener noreferrer">Ioannis Savidis</a>
</p>

{% include publication_filters.liquid %}

<div class="publications publications--catalog">
{% for group in site.data.publication_groups %}
  <section class="publication-group" id="pub-{{ group.id }}" data-ice-type="{{ group.id }}">
    <h2 class="publications-category">{{ group.title }}</h2>
    {% case group.id %}
      {% when 'tutorials' %}
        {% bibliography --group_by none --query @*[ice_type=tutorials]* %}
      {% when 'book' %}
        {% bibliography --group_by none --query @*[ice_type=book]* %}
      {% when 'book_chapter' %}
        {% bibliography --group_by none --query @*[ice_type=book_chapter]* %}
      {% when 'dissertations' %}
        {% bibliography --group_by none --query @*[ice_type=dissertations]* %}
      {% when 'journal_papers' %}
        {% bibliography --group_by none --query @*[ice_type=journal_papers]* %}
      {% when 'conference_papers' %}
        {% bibliography --group_by none --query @*[ice_type=conference_papers]* %}
      {% when 'workshop_presentations' %}
        {% bibliography --group_by none --query @*[ice_type=workshop_presentations]* %}
      {% when 'conference_presenter' %}
        {% bibliography --group_by none --query @*[ice_type=conference_presenter]* %}
      {% when 'technical_industrial' %}
        {% bibliography --group_by none --query @*[ice_type=technical_industrial]* %}
    {% endcase %}
  </section>
{% endfor %}
</div>
