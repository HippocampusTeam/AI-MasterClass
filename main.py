def activation_func(x):
    return x / (abs(x) + 1)


def calculate(input, weights, bias):
    output = 0
    for i in range(len(input)):
        output += input[i] * weights[i] 
    return activation_func(output + bias)


# inputs
first = [8.5, 9.5, 9.9, 9.0]
second = [0.65, 0.8, 0.8, 0.9]
third = [1.2, 1.3, 0.5, 1.0]

weights = [0.1, 0.2, 0]
bias = 0.4

input = [first[0], second[0], third[0]] 
prediction = calculate(input, weights, bias)
print(prediction)
