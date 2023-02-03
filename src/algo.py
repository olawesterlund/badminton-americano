import numpy as np


def depth_first_search_base(mat: np.array) -> np.array:
    return depth_first_search(mat, (1,2))


def depth_first_search(mat: np.array, curr_depth: tuple) -> np.array:
    # Recursive method to find a working schedule
    size = mat[0].size

    print(mat)
    print(" ")

    # end state
    if curr_depth == (size - 1, size - 1):
        return mat

    # end of row, jump to next row
    if curr_depth[1] > size - 1:
        mat = depth_first_search(mat, (curr_depth[0] + 1, 1))

    # on the diagonal, going down, move one step forward x
    if mat[curr_depth[0], curr_depth[1]] == -2:
        mat[curr_depth[0], curr_depth[1]] = -3
        mat = depth_first_search(mat, (curr_depth[0], curr_depth[1] + 1))

    # on the diagonal, going up, move one step back x
    if mat[curr_depth[0], curr_depth[1]] == -3:
        mat[curr_depth[0], curr_depth[1]] = -2
        mat = depth_first_search(mat, (curr_depth[0], curr_depth[1] + 1))

    # general case, increment number in field and check if valid,
    # if valid continue deeper, if not step back
    curr_val = 0
    test_mat = mat
    while curr_val <= size - 2:
    #if mat[curr_depth[0], curr_depth[1]] <= size - 2:
        test_mat[curr_depth[0], curr_depth[1]] = curr_val 

        if test_valid_schedule(test_mat):
            mat = test_mat
            mat = depth_first_search(mat, (curr_depth[0], curr_depth[1] + 1))
            return mat

        curr_val += 1

    return mat
    

def test_valid_schedule(mat: np.array):
    mat_t = mat.transpose()
    for coord in range(mat[0].size - 1):
        xSet = [x for x in mat[coord] if x >= 0]
        ySet = [x for x in mat_t[coord] if x>= 0]

        dupX = any(xSet.count(x) > 1 for x in xSet)
        dupY = any(ySet.count(x) > 1 for x in ySet)

        if dupX or dupY:
            return False

    return True



def calculate_schedule(no_of_players: int) -> list:
    if no_of_players % 2 != 0:
        raise ValueError("invalid number of players")
    
    mat = np.zeros([no_of_players, no_of_players])
    mat = mat - 1

    for x in range(no_of_players):
        mat[0, x] = x - 1
        mat[x, 0] = x - 1
        mat[x, x] = -2
    
    mat = depth_first_search_base(mat)

    print(mat)

    return [] 

def main():
    calculate_schedule(8)

if __name__ == "__main__":
    main()