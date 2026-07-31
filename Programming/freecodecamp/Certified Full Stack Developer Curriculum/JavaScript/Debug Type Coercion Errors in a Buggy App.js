// Before
var firstResult = 5 + "10";
console.log(`5 + 10 = ${firstResult}`);

var secondResult = "Eight" - 5;
console.log(`8 - 5 = ${secondResult}`);

var thirdResult = true + 5;
console.log(`1 + 5 = ${thirdResult}`);

var fourthResult = false + 8;
console.log(`0 + 8 = ${fourthResult}`);

var fifthResult = "10" * 2;
console.log(`10 * 2 = ${fifthResult}`);

var sixthResult = null + 22;
console.log(`0 + 22 = ${sixthResult}`);


// After

var firstResult = 5 + 10;
console.log(`5 + 10 = ${firstResult}`);

var secondResult = "8" - 5;
console.log(`8 - 5 = ${secondResult}`);

var thirdResult = 1 + 5;
console.log(`1 + 5 = ${thirdResult}`);

var fourthResult = 0 + 8;
console.log(`0 + 8 = ${fourthResult}`);

var fifthResult = 10 * 2;
console.log(`10 * 2 = ${fifthResult}`);

var sixthResult = 0 + 22;
console.log(`0 + 22 = ${sixthResult}`);