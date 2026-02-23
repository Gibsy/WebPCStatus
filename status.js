async function updateStatus() {
    try {
        const res = await fetch("status.json?_=" + Date.now());
        const data = await res.json();
        const now = Date.now();
        const lastUpdate = new Date(data.last_update).getTime();
        const onlineSince = new Date(data.online_since).getTime();
        const diffLastMs = now - lastUpdate;
        const isOnline = diffLastMs <= 240_000;

        let diffMs;
        let label;
        let color;
        if (isOnline) {
            diffMs = now - onlineSince;
            label = "Online for";
            color = "#047826";
        } else {
            diffMs = diffLastMs;
            label = "Offline for";
            color = "#b00202";
        }

        const diffMin = Math.floor(diffMs / 60000);
        const h = Math.floor(diffMin / 60);
        const m = diffMin % 60;
        let timeText = "";
        if (h > 0) timeText += `${h}h `;
        timeText += `${m}min`;

        const statusEl = document.getElementById("pcStatus");
        statusEl.style.color = color;
        statusEl.textContent = `${label} ${timeText.trim()}`;

    } catch (e) {
        const statusEl = document.getElementById("pcStatus");
        statusEl.textContent = "Status error";
        statusEl.style.color = "orange";
        console.error("Status fetch error:", e);
    }
}

updateStatus();
setInterval(updateStatus, 30000);
