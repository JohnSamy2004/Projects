function chunkArrayInGroups(arr, limit){
  let groups = [];
  let items = [...arr];
  for (let i = 0; i < items.length; i += limit){
     groups.push(items.slice(i, i + limit))
  }
  return groups;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2))