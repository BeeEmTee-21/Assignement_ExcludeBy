def exclude_by(source, comparison):
    new_list = []
    for item in source:
        if item not in comparison:
            new_list.append(item)

    return new_list
# print(f"Results: {name_not_decided(source=name, comparison=guessed_names)}")