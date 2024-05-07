---
hide:
  - navigation
---

# Examples

Elements in beautiful READMEs include, 
but are not limited to: images, screenshots, 
GIFs, text formatting, etc.

{% for project in projects %}
??? example "[{{ project.name }}]({{ project.url }})<br>{{ project.description }}"
    <a href="{{ project.url }}">
    <img src="{{ project.images }}" align="center">
    </a>
{% endfor %}