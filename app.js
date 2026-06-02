// app.js vistor count update logic
async function updateVisitorCount() {
  try {
    const response = await fetch(
      "https://<YOUR_FUNCTION_APP>.azurewebsites.net/api/visitor_counter",
      { method: "POST" }
    );
    const data = await response.json();
    document.getElementById("visitor-count").innerText = data.count;
  } catch (error) {
    console.error("Failed to fetch visitor count:", error);
  }
}

updateVisitorCount();