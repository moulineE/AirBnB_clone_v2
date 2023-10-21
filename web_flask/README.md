# 0x04. AirBnB Clone - Web Framework

**By: Guillaume, CTO at Holberton School**
**Weight: 2**
**Project Started: October 19, 2023, 4:00 AM**
**Project Deadline: October 23, 2023, 4:00 AM**
**Checker Release: October 20, 2023, 4:00 AM**
**Manual QA Review Required**

## Concepts

In this project, you will be working on an AirBnB clone web framework using Flask. Before you start, make sure to familiarize yourself with the following concepts and resources:

- [AirBnB Clone](#AirBnB-clone)
- [Web Framework](#What-is-a-Web-Framework)
- [Flask](#Flask)
- [Jinja](#Jinja)
- [HTML/CSS](#HTML/CSS-Files)

### Recommended Learning Resources

We suggest you watch the following YouTube playlist to get started with Flask:

- [Python: Flask the web framework](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## Learning Objectives

Upon completing this project, you should be able to explain the following concepts without using external references:

### General

- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create an HTML response in Flask using a template
- How to create a dynamic template (loops, conditions...)
- How to display data from a MySQL database in HTML

## Copyright - Plagiarism

Please note that you are responsible for finding solutions for the project tasks yourself. Copying and pasting someone else's work or any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the project folder, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`)

A documentation is not just a single word but a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).

### HTML/CSS Files

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- A README.md file at the root of the project folder is mandatory
- Your code should be W3C compliant and validate with the W3C-Validator (except for Jinja templates)
- All your CSS files should be in the styles folder
- All your images should be in the images folder
- You are not allowed to use `!important` or id (`#...` in the CSS file)
- All HTML tags must be in uppercase
- Current screenshots have been done on Chrome 56.0.2924.87.
- No cross-browser compatibility is required

### More Information

To install Flask, run:

```
$ pip3 install Flask
```

## Manual QA Review

It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have reviewed, you should request a review from a TA or staff member.

## Tasks

### Task 0: Hello Flask!

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
- You must use the option `strict_slashes=False` in your route definition

### Task 1: HBNB

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
- You must use the option `strict_slashes=False` in your route definition

### Task 2: C is fun!

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
- You must use the option `strict_slashes=False` in your route definition

### Task 3: Python is cool!

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/<text>`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
- The default value of text is "is cool"
- You must use the option `strict_slashes=False` in your route definition

### Task 4: Is it a number?

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is "is cool"
  - `/number/<n>`: display "n is a number" only if n is an integer
- You must use the option `strict_slashes=False` in your route definition

### Task 5: Number template

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port

 `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is "is cool"
  - `/number/<n>`: display "n is a number" only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n" inside the tag BODY
- You must use the option `strict_slashes=False` in your route definition

### Task 6: Odd or even?

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is "is cool"
  - `/number/<n>`: display "n is a number" only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n" inside the tag BODY
  - `/number_odd_or_even/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n is even|odd" inside the tag BODY
- You must use the option `strict_slashes=False` in your route definition

### Task 7: Improve engines

Prepare a “”“"fake”“” (a simple function that returns a string) as a response for:
- The URL `/number_odd_or_even/number_template/<n>`

- This time, the response body should be a HTML:
    - H1 tag: "Number: n is even|odd" inside the BODY tag
- Your function should receive two arguments
    - A request argument
    - An integer argument (number)

### Task 8: List of states

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is "is cool"
  - `/number/<n>`: display "n is a number" only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n" inside the tag BODY
  - `/number_odd_or_even/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n is even|odd" inside the tag BODY
  - `/states_list`:
    - Display a HTML page: (inside the BODY tag)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
- You must use the option `strict_slashes=False` in your route definition

### Task 9: Cities by states

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display "Hello HBNB!"
  - `/hbnb`: display "HBNB"
  - `/c/<text>`: display "C ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display "Python ", followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is "is cool"
  - `/number/<n>`: display "n is a number" only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n" inside the tag BODY
  - `/number_odd_or_even/<n>`: display a HTML page only if n is an integer
    - H1 tag: "Number: n is even|odd" inside the tag BODY
  - `/states_list`:
    - Display a HTML page: (inside the BODY tag)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
  - `/cities_by_states`:
    - Display a HTML page: (inside the BODY tag)
      - H1 tag: “States”
      - UL tag: with the list of all City objects linked to the State sorted by name (A->Z)
- You must use the option `strict_slashes=False` in your route definition

### Task 10: States and State

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is “is cool”
  - `/number/<n>`: display “n is a number” only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: “Number: n” inside the tag BODY
  - `/number_odd_or_even/<n>`: display a HTML page only if n is an integer
    - H1 tag: “Number: n is even|odd” inside the tag BODY
  - `/states_list`:
    - Display a HTML page: (inside the BODY tag)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
  - `/states/<id>`:
    - Display a HTML page: (inside the BODY tag)
      - If id is not linked to any

 State, display “Not found”
      - H1 tag: “State: name” inside the tag BODY - name being the name of State
- You must use the option `strict_slashes=False` in your route definition

### Task 11: HBNB filters

Write a script that starts a Flask web application:

- Your web application must be listening on `0.0.0.0`, port `5000`
- Routes:
  - `/`: display “Hello HBNB!”
  - `/hbnb`: display “HBNB”
  - `/c/<text>`: display “C ”, followed by the value of the text variable (replace underscore `_` symbols with a space)
  - `/python/(<text>)`: display “Python ”, followed by the value of the text variable (replace underscore `_` symbols with a space)
  - The default value of text is “is cool”
  - `/number/<n>`: display “n is a number” only if n is an integer
  - `/number_template/<n>`: display a HTML page only if n is an integer
    - H1 tag: “Number: n” inside the tag BODY
  - `/number_odd_or_even/<n>`: display a HTML page only if n is an integer
    - H1 tag: “Number: n is even|odd” inside the tag BODY
  - `/states_list`:
    - Display a HTML page: (inside the BODY tag)
      - H1 tag: “States”
      - UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)
  - `/states/<id>`:
    - Display a HTML page: (inside the BODY tag)
      - If id is not linked to any State, display “Not found”
      - H1 tag: “State: name” inside the tag BODY - name being the name of State
  - `/cities_by_states`:
    - Display an HTML page (inside the BODY tag)
    - H1 tag: “States”
    - UL tag: with the list of all City objects linked to the State sorted by name (A->Z)
  - `/states_list/<n>`:
    - Display an HTML page: (inside the BODY tag)
    - H1 tag: “States”
    - UL tag: with the first n State objects present in DBStorage sorted by name (A->Z)
- When n is not an integer, 404 error page is displayed
  - You must use the option `strict_slashes=False` in your route definition
- Templates must be stored in the `templates` folder


## What is a Web Framework?

A web framework is a software framework designed to aid the development of web applications including web services, web resources, and web APIs. They offer various tools, libraries, and design patterns to streamline the process of creating web applications.

## Flask

Flask is a lightweight and micro web framework for Python. It is widely used to build web applications because of its simplicity and minimalistic design. Flask provides the basics for building a web application, such as routing, request handling, and rendering templates. It's known for its flexibility and ease of use.

## Jinja

Jinja is a templating engine for Python that allows you to embed dynamic data into HTML and other text-based files. It's widely used in web development for generating HTML, XML, and other markup formats. With Jinja, you can create templates with placeholders for dynamic content and then fill in those placeholders with actual data.

## HTML/CSS Files

For web development, HTML (HyperText Markup Language) is used to structure content on the web, while CSS (Cascading Style Sheets) is used for styling and layout. HTML is used to create the structure of a web page, defining elements like headings, paragraphs, images, links, and more. CSS is used to control the appearance of these elements, specifying properties like colors, fonts, spacing, and positioning.

In this project, you'll need to create and style HTML files using CSS, ensuring they are W3C compliant and can be validated using the W3C-Validator.
