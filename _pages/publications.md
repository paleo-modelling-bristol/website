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
    {% for pub in site.data.publications %}
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

<script>
  function filterPubs(year, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.pub-item').forEach(item => {
      item.style.display = (year === 'all' || item.dataset.year === String(year)) ? '' : 'none';
    });
  }
</script>
