def getScore(c1, c2):
    row = "AGTC-".index(c1)
    col = "AGTC-".index(c2)
    return scoringMatrix[row][col]

scoringMatrix = [[1, -0.8, -0.2, -2.3, -0.6],
                 [-0.8, 1, -1.1, -0.7, -1.5],
                 [-0.2, -1.1, 1, -0.5, -0.9],
                 [-2.3, -0.7, -0.5, 1, -1],
                 [-0.6, -1.5, -0.9, -1, 0]]

s1 = input('Input sequence 1: ')
s2 = input('Input sequence 2: ')

def align():
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] 
    traceback = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] 

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):

            matching = round(m[i - 1][j - 1] + getScore(s1[i - 1], s2[j - 1]), 1)
            first = round(m[i - 1][j] + getScore(s1[i - 1], "-"), 1)
            second = round(m[i][j - 1] + getScore("-", s2[j - 1]), 1)

            if (matching > first and matching > second):
                m[i][j] = matching
                traceback[i][j] = "match"
            elif (matching < first and first > second):
                m[i][j] = first
                traceback[i][j] = "first"
            else:
                m[i][j] = second
                traceback[i][j] = "second"
    aligns1, aligns2 = "", ""
    i, j = len(s1), len(s2)
    while i > 0 or j > 0:
        t = traceback[i][j]

        if t == "match":
            aligns1 = s1[i - 1] + aligns1
            aligns2 = s2[j - 1] + aligns2
            i -= 1
            j -= 1
        elif t == "first":
            aligns1 = s1[i - 1] + aligns1
            aligns2 = "-" + aligns2
            i -= 1
        else:
            aligns1 = "-" + aligns1
            aligns2 = s2[j - 1] + aligns2
            j -= 1

    return aligns1, aligns2

aligns1, aligns2 = align()
print("Alignment of sequence 1:", aligns1)
print("Alignment of sequence 2:", aligns2)

def getTotalScore(s1, s2):
    sum = 0
    for i in range(0, len(s1)):
        sum = round(sum + getScore(s1[i], s2[i]), 1)
    return sum

print("Their sum is: ", getTotalScore(aligns1, aligns2))
