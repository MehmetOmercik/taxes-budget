const budgetButton = document.getElementById("id_budget");
const budgetSection = document.getElementById("budget_section");

const budgetChecker = () => {
  if (budgetButton.value == "True") {
    console.log(budgetButton.value);
    budgetSection.removeAttribute("hidden");
  } else {
    budgetSection.setAttribute("hidden", "hidden");
  }
  //   console.log("hello");
};

budgetButton.addEventListener("change", budgetChecker);
