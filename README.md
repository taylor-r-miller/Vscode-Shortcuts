# Vscode-Shortcuts

A simple script to extend the Vscode "code" shortcut.

*note this is made for mac and the base path may need to be adjust on windows. If this is the case uncommenting the line 5 and supplying the base dir should work.

<h4>Purpose</h4>
Create shortcuts so you do not have to type the full path to your file to use the command line to launch Vscode

<h4>How to Use</h4>
This is meant to be used in conjunction with a alias in your bash profile, so you can just type "work" or "projects" from a terminal window. The code is designed so you can spescify paths and it will list all the files in the directory so you can chose which to open. You can adjust this for yourself by changing the SHORTCUTS dictionary at the top of the code.

<h4>Setting up the alias</h4>
Here are the alias I set up in my computer. *Note the initial cd Documents/Projects/Vscode-Shortcuts is the path to this code. We are just changing into the directory running the code and passing in name of the file and the shortcut to run. This path will need to change for wherever you place this folder. It is also important to note that the name that is passed after Index.py needs to match exactly to the shortcut in the SHORTCUTS dictionary.
<br/><br/>To set these in your bash profile run nano ~/.bash_profile

<br/>#Projects shortcut <br/>
alias projects='cd Documents/Projects/Vscode-Shortcuts && python3 Index.py projects && cd' <br/>
#Work shortcut<br/>
alias work='cd Documents/Projects/Vscode-Shortcuts && python3 Index.py work && cd'
