from copy import deepcopy

debug = False

ones = [
    [[1, 0], [0, 0]],
    [[0, 1], [0, 0]],
    [[0, 0], [1, 0]],
    [[0, 0], [0, 1]]
]

zeros = [
    [[0, 0], [0, 0]],
    # 2 1's
    [[1, 1], [0, 0]],
    [[1, 0], [1, 0]],
    [[1, 0], [0, 1]],
    [[0, 1], [1, 0]],
    [[0, 1], [0, 1]],
    [[0, 0], [1, 1]],
    # 3 1's
    [[1, 1], [1, 0]],
    [[1, 1], [0, 1]],
    [[1, 0], [1, 1]],
    [[0, 1], [1, 1]],
    # 4 1's
    [[1, 1], [1, 1]]
]

def isMatch(M, N):
    # Inputs two matrices M and N and computes whether the right column
    # of M = left column of N
    colM = [row[-1] for row in M]
    colN = [row[0] for row in N]
    if debug:
        print("isMatch comparing {} to {}".format(colM, colN))
    return colM == colN

def testIsMatch():
    M = [[1, 1, 1], [0, 0, 0]]
    N = [[1, 0], [1, 1]]
    print(isMatch(M, N))


def genRow(row, current, result, ones, zeros):
    # Input a 1x(N-1) row and outputs a collection of 2xN rows
    # each of which evaluate to the given row
    if current == []:
        currIndex = 0
    else:
        currIndex = len(current[0]) - 1
    if debug:
        print("currIndex = {}".format(currIndex))
    if currIndex == len(row):
        # append the current legitimate row to results and return
        if debug:
            print("Adding ", current)
        result.append(deepcopy(current))
        return
    if row[currIndex] == 0:
        for zero in zeros:
            if debug:
                print("Checking {} against {}".format(current, zero))
            if currIndex == 0:
                temp = deepcopy(zero)
                genRow(row, temp, result, ones, zeros)
            elif isMatch(current, zero):
                if debug:
                    print(current, zero)
                temp = deepcopy(current)
                temp[0].append(zero[0][1])
                temp[1].append(zero[1][1])
                genRow(row, temp, result, ones, zeros)
    else:
        for one in ones:
            if debug:
                print("Checking {} against {}".format(current, one))
            if currIndex == 0:
                temp = deepcopy(one)
                genRow(row, temp, result, ones, zeros)

            elif isMatch(current, one):
                if debug:
                    print(current, one)
                temp = deepcopy(current)
                temp[0].append(one[0][1])
                temp[1].append(one[1][1])
                genRow(row, temp, result, ones, zeros)


def testGenRow():
    print("-"*80)
    print("Testing gen row:")
    r1 = [1, 1]
    result = []
    genRow(r1, [], result, ones, zeros)
    print(result)


def isSolution(old, new):
    n = len(old)
    # iterate over each possible 2x2 minor
    for i in range(n - 1):
        for j in range(n - 1):
            # Extract 2x2 minor from old
            I = [row[j:j + 2] for row in old[i:i+2]]
            if debug:
                print("i = {}, j = {}".format(i, j))
                for row in I:
                    print(row)
            # Compute whether the minor sum is 1 or not
            if (sum([sum(row) for row in I]) == 1) ^ new[i][j]:
                if debug:
                    print("Found {}, but was expecting {}".format(sum([sum(row) for row in I]), new[i][j]))
                return False
    return True

def gen_rows(neb, ones, zeros):
    rows = []
    for row in neb:
        temp = []
        genRow(row, [], temp, ones, zeros)
        rows.append(temp)
    return rows

def collapse(mat):
    totals = {str(row): 1 for row in mat[0]}
    # totals = [[row, 1] for row in mat[0]]
    temp = {}
    while len(mat) > 1:
        # print(totals)
        temp = {}
        # print(mat, "="*40, len(mat))
        for new in mat[1]:
            count = 0
            # print(orig)
            for orig in mat[0]:
                if orig[1] == new[0]:
                    count += totals[str(orig)]
            temp[str(new)] = count
            # print(temp)
        totals = deepcopy(temp)
        mat = mat[1:]

    # print(totals)
    return sum(totals.values())

def test_collapse():
    neb2 = [[True, False, True], 
        [False, True, False],
        [True, False, True]]

    result = gen_rows(neb2, ones, zeros)

    print(collapse(result))

def test_gen_rows():
    neb2 = [[True, False, True], 
        [False, True, False],
        [True, False, True]]

    result = gen_rows(neb2, ones, zeros)
    for row in result:
        print("-"*80)
        for mat in row:
            print(mat)

def solution(neb):
    return collapse(gen_rows(neb, ones, zeros))

def print_test(expected, found):
    print("Expected {}, and found {}".format(expected, found))

def test_isSolution():
    # test case 2: given by google
    neb2 = [[True, False, True], 
        [False, True, False],
        [True, False, True]]
    pot1 = [[False, False, False, True], [
        True, False, False, False], 
        [False, True, False, False], 
        [False, False, True, False]]

    print("Expected {}, found {}".format(True, isSolution(pot1, neb2)))

def test():
    # test case 1: given by google
    neb1 = [[True, True, False, True, False, True, False, True, True, False], 
        [True, True, False, False, False, False, True, True, True, False], 
        [True, True, False, False, False, False, False, False, False, True], 
        [False, True, False, False, False, False, True, True, False, False]]
    num = solution(neb1)
    print_test(11567, num)

    # test case 2: given by google
    neb2 = [[True, False, True], 
        [False, True, False], 
        [True, False, True]]
    num = solution(neb2)
    print_test(4, num)

    # test case 3: given by google
    neb3 = [[True, False, True, False, False, True, True, True], 
        [True, False, True, False, False, False, True, False], 
        [True, True, True, False, False, False, True, False], 
        [True, False, True, False, False, False, True, False], 
        [True, False, True, False, False, True, True, True]]
    num = solution(neb3)
    print_test(254, num)

    # test case 4: nebula with one row
    neb4 = [[True, False, True, False]]
    num = solution(neb4)
    print_test(-1, num) 

    # test case 5: asymmetrical nebula
    neb5 = [[True, False],
        [True, False],
        [False, True],
        [True, False]
        ]
    print_test(-1, solution(neb5))

    # test 6: long nebula
    neb6 = [[True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False]]
    print_test(-1, solution(neb6))

if __name__ == "__main__":
    # test_isSolution()
    # testIsMatch()
    # testGenRow()

    # test_gen_rows()
    test()