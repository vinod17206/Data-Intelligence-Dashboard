function toggleTheme() {
    document.body.classList.toggle("light-mode");
}

console.log("Ultra Premium UI Loaded");

// KPI animation
document.querySelectorAll(".kpi").forEach(card => {
    card.addEventListener("mouseover", () => {
        card.style.transform = "scale(1.05)";
    });

    card.addEventListener("mouseout", () => {
        card.style.transform = "scale(1)";
    });
});
function toggleTheme() {
    document.body.classList.toggle("light-mode");
}

function showToast(message) {
    const toast = document.getElementById("toast");
    if(!toast) return;

    toast.innerText = message;
    toast.classList.remove("hidden");

    setTimeout(() => {
        toast.classList.add("hidden");
    }, 3000);
}

console.log("Ultra Premium UI Loaded");

// KPI animation
document.querySelectorAll(".kpi").forEach(card => {
    card.addEventListener("mouseover", () => {
        card.style.transform = "scale(1.05)";
    });

    card.addEventListener("mouseout", () => {
        card.style.transform = "scale(1)";
    });
});