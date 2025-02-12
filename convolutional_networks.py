input_1 = [15, 15, 1]
filter_1 = [3, 3, 1, 5]
filter_2 = [2, 2, 5, 5]
output_1 = 10

filters_1 = [[3, 3, 1, 5],
             [2, 2, 5, 5]]

def convoluted_layer_output(input: list, filter: list):
    result = ((input[0]-filter[0]+1)*(input[1]-filter[1]+1) * (filter[3]))
    return result

def next_input(input: list, current: list):
    new_input = []
    new_input.insert(0, input[0]-current[0] +1)
    new_input.insert(1, input[1]-current[1] +1)
    new_input.insert(2, current[3])
    return new_input

def multi_con_layer(input: list, filters: list, output: int, counter = 0):
    for layer in filters:
        weight = convoluted_layer_output(input, filters[counter])
        print(f"Weights at layer {counter}: {weight}")
        input = next_input(input, filters[counter])
        counter += 1
    
    print(f"Output weights: {weight * output + output}")


def main():

    """print (next_con_layer_input(input_1, filter_1, 5))"""
    
    """print(next_input(input_1, filters_1[0]))"""

    multi_con_layer(input_1, filters_1, output_1)

if __name__ == "__main__":
    main()