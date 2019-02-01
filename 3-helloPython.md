1) For Loops
I found that a normal for loop in JavaScript looks like this:

for (var i = 0; i < array.length; i++) {
    array[i]
  }
However, in Python, it looks more like the JavaScript “for in” loop:

for x in range(0, 3):
    print "We're on time %d" % (x)
for loop from 0 to 2, therefore running 3 times.

2) Variables
In JavaScript, variables need to be defined by first calling “let, var or const”.

let x = 1
const y = 2
var z = 3
let my_array = [1, 2, 3, 4]
In Python, you can simply type the variable name without defining it as a variable.

x = 1
y = 2
z = 3
my_array = [1, 2, 3, 4]
3) Functions
In JavaScript, functions are called using “function” and can take a parameter, or multiple parameters:

function test_prime(n){
// do stuff
}
In Python, they are basically the same but are called using the keyword “def” instead.

def test_prime(n):
   //do stuff
Another major difference between function calls is that in JavaScript, the work inside the function is always between curly braces, following the parameters. In Python, a function begins with a colon, and instead of curly braces, the function is anything indented below the line calling the function. With some of the packages we installed earlier, you’ll often see “unexpected indent” letting you know that you’ve indented something that doesn’t need to be there. This is a little hard to get used to, if you’re more familiar with something like JavaScript, where indentions don’t affect the code.

4) console log
In JavaScript, if you want to run a script, or block of code, you can simply console.log it

console.log(my_function);
In Python, you generally use the “print” command

print solution
