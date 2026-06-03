async function updateVisitorCount() {
  const lastVisit = localStorage.getItem("lastVisit");
  const now = Date.now();

  // Only count once per 30 minutes per browser to prevent refresh spamming from inflating the count
  if (lastVisit && now - lastVisit < 30 * 60 * 1000) {
    const cached = localStorage.getItem("cachedCount");
    if (cached) {
      document.getElementById("visitor-count").innerText = cached;
      return;
    }
  }

  try {
    const response = await fetch(
      "https://tylerharnapi-gab9b7gkd5grdphy.canadacentral-01.azurewebsites.net/api/VisitorCounter",
      { method: "GET" }
    );
    const data = await response.json();
    document.getElementById("visitor-count").innerText = data.count;
    localStorage.setItem("lastVisit", now);
    localStorage.setItem("cachedCount", data.count);
  } catch (error) {
    console.error("Failed to fetch visitor count:", error);
  }
}