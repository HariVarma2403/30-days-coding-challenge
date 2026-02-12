// Clock
function updateClock() {
    const now = new Date();
    document.getElementById("clock").innerText =
        now.toLocaleTimeString();
}
setInterval(updateClock, 1000);
updateClock();

// Medicine
let medicines = JSON.parse(localStorage.getItem("medicines")) || [];

function addMedicine() {
    const name = medName.value;
    const time = medTime.value;

    if (!name) return;

    medicines.push(`${name} - ${time}`);
    localStorage.setItem("medicines", JSON.stringify(medicines));
    renderMedicines();
    medName.value = "";
}

function renderMedicines() {
    medicineList.innerHTML = "";
    medicines.forEach(m => {
        const li = document.createElement("li");
        li.innerText = m;
        medicineList.appendChild(li);
    });
}

renderMedicines();

// Register Service Worker
if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("service-worker.js");
}
