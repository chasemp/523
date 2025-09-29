document.addEventListener('DOMContentLoaded', () => {
  const dropdowns = Array.from(document.querySelectorAll('.dropdown'));

  function setAriaExpanded(dropdown, expanded) {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    if (toggle) toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
  }

  function closeAllDropdowns(exceptDropdown) {
    dropdowns.forEach((dropdown) => {
      if (dropdown !== exceptDropdown) {
        dropdown.classList.remove('open', 'dropup');
        setAriaExpanded(dropdown, false);
      }
    });
  }

  function measureMenuHeight(dropdown) {
    const menu = dropdown.querySelector('.dropdown-menu');
    if (!menu) return 0;
    const prevDisplay = menu.style.display;
    const prevVisibility = menu.style.visibility;
    const prevMaxHeight = menu.style.maxHeight;

    menu.style.visibility = 'hidden';
    menu.style.display = 'block';
    menu.style.maxHeight = 'none';

    const height = menu.scrollHeight;

    menu.style.maxHeight = prevMaxHeight;
    menu.style.display = prevDisplay;
    menu.style.visibility = prevVisibility;

    return height;
  }

  function computeAndSetDirection(dropdown) {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');
    if (!toggle || !menu) return;

    const rect = toggle.getBoundingClientRect();
    const viewportHeight = (window.visualViewport && window.visualViewport.height) || window.innerHeight;
    const spaceBelow = viewportHeight - rect.bottom;
    const spaceAbove = rect.top;

    const computedMax = getComputedStyle(menu).maxHeight;
    let maxPixels = Number.POSITIVE_INFINITY;
    if (computedMax && computedMax !== 'none') {
      const numeric = parseFloat(computedMax);
      if (!Number.isNaN(numeric)) maxPixels = numeric;
    }

    const menuNaturalHeight = measureMenuHeight(dropdown);
    const effectiveHeight = Math.min(menuNaturalHeight, maxPixels);

    if (spaceBelow < effectiveHeight && spaceAbove > spaceBelow) {
      dropdown.classList.add('dropup');
    } else {
      dropdown.classList.remove('dropup');
    }
  }

  dropdowns.forEach((dropdown) => {
    const toggle = dropdown.querySelector('.dropdown-toggle');
    const menu = dropdown.querySelector('.dropdown-menu');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', (event) => {
      event.preventDefault();
      const isOpen = dropdown.classList.contains('open');
      closeAllDropdowns(dropdown);
      if (!isOpen) {
        computeAndSetDirection(dropdown);
        dropdown.classList.add('open');
        setAriaExpanded(dropdown, true);
      } else {
        dropdown.classList.remove('open', 'dropup');
        setAriaExpanded(dropdown, false);
      }
    });

    toggle.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        computeAndSetDirection(dropdown);
        dropdown.classList.add('open');
        setAriaExpanded(dropdown, true);
      }
      if (event.key === 'ArrowDown') {
        event.preventDefault();
        computeAndSetDirection(dropdown);
        dropdown.classList.add('open');
        setAriaExpanded(dropdown, true);
        const firstItem = dropdown.querySelector('.dropdown-menu a');
        if (firstItem) firstItem.focus({ preventScroll: true });
      }
      if (event.key === 'ArrowUp') {
        event.preventDefault();
        computeAndSetDirection(dropdown);
        dropdown.classList.add('open', 'dropup');
        setAriaExpanded(dropdown, true);
      }
    });

    menu.addEventListener('click', (event) => {
      const target = event.target;
      if (target && target.closest('a')) {
        dropdown.classList.remove('open', 'dropup');
        setAriaExpanded(dropdown, false);
      }
    });
  });

  document.addEventListener('click', (event) => {
    const target = event.target;
    if (!(target instanceof Element)) return;
    const inDropdown = target.closest('.dropdown');
    if (!inDropdown) {
      closeAllDropdowns();
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      closeAllDropdowns();
    }
  });

  const recomputeOpenDropdown = () => {
    const openDropdown = document.querySelector('.dropdown.open');
    if (openDropdown) computeAndSetDirection(openDropdown);
  };

  window.addEventListener('resize', recomputeOpenDropdown);
  window.addEventListener('scroll', recomputeOpenDropdown, { passive: true });
});

