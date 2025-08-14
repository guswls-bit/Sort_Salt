def select(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)-(i+1)):
            if input_list[i] > input_list[i+j+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+j+1]
                input_list[i+j+1] = temp
            else:
                continue

    return input_list