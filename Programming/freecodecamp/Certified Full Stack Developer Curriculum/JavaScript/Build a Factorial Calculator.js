let num = 5;
function factorialCalculator(num){
  if (!(num >= 1 && num <= 20)){
    return
  }
  let result = 1;
  for (let i = num; i <= num; i--){
    if (i === 0){
      break;
    }
     result *= i
  }
  return result;
}

let factorial = factorialCalculator(num);
let resultMsg = `Factorial of ${num} is ${factorial}`;
console.log(resultMsg);