const items = document.querySelectorAll('.accordion .accordion-button');

function toggleAccordion() {
  const itemToggle = this.getAttribute('aria-expanded');

  for (let item of items) {
    item.setAttribute('aria-expanded', 'false');
    item.nextElementSibling.style.maxHeight = null;
  }

  if (itemToggle === 'false') {
    this.setAttribute('aria-expanded', 'true');
    this.nextElementSibling.style.maxHeight = this.nextElementSibling.scrollHeight + "px";
  }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));
