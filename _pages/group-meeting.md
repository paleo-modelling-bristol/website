---
layout: default
title: "Group Meetings"
permalink: /group-meeting/
---
<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / Group Meetings</div>
  <h1>Group Meetings</h1>
</div>

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterSeminars('all', this)">All</button>
  <button class="filter-btn" onclick="filterSeminars('internal', this)">Internal</button>
  <button class="filter-btn" onclick="filterSeminars('external', this)">External Speaker</button>
  <button class="filter-btn" onclick="filterSeminars('upcoming', this)">Upcoming</button>
</div>

<div class="seminar-wrap">
  {% for group in site.data.seminars %}
  <div class="seminar-year" data-year="{{ group.year }}">
    <div class="year-title">{{ group.year }}</div>
    <div class="seminar-list">
      {% for talk in group.talks %}
      <div class="seminar-item" data-type="{{ talk.type }}"{% if talk.upcoming %} data-upcoming="true"{% endif %}>
        <div class="seminar-date">
          <div class="day">{{ talk.day }}</div>
          <div class="month">{{ talk.month }}</div>
        </div>
        <div class="seminar-body">
          <div class="seminar-title">{{ talk.title }}</div>
          <div class="seminar-speaker">
            <i class="ti ti-user" style="font-size:13px;color:#bbb;"></i>
            {% if talk.speaker_url and talk.speaker_url != "" %}<a href="{{ talk.speaker_url }}">{{ talk.speaker }}</a>{% else %}{{ talk.speaker }}{% endif %} · {{ talk.affiliation }}
          </div>
          <div class="seminar-meta">
            {% if talk.upcoming %}<span class="tag upcoming">Upcoming</span>{% endif %}
            {% if talk.type == "external" %}<span class="tag external">External Speaker</span>{% else %}<span class="tag">Internal</span>{% endif %}
          </div>
          {% if talk.abstract and talk.abstract != "" %}
          <button class="toggle-abstract" onclick="toggleAbstract(this)">
            <i class="ti ti-chevron-down"></i> Abstract
          </button>
          <div class="seminar-abstract">{{ talk.abstract }}</div>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<script>
  function filterSeminars(type, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.seminar-item').forEach(item => {
      if (type === 'all') {
        item.style.display = '';
      } else if (type === 'upcoming') {
        item.style.display = item.dataset.upcoming === 'true' ? '' : 'none';
      } else {
        item.style.display = item.dataset.type === type ? '' : 'none';
      }
    });
    document.querySelectorAll('.seminar-year').forEach(section => {
      const visible = Array.from(section.querySelectorAll('.seminar-item')).some(i => i.style.display !== 'none');
      section.style.display = visible ? '' : 'none';
    });
  }

  function toggleAbstract(btn) {
    const abstract = btn.nextElementSibling;
    const isOpen = abstract.classList.toggle('open');
    btn.innerHTML = isOpen
      ? '<i class="ti ti-chevron-up"></i> Abstract'
      : '<i class="ti ti-chevron-down"></i> Abstract';
  }
</script>
