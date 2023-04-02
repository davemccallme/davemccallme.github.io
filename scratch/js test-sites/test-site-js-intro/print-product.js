
const list = document.querySelector('.output ul');
const totalBox = document.querySelector('.output p');
let total = 0;
list.innerHTML = '';
totalBox.textContent = '';
// number 1

const data = "'Underpants:6.99''Socks:5.99''T-shirt:14.99''Trousers:31.99''Shoes:23.99'";
    console.log(data);    
const dataDelim = data.replaceAll("'",",");    //'word','word' = [,word,,word,,...
    console.log(dataDelim);
const dataCSV = dataDelim.replaceAll(",,",",");  //replacce ',,,' with ', ' -> [,word, word, word]
    console.log(dataCSV);
const products = dataCSV.split(','); // split into array by ','....
    console.log(products);
products.shift();  //.shift[0] to remove first empty array value [(,)word, word, ...]
    console.log(products);
products.pop();  // to remove last empty array value comma [(,)word, word, ...]
    console.log(products);

// number 2
    
    for (const product of products) {
// number 3
        const subArr = product.split(':');         // [['Underpants', '6.99'],['Socks', '5.99'], ....]
        const productName = subArr[0]; //[[Underpants],[socks],[...]]
        const productPrice = Number(subArr[1]);  //[[14.99],[5.99], [...]]
// number 4
        total += productPrice;
// number 5
        let itemText =`${productName} - $${productPrice}`;
       
        const listItem = document.createElement('li');
        listItem.textContent = itemText;
        list.appendChild(listItem);
// number 6
    }
    totalBox.textContent = `Total: $${total.toFixed(2)}`;
