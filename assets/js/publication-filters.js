document.addEventListener("DOMContentLoaded", () => {
  const yearSelect = document.getElementById("pub-year-filter");
  const typeButtons = document.querySelectorAll(".pub-filter-btn[data-ice-type]");
  const textInput = document.getElementById("bibsearch");
  if (!yearSelect || !typeButtons.length) {
    return;
  }

  const years = new Set();
  document.querySelectorAll(".pub-entry[data-pub-year]").forEach((entry) => {
    const year = entry.getAttribute("data-pub-year");
    if (year) {
      years.add(year);
    }
  });

  [...years]
    .sort((a, b) => Number(b) - Number(a))
    .forEach((year) => {
      const option = document.createElement("option");
      option.value = year;
      option.textContent = year;
      yearSelect.appendChild(option);
    });

  let activeType = "all";

  const applyFilters = () => {
    const year = yearSelect.value;
    const text = (textInput?.value || "").trim().toLowerCase();

    document.querySelectorAll(".publication-group").forEach((section) => {
      let visibleInSection = 0;
      section.querySelectorAll(".bibliography > li").forEach((item) => {
        const entry = item.querySelector(".pub-entry");
        const entryType = entry?.getAttribute("data-ice-type") || "";
        const entryYear = entry?.getAttribute("data-pub-year") || "";
        const matchesType = activeType === "all" || entryType === activeType;
        const matchesYear = !year || entryYear === year;
        const matchesText = !text || item.innerText.toLowerCase().includes(text);
        const visible = matchesType && matchesYear && matchesText;
        item.classList.toggle("unloaded", !visible);
        if (visible) {
          visibleInSection += 1;
        }
      });
      section.classList.toggle("unloaded", visibleInSection === 0);
    });
  };

  typeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeType = button.getAttribute("data-ice-type") || "all";
      typeButtons.forEach((btn) => btn.classList.toggle("active", btn === button));
      applyFilters();
    });
  });

  yearSelect.addEventListener("change", applyFilters);

  if (textInput) {
    let timeoutId;
    textInput.addEventListener("input", () => {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(applyFilters, 200);
    });
    window.addEventListener("hashchange", () => {
      textInput.value = decodeURIComponent(window.location.hash.substring(1));
      applyFilters();
    });
  }

  applyFilters();
});
