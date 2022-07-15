//https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Test_your_skills:_Strings

const theorem = 'Pythagorean theorem';

const a = 5;
const b = 8;
//a**2 + b**2 = c**2 
const c = ((a**2+b**2)**0.5)

const myString = 'Using *, we can work out that that if the two shortest sides of a right-angled triangle have lengths of * and *, the length of the hypotenuse is *.';

const firstAst = myString.indexOf('*'); // #
const secondAst = myString.indexOf('*', firstAst+1); // #
const thirdAst = myString.indexOf('*', secondAst+1); // #
const fourthAst = myString.indexOf('*', thirdAst+1); // #

const sliceOne = myString.slice(0,firstAst+1) // Using *,
const sliceTwo = myString.slice(firstAst+1, secondAst+1) // ...lengths of *
const sliceThree = myString.slice(secondAst+1, thirdAst+1) //  and *,
const sliceFour = myString.slice(thirdAst+1, fourthAst+1) // ...hypotenuse is *.

const subOne = sliceOne.replace('*', theorem)
const subTwo = sliceTwo.replace('*', a)
const subThree = sliceThree.replace('*', b)
const subFour = sliceFour.replace('*', c)


const myStringTemplate = `${subOne}${subTwo}${subThree}${subFour}`;


// Don't edit the code below here!

section.innerHTML = ' ';
const para1 = document.createElement('p');
para1.textContent = myStringTemplate;

section.appendChild(para1);
    