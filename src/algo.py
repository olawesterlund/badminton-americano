import numpy as np

def calculate_schedule(no_of_players: int) -> list:
    if no_of_players % 2 != 0:
        raise ValueError("invalid number of players")
    
    mat = np.zeros([no_of_players, no_of_players])

    for x in range(no_of_players):
        mat[x, x] = -1

    print("Hello World!")
    return [] 

def main():
    calculate_schedule(8)

if __name__ == "__main__":
    main()