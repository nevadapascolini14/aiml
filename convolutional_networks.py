from math import prod

def next_input(input: list, current: list):
    new_input = []
    new_input.insert(0, input[0]-current[0] +1)
    new_input.insert(1, input[1]-current[1] +1)
    new_input.insert(2, current[3])
    return new_input

def multi_con_layer(input: list, filters: list, output: int, counter = 0):
    weights = []

    for layer in filters:
        weight = (prod(filters[counter][0:3]) + 1) * filters[counter][3]
        print(f"Weights at layer {counter}: {weight}")
        weights.append(weight)
        input = next_input(input, filters[counter])
        counter += 1
    
    output_layer_weights = prod(input) * output + output
    print(f"Output layer weights: {output_layer_weights}")
    print(f"Total weights = {sum(weights) + output_layer_weights}")

def main():
    input_1 = [7, 7, 1]
    output_1 = 5
    filters_1 = [[3, 3, 1, 1]]

    multi_con_layer(input_1, filters_1, output_1)

if __name__ == "__main__":
    main()