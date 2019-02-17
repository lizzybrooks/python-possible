# Scraping the Web: Part 1

Before we begin scraping the web with python scripts, it helps to know what you're looking at when you see a web page.
Here's a lightning introduction to HTML, which, in combination with JavaScript, creates the appearance, structure and functionality of the web. 

# Intro to HTML

HTML is a markup language. 
HTML literally stands for hyper text markup language. 
Markup language means a computer language that defines the structure and appearance of raw text. 


## Tags

1. Create a new file called index.html and copy and paste the contents of [this starter](https://github.com/lizzybrooks/python-possible/blob/master/templates/index.html) into it. 

2. Open your index.html file with your web browser (aka Chrome or Firefox). 

3. Practice changing the text that displays in your browser (edit your index.html file, save, and refresh). 

HTML works as a series of **tags**.
A tag looks like:

    <tagname>some stuff</tagname>

The beginning of the tag, the contents of it, and the closing of a tag. Note that the closing tag has a / before the tagname. 

There’s different types for different things


- \<p\> paragraph
- \<strong\> makes text bold
```
  - this text is normal and \<strong\>this text is bold\</strong\>
```  

- <p> paragraph
- <strong> makes text bold
```
  - this text is normal and <strong>this text is bold</strong>
```  
- <a> makes a link
```
  - <a href=”http://www.google.com>go to google</a>
```  
- <h1> makes a header
```
  - \<h1\>My Header\</h1\>
```  
- \<div\> represents a random division of text
```
  - \<div\>I’m a div\</div\>
``` 

4. Add some headers and a link or two to your index.html file.

## Attributes

Each tag can have a series of attributes, a set of **key** and **value** pairs
Two most important ones for scraping is

- **id** attribute 
  - gives a unique identifier to a particular tag
    - \<p id=”the-most-important-paragraph”\>Hi I’m very important\</p\>
  - an id can only be applied to one tag
- **class** attribute
  - designates a category of tag, that the author of the page uses to find or group
  - you can have multiple tags with the same class
    - \<p class=”moderately-important”\>I am somewhat important\</p\>
    - \<p class=”moderately-important”\>I am also somewhat important\</p\>


## Specific attributes

There’s some attributes that can only be applied to certain tags

- **href** is only applied to \<a\> to indicate where to go when you click on a link
  - \<a href=”http://www.google.com”\>google\</a\>
- **src** only applied to \<img\> to indicate which image
  - \<img src=”logo.png\>


## Structure

A web page looks like this

    
    \<html\>
      \<head\>
        \<title\>My page title\</title\>
      \</head\>
      \<body\>
        \<h1\>Hello i am header\</h1\>
    
        \<p\>a paragraph\</p\>
        
      \</body\>
    \</html\>


## CSS

Cascading Style Sheets, 
just know that CSS is used to apply style to a page
so the HTML stays the same for the content but the CSS indicates text color, sizes, etc.

it’s comprised of a selector, that references a part of the page, brackets that contain style

A CSS style sheet looks like this

    // this sets all the p tags to have a red border
    p {
      border: 1px solid red;
    }
    

Different selectors

    
    // style the p tags and all the strong tags
    p, strong {
    }
    
    // style all the \<a\> tags inside all the \<p\> tags
    p a {
    
    }
    
    // style everything with a certain class name, preseed with a period
    .moderately-important {
    
    }
    
    // style an id, using #. e.g. style this \<p id="logo"\>logo text\</p\>
    #logo {
    
    }
    
    // style the \<a\> tags inside \<p\> tags, but only if they're a certain class
    p a.moderately-important {
    
    }
    
# Web scraping


Open Chrome


## View source 

go to a website
e.g. https://newyork.craigslist.org/d/antiques/search/ata

Right click \> View Source
to see the source code



## See source code for specific elements

Right click \> Inspect

Highlights the part of the website as you hover over the source code.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491358282_image.png)





## To scrape you want to figure out how to find a certain element

We right click a header and inspect the structure of the page where that element is.

We see that it’s a specific **class**, so we can find all elements of that class to see if that gives us all the headers/

We right click a craigslist header and find:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491758062_image.png)


we see that its class attribute says **result-title,** and that it’s inside an **\<a\>** tag
so we’ll try to find **all the \<a\> tags with the result-title attribute, to find all the headers**

## Testing inside the browser

You can quickly find elements inside the browser using the **Console.**

you can use the document.querySelectorAll() that takes one argument that is a css selector


    
    document.querySelectorAll("h2") // finds all the h2 tags
    




## Getting the CSS selector for an element automatically

On the console:
Right click \> Copy \> Copy Selector
gets you the CSS selector
**but this only helps sometimes**

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D67961504E4563B95DDF29A2542D190EAEAA0F940919FBD5CB2C6591C6D3326E_1538491844671_image.png)
