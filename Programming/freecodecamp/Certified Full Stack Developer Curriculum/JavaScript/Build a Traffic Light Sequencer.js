const config1 = {
  fault: false,
  phases: [
    { color: "green", duration: 5 },
    { color: "yellow", duration: 2 },
    { color: "red", duration: 4 }
  ]
};

const config2 = {
  fault: false,
  phases: [
    { color: "red", duration: 3 },
    { color: "yellow", duration: -2 },
    { color: "green", duration: 6 }
  ]
};

const config3 = {
  fault: true,
  phases: [
    { color: "green", duration: 5 },
    { color: "yellow", duration: 2 },
    { color: "red", duration: 6 }
  ]
};

const config4 = {
  fault: false,
  phases: []
};

function runSequence(config, cycles){
  if (config.fault){
        console.log("Faulted phase!");
        return;
  }
  if (config.phases.length <= 0){
        console.log("No phases found");
  }
  for (let j = 0; j < cycles; j++){
    for (let i = 0; i < config.phases.length; i++){
       if (config.phases[i].duration <= 0){
        console.log("Invalid phase detected");
    } else {
      console.log(`Switching to ${config.phases[i].color} for ${config.phases[i].duration} s`);
    }
  }
}
}

function generateTimeline(config, cycles){
  let total = 0;
  let sum = []
  for (let j = 0; j < cycles; j++){
    for (let i = 0; i < config.phases.length; i++){
      if (config.fault || config.phases[i].duration <= 0){
        
      }
      total += config.phases[i].duration;
      sum.push(total);
    }
  }
  return sum;
}
