# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=false

if __name__ == '__main__':
    # pythonic code
    students = []
    scores = set()  # to prevent dublicated scores 

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.add(score)
    
    sec_min_score = sorted(scores)[1]

    names = []
    for name, score in students:
        if score == sec_min_score:
            names.append(name)
    
    for name in sorted(names):
        print(name)

    # my first solution as an C++ programmer
    students = []
    f_min = 0
    s_min = -1

    for i in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students.append([name, score])
        if score != students[f_min][1]:
            if score < students[f_min][1]:
                s_min = f_min
                f_min = i
            elif s_min == -1 or score < students[s_min][1]:
                s_min = i
        
    li = []
    for s in students:
        if s[1] == students[s_min][1]:
            li.append(s[0])
    li.sort()
    for s in li:
        print(s)