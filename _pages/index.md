---
layout: default
permalink: /
title: "Home"
---
{% assign pi_count = site.people | where: "section", "pi" | size %}
{% assign postdoc_count = site.people | where: "section", "postdoc" | size %}
{% assign pgr_count = site.people | where: "section", "pgr" | size %}
{% assign pub_count = site.data.publications | size %}

<div class="hero">
  <div class="hero-overlay"></div>
  <div class="hero-text">
    <h1>{{ site.title }}</h1>
    <p>{{ site.tagline }}</p>
  </div>
</div>

<section id="research">
  <div class="cards-grid">

    <div class="card">
      <div class="card-img">[ Replace with people image ]</div>
      <div class="card-body">
        <h3>People</h3>
        <p>Fig text fig text fig text meet our team of researchers.</p>
        <a class="card-link" href="{{ '/people/' | relative_url }}">View People <i class="ti ti-arrow-right"></i></a>
      </div>
    </div>

    <div class="card">
      <div class="card-img">[ Replace with publications image ]</div>
      <div class="card-body">
        <h3>Publications</h3>
        <p>Fig text fig text fig text browse our recent publications.</p>
        <a class="card-link" href="{{ '/publications/' | relative_url }}">View Publications <i class="ti ti-arrow-right"></i></a>
      </div>
    </div>

    <div class="card">
      <div class="card-img">[ Replace with join us image ]</div>
      <div class="card-body">
        <h3>Join Us</h3>
        <p>Fig text fig text fig text open positions in the group.</p>
        <a class="card-link" href="{{ '/join/' | relative_url }}">View Positions <i class="ti ti-arrow-right"></i></a>
      </div>
    </div>

  </div>
</section>

<section>
  <h2 class="section-title">About Us</h2>
  <div class="about-grid">
    <div class="about-text">
      <!-- TODO: replace with a real "about the group" description -->
      <p>Fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text.</p>
      <p>Fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text fig text.</p>
    </div>
    <div class="about-stats">
      <div class="stat-card">
        <div class="num">{{ pi_count }}</div>
        <div class="label">Faculty members</div>
      </div>
      <div class="stat-card">
        <div class="num">{{ postdoc_count }}</div>
        <div class="label">Postdoctoral researchers</div>
      </div>
      <div class="stat-card">
        <div class="num">{{ pgr_count }}</div>
        <div class="label">Postgraduate researchers</div>
      </div>
      <div class="stat-card">
        <div class="num">{{ pub_count }}</div>
        <div class="label">Publications</div>
      </div>
    </div>
  </div>
</section>

<section id="news">
  <h2 class="section-title">Latest News</h2>
  <div class="news-list">
    {% for item in site.data.news %}
    <div class="news-item">
      <span class="news-date">{{ item.date }}</span>
      <div class="news-content">
        <h4>{{ item.title }}</h4>
        <p>{{ item.description }}</p>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
