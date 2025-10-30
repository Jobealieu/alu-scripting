API Advanced
Description
This project focuses on working with APIs, specifically the Reddit API. It covers essential concepts like API pagination, recursive functions, JSON parsing, and data manipulation. The tasks involve querying Reddit's API to retrieve and process information about subreddits, posts, and keywords.

Learning Objectives
By the end of this project, you should be able to:

	* Read API documentation to find the endpoints you need
	* Use an API with pagination
	* Parse JSON results from an API
	* Make recursive API calls
	* Sort a dictionary by value

Requirements
General
	* Allowed editors: vi, vim, emacs
	* Interpreter/Compiler: Ubuntu 14.04 LTS using python3 (version 3.4.3)
	* All files must end with a new line
	* The first line of all files must be exactly #!/usr/bin/python3
	* Libraries imported must be organized in alphabetical order
	* A README.md file at the root of the project folder is mandatory
	* Code must follow PEP 8 style guidelines
	* All files must be executable
	* File length will be tested using wc
	* All modules must have documentation: python3 -c 'print(__import__("my_module").__doc__)'
	* You must use the Requests module for sending HTTP requests to the Reddit API

Reddit API Notes
	* Reddit API has rate limits and requires a specific UserAgent
	* Follow OAuth authentication process when necessary
	* Most features don't require authentication
	* Set a custom User-Agent to avoid "Too Many Requests" errors

Project Structure
alu-scripting/
└── api_advanced/
    ├── README.md
    ├── 0-subs.py
    ├── 1-top_ten.py
    ├── 2-recurse.py
    └── 3-count.py

Tasks
0. How many subs?
File: 0-subs.py

Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit.

Prototype: def number_of_subscribers(subreddit)

Usage:

python3 0-main.py programming
# Output: 756024

python3 0-main.py this_is_a_fake_subreddit
# Output: 0

1. Top Ten
File: 1-top_ten.py

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

Prototype: def top_ten(subreddit)

Usage:

python3 1-main.py programming
# Prints titles of top 10 hot posts

python3 1-main.py this_is_a_fake_subreddit
# Output: None

2. Recurse it!
File: 2-recurse.py

Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

Prototype: def recurse(subreddit, hot_list=[])

Usage:

python3 2-main.py programming
# Output: 932 (number of articles found)

python3 2-main.py this_is_a_fake_subreddit
# Output: None

3. Count it!
File: 3-count.py

Write a recursive function that queries the Reddit API, parses titles of all hot articles, and prints a sorted count of given keywords.

Prototype: def count_words(subreddit, word_list)

Usage:

python3 3-main.py programming 'python java javascript'
# Prints sorted count of keywords found in post titles

Resources
	* Reddit API Documentation
	* Query String
	* Reddit API OAuth Authentication

Author
Alieu O. Jobe

Repository
	* GitHub repository: alu-scripting
	* Directory: api_advanced

License
Copyright © 2025 ALU, All rights reserved.
