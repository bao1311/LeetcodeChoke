document.getElementById("loginBtn").addEventListener("click", () => {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
  
    // Demo-only check — replace with real auth later
    if (username && password) {
      // Save user info in session
      sessionStorage.setItem("username", username);
  
      // Redirect to the chat page
      window.location.href = "sidepanel.html";
    } else {
      alert("Please enter both username and password.");
    }
  });
  