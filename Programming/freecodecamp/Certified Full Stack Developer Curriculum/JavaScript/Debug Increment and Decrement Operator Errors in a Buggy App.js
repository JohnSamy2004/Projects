// Before

var counter = 10;
console.log(`Counter is currently ${counter}`);

var updatedCounter = counter++;
console.log(`Counter is now ${updatedCounter}`);

var score = 8;
console.log(`Score is currently ${score}`);

var finalScore = ++score;
console.log(`Score is still ${finalScore}`);

var coins = 3;
console.log(`Coins is currently ${coins}`);

var updatedCoins = coins--;
console.log(`Coins is now ${updatedCoins}`);

var health = 7;
console.log(`Health is currently ${health}`);

var newHealth = --health;
console.log(`Health is still ${newHealth}`);

// After

var counter = 10;
console.log(`Counter is currently ${counter}`);

var updatedCounter = ++counter;
console.log(`Counter is now ${updatedCounter}`);

var score = 8;
console.log(`Score is currently ${score}`);

var finalScore = score++;
console.log(`Score is still ${finalScore}`);

var coins = 3;
console.log(`Coins is currently ${coins}`);

var updatedCoins = --coins;
console.log(`Coins is now ${updatedCoins}`);

var health = 7;
console.log(`Health is currently ${health}`);

var newHealth = health--;
console.log(`Health is still ${newHealth}`);