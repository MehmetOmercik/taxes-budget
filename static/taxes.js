const budgetButton = document.getElementById("id_budget");
const budgetSection = document.getElementById("budget_section");
const resetButton = document.getElementById("reset");

//Used to hide/reveal budget section
const budgetChecker = () => {
  if (budgetButton.value == "True") {
    budgetSection.removeAttribute("hidden");
  } else {
    budgetSection.setAttribute("hidden", "hidden");
  }
};

const resetHandler = () => {
  window.location.reload();
};

//Ensures that budget section remains visible after submission
if (budgetButton.value == "True") {
  budgetSection.removeAttribute("hidden");
}

//Resets everything after refreshing page rather than getting a confirm form submission (AKA GET request instead of POST)
if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}

budgetButton.addEventListener("change", budgetChecker);
resetButton.addEventListener("click", resetHandler);
