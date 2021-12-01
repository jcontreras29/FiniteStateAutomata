CMSCI 385 – Theory of Computation
Project 1
Value: 50 points
Due: Friday, February 21 by 9:00 PM

In this project, you will simulate a deterministic finite-state automaton. The specification for the automaton will be in a text file. Your program will process the file and then prompt the user to enter strings. For each string, your program will output whether or not it is accepted by the automaton.

File Format

A valid input file to your program will consist of the following lines. You may assume that the input files are correctly formatted.

The first line will be an integer specifying the number Q of states in the automaton. You may then assume the states are numbered from 0 up to and including Q-1. State 0 will always be the initial state of the automaton.

The second line will be an integer A denoting the size of the input alphabet. The third line will consist of exactly A characters, individually separated by spaces, that make up the alphabet. If it helps, you may assume these characters will either be lower-case letters or digits. (So a valid alphabet would be a b c 1 2.)

The next Q lines of the file will give the transition function for the automaton. This will be in the form of a table. The ith line will have A space-separated numbers, each in the range from 0 to Q-1. These give the transitions out of the ith state. 

It’s easiest to see what’s going on via an example. Consider the following DFA:
 

There are six states, numbered from 0 to 5. The alphabet is 0 1. The transition table would look like the following:
1 2
1 2
3 4
5 1
2 3
4 5

From state 0, on a 0, the machine goes to state 1, and on a 1, it goes to state 2. Therefore the first line of the table is 1 2. Similarly, if the machine is in state 1, on a 0, it stays in state 1, and on a 1, it moves to state 2. So the line for state 1 is also 1 2.

Following the table, on a line by itself, is a number denoting the number F of final states. (In my example, it would be 1.) Then, on the last line, there will be F numbers, each between 0 and Q-1, denoting which states are final. (Again, in my example, that would be 1.) These numbers may or may not be in numerical order; you can assume they will all be distinct.

Here is the complete text of the file that specifies the automaton seen above:
6
2
0 1
1 2
1 2
3 4
5 1
2 3
4 5
1
1

Note that if the alphabet was given as 1 0, then the lines in the transition table would be reversed.

Here is a second example. This screenshot  
would be equivalent to
7
2
a b
2 1
3 4
2 3
3 5
5 6
5 6
6 6
2
4 5
Both of these automata are given as sample1.txt and sample2.txt on Canvas.

Testing Strings

Your program should begin by prompting the user for a filename for the automaton specification. You may assume this name will be entered correctly.

Then repeatedly prompt for a string. This string will consist entirely of lower-case letters or digits unless it is the exact string LAMBDA in all capital letters, which will represent the empty string.  There will be no spaces in the strings. Your program should then output one of the following messages for each string:
•	YES if the string would be accepted by the automaton
•	NO if the string would not be accepted by the automaton
•	ERROR: x if the string contains a character that is not part of the automaton’s alphabet. x should be replaced with whatever the first such incorrect character is. For example, if the alphabet was {a, b, c}, and the entered string was babacbdbea, the response would be ERROR: d. Note that this case does not apply to LAMBDA.
Use the input STOP (again in all caps) to terminate running the program.

As an example, for the automaton in the first screenshot, if the user entered 00101, the program would print YES. If the user then entered 1110, the program would output NO.

I would recommend that you print out the series of states the automaton goes through for debugging purposes. However, any such debugging code should not be included in the program you turn in. There will be points taken off for extraneous code that is not requested in this specification.

You may use either Python or Java to code this project. If you use Java, please zip and upload the entire Netbeans or Eclipse project folder to Moodle. Projects are due by 9 PM on February 21.

Grading Scheme:
5 pts – reads all data from file
5 pts – has appropriate data structure to store transition function
5 pts – correctly converts text file’s transition function into internal structure
5 pts – correctly denotes final states
5 pts – repeatedly reads in strings
5 pts – correctly processes LAMBDA
5 pts – processes non-empty string correctly (i.e. moves from state to state correctly)
5 pts – correctly outputs YES or NO
5 pts – correctly outputs ERROR message when appropriate
5 pts – code is readable, well-commented, efficiently implemented, and delivered on time
