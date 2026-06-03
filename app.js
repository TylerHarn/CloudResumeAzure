async function updateVisitorCount() {
  try {
    const response = await fetch(
      "https://tylerharnapi-gab9b7gkd5grdphy.canadacentral-01.azurewebsites.net/api/VisitorCounter",
      { method: "GET" }
    );
    const data = await response.json();
    document.getElementById("visitor-count").innerText = data.count;
  } catch (error) {
    console.error("Failed to fetch visitor count:", error);
  }
}

updateVisitorCount();