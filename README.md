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
- Open your terminal program if you are using MacOS or open your Console program if you are on Windows
- Change directory to the folder holding the repository
- Type "python -m Tic_tac_toe" to run the program. 

# Testing the Program
- In the repository there is a test file named "test_TTT_unittest.py"
- To run the test file, navigate to your terminal program
- Change directory to the folder holding the repository
- Type into the command line "python -m Change test_TTT_unittest"
- First, the test file checks to see if the first turn is chosen at random by testing the function "firstMove"
  - The function is called 100 times. The test file outputs the percent of the time player 1 is chosen to go first. If random, this output will be 50%
- Next, the test files tests to make sure the "checkWinner" function correctly identifies a winner only when there is actually a winner
  - There are eight different ways to win, so the next eight outputs should be "true"
- Lastly, the test file tests to make sure that, when the first player selects their symbol, the program assigns the player the correct symbol. 
  - The file tests all four possible inputs for a symbol, so the last four outputs should all be "true" as long as the program is accurate
  
# Logging the Program
- We have added logs to the program file "Tic_tac_toe.py" (log formatting done using the logging class: "game_log.py")
- To view these logs, first run the program
- Next, navigate to the file in the repository "game-log.log"
- There should be a log for each space selected, and two boolean logs, one that is true if there is a winner, the other is true if the board is full
