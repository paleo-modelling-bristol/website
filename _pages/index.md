---
layout: default
permalink: /
title: "Home"
---
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
  <div class="about-text">
    <p>Our main focus is on paleoclimate modelling across multiple timescales of Earth's history. Broadly speaking, our aims are twofold - (1) to better understand Earth's climate history, with a focus on the mechanisms and feedbacks that translate climate forcings into a climate response, and (2) to evaluate and improve climate models through paleo model-data comparisons, with the aim of improving future climate projections. In this regard, we work closely with the paleo data community in order to rigorously evaluate our climate models.</p>
    <p>The Bristol Paleo modelling group was founded in 2002, and is a part of the wider BRIDGE research group within the School of Geographical Sciences at the University of Bristol.</p>
    <p>We are a very international group, and we welcome visiting scientists from across the world, including visiting PhD and Masters students.</p>
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
