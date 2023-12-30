# Password-CLI

This project is a command-line interface (CLI) tool for generating random passwords. It utilizes Typer for the CLI aspect.

## Features

- Generate random passwords with customizable options
- Option to exclude special characters and numbers
- Generate readable passwords
- History of generated passwords stored in a text file
- Command to clear the history of generated passwords
- If one password is generated, it is copied to the clipboard

## Installation

To install the Password-CLI tool, follow these steps:

1. Clone the repository: `git clone https://github.com/username/Password-CLI.git`
2. Navigate to the project directory: `cd Password-CLI`
3. Install the required dependencies: `conda install --file requirements.txt`
   conda env create -f environments.yml

## Usage

To call the program, use the command `python main.py` followed by the desired options.

## Options

Use python main.py --help to see the options, below are some examples of commands:

- `python main.py gen --length 20` - Generates a password with a length of 20 characters
- `python main.py gen --length 20 --nsc` - Generates a password with a length of 20 characters and no special characters
- `python main.py gen --length 20 --nn` - Generates a password with a length of 20 characters and no numbers
- `python main.py gen --readable` - Generates a readable password with the default length of 12 characters
- `python main.py clear` - Clears the history of generated passwords
- `python main.py history` - Displays the history of generated passwords
