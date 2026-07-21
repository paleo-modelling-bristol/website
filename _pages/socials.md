---
layout: default
title: "Group Socials"
permalink: /socials/
---
<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / Group Socials</div>
  <h1>Group Socials</h1>
</div>

<div class="filter-bar">
  <button class="filter-btn active" onclick="filterGallery('all', this)">All</button>
  <button class="filter-btn" onclick="filterGallery('fieldwork', this)">Fieldwork</button>
  <button class="filter-btn" onclick="filterGallery('conference', this)">Conferences</button>
  <button class="filter-btn" onclick="filterGallery('social', this)">Group Socials</button>
</div>

<div class="gallery-wrap">
  {% for section in site.data.socials %}
  <div class="gallery-section" data-tag="{{ section.tag }}">
    <div class="gallery-section-title">
      {{ section.title }}
      <span class="event-date">{{ section.date }}</span>
    </div>
    <div class="masonry">
      {% for img in section.images %}
      {% if img.placeholder %}
      <div class="masonry-placeholder" style="height:{{ img.height }}px;">[ photo ]</div>
      {% elsif img.video %}
      <div class="masonry-item video-item" data-video="{{ img.video | relative_url }}" data-caption="{{ img.caption }}">
        <img src="{{ img.thumb | relative_url }}" alt="{{ img.caption }}">
        <div class="video-overlay"><div class="play-btn"><i class="ti ti-player-play-filled"></i></div></div>
      </div>
      {% else %}
      <div class="masonry-item" data-src="{{ img.src | relative_url }}" data-caption="{{ img.caption }}">
        <img src="{{ img.src | relative_url }}" alt="{{ img.caption }}"{% if img.height %} style="height:{{ img.height }}px; object-fit: cover;"{% endif %}>
      </div>
      {% endif %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
  <div class="lightbox-inner" id="lightbox-inner">
    <button class="lightbox-close" onclick="closeLightbox()"><i class="ti ti-x"></i></button>
    <button class="lightbox-nav prev" onclick="navigateLightbox(-1, event)"><i class="ti ti-chevron-left"></i></button>
    <button class="lightbox-nav next" onclick="navigateLightbox(1, event)"><i class="ti ti-chevron-right"></i></button>
    <div id="lightbox-media"></div>
    <div class="lightbox-caption" id="lightbox-caption"></div>
  </div>
</div>

<script>
  function filterGallery(tag, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.gallery-section').forEach(section => {
      section.style.display = (tag === 'all' || section.dataset.tag === tag) ? '' : 'none';
    });
  }

  let items = [], currentIndex = 0;

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.masonry-item').forEach((el, i) => {
      el.addEventListener('click', () => openLightbox(i));
    });
    items = Array.from(document.querySelectorAll('.masonry-item'));
  });

  function openLightbox(index) {
    currentIndex = index;
    renderLightbox();
    document.getElementById('lightbox').classList.add('open');
  }

  function renderLightbox() {
    const el = items[currentIndex];
    const media = document.getElementById('lightbox-media');
    const caption = el.dataset.caption || '';
    document.getElementById('lightbox-caption').textContent = caption;

    if (el.dataset.video) {
      media.innerHTML = `<video src="${el.dataset.video}" controls autoplay style="max-width:90vw;max-height:85vh;border-radius:6px;display:block;"></video>`;
    } else {
      media.innerHTML = `<img src="${el.dataset.src}" alt="${caption}">`;
    }
  }

  function closeLightbox(e) {
    if (e && e.target !== document.getElementById('lightbox')) return;
    document.getElementById('lightbox').classList.remove('open');
    document.getElementById('lightbox-media').innerHTML = '';
  }

  function navigateLightbox(dir, e) {
    e.stopPropagation();
    currentIndex = (currentIndex + dir + items.length) % items.length;
    renderLightbox();
  }

  document.addEventListener('keydown', e => {
    const lb = document.getElementById('lightbox');
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowRight') navigateLightbox(1, { stopPropagation: () => {} });
    if (e.key === 'ArrowLeft') navigateLightbox(-1, { stopPropagation: () => {} });
  });
</script>
