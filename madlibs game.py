# user input ( mad lips)

your_name = input("Your name, PLease ?:  ")
colour = input("Please input a colour:")
favNum = input("Please input favorite number: ")
favCelab = input("Please input name of fav Celeb: ")


def inputMadInput(your_name, colour, favNum, favCelab):
    print(your_name)
    print(colour)
    print(favNum)
    print(favCelab)


print(inputMadInput)

mad_output = "Hi my name is {} , my favorit colour i, my favorit number is {} and my favorite celeb is {}. This is who I am"
print(mad_output.format(your_name, colour, favNum, favCelab))
