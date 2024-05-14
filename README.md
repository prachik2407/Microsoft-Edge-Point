# Microsoft-Edge-Point
Working with a Python script that uses the `pyautogui` library to automate searches. Here's a brief explanation of what code does:

- The `search(query)` function simulates typing a query into a search bar and pressing enter. It uses the `pyautogui` library to simulate keyboard inputs.

- There are several commented-out sections in your code. One of them is a function `imageFind(image,g,double)` which seems to locate an image on the screen and click or double click on it.

- Another commented-out section seems to be a password check using the `sha256` hash function. It prompts the user for a password and checks if the hashed password matches a specific hash.

- The last part of your code generates a random string from a set of characters and numbers, and then uses the `search` function to search for each prefix of this string.

Please note that the `pyautogui` library controls the mouse and keyboard, so be careful when running scripts that use it. You might lose control of your mouse and keyboard during the execution of the script.

You can change the number of searches according to your need from line 77 as in the given code it is 32, and change the number of seconds from line 73 and 82 as the difference of seconds you need in each search as in the given code it is 6.
Run the code, then it will show starting.... in the output terminal,
then you have to open the edge, and it will automatically start searching
