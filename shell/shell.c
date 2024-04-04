/*
File: shell.c
Author: Siyu Ai
Date: March 25, 2024
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <signal.h>
#include <sys/wait.h>
#include <time.h>  // Include time.h for time function
#define MAXARGS 4
#define MAXLINE 8192

// Array of built-in commands
char* commands[MAXARGS] = {"cd", "help", "exit", "game"};

// Forward declarations
void* cd(void* input);
void* help(void* input);
void* exit_shell(void* input);
void* game(void* input);  // Added declaration for game function
int builtin_command(char** argv);
void eval(char *cmdline);

/*
 *Function pointers for built-in commands
 */
// Updated function pointer array
void* (*command_functions[MAXARGS])(void* arg) = {cd, help, exit_shell, game};

/*
 * Implementations of built-in commands
 */
// Implement cd command
void* cd(void* input) {
    char* directory = (char*)input;
    if (directory == NULL || strcmp(directory, "") == 0) {
        // Change to the home directory
        directory = getenv("HOME");
        if (directory == NULL) {
            fprintf(stderr, "cd: HOME directory not found\n");
            return NULL;
        }
    } else {
        // Attempt to change to the specified directory
        if (chdir(directory) == -1) {
            perror("cd");
            return NULL;
        }
    }

    // Display the current working directory
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) == NULL) {
        perror("getcwd");
        return NULL;
    }
    printf("Current working directory: %s\n", cwd);

    return NULL;
}

// Implement help command
void* help(void* input) {
    printf("Built-in commands:\n");
    printf("cd <directory> : Change directory\n");
    printf("help : Display this help message\n");
    printf("exit : Exit the shell\n");
    printf("game : Play a simple guessing game\n");  // Updated help message
    return NULL;
}

// Implement exit command
void* exit_shell(void* input) {
    exit(0);
}

// Implement game command
// A number guessing game
void* game(void* input) {
    printf("Welcome to the Guessing Game!\n");
    printf("I'm thinking of a number between 1 and 100.\n");
    printf("Try to guess it!\n");

    // Generate a random number between 1 and 100
    // using rand_r() for thread safety
    unsigned int seed = time(NULL);  // Use time as seed
    int number = rand_r(&seed) % 100 + 1;
    int guess;
    int attempts = 0;

    do {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        getchar();  // Consume newline character from input buffer
        attempts++;

        if (guess < number) {
            printf("Too low, please try again.\n");
        } else if (guess > number) {
            printf("Too high, please try again.\n");
        } else {
            printf("Congratulations! You guessed it right in\n");
            printf("%d attempts.\n", attempts);
        }
    } while (guess != number);

    return NULL;
}

/***
 **  Wrapper of fork(). Checks for fork errors, quits on error. 
 **/
pid_t Fork(void) {
  pid_t pid;
  if ((pid = fork()) < 0) {
    fprintf(stderr, "%s: %s\n", "fork error", strerror(errno));
    exit(0);
  }
  return pid;
}

/***
 **  Wrapper of fgets. Checks and quits on Unix error. 
 **/
char* Fgets(char *ptr, int n, FILE *stream) {
  char *rptr;
  if (((rptr = fgets(ptr, n, stream)) == NULL) && ferror(stream)) {
    fprintf(stderr, "%s\n", "fgets error");
    exit(0);
  }
  return rptr;
}

// Is the command one built into the shell?
// That is, that the *shell* has implemented?
// If so, execute it here
int builtin_command(char** argv) {
  // Loop through
  for (int i = 0; i < MAXARGS; i++) {
    // write loop to get the "right" i
    int res = strcmp(commands[i], argv[0]);

    if (res == 0) {
      // call the right function.
      (command_functions[i])(argv[0]);  // some argument
      return 1;
    }
  }
  return 0;
}

// Evaluate the command line and execute
void eval(char *cmdline) {
    char *argv[MAXARGS]; /* Argument list execve() */
    char buf[MAXLINE]; /* Holds modified command line */
    pid_t pid; /* Process id */

    strcpy(buf, cmdline);
    // Split buf into args

    int argc = 0;
    argv[argc] = strtok(buf, " \t\n");
    while (argv[argc] != NULL && argc < MAXARGS - 1) {
        argc++;
        argv[argc] = strtok(NULL, " \t\n");
    }
    argv[argc] = NULL;

    if (argv[0] == NULL)
        return;  /* Ignore empty lines */

    if (strcmp(argv[0], "cd") == 0) {
        cd(argv[1]);  // Pass the directory argument to the cd function
    } else if (!builtin_command(argv)) {  // pass into other built-in commands
        pid_t pid = Fork();
        if (pid == 0) {  // Child process
            execvp(argv[0], argv);
            // perror("Command not found.");
            // Inform user of unknown command
            printf("No such command: %s\n", argv[0]);
            exit(0);
        } else {  // Parent process
            int status;
            if (waitpid(pid, &status, 0) < 0) {
                // Wait for the child process to terminate
                perror("waitpid error");
                exit(0);
            }
        }
    }
}

int main() {
  // Seed the random number generator
  srand((unsigned int)time(NULL));

  char cmdline[MAXLINE];  /* command line buffer */
  while (1) {
    // Print command prompt
    printf("k-sea-shell> ");
    // Read input from user
    Fgets(cmdline, MAXLINE, stdin);
    // If we get the eof, quit the program/shell
    if (feof(stdin))
      exit(0);

    // Otherwise, evaluate the input and execute.
    eval(cmdline);
  }
  return 0;
}
