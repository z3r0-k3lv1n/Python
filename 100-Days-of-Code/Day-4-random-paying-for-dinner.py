# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
# Size of the list of names
size = len(names)
# Generate a random number based on the size of the list of names
dinner_bitch = random.randint(0, size - 1)
# Print the name with the index number of the randomly generated number from within the list of names.
print(names[dinner_bitch],"is the dinner bitch, they're paying for dinner tonight.")

#Do it with less code
dinner_bitch1 = random.choice(names)
print(dinner_bitch1,"is also the dinner bitch")


# print(names_string,"\n",names,"\n")

# USE THIS LIST
# NAMES LIST: George, Sue, Cassie, Stephen, Robert, Peter, Lily, Gemma, Mandy, Kaylah, Hayden, Jazmyn