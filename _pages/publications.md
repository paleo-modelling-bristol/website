---
layout: default
title: "Publications"
permalink: /publications/
---
{% assign years = site.data.publications | map: "year" | uniq | sort | reverse %}

<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / Publications</div>
  <h1>Publications</h1>
</div>

<div class="pub-wrap">
  <div class="pub-filters">
    <button class="filter-btn active" onclick="filterPubs('all', this)">All</button>
    {% for year in years %}
    <button class="filter-btn" onclick="filterPubs('{{ year }}', this)">{{ year }}</button>
    {% endfor %}
  </div>

  <div class="pub-list">
    {% assign prev_year = "" %}
    {% for pub in site.data.publications %}
    {% assign this_year = pub.year | append: "" %}
    {% if this_year != prev_year %}
    <h2 class="pub-year-heading" data-year="{{ pub.year }}">{{ pub.year }}</h2>
    {% assign prev_year = this_year %}
    {% endif %}
    <div class="pub-item" data-year="{{ pub.year }}">
      <div class="pub-title">{{ pub.title }}</div>
      <div class="pub-authors">{{ pub.authors }} ({{ pub.year }})</div>
      <div class="pub-journal">{{ pub.journal }}</div>
      <div class="pub-meta">
        <span class="pub-year">{{ pub.year }}</span>
        {% if pub.doi %}<a class="pub-link" href="{{ pub.doi }}">DOI <i class="ti ti-external-link"></i></a>{% endif %}
        {% if pub.pdf %}<a class="pub-link" href="{{ pub.pdf }}">PDF <i class="ti ti-file-type-pdf"></i></a>{% endif %}
      </div>
    </div>
    {% endfor %}
  </div>
</div>

<style>
  .pub-year-heading {
    font-size: 2rem; font-weight: 700; letter-spacing: 0.02em;
    color: #993C1D; margin: 1.5rem 0 0; padding-bottom: 0.4rem;
    border-bottom: 2px solid #e8e8e8;
  }
  .pub-list > .pub-year-heading:first-child { margin-top: 0; }
  .pub-authors strong { color: #1a1a1a; font-weight: 700; }
</style>

<script>
  function filterPubs(year, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.pub-item, .pub-year-heading').forEach(item => {
      item.style.display = (year === 'all' || item.dataset.year === String(year)) ? '' : 'none';
    });
  }
</script>
