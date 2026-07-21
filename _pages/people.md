---
layout: default
title: "People"
permalink: /people/
sections:
  - key: pi
    label: "PIs"
  - key: postdoc
    label: "Research Fellows and Postdocs"
  - key: pgr
    label: "Postgraduate Researcher"
  - key: visitor
    label: "Visitors"
---
<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / People</div>
  <h1>People</h1>
</div>

{% for section in page.sections %}
{% assign group = site.people | where: "section", section.key %}
{% if group.size > 0 %}
<section class="people-section">
  <h2 class="section-title">{{ section.label }}</h2>
  <div class="people-grid">
    {% for person in group %}
    <a class="person-card" href="{{ person.url | relative_url }}">
      <div class="person-photo">
        {% if person.photo and person.photo != "" %}
        <img src="{{ person.photo }}" alt="{{ person.name }}">
        {% else %}
        <i class="ti ti-user placeholder-icon"></i>
        {% endif %}
      </div>
      <div class="person-name">{{ person.name }}</div>
      <div class="person-role">{{ person.role }}{% if person.affiliation and person.affiliation != "" %} · {{ person.affiliation }}{% endif %}</div>
      <div class="person-links">
        {% if person.website and person.website != "" %}<span title="Website"><i class="ti ti-world"></i></span>{% endif %}
        {% if person.email and person.email != "" %}<span title="Email"><i class="ti ti-mail"></i></span>{% endif %}
        {% if person.scholar and person.scholar != "" %}<span title="Google Scholar"><i class="ti ti-brand-google-scholar"></i></span>{% endif %}
      </div>
    </a>
    {% endfor %}
  </div>
</section>
{% endif %}
{% endfor %}
