function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  addMessage("user", message);
  fetchBot(message);
  // Simulate bot reply
  // setTimeout(() => {
  //   addMessage(
  //     "bot",
  //     reply
  //   );
  // }, 500);

  input.value = "";
}
function processJSON(jsonData)
{
  console.log(jsonData)
  const content = jsonData.choices[0].message.content

  return content
}
function fetchBot(message) {
  // Simulate API call

  const chatRequest = {
    messages: [
      {role: "user", content: message}
    ]
  };
  fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(chatRequest), // Sending the user's message
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Assuming the API response has a `reply` field
      result = processJSON(JSON.parse(data.reply))
      addMessage("bot", result);
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
      addMessage("bot", "Sorry, something went wrong.");
    });
}

// function addMessage(sender, text) {
//   const chatWindow = document.getElementById("chat-window");
//   const messageDiv = document.createElement("div");
//   messageDiv.classList.add("message", sender);
//   messageDiv.textContent = text;
//   chatWindow.appendChild(messageDiv);
//   chatWindow.scrollTop = chatWindow.scrollHeight;
// }

// function addMessage(sender, text) {
//     const chatWindow = document.getElementById("chat-window");

//     const messageWrapper = document.createElement("div");
//     messageWrapper.classList.add("message", sender);

//     const bubble = document.createElement("div");
//     bubble.classList.add("bubble");
//     bubble.textContent = text;

//     messageWrapper.appendChild(bubble);
//     chatWindow.appendChild(messageWrapper);
//     chatWindow.scrollTop = chatWindow.scrollHeight;
//   }

document.body.classList.add("no-scroll"); // to disable scrolling

function addMessage(sender, text) {
  const chatWindow = document.getElementById("chat-window");

  const messageWrapper = document.createElement("div");
  messageWrapper.classList.add("message", sender);

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");

  // Convert [spoiler]text[/spoiler] to span
  const safeText = text.replace(
    /\[spoiler\](.*?)\[\/spoiler\]/g,
    '<span class="spoiler">$1</span>'
  );
  bubble.innerHTML = safeText;

  // // Allow rendering HTML like spoiler spans
  // bubble.innerHTML = text;

  // Attach click event to spoiler spans
  bubble.querySelectorAll(".spoiler").forEach((spoiler) => {
    spoiler.addEventListener("click", () => {
      spoiler.classList.toggle("revealed");
    });
  });

  messageWrapper.appendChild(bubble);
  chatWindow.appendChild(messageWrapper);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("userInput");
  const sendBtn = document.getElementById("sendBtn");

  // Event listener for Enter key
  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      sendMessage();
    }
  });

  // Event listener for Send button click
  sendBtn.addEventListener("click", () => {
    sendMessage();
  });
});
