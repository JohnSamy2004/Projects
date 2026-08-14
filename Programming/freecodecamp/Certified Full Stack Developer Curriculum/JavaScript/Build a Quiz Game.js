const questions = [];

const q1 = {
  category: "General Knowledge",
  question: "What is the largest ocean in the world?",
  choices: ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean"],
  answer: "Pacific Ocean"
};

const q2 = {
  category: "Science",
  question: "What planet is known as the Red Planet?",
  choices: ["Mars", "Venus", "Jupiter"],
  answer: "Mars"
};

const q3 = {
  category: "History",
  question: "Who was the first president of the United States?",
  choices: ["Abraham Lincoln", "George Washington", "Thomas Jefferson"],
  answer: "George Washington"
};

const q4 = {
  category: "Geography",
  question: "What is the capital city of France?",
  choices: ["London", "Rome", "Paris"],
  answer: "Paris"
};

const q5 = {
  category: "Sports",
  question: "How many players are there on a soccer team on the field?",
  choices: ["11", "9", "12"],
  answer: "11"
};

questions.push(q1, q2, q3, q4, q5);


function getRandomQuestion(arr) {
  let randomNumber = Math.floor(Math.random() * arr.length);
  return arr[randomNumber];
}

function getRandomComputerChoice(choices) {
  let randomChoice = Math.floor(Math.random() * choices.length);

  return choices[randomChoice];
}

function getResults(qObject, choice) {
  if (choice === qObject.answer) {
    return "The computer's choice is correct!";
  } else {
    return `The computer's choice is wrong. The correct answer is: ${qObject.answer}`;
  }
}