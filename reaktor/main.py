temperature = 10
neurons = 600


def is_criticality_balanced(kelvins, neuron):
    return True if kelvins * neuron < 500000 and kelvins < 800 and neurons > 500 else False


'''
if is_criticality_balanced(temperature, neurons):
    print("Jest git")
else:
    print("nie git")
'''


def reactor_efficiency(voltage, current, theoretical_max_power):
    percent_value = (voltage * current / theoretical_max_power) * 100
    if percent_value >= 80:
        return 'Green'
    if percent_value >= 60:
        return 'Orange'
    if percent_value >= 40:
        return 'Red'
    else:
        return 'Black'

#print(reactor_efficiency(10, 10, 100))

def fail_safe():
    #test mergea
