import numpy as np

def calculate_schedule(no_of_pairs: int) -> list:
    if no_of_pairs % 2 != 0:
        raise ValueError('A very specific bad thing happened.')
    
    mat = np.zeros([no_of_pairs, no_of_pairs])

    for x in range(no_of_pairs):
        mat[x, x] = -1

    print("Hello World!")
    return [] 

def main():
    calculate_schedule(8)

if __name__ == "__main__":
    main()