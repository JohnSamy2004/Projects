function truncateString(string, n){
  if(string.length <= n){
    return string
  } else {
    return string.slice(0, n) + '...'
  }
}

console.log(truncateString("A-tisket a-tasket A green and yellow basket", 8))