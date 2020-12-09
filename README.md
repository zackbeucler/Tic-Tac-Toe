# Tic-Tac-Toe

# Prerequisites
- You need to have a version of Python at least as recent as 3.0
- You need a terminal program to run the Tic Tac Toe game
- You must have Tic_tac_toe.py installed

# Downloading the Program
- Go to the github repository: https://github.com/zackbeucler/Tic-Tac-Toe
- Click the "code" button then click "download zip"
- Remove the repository foilder from the zip file

# Running the Program
- In your file explorer, navigate to the repository folder and copy the file path (Tic_tac_toe.py is the main program file)
- Open your terminal program
- Change directory to the folder holding the repository
- Type "python -m Tic_tac_toe" to run the program. 

# Testing the Program
- In the repository there is a test file named "test_TTT_unittest.py"
- To run the test file, navigate to your terminal program
- Change directory to the folder holding the repository
- Type into the command line "python -m Change test_TTT_unittest"
- First, the test file checks to see if the first turn is chosen at random by testing the function "firstMove()"
  - The function is called 100 times. The test file outputs the percent of the time player 0 is chosen to go first. If random, this output will be 50%
- We have added logs to the program file. To view the logs, navigate to the directory of the repository and open the file game-log.log
