---
layout: default
title: "Join Us"
permalink: /join/
---
<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / Join Us</div>
  <h1>Join Us</h1>
</div>

<div class="content">

  <div class="join-section">
    <!-- TODO: replace with a real intro paragraph -->
    <p>Fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text.</p>
    <p>Fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text.</p>
  </div>

  <div class="join-section">
    <div class="section-label">Open Positions</div>
    <div class="positions">
      {% for position in site.data.positions %}
      <div class="position-card"{% if position.status == "closed" %} style="opacity: 0.6;"{% endif %}>
        <div>
          <div class="position-title">{{ position.title }}</div>
          <div class="position-desc">{{ position.description }}</div>
          <div class="position-meta">
            <span class="badge {{ position.status }}">{{ position.status | capitalize }}</span>
            {% for tag in position.tags %}<span class="badge">{{ tag }}</span>{% endfor %}
          </div>
        </div>
        <div class="position-actions">
          {% if position.status == "open" %}
          <a class="btn btn-primary" href="{{ position.apply_url }}">Apply <i class="ti ti-arrow-right"></i></a>
          <span class="deadline">Deadline: {{ position.deadline }}</span>
          {% else %}
          <button class="btn btn-outline" disabled>Closed</button>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <div class="join-section">
    <div class="section-label">Get in Touch</div>
    <div class="contact-box">
      <p>Fig text fig text fig text fig text fig text fig text if you have questions about opportunities in the group, feel free to reach out directly.</p>
      <div class="contact-links">
        <a class="contact-link" href="mailto:{{ site.contact_email }}">
          <i class="ti ti-mail"></i> {{ site.contact_email }}
        </a>
        <a class="contact-link" href="#">
          <i class="ti ti-map-pin"></i> Fig Text Building, University of Bristol
        </a>
      </div>
    </div>
  </div>

</div>
