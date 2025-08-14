import time

def select(input_list):
    start = time.time()
    for i in range(len(input_list)):
        for j in range(len(input_list)-(i+1)):
            if input_list[i] > input_list[i+j+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+j+1]
                input_list[i+j+1] = temp
            else:
                continue
    end = time.time()
    print(f"select: {end - start:.6f}")
    return input_list