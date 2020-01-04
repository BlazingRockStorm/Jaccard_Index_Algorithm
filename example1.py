def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))
A = ['Haruka Kudo', 'Okuyama Kazusa', 'Noa Tsurushima']
B = ['Okuyama Kazusa', 'Noa Tsurushima', 'Chika Osaki']
C = ['Haruka Kudo', 'Sakurako Okubo', 'Hiroe Igeta']

def simple_recommender_sys(list1, list2, list3):
    J1 = jaccard_similarity(list1, list2)
    J2 = jaccard_similarity(list2, list3)
    J3 = jaccard_similarity(list3, list1)
    if J1 > J2:
        if J1 > J3:
            print("[",list1,", ",list2,"]")
        elif J1 == J3:
            print("[",list1,", ",list2,"], [",list1,", ",list3,"]")
        else: 
            print("[",list1,", ",list3,"]")
    elif J1 == J2:
        if J1 > J3:
            print("[",list1,", ",list2,"], [",list2,", ",list3,"]")
        elif J1 == J3:
            print("[",list1,", ",list2,"], [",list2,", ",list3,"], [",list1,", ",list3,"]")
        else: 
            print("[",list1,", ",list3,"]")
    elif J1 < J2:
        if J2 > J3:
            print("[",list2,", ",list3,"]")
        elif J2 == J3:
            print("[",list2,", ",list3,"], [",list1,", ",list3,"]")
        else: 
            print("[",list1,", ",list3,"]")
            
simple_recommender_sys(A, B, C)
