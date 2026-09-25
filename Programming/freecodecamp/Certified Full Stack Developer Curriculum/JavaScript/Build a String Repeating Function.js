function repeatStringNumTimes(str, num){
  let repeatedString = "";
  for (let i = 0; i < num; i++){
    repeatedString += str
  }
  return repeatedString
}

console.log(repeatStringNumTimes("*", 3))