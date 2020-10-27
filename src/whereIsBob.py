def csWhereIsBob(names):
    for name in names:
        if name =="Bob":
            x = names.index(name)
            return x

    else:
        return -1

print(csWhereIsBob(["Amy", "Jack"]))