TurtleGram
==
**A platform to share and create Python Turtle Art**

This is a prototype of a contest platform where users can create Python turtle art and share them with the world. People can also 'upvote' the python turtle art created.

## Installation

To install Flask:  
Install `virtualenv` and `pip`
Checkout and cd to the directory that you checkout

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install Flask
 
To run the application:

    $ python turtlegram.py


## Third-party APIs/Services

- **Front-end HTML/CSS**: Bootstrap 2.3.2
- **Front-end MVC**: AngularJS
- **In-browser python interpreter**: Skulpt
- **In-browser code editor**: CodeMirror
- **Back-end persistence**: Firebase
- **Facebook SDK**: For commenting on individual python turtle art and sharing to timeline
- **Aviary Photo-editing SDK**: Filters anyone?

## Model

For the prototype, only one object is needed: Python Turtle Art
- **python_turtle_art**
  - **id**: int
  - **title**: string
  - **description**: string
  - **code**: string
  - **upvotes**: int
  - **image_url**: string
  - **creator**: string
  - **date_created**: string/int(?)

## Authors

**Tay Yang Shun** 

+ [http://github.com/yangshun](http://github.com/yangshun)
+ [http://twitter.com/yangshunz](http://twitter.com/yangshunz)

**Soedarsono Lim**

+ [http://github.com/soedar](http://github.com/soedar)
+ [http://twitter.com/soedar](http://twitter.com/soedar)
