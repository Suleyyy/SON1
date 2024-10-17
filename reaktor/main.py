temperature = 10
neurons = 600
def is_criticality_balanced(kelvins, neuron):
    return True if kelvins * neuron < 500000 and kelvins < 800 and neurons > 500 else False


if is_criticality_balanced(temperature, neurons):
    print("Jest git")
else:
    print("nie git")
