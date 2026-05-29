---
layout: page
title: team
permalink: /team/
description: Current and former members of the ICE Lab.
nav: true
nav_order: 2
display_categories: [faculty, phd, masters, alumni]
horizontal: false
---

Meet the researchers and students driving innovation at the ICE Lab.

<!-- _pages/team.md -->
<div class="projects team-members">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
    {% assign categorized_members = site.team | where: "category", category %}
    {% assign sorted_members = categorized_members | sort: "importance" %}
    {% if sorted_members.size > 0 %}
      {% if category == "faculty" %}
        <h2 class="category">Faculty & Staff</h2>
      {% elsif category == "phd" %}
        <h2 class="category">PhD Students</h2>
      {% elsif category == "masters" %}
        <h2 class="category">MS Students</h2>
      {% elsif category == "undergraduate" %}
        <h2 class="category">Undergraduate Researchers</h2>
      {% elsif category == "alumni" %}
        <h2 class="category">Alumni</h2>
      {% else %}
        <h2 class="category">{{ category | capitalize }}</h2>
      {% endif %}
      {% if category == "faculty" %}
        <div class="row row-cols-1">
          {% for project in sorted_members %}
            {% include projects_horizontal.liquid %}
          {% endfor %}
        </div>
      {% elsif page.horizontal %}
        <div class="container">
          <div class="row row-cols-1 row-cols-md-2">
            {% for project in sorted_members %}
              {% include projects_horizontal.liquid %}
            {% endfor %}
          </div>
        </div>
      {% else %}
        <div class="row row-cols-1 row-cols-md-3">
          {% for project in sorted_members %}
            {% include projects.liquid %}
          {% endfor %}
        </div>
      {% endif %}
    {% endif %}
  {% endfor %}

{% else %}

{% assign sorted_members = site.team | sort: "importance" %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_members %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
{% endif %}
</div>
