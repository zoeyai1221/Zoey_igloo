# K-SEA Shell
## Description:
K-SEA Shell is a simple shell program written in C. It provides a basic command-line interface where users can execute commands, navigate directories, and play a game implemented within the shell.

## External Resources:
- https://github.com/angrave/SystemProgramming/wiki#10-signals
- https://www.tutorialspoint.com/unix/unix-processes.htm
- https://linux.die.net/man/3/exec

## Built-in Commands:
1. **cd <directory>** : Change directory to the specified directory.
2. **help** : Display a list of built-in commands and their descriptions.
3. **exit** : Terminate the shell.
4. **game** : Play a game (Placeholder for user-defined game).

## Implementation Notes:
- The shell supports basic functionalities such as executing external commands, changing directories, displaying help information, and exiting the shell.
- Built-in commands are implemented using function pointers, allowing for easy extensibility.
- Error handling is implemented for various scenarios, such as command not found or fork/exec errors.
- The shell provides a simple prompt "k-sea-shell>" for user interaction.

## How to build and run the code

- Compilation: Compile the code using the following command:

gcc shell.c -o shell

- Execution: Run the shell using the following command:

./shell

Then you should see the prompt k-sea-shell> indicating that the shell is ready to accept commands. You can now enter commands like help, cd, or any external commands available on your system.


## Commands implementation (Examples of input and output)
### Command cd
- cd: moving up or down the directory tree
bash-4.4$ ./shell
```bash
k-sea-shell> cd
Current working directory: /home/zoeyai1221/zoeyai1221/shell
k-sea-shell> cd ..
Current working directory: /home/zoeyai1221/zoeyai1221
k-sea-shell> cd shell
Current working directory: /home/zoeyai1221/zoeyai1221/shell
k-sea-shell> cd NoSuchDirectory
cd: No such file or directory
k-sea-shell> ls
README.md shell  shell.c
```
- help: print out all of the built-in commands
```bash
k-sea-shell> help
Built-in commands:
cd <directory> : Change directory
help : Display this help message
exit : Exit the shell
game : Play a simple guessing game
```

- game: start a game to pick up and guess a random number
```bash
k-sea-shell> game
Welcome to the Guessing Game!
I'm thinking of a number between 1 and 100.
Try to guess it!
Enter your guess: 50
Too high, please try again.
Enter your guess: 30
Too high, please try again.
Enter your guess: 10
Congratulations! You guessed it right in
3 attempts.
```

- exit: terminate the shell
```bash
k-sea-shell> exit
```

- NoSuchCommand: If a command is not found, the shell would print out an error message, and resume execution
```bash
bash-4.4$ ./shell
k-sea-shell> NotSuchCommand
No such command: NotSuchCommand
```