#This is the tic tac toe assignment for week 1 of programming with classes. 
#Authors: Dawson Packer 

def main(): 
    play_game()

def play_game():
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_turn = True
    o_turn = False

    tic_tac_toe_plays = 1
    while tic_tac_toe_plays < 10:
        print("")
        print(f"{numbers_list[0]}|{numbers_list[1]}|{numbers_list[2]}")
        print("-+-+-")
        print(f"{numbers_list[3]}|{numbers_list[4]}|{numbers_list[5]}")
        print("-+-+-")
        print(f"{numbers_list[6]}|{numbers_list[7]}|{numbers_list[8]}")
        print("")

        if x_turn == True: 
            x = int(input("x's turn to choose a square (1-9): "))
            if numbers_list[(x - 1)] == x:
                numbers_list[(x - 1)] = 'x'

            x_turn = False
            o_turn = True
        elif o_turn == True: 
            o = int(input("o's turn to choose a square (1-9): "))
            if numbers_list[(o - 1)] == o:
                numbers_list[(o - 1)] = 'o'
            x_turn = True
            o_turn = False
        if (numbers_list[0] == 'x' and numbers_list[1] == 'x' and numbers_list[2] == 'x') or (numbers_list[3] == 'x' and numbers_list[4] == 'x' and numbers_list[5] == 'x') or (numbers_list[6] == 'x' and numbers_list[7] == 'x' and numbers_list[8] == 'x') or (numbers_list[0] == 'x' and numbers_list[3] == 'x' and numbers_list[6] == 'x') or (numbers_list[1] == 'x' and numbers_list[4] == 'x' and numbers_list[7] == 'x') or (numbers_list[4] == 'x' and numbers_list[7] == 'x' and numbers_list[8] == 'x') or (numbers_list[0] == 'x' and numbers_list[4] == 'x' and numbers_list[8] == 'x') or (numbers_list[0] == 'o' and numbers_list[1] == 'o' and numbers_list[2] == 'o') or (numbers_list[3] == 'o' and numbers_list[4] == 'o' and numbers_list[5] == 'o') or (numbers_list[6] == 'o' and numbers_list[7] == 'o' and numbers_list[8] == 'o') or (numbers_list[0] == 'o' and numbers_list[3] == 'o' and numbers_list[6] == 'o') or (numbers_list[1] == 'o' and numbers_list[4] == 'o' and numbers_list[7] == 'o') or (numbers_list[4] == 'o' and numbers_list[7] == 'o' and numbers_list[8] == 'o') or (numbers_list[0] == 'o' and numbers_list[4] == 'o' and numbers_list[8] == 'o'):
            
            print("")
            print(f"{numbers_list[0]}|{numbers_list[1]}|{numbers_list[2]}")
            print("-+-+-")
            print(f"{numbers_list[3]}|{numbers_list[4]}|{numbers_list[5]}")
            print("-+-+-")
            print(f"{numbers_list[6]}|{numbers_list[7]}|{numbers_list[8]}")
            print("")

            print('Good Game. We have a winner.')
            break
        tic_tac_toe_plays += 1

        if tic_tac_toe_plays == 10: 
            print("")
            print(f"{numbers_list[0]}|{numbers_list[1]}|{numbers_list[2]}")
            print("-+-+-")
            print(f"{numbers_list[3]}|{numbers_list[4]}|{numbers_list[5]}")
            print("-+-+-")
            print(f"{numbers_list[6]}|{numbers_list[7]}|{numbers_list[8]}")
            print("")

if __name__ == "__main__": 
    main()