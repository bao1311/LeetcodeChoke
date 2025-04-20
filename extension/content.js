console.log("content.js loaded");

getProblem();

function getProblem(){
    const title = document.querySelector('.text-title-large')?.innerText;
    const contentHTML = document.querySelector('div[data-track-load="description_content"]')?.innerHTML;
    let difficulty = document.querySelector('.text-difficulty-easy')?.innerText;
    if (!difficulty)
        difficulty = document.querySelector('.text-difficulty-medium')?.innerText;
    if (!difficulty)
        difficulty = document.querySelector('.text-difficulty-hard')?.innerText;

    console.log("LeetCode Problem Title:", title);
    console.log("Difficulty:", difficulty);
    console.log("Content:", contentHTML);

    // You can also send this to your extension popup or background script
    chrome.runtime.sendMessage({
        type: "leetcode-problem",
        title,
        contentHTML,
        difficulty
    });
}



