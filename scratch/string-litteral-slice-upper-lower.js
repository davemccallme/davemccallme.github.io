
const list = document.querySelector('.output ul');
list.innerHTML = '';
const cities = ['lonDon', 'ManCHESTer', 'BiRmiNGHAM', 'liVERpoOL'];

for (let city of cities) {
  // write your code just below here

  const lower = city.toLowerCase();
  const removeFirstLetter = lower.slice(1);
  const firstLetter = city.slice(0,1);
  const capitalizeFirstLetter = firstLetter.toUpperCase();

  const result =(`${capitalizeFirstLetter}${removeFirstLetter}`);
  const listItem = document.createElement('li');
  listItem.textContent = result;
  list.appendChild(listItem);
}
