'use strict';

const numbers = [];
let number;

do {
  number = Number(prompt('Enter a number (0 to stop):'));
  if (number !== 0) {
    numbers.push(number);
  }
} while (number !== 0);

numbers.sort((a, b) => b - a);

console.log('Numbers from largest to smallest:');
for (const n of numbers) {
  console.log(n);
}