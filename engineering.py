# name = ["David","Joyce","Vivian","Bernard","Desmond","Daniel"]
# guessed_names = ["David","Vivian",]

# for n in name:
#     for g in guessed_names:
#         if g in n:
#             name.remove(g)
#
#
# print(name)


def compare(source, comparison):
    new_list = []
    for item in source:
        if item not in comparison:
            new_list.append(item)

    return new_list
# print(f"Results: {name_not_decided(source=name, comparison=guessed_names)}")