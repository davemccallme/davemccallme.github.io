
   //You can also concatenate strings using the + operator:
   const greeting = "Hello";
   const name = "Chris";
   console.log(greeting + ", " + name); // "Hello, Chris"

   //However, template literals usually give you more readable code:
   const greeting2 = "Hello";
   const name2 = "Chris";
   console.log(`${greeting2}, ${name2}`); // "Hello, Chris"

//--------------------------------------------------------------------/
   //Template literals respect the line breaks in the source code, so you can write strings that span multiple lines like this:
  
  //ref: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
   const output = `I like the song.
   I gave it a score of 90%.`;
   console.log(output);  // I like the song.
                         // I gave it a score of 90%.
   

   const output = 'I like the song.\nI gave it a score of 90%.';
   console.log(output);  // I like the song.
                        // I gave it a score of 90%.
                         
//--------------------------------------------------------/



//Without template literals, when you want to combine output from expressions with strings, you'd concatenate them using the "+" (plus sign) (addition operator):                    
   let a = 5;
   let b = 10;
      console.log('Fifteen is ' + (a + b) + ' and\nnot ' + (2 * a + b) + '.');
   // "Fifteen is 15 and
   // not 20."             
 
/*That can be hard to read – especially when you have multiple expressions.
With template literals,
you can avoid the concatenation operator — and improve the readability of your code — by using placeholders of the form "${expression}" to perform substitutions for embedded expressions:
 */
   let a = 5;
   let b = 10;
   console.log(`Fifteen is ${a + b} and
   not ${2 * a + b}.`);
   // "Fifteen is 15 and
   // not 20."

   //------------------------------------------------------------------------------------//
