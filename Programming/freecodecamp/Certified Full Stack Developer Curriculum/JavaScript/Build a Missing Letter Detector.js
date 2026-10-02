let alphabets = "abcdefghijklmnopqrstuvwxyz";

function fearNotLetter(str) {

  let start = alphabets.indexOf(str[0]);

  for (let i = 0; i < str.length; i++) {

    if (str[i] !== alphabets[start + i]) {
      return alphabets[start + i];
    }

  }

  return undefined;
}