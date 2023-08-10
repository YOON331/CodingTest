def solution(today, terms, privacies):
    print(today)
    answer = []
    t_dict = {}
    for x in terms:
        new_t = x.split()
        t_dict[new_t[0]] = {new_t[1]}

    idx = 1
    new_td = today.split(".")
    for y in privacies:
        new_p = y.split(".")
        t = int("".join(list(t_dict[y[-1]])))
        new_p[0] = int(new_p[0]) + t // 12
        new_p[1] = int(new_p[1]) + t % 12
        if new_p[1] >12:
            new_p[0] += 1
            new_p[1] -= 12
        tmp = new_p[2].split()
        if int(new_td[0]) > int(new_p[0]):
            answer.append(idx)
        elif (int(new_td[0]) == int(new_p[0])) and (int(new_td[1]) > int(new_p[1])) :
            answer.append(idx)
        elif (int(new_td[0]) == int(new_p[0])) and (int(new_td[1]) == int(new_p[1])) and ( int(new_td[2]) >= int(tmp[0])):
            answer.append(idx)
        idx += 1
    print(answer)
    return answer



# solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
# solution("2016.02.15", ["A 100"], ["2000.06.16 A", "2008.02.15 A"]) #1
# solution("2019.12.09", ["A 12"], ["2018.12.10 A", "2010.10.10 A"])  #2
solution("2021.01.28", ["A 2"], ["2020.12.01 A", "2010.01.01 A"]) #2
# print("check")
# solution("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"])  #1,2
# solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
# solution("2020.01.01", ["A 1"], ["2019.12.01 A"])
# solution("2020.04.16", ["A 36", "S 4"], ["2017.04.17 A", "2014.04.16 S"])
# solution( "2019.11.01", ["A 5"], ["2019.06.01 A", "2018.01.01 A"])  #1,2
# solution("2020.01.01", ["A 1"], ["2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.09 A", "2019.12.01 A"])   #11
# solution("2020.05.17", ["A 3", "B 12"], ["2020.01.01 A", "2020.05.17 B"])   #1
# solution("2010.06.17",["A 16"],["2009.01.19 A","2000.01.05 A"]) #1,2