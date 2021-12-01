# Joseph Contreras
# Theory of Computation Project 1
# 2/15/2020
# This is my own original work

f = input("Which file would you like to use: ")
f = str(f)

# These are the imported operations for our automata
# This code puts each line into list within a list
# Right here is where we can choose the file we wish to use.

operations = []
file = open(f, 'r')
for line in file.readlines():
    operations.append(line.split())


# Number of states in automata

states = int(operations[0][0])


# Size of alphabet

alph_size = int(operations[1][0])

# Alphabet
# All possible characters our user wants to incoorporate

alph = [x for x in operations[2]]
alph = "".join(alph)

# This right here is not entirely necessary but it is
# helpful to catch any early mistakes
if (alph_size != len(alph)):
    print("Your alphabet is messed up. Revisit your file.")
    quit()


# Let's use this Digraph class to mimic our automata
# This class mimics a graph used in graph in graph theory
# in order to display moving from one vertice to another

class Digraph(dict):
    def add(self, v):
        self[v] = list()

    def transition(self, u, v):
        self[u].append(v)


# Making all the states in our automata
# And then representing them as vertices

automata = Digraph()
for i in range(states):
    automata.add(i)



# Adding transitions to each state
# Basically adding directed edges from one state to another

transitions = []
for i in range(3, 3+states):
    transitions.append(operations[i])

for i in range(len(transitions)):
    for j in transitions[i]:
        automata.transition(i,j)



# Getting our final states and then making our automata
# aware of which states are final. No need to do this for
# our initial state because that will always be 0 for this
# program

num_finals = operations[3+states]
for i in operations[4+states]:
    automata.transition(int(i), "FINAL")



# A mapping of our transitions will be helpful
# I want to be easily able to access the index of
# our alphabet. Can see this be used in the is_accepted()
# function

mapping = {"Transition map": operations[2]}



# Finally, here is the function that checks to see if a
# string is accepted in our automata...

def is_accepted(automata, string, mapping, transitions):
    start = 0
    path = []
    path.append(start)
    string = str(string)
    for i in range(len(string)):
        direction = string[i]
        if (direction not in mapping['Transition map']):
            print("This character is not in your alphabet:", direction)
            return False
        index = mapping['Transition map'].index(direction)
        start = int(automata[start][index])
        path.append(start)
    if ("FINAL" in automata[path[-1]]):
        return True
    else:
        return False




# This is the user interaction part of the program
# which falls in accordance with Professor Weiss' wishes
        
while True:
    string = input("Input your string: ")
    string = str(string)
    if (string == 'STOP'):
        print("Thanks for using me")
        print("A Joseph Contreras project")
        break
    if (string == 'LAMBDA'):
        if ('FINAL' in automata[0]):
            print("Accepted")
        else:
            print("Declined")
    elif (is_accepted(automata, string, mapping, transitions)):
        print("Accepted")
    else:
        print("Declined")
        









    
