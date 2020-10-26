def csWhereIsBob(names):
    for name in names:
        if name =="Bob":
            return names.index(name)
        else:
            return -1

print(csWhereIsBob(["Layla", "Bob", "Kaitlyn", "Bob", "Patricia"]))