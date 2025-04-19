let timer = 25 * 60;
let interval;

function updateTimer() {
  const minutes = Math.floor(timer / 60).toString().padStart(2, '0');
  const seconds = (timer % 60).toString().padStart(2, '0');
  document.getElementById('timer').innerText = `${minutes}:${seconds}`;
}

document.getElementById('start').addEventListener('click', () => {
  clearInterval(interval);
  timer = 25 * 60;
  interval = setInterval(() => {
    timer--;
    updateTimer();
    if (timer <= 0) {
      clearInterval(interval);
      alert("⏰ Time's up! Take a break or try a new LeetCode problem.");
    }
  }, 1000);
});

updateTimer();
