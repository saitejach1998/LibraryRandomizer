# Building
Build the application by cloning the repository and executing the command
~~~~
 pip install --editable .
~~~~

This will install it into your python libs folder. To use it as a exectable anywhere on the system, make sure python and its libs floder are added to the path.

# Usage
~~~~
randomizer
~~~~
runs the application and will index your library if not indexed already.

To re-index libraries after you have made changes use
 ~~~~
 randomizer -i
 ~~~~
 or
 ~~~~
 randomizer -index
 ~~~~
