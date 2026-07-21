---
layout: default
title: "Model Outputs"
permalink: /model-outputs/
---
<div class="page-header">
  <div class="breadcrumb"><a href="{{ '/' | relative_url }}">Home</a> / Model Outputs</div>
  <h1>Model Outputs</h1>
</div>

<div class="model-wrap">
  <div class="model-grid">
    {% for item in site.data.model_outputs %}
    <div class="model-card">
      <div class="model-thumb">
        {% if item.thumb and item.thumb != "" %}
        <img src="{{ item.thumb | relative_url }}" alt="{{ item.title }}">
        {% else %}
        [ Replace with model output image ]
        {% endif %}
      </div>
      <div class="model-body">
        <div class="model-title">{{ item.title }}</div>
        <div class="model-desc">{{ item.description }}</div>
        <div class="model-meta">
          <span class="model-tag">{{ item.tag }}</span>
          <a class="model-link" href="{{ item.link }}">Download <i class="ti ti-download"></i></a>
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>
