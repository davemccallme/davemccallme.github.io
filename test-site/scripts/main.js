let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/24hr of Lemons - Collage 1.png') {
      myImage.setAttribute('src','images/My test image.jpg');
    } else {
      myImage.setAttribute('src','images/24hr of Lemons - Collage 1.png');
    }
}

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

let lemon = '24hr of Lemons';

function setUserName() {
    let myName = prompt('Please enter your name.');
    if(!myName) {
      setUserName();
    } else {
      localStorage.setItem('name', myName);
      myHeading.textContent = lemon + ' is cool, ' + myName;
    }
  }

  if(!localStorage.getItem('name')) {
    setUserName();
  } else {
    let storedName = localStorage.getItem('name');
    myHeading.textContent = lemon + '  is cool, ' + storedName;
  }

  myButton.onclick = function() {
    setUserName();
  }
  