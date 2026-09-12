function findLongestWordLength(str){
  let temp = 0;
  let wordArray = str.split(" ")
  for (let i = 0; i < wordArray.length; i++){
     if (temp < wordArray[i].length){
      temp = wordArray[i].length;
     }
  }
  return temp;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog")