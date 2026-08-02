function confirmEnding(str1, str2){
  let ending = str1.slice(-str2.length)
  return ending.includes(str2)
}

console.log(confirmEnding("Connor", "n"));