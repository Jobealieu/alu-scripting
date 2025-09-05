
# Regular Expressions Project

This project focuses on building and understanding regular expressions using Ruby and the Oniguruma library. The tasks progress from simple pattern matching to complex text processing scenarios.

## Project Overview

**Author:** Alieu O. Jobe  
**School:** ALU (African Leadership University)  
**Course:** Front-End Web Development  
**Topic:** Regular Expressions  
**Duration:** September 1-6, 2025  

## Background Context

This project uses the Oniguruma regular expression library, which is Ruby's default regex engine. The focus is on understanding and implementing various regex patterns to solve real-world text processing problems.

## Learning Objectives

By completing this project, you will understand:
- Basic regular expression syntax and patterns
- Character matching and repetition tokens
- Anchoring patterns (beginning and end matching)
- Character classes and special sequences
- Practical applications of regex in text processing
- Ruby's regex implementation using the `scan()` method

## Project Structure


regular_expressions/
├── README.md
├── 0-simply_match_school.rb
├── 1-repetition_token_0.rb
├── 2-repetition_token_1.rb
├── 3-repetition_token_2.rb
├── 4-repetition_token_3.rb
├── 5-beginning_and_end.rb
├── 6-phone_number.rb
├── 7-OMG_WHY_ARE_YOU_SHOUTING.rb
├── 8-textme.rb
└── 9-passed_linkedin_regex_challenge.jpg


## Requirements

### General Requirements
- **Allowed editors:** `vi`, `vim`, `emacs`
- **Environment:** Ubuntu 20.04 LTS
- **Language:** Ruby with Oniguruma regex library
- All files must end with a new line
- All Bash script files must be executable
- First line of all scripts: `#!/usr/bin/env ruby`

### Ruby Script Template
All scripts follow this basic structure:

ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/YOUR_REGEX_HERE/).join

## Task Descriptions

### 0. Simply matching School
**Objective:** Create a regex that matches the literal string "School"
- **File:** `0-simply_match_school.rb`
- **Regex Pattern:** `/School/`

### 1-4. Repetition Tokens
**Objective:** Practice different repetition quantifiers
- **Files:** `1-repetition_token_0.rb` through `4-repetition_token_3.rb`
- **Concepts:** `*`, `+`, `?`, `{n,m}` quantifiers

### 5. Not quite HBTN yet
**Objective:** Match strings starting with 'h', ending with 'n', with any single character between
- **File:** `5-beginning_and_end.rb`
- **Pattern:** Three-character strings (h + any character + n)

### 6. Call me maybe
**Objective:** Validate 10-digit phone numbers
- **File:** `6-phone_number.rb`
- **Pattern:** Exactly 10 consecutive digits

### 7. OMG WHY ARE YOU SHOUTING?
**Objective:** Extract only capital letters from input
- **File:** `7-OMG_WHY_ARE_YOU_SHOUTING.rb`
- **Pattern:** Match uppercase letters only

### 8. TextMe
**Objective:** Parse VoIP log files to extract sender, receiver, and flags
- **File:** `8-textme.rb`
- **Output Format:** `[SENDER],[RECEIVER],[FLAGS]`
- **Real-world application:** Log file analysis

### 9. LinkedIn Technical Interview
**Objective:** Solve LinkedIn's regex puzzle challenge
- **File:** `9-passed_linkedin_regex_challenge.jpg`
- **Requirement:** Screenshot of completion with timestamp

## Usage Examples

### Running the Scripts

bash
# Make script executable
chmod +x 0-simply_match_school.rb
Run with test input
./0-simply_match_school.rb "Best School"

Output: School
./5-beginning_and_end.rb "hbn"

Output: hbn
./6-phone_number.rb "4155049898"

Output: 4155049898
./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I LOVE CODING"

Output: ILOVECODING

## Key Regex Concepts Covered

1. **Literal Matching:** Direct string matching
2. **Quantifiers:** `*` (zero or more), `+` (one or more), `?` (zero or one)
3. **Anchors:** `^` (start), `$` (end)
4. **Character Classes:** `[A-Z]`, `[0-9]`, `.` (any character)
5. **Grouping:** `()` for capturing groups
6. **Escaping:** `\` for literal special characters

## Testing Your Regex

Use [Rubular](https://rubular.com/) to test and debug your regular expressions interactively before implementing them in your Ruby scripts.

## Resources

- [Regular expressions - basics](https://www.regular-expressions.info/tutorial.html)
- [Regular expressions - advanced](https://www.regular-expressions.info/advanced.html)
- [Rubular - Ruby regex editor](https://rubular.com/)
- [RegexOne - Interactive tutorial](https://regexone.com/)

## Repository Information

- **GitHub Repository:** `alu-scripting`
- **Directory:** `regular_expressions`
- **Branch:** `main`

## Author Notes

This project demonstrates the power and versatility of regular expressions in text processing. Each task builds upon previous concepts, culminating in real-world applications like log file parsing and technical interview challenges.

Remember: "Some people, when confronted with a problem, think 'I know, I'll use regular expressions.' Now they have two problems." - Use regex wisely! 😄

---

*Project completed as part of ALU's Front-End Web Development curriculum.*
