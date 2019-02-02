# Python Installation and Creating a Virtual Environment 

There are two versions of Python, Python 2 and Python 3. For this class we will be using Python 3, which you will need to install on your computer. 

## Windows
I will figure this out soon using [this guide](https://docs.python-guide.org/starting/install3/win/)



## Mac
### Install Homebrew
Homebrew is what's called a package manager. It allows you to install software via the command line.

Visit [Homebrew's website](https://brew.sh/) and follow the instructions there, or just copy and paste the following into your terminal:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Install Python 3

Once Homebrew is done, you can use it to install Python and a number of other extremely useful command line tools.

```bash
brew install python3
```

NOTE: If you think you may already have Python installed, you can run this command to check:

```bash
python --version
```

## Create a Virtual Environment for your Python Project

One of the great things about Python is that it's modular. There's a basic template, Python 2.7 or 3, which you installed, and then there are lots of other pieces that you can add when you need them. These pieces are called packages or dependencies. They're like code libraries that bring you extra functionality and you can install them a la carte. Python stays relatively lightweight and you install what you need. 

The problem with this system is that sometimes the packages conflict with one another. You might have code that you wrote 2 years ago that uses Python 2.7 and code that you wrote yesterday that uses Python 3. If you try to run your 2.7 code in 3, it breaks. 

Ugg. 

The solution is to create a special folder on your hard drive for each Python project. This folder is called a **Virtual Environment**

Your virtual environment contains an isolated copy of Python and the packages that you need for your project. Each project should have its own virtual environment. 

#### If you prefer watching videos to reading instructions, you can follow [this tutorial](https://www.youtube.com/watch?v=nnhjvHYRsmM) to set up virtual environments. 

#### If you prefer following written instructions, read on:

1. Install virtualenv. Virtualenv is a tool to create isolated Python environments. It basically creates a folder that's a copy of your Python installation, with everything you need inside. Then you build your Python project inside that folder. 

You install virtualenv via the command line, with this simple line of code: 

```bash
pip install virtualenv
```
If that gives you an error, make sure you have pip installed (pip is Python's package manager). 

```bash
pip --version
```
2. Test your installation of virtualenv:

```bash
virtualenv --version
```
If that gives you some number (e.g. 16.3.0), that means that you have the software installed. Good job. 

3. cd to your Documents (or Desktop, if you prefer to store your work there), and make a folder to hold the projects that you will do in this class. I'm going to call mine pythonland, but you feel free to come up with a better name. 

```bash
cd Documents
mkdir pythonland
cd pythonland
```
4. Inside pythonland (or your project folder), create a virtual environment, aka a copy of your python installation. I'll call mind february_projects. Again, call yours what you want. 
If you don't give it a name and just type virtualenv, it will copy all the python files into the current directory (i.e. pythonland). 

```bash
virtualenv february_projects
```
Okay. Now you should see a folder called february_projects (or whatever you called yours) that holds a lot of Python files. I hope it worked!

## Run Python from the command line



## Add a script extension to your favorite text editor 

Unlike JavaScript, which runs when you load your website into a browser, a python script needs to be told "go". You can install an extension in your editor that will let you run your python code. 
I will update this list with links to good script packages. 

* Atom : Go to Atom --> Preferences --> Packages and search for **Script**. 
  * You might also want a Python autocomplete package. [Here's a good one](https://atom.io/packages/autocomplete-python). 
  * While you're installing stuff in Atom, you might play around with themes to color the text and background. I like Atom-Material [syntax](https://atom.io/themes/atom-material-syntax) and [UI](https://atom.io/themes/atom-material-ui). 

* [Visual Studio Code](https://code.visualstudio.com/)
  * Install the [Python Extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python), which essentially makes your text editor into an IDE (I think). 
  * Install [CodeRunner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner)

