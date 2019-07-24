def unique_names(names1, names2):
    unique_list = list()
    [unique_list.append(name) for name in (names1+names2) if name not in unique_list]
    return unique_list
# Another way is to use a set() and iterates the union array


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))