const espresso = require('espresso-logic-minimizer');

const pla = [
    '.i 4',
    '.o 1',
    '0000 0',
    '0001 1',
    '0010 0',
    '0011 1',
    '0100 0',
    '0101 1',
    '0110 0',
    '0111 1',
    '1000 0',
    '1001 1',
    '1010 0',
    '1011 1',
    '1100 0',
    '1101 0',
    '1110 0',
    '1111 1',
    '.e'
  ];

console.log('result = ', espresso.minimize(pla));
