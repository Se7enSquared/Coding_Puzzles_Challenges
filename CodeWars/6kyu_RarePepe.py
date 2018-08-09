def find_rarest_pepe(pepes):
    list_of_pepes = {}
    for pepe in pepes:
        if pepe in list_of_pepes:
            list_of_pepes[pepe] += 1
        else:
            list_of_pepes[pepe] = 1
    rarest_pepe = []
    minimum = 10
    for pepe in list_of_pepes:
        if list_of_pepes[pepe] < minimum:
            minimum = list_of_pepes[pepe]
    return rarest_pepe

print(find_rarest_pepe(['a', 'b', 'c', 'a']))