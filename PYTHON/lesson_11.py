# words = ["cat", "car", "code", "home", "learn", 
#     "fun", "job", "love", "friend", "zoo", "enjoy",
#     "happiness", "family", "goal", "desire"]
# letter = input("")
# for x in words:
#     if letter in x:
#         print(x)


# alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
#  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
#   "T", "U", "V", "W", "X", "Y", "Z"]

# in1 = int(input())

# in2 = int(input())

# in3 = int(input())

# out1 = alpha[in1]

# out2 = alpha[in2]

# out3 = alpha[in3]

# print(out1+out2+out3)

supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]

input_command = input()

for word in supported:
    if input_command in supported:
        print("OK")
        break
    else:
        print("Unknown")
        break