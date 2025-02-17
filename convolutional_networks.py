from math import prod

def multi_weights(layers: list):
    """Calculates the total weights in a multilayer neural network.

    Args:
        layers (list): A list of the numbers of neurons in each layer.

    Returns:
        int: The total number of weights in the network.
    """
    running_total = []
    
    for i in range(len(layers) - 1):  
        current_layer = layers[i]
        next_layer = layers[i + 1] 
        weights = (current_layer * next_layer) + next_layer
        running_total.append(weights)

    total = sum(running_total) 
    return total

def next_input(input: list, current: list):
    """Calculates the output volume of a layer of a convolutional neural network.

    Args:
        input (list): A list of the dimensions of the layer that fed input to the current layer.
        current (list): A list of the dimensions of the current filter.

    Returns:
        list: The output volume of the filter.
    """
    
    new_input = []
    new_input.insert(0, input[0]-current[0] +1)
    new_input.insert(1, input[1]-current[1] +1)
    new_input.insert(2, current[3])
    return new_input

def multi_con_layer(input: list, filters: list, output: int, counter = 0):
    """Calculates the weights at each layer of a convolutional neural network, and 
    the total weights in the network.

    Args:
        input (list): The dimensions of the input 'image'.
        filters (list): A list of lists signifying the dimensions of each filter.
        output (int): The number of fully connected output neurons.
        counter (int, optional): An iterator variable.
    """
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
    nn = [10, 10, 10, 5]

    print(multi_weights(nn))
        
    """input_1 = [7, 7, 1]
    output_1 = 5
    filters_1 = [[3, 3, 1, 1]]

    multi_con_layer(input_1, filters_1, output_1)"""

if __name__ == "__main__":
    main()