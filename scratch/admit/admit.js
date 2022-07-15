const people = ['Chris', 'Anne', 'Colin', 'Terri', 'Phil', 'Lola', 'Sam', 'Kay', 'Bruce'];

const info = document.createElement('p');
const html = document.querySelector('html');

const admit = admitted.textContent = 'Admit: ';
const refuse = refused.textContent = 'Refuse: ';

// loop starts here
	
    for (const name of people) {
        if (name === 'Phil' || name === 'Lola') {
            refused.textContent += `${name}, `;
        } else admitted.textContent += `${name}, `;
    }


    console.log(refused.textContent.length);


 
 

