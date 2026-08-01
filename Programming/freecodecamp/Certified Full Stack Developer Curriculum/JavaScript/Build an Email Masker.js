function maskEmail(email){
  let firstCharacter = email[0];
  let lastCharacter = email[email.indexOf('@') - 1];
  let userName = email.slice(1, email.indexOf('@') - 1);
  let lengthUserName = userName.length;
  let asteriskRepeated = '*'.repeat(lengthUserName);

  let domainName = email.slice(email.indexOf('@'));


  return firstCharacter + asteriskRepeated + lastCharacter + domainName;

}

let email = "myEmail@email.com";
console.log(maskEmail(email));