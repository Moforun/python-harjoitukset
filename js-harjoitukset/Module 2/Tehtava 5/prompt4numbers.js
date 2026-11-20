'use strict';

const numbers = [];
let repeated = false;

while (!repeated) {
  const number = Number(prompt('Enter a number:'));

  if (numbers.includes(number)) {
    alert(`The number ${number} has already been given.`);
    repeated = true;
  } else {
    numbers.push(number);
  }
}

numbers.sort((a, b) => a - b);

console.log('Numbers in ascending order:');
for (const n of numbers) {
  console.log(n);
}