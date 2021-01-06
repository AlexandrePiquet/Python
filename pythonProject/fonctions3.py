def my_filter(lst, f):
    """
    Etablit une liste des éléments de lst pour lesquels f(élément) = True
    :param lst:
    :param f:
    :return:
    """

    liste = []

    for element in lst:
        if f(element):
            liste.append(element)

    return liste

print(my_filter([-2, 0, 4, -5, -6], lambda x : x < 0))