'use strict';

const count = Number(prompt('How many participants?'));
const names = [];

for (let i = 0; i < count; i++) {
  const name = prompt(`Enter the name of participant ${i + 1}:`);
  names.push(name);
}

names.sort((a, b) => a.localeCompare(b));

const list = document.getElementById('participants');

for (const name of names) {
  const li = document.createElement('li');
  li.textContent = name;
  list.appendChild(li);
}