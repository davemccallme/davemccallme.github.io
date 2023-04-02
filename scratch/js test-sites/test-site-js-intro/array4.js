/*
Find the index of the "Eagles" item, and use that to remove the "Eagles" item.
Make a new array from this one, called eBirds, that contains only birds from the original array whose names begin with the letter "E". 
Note that startsWith() is a great way to check whether a string starts with a given character.
If it works, you should see "Emus,Egrets" appear in the termial.
*/



const birds = [ "Parrots", "Falcons", "Eagles", "Emus", "Caracaras", "Egrets" ];

const removeEagle = birds.indexOf('Eagles')
birds.splice(removeEagle,1);

const eBirds = birds
    .filter(value => value.startsWith('E'))
    .join(',');
console.log(eBirds);
