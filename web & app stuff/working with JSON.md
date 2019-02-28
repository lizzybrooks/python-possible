# JSON files and Python 
---
The reference in this folder explains briefly what JSON is. 
I am sure you remember objects from javascript
```
var person = {
  firstName: "John",
  lastName: "Doe",
  age: 50,
  eyeColor: "blue"
};
```
and then to access the items in `person` you just say `person.firstName` for example. 

Ok, so now there is one last super simple but super important thing to know about JSON. The whole file is an object! that means that it starts with `{` and ends with `}` and is NOT set to a variable it is just there. 

* as a sidenote, if you have an unknow number of things to add to your JSON file then what you can do is this: 
```
{
  "array_name":[ some elements ] // the quotes on the name matter also this is a comment. the parser (which will be seen shortly) can't handle these in most languages
}
```
 Now we have enough information to dive in!
