//https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals
if ( choice === 'April'  
  || choice === 'June' 
  || choice === 'September' 
  || choice === 'November'
  ){ days = 30;
} else if (choice === 'February') {
  days = 28;
} else {
  days = 31; // Jan, Mar, May, July, Aug, Oct, Dec
}
console.log(month, days)
