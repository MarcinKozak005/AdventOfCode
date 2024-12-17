

def main():
    data = open('02data.txt')

    # part1: his_play:(my_play,output)
    round_score = {
        'A': {'X': 3, 'Y': 6, 'Z': 0},
        'B': {'X': 0, 'Y': 3, 'Z': 6},
        'C': {'X': 6, 'Y': 0, 'Z': 3},
    }

    # part1: points for playing each shape
    shape_score = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    } 

    # part2: what number (0,3,6) are we looking in round_score
    output_table = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }

    # part 2 start
    def determine_my_shape(his_play, expected_result):
        expected_result = output_table[expected_result]
        for (x,y) in round_score[his_play].items():
            if y == expected_result:
                return x
    # part 2 end

    score = 0
    for line in data:
        his_play = line[0]
        my_play = line[2]
        # part 2
        # expected_result = line[2]
        # my_play = determine_my_shape(his_play, expected_result)
        # part 2
        score += (round_score[his_play][my_play] + shape_score[my_play])
    print(score)

if __name__ == '__main__':
    main()