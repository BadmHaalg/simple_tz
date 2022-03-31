
know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


# в условии все и так хорошо сформулировано - нужно просто реализовать
# пересечение трех множеств, т.е. найти тех, кто присутствует в каждом из списков
def find_athlets(list1, list2, list3):
    return list((set(list1).intersection(set(list2))).intersection(set(list3)))


print(find_athlets(know_english, sportsmen, more_than_20_years))
