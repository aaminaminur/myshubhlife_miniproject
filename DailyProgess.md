This is the test Readme.

Day1: Reading and exploring library and studying its working.

Language Choosen: Python
Framework: Flask
Library: requests, bs4

Day2:

Used bs4 to scrap through urls.
Used scrapping recursively to till our list length is less then 5000.
But, since every successive iteration results in more number of urls, we are getting around 5000 + 50-60.
We can slice it as per requirement.
Using flask created database in mongodb dynamically.
Tried adding that list into db, but facing error due to bulk adding of 5000+ at a time. I will attempt to add one by one.
I can display all the database contents, I will implement filters.

Day3:

Worked on adding 5000+ content to db.
Worked on to take URL dynamically using POST method.
Tried using Mongo DB filter using createIndex, but faced some errors.
Implemented the filter to display top 10 using Python Algorithm.
Tried capping the DB size, but I need to learn to implement it dynamically.
Explored about JWT Token, faced some issue with jwt.decode method. I need to explore that deeper in future.
