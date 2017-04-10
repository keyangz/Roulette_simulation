import numpy as np

roulette = [{'number':-1, 'color':'green', 'odd-even':'NA'}, {'number':1, 'color':'red', 'odd-even':'odd'},
            {'number': 13, 'color': 'black', 'odd-even': 'odd'}, {'number': 36, 'color': 'red', 'odd-even': 'even'},
            {'number': 24, 'color': 'black', 'odd-even': 'even'}, {'number': 3, 'color': 'red', 'odd-even': 'odd'},
            {'number': 15, 'color': 'black', 'odd-even': 'odd'}, {'number': 34, 'color': 'red', 'odd-even': 'even'},
            {'number': 22, 'color': 'black', 'odd-even': 'even'}, {'number': 5, 'color': 'red', 'odd-even': 'odd'},
            {'number': 17, 'color': 'black', 'odd-even': 'odd'}, {'number': 32, 'color': 'red', 'odd-even': 'even'},
            {'number': 20, 'color': 'black', 'odd-even': 'even'}, {'number': 7, 'color': 'red', 'odd-even': 'odd'},
            {'number': 11, 'color': 'black', 'odd-even': 'odd'}, {'number': 30, 'color': 'red', 'odd-even': 'even'},
            {'number': 26, 'color': 'black', 'odd-even': 'even'}, {'number': 9, 'color': 'red', 'odd-even': 'odd'},
            {'number': 28, 'color': 'black', 'odd-even': 'even'}, {'number': 0, 'color': 'green', 'odd-even': 'NA'},
            {'number': 2, 'color': 'black', 'odd-even': 'even'}, {'number': 14, 'color': 'red', 'odd-even': 'even'},
            {'number': 35, 'color': 'black', 'odd-even': 'odd'},
            {'number': 23, 'color': 'red', 'odd-even': 'odd'}, {'number': 4, 'color': 'black', 'odd-even': 'even'},
            {'number': 16, 'color': 'red', 'odd-even': 'even'}, {'number': 33, 'color': 'black', 'odd-even': 'odd'},
            {'number': 21, 'color': 'red', 'odd-even': 'odd'}, {'number': 6, 'color': 'black', 'odd-even': 'even'},
            {'number': 18, 'color': 'red', 'odd-even': 'even'},
            {'number': 31, 'color': 'black', 'odd-even': 'odd'}, {'number': 19, 'color': 'red', 'odd-even': 'odd'},
            {'number': 8, 'color': 'black', 'odd-even': 'even'}, {'number': 12, 'color': 'red', 'odd-even': 'even'},
            {'number': 29, 'color': 'black', 'odd-even': 'odd'}, {'number': 25, 'color': 'red', 'odd-even': 'odd'},
            {'number': 10, 'color': 'black', 'odd-even': 'even'}, {'number': 27, 'color': 'red', 'odd-even': 'odd'}]

def get_round_result(roulette, n_round):
    result_number = []
    result_color = []
    result_odd_even = []

    for i in range(n_round):
        choose = np.random.randint(low=0, high=38)
        result_number.append(roulette[choose]['number'])
        result_color.append(roulette[choose]['color'])
        result_odd_even.append(roulette[choose]['odd-even'])

    return result_number, result_color, result_odd_even

def compute_stat(result_number, result_color, result_odd_even):
    same_num_in_row = 0
    same_color_in_row_max = 1
    same_odd_even_in_row_max = 1
    same_color = 1
    same_odd_even = 1
    for i in range(len(result_number)-1):
        if result_number[i] == result_number[i+1]:
            same_num_in_row += 1

        if result_color[i] == result_color[i+1]:
            same_color += 1
            if same_color > same_color_in_row_max:
                same_color_in_row_max = same_color
        else:
            same_color = 1

        if result_odd_even[i] == result_odd_even[i+1]:
            same_odd_even += 1
            if same_odd_even > same_odd_even_in_row_max:
                same_odd_even_in_row_max = same_odd_even
        else:
            same_odd_even = 1

    green_percent = result_color.count('green')*1.0/len(result_color)
    black_percent = result_color.count('black')*1.0/len(result_color)
    red_percent = result_color.count('red')*1.0/len(result_color)
    odd_percent = result_odd_even.count('odd')*1.0/len(result_odd_even)
    even_percent = result_odd_even.count('even')*1.0/len(result_odd_even)

    return green_percent, black_percent, red_percent, odd_percent, even_percent, same_num_in_row, \
           same_color_in_row_max, same_odd_even_in_row_max

def simulate(simulation_time):
    green_pct_avg = []
    black_pct_avg = []
    red_pct_avg = []
    odd_pct_avg = []
    even_pct_avg = []
    same_num = []
    same_color_max = []
    same_odd_even_max = []
    for i in range(simulation_time):
        result_number, result_color, result_odd_even = get_round_result(roulette, 40)
        green_percent, black_percent, red_percent, odd_percent, even_percent, same_num_in_row, same_color_in_row_max, \
        same_odd_even_in_row_max = compute_stat(result_number, result_color, result_odd_even)
        green_pct_avg.append(green_percent)
        black_pct_avg.append(black_percent)
        red_pct_avg.append(red_percent)
        odd_pct_avg.append(odd_percent)
        even_pct_avg.append(even_percent)
        same_num.append(same_num_in_row)
        same_color_max.append(same_color_in_row_max)
        same_odd_even_max.append(same_odd_even_in_row_max)

    green_average = np.mean(green_pct_avg)
    black_average = np.mean(black_pct_avg)
    red_average = np.mean(red_pct_avg)
    odd_average = np.mean(odd_pct_avg)
    even_average = np.mean(even_pct_avg)

    same_num_in_row_average = np.mean(same_num)
    same_num = np.array(same_num)
    same_num_greater_3 = sum(same_num>3)

    same_color_max_average = np.mean(same_color_max)
    same_color_max = np.array(same_color_max)
    same_color_greater_8 = sum(same_color_max>8)

    same_odd_even_max_average = np.mean(same_odd_even_max)
    same_odd_even_max = np.array(same_odd_even_max)
    same_odd_even_greater_8 = sum(same_odd_even_max>8)

    print 'Green Percentage Average: %s' %green_average
    print 'Black Percentage Average: %s' %black_average
    print 'Red Percentage Average: %s' %red_average
    print 'Odd Percentage Average: %s' %odd_average
    print 'Even Percentage Average: %s' %even_average
    print 'Same Number in Row Average: %s' %same_num_in_row_average
    print 'Same Color Max Average: %s' %same_color_max_average
    print 'Same Odd-Even Max Average: %s' %same_odd_even_max_average
    print 'same number in row p_value %s' %(same_num_greater_3*1.0/simulation_time)
    print 'color_p_value: %s' %(same_color_greater_8*1.0/simulation_time)
    print 'odd_even_p_value: %s' %(same_odd_even_greater_8*1.0/simulation_time)

simulate(10000)

