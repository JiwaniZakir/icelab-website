---
layout: page
title: projects
permalink: /projects/
description: Active research projects at the ICE Lab.
nav: true
nav_order: 3
display_categories: [active, completed]
horizontal: false
---

Explore our current and completed research projects.

<!-- _pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  {% for category in page.display_categories %}
    <a id="{{ category }}" href=".#{{ category }}">
      {% if category == "active" %}
        <h2 class="category">Active Projects</h2>
      {% elsif category == "completed" %}
        <h2 class="category">Completed Projects</h2>
      {% else %}
        <h2 class="category">{{ category | capitalize }}</h2>
      {% endif %}
    </a>
    {% assign categorized_projects = site.projects | where: "category", category %}
    {% assign sorted_projects = categorized_projects | sort: "importance" %}
    {% if page.horizontal %}
      <div class="container">
        <div class="row row-cols-1 row-cols-md-2">
          {% for project in sorted_projects %}
            {% include projects_horizontal.liquid %}
          {% endfor %}
        </div>
      </div>
    {% else %}
      <div class="row row-cols-1 row-cols-md-3">
        {% for project in sorted_projects %}
          {% include projects.liquid %}
        {% endfor %}
      </div>
    {% endif %}
  {% endfor %}

{% else %}

{% assign sorted_projects = site.projects | sort: "importance" %}
  {% if page.horizontal %}
    <div class="container">
      <div class="row row-cols-1 row-cols-md-2">
        {% for project in sorted_projects %}
          {% include projects_horizontal.liquid %}
        {% endfor %}
      </div>
    </div>
  {% else %}
    <div class="row row-cols-1 row-cols-md-3">
      {% for project in sorted_projects %}
        {% include projects.liquid %}
      {% endfor %}
    </div>
  {% endif %}
{% endif %}
</div>
