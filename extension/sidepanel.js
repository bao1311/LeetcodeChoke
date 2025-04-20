var startRating = 1100
const messages = [{role: "user", content: "My current rating is ${startRating}"}];
function retrieveQuestion()
{
  const bodyRequest = {
    min_rating: 1100,
    max_rating: 1200
  };
  const url = `http://127.0.0.1:8000/problems?min_rating=${startRating}&max_rating=${startRating+100}`
  fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      // Assuming the API response has a `reply` field
      console.log(data);
      messages.push({role: "assistant", content: data.reply})
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
      addMessage("bot", "Sorry, something went wrong.");
    });

}
function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;
  messages.push({role: "user", content: message + "\n It has been ${seconds} since we start working together"})
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
// function processJSON(jsonData)
// {
//   console.log(jsonData)
//   const content = jsonData.choices[0].message.content

//   return content
// }
function fetchBot(message) {
  // Simulate API call
  // messages.push({role: "user", content: message})

  const chatRequest = {
    messages: messages 
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
      console.log(data);
      messages.push({role: "assistant", content: data.reply})
      addMessage("bot", data["reply"]);
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

// function addMessage(sender, text) {
//   const chatWindow = document.getElementById("chat-window");

//   const messageWrapper = document.createElement("div");
//   messageWrapper.classList.add("message", sender);

//   const bubble = document.createElement("div");
//   bubble.classList.add("bubble");

//   // Convert [spoiler]text[/spoiler] to span
//   const safeText = text.replace(
//     /\[spoiler\](.*?)\[\/spoiler\]/g,
//     '<span class="spoiler">$1</span>'
//   );
//   bubble.innerHTML = safeText;

//   // // Allow rendering HTML like spoiler spans
//   // bubble.innerHTML = text;

//   // Attach click event to spoiler spans
//   bubble.querySelectorAll(".spoiler").forEach((spoiler) => {
//     spoiler.addEventListener("click", () => {
//       spoiler.classList.toggle("revealed");
//     });
//   });

//   messageWrapper.appendChild(bubble);
//   chatWindow.appendChild(messageWrapper);
//   chatWindow.scrollTop = chatWindow.scrollHeight;
// }

function addMessage(sender, text) {
  const chatWindow = document.getElementById("chat-window");

  const messageWrapper = document.createElement("div");
  messageWrapper.classList.add("message", sender);

  const bubble = document.createElement("div");
  bubble.classList.add("bubble");

  // Optional: Handle [spoiler] tags first
 const withSpoilers = text;//.replace(/\[spoiler\](.*?)\[\/spoiler\]/g, '<span class="spoiler">$1</span>');

  // Convert markdown to HTML
  // const html = marked.parse(withSpoilers);
  // html = withSpoilers;

  bubble.innerHTML = withSpoilers;

  // Click to reveal spoilers
  bubble.querySelectorAll(".spoiler").forEach(spoiler => {
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
    // retrieveQuestion();
    sendMessage();
  });
});

const username = sessionStorage.getItem("username");

// Redirect if not logged in
if (!username) {
  window.location.href = "login.html";
}

// Show welcome message in chat

let seconds = 0;

window.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {
    addMessage("bot", `Welcome, ${username}!`, "system");
  }, 500);

  setInterval(() => {
    seconds++;
    //console.log("Its been " + seconds + " seconds since we started");
  }, 1000);
});

// window.addEventListener('load', function() {
//   // Step 1: Extract the problem slug from the URL
//   const url = window.location.href; // Get the current page URL
//   const titleSlug = url.split('/').pop(); // Extract the part after /problems/
  
//   console.log("Problem Slug:", titleSlug);

// fetch("https://leetcode.com/graphql", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//   },
//   body: JSON.stringify({
//     query: `
//       query getQuestionDetail($titleSlug: String!) {
//         question(titleSlug: $titleSlug) {
//           title
//           content
//           difficulty
//           likes
//           dislikes
//           topicTags {
//             name
//           }
//         }
//       }
//     `,
//     // variables: {
//     //   titleSlug: "last-day-where-you-can-still-cross",
//     // },
//   }),
// })
//   .then((res) => res.json())
//   .then((data) => {
//     const q = data.data.question;
//     console.log("Title:", q.title);
//     console.log("Difficulty:", q.difficulty);
//     console.log("Tags:", q.topicTags.map((tag) => tag.name).join(", "));
//     // document.body.innerHTML = q.content; // contains full HTML-formatted problem description
// });
// });


// fetch("https://leetcode.com/graphql", {
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//   },
//   body: JSON.stringify({
//     query: `
//       query getQuestionDetail($titleSlug: String!) {
//         question(titleSlug: $titleSlug) {
//           title
//           content
//           difficulty
//           likes
//           dislikes
//           topicTags {
//             name
//           }
//         }
//       }
//     `,
//     variables: {
//       titleSlug: "last-day-where-you-can-still-cross",
//     },
//   }),
// })
//   .then((res) => res.json())
//   .then((data) => {
//     const q = data.data.question;
//     console.log("Title:", q.title);
//     console.log("Difficulty:", q.difficulty);
//     console.log("Tags:", q.topicTags.map((tag) => tag.name).join(", "));
//     // document.body.innerHTML = q.content; // contains full HTML-formatted problem description
// });

function injectContentScript(tabId, url) {
  if (url && url.includes('https://leetcode.com/problems/')) {
    chrome.scripting.executeScript({
      target: { tabId },
      files: ['content.js']
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const activeTab = tabs[0];
    if (activeTab.url && activeTab.url.includes('https://leetcode.com/problems/')) {
      chrome.scripting.executeScript({
        target: { tabId: activeTab.id },
        files: ['content.js']
      });
    }
  });
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.status === 'complete') {
    injectContentScript(tabId, tab.url);
  }
});

// Fires when the user switches tabs
chrome.tabs.onActivated.addListener(activeInfo => {
  chrome.tabs.get(activeInfo.tabId, (tab) => {
    if (tab.status === 'complete') {
      injectContentScript(tab.id, tab.url);
    }
  });
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "leetcode-problem") {
    const { title, contentHTML, difficulty } = message;
    messages.push({role: 'user', content: contentHTML});
    console.log(contentHTML)
    addMessage("bot", title);
    addMessage("bot", contentHTML);
    addMessage("bot", difficulty);

    console.log("aaaaa");
  }
});

