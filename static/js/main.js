const textArea = document.getElementById("source-text");
const charCount = document.getElementById("char-count");
const levelButtons = document.querySelectorAll(".level-btn");
const explainBtn = document.getElementById("explain-btn");
const btnLabel = document.getElementById("btn-label");
const errorText = document.getElementById("error-text");
const outputPanel = document.getElementById("output-panel");
const outputText = document.getElementById("output-text");
const resetBtn = document.getElementById("reset-btn");
const inputPanel = document.querySelector(".input-panel");

let selectedLevel = "college";

textArea.addEventListener("input", () => {
  charCount.textContent = textArea.value.length;
});

levelButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    levelButtons.forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    selectedLevel = btn.dataset.level;
  });
});

function showError(message) {
  errorText.textContent = message;
  errorText.hidden = false;
}

function clearError() {
  errorText.hidden = true;
  errorText.textContent = "";
}

function renderExplanation(text) {
  outputText.innerHTML = "";
  text
    .split(/\n\s*\n/)
    .map((p) => p.trim())
    .filter(Boolean)
    .forEach((paragraph) => {
      const p = document.createElement("p");
      p.textContent = paragraph;
      outputText.appendChild(p);
    });
  outputPanel.hidden = false;
  inputPanel.hidden = true;
  outputPanel.scrollIntoView({ behavior: "smooth", block: "start" });
}

async function explain() {
  clearError();
  const text = textArea.value.trim();

  if (!text) {
    showError("Paste some text first.");
    return;
  }

  explainBtn.disabled = true;
  btnLabel.textContent = "Focusing…";

  try {
    const res = await fetch("/api/explain", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, level: selectedLevel }),
    });
    const data = await res.json();

    if (!res.ok) {
      showError(data.error || "Something went wrong. Try again.");
      return;
    }

    renderExplanation(data.explanation);
  } catch (err) {
    showError("Couldn't reach the server. Is the Flask app running?");
  } finally {
    explainBtn.disabled = false;
    btnLabel.textContent = "Bring into focus";
  }
}

explainBtn.addEventListener("click", explain);

resetBtn.addEventListener("click", () => {
  outputPanel.hidden = true;
  inputPanel.hidden = false;
  textArea.value = "";
  charCount.textContent = "0";
  clearError();
  textArea.focus();
});
