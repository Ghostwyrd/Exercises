# a python program to mirror an input number

user_input = input("Enter what you see in the mirror: ")
#verification step
#print("You entered: ",(user_input))
#unpack user_input string and assign as tuple "emagi"
image = [*user_input]
#verification step
#print(image)


egami = image[::-1]
mirror = ''.join(egami)

print(mirror)

