from generator import get_input, generator

output = generator(30, 30)
with open("saved_shapes.txt", "w") as file:
    file.write(output)