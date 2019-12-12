class Person:
    def __init__(self, id, trust):
        self.id = id
        self.trust = trust


def findJudge(N, trust):
        if N-1 != len(trust):
            return -1
        if (len(trust) == 0):
            return -1
        listOfPersons = []
        for t in trust:
            person = Person(t[0], t[1])
            listOfPersons.append(person)
        trusts = {}
        print (listOfPersons)
        for person in listOfPersons:
            if person.trust in trusts:
                trusts[person.trust] += 1
            else:
                trusts[person.trust] = 1    

        return max(trusts.values())


s = findJudge(2,  [[1, 2]])
print (s)


