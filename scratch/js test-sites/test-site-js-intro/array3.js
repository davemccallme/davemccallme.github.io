// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Test_your_skills:_Arrays 

let myArray = [ "Ryu", "Ken", "Chun-Li", "Cammy", "Guile", "Sakura", "Sagat", "Juri" ];
const name1 = 'Chelito';
const name2 = 'Bonita';

//remove last item
myArray.pop();

//add two names to end of array
myArray.push(name1, name2);

//add index number to each item in array i.e. 'Ryo (0)' (ES6)
const nameIndex = myArray.map((value, index) => (`${value}  (${index})`)); 

//for ES5 
//function nameIndex (value, index) {
//    return (`${value}  (${index}) -`); 
//}

let myString = nameIndex.join(' - ')
console.log(myString);

// Don't edit the code below here!

    