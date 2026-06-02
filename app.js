async function getVisitorCount() {
  try {
    // Temporarily mock the response — replace with real URL in Step 9
    const mockData = { count: 123 };
    document.getElementById("visitor-count").textContent = mockData.count;
  } catch (error) {
    console.error("Error fetching visitor count:", error);
    document.getElementById("visitor-count").textContent = "N/A";
  }
}

getVisitorCount();