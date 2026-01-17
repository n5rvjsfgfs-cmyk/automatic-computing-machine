let score = 0;
const tapButton = document.getElementById('tapButton');
const scoreDisplay = document.getElementById('score');

tapButton.addEventListener('click', () => {
  score++;
  scoreDisplay.textContent = score;

  if (window.Telegram?.WebApp) {
    window.Telegram.WebApp.sendData(JSON.stringify({ score: score }));
  }
});