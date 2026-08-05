let lunches = [];

function addLunchToEnd(arr, str) {
  arr.push(str);
  console.log(`${str} added to the end of the lunch menu.`);
  return arr;
}

function addLunchToStart(arr, str) {
  arr.unshift(str);
  console.log(`${str} added to the start of the lunch menu.`);
  return arr;
}

function removeLastLunch(arr) {
  if (arr[arr.length - 1]) {
    let lastItem = arr[arr.length - 1];
    arr.pop();
    console.log(`${lastItem} removed from the end of the lunch menu.`);
    return arr;
  } else {
    console.log("No lunches to remove.");
  }
}

function removeFirstLunch(arr) {
  if (arr[0]) {
    let firstItem = arr[0];
    arr.shift();
    console.log(`${firstItem} removed from the start of the lunch menu.`);
    return arr;
  } else {
    console.log("No lunches to remove.");
  }
}

function getRandomLunch(arr) {
  if (arr.length > 0) {
    console.log(`Randomly selected lunch: ${arr[Math.floor(Math.random() * arr.length)]}`);
  } else {
    console.log("No lunches available.");
  }
}

function showLunchMenu(arr) {
  if (arr.length > 0) {
    console.log(`Menu items: ${arr.join(", ")}`);
  } else {
    console.log("The menu is empty.");
  }
}

getRandomLunch(["Stew", "Soup", "Toast"]);