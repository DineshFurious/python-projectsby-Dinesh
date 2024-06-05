
def get_average():
    with open("todos", 'r') as file:
        read = file.readlines()
    # values = read[1:]
    values = [float(i) for i in read[1:]]
    average_local = sum(values) / len(values)
    return average_local



average = get_average()
print(average)

#
# Create a file and post informations like below
#
# temparatures
# 5
# 7
# 12
# 10