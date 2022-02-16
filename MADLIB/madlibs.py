# string concatenation (aka how to put strings together)
# suppose we want to create  string that says "subscribe to _____"
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this 
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It Makes me so excited all the time because \
    I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
