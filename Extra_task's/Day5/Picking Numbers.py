def pickingNumbers(a):
    for i in a:
        #max_pair_of_elements.append(a.count(i)+a.count(i+1))
        ab=a.count(i)
        bc=a.count(i+1)
        print(ab)
        print("---------------")
        print(ab)
        print("-----------")
        print(bc+ab)
        #print(a.count(i+1))
        #ab=a.count(i)+a.count(i+1)
        #print(ab)
    return max(max_pair_of_elements)

a=[4, 6, 5, 3, 3, 1]
max_pair_of_elements=pickingNumbers(a)
print(max_pair_of_elements)