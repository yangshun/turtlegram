TurtleGram
==
**A platform to share and create Python Turtle Art**

This is a prototype of a contest platform where users can create Python turtle art and share them with the world. People can also 'upvote' the python turtle art created.

Third-party APIs/Services
--
- **Front-end HTML/CSS**: Bootstrap 2.3.2
- **Front-end MVC**: AngularJS
- **In-browser python interpreter**: Skulpt
- **Back-end persistence**: Firebase/Parse
- **Storing images**: Imgur/Filepicker.io
- **Facebook SDK**: For commenting on individual python turtle art and sharing to timeline
- **Aviary Photo-editing SDK**: Filters anyone?

Model
--

For the prototype, only one type of object is needed: Python Turtle Art
- **python_turtle_art**
  - **id**: int
  - **title**: string
  - **description**: string
  - **code**: string
  - **upvotes**: int
  - **image_url**: string
  - **creator**: string
  - **date_created**: string/int(?)

