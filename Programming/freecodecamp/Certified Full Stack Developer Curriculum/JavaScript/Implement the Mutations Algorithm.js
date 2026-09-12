function mutation(arr){
  let firstWord = arr[0].toLowerCase();
  let secondWord = arr[1].toLowerCase();

  for (let i = 0; i < secondWord.length; i++){
    if(firstWord.indexOf(secondWord[i]) === -1){
      return false
    }
  }

  return true;
}