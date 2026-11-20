'use strict';

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

const list = document.getElementById('rolls');
let roll;

do {
  roll = rollDice();
  const li = document.createElement('li');
  li.textContent = roll;
  list.appendChild(li);
} while (roll !== 6);