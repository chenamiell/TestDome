def group_by_owners(files):
    owners_dict = dict()
    for key in files:
        if files[key] in owners_dict.keys():
            owners_dict[files[key]].append(key)
        else:
            owners_dict[files[key]] = [key]
    return owners_dict


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

print(group_by_owners(files))
