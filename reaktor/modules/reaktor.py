class Reaktor:
    def __init__(self, kelvins, neuron, voltage, current, theoretical_max_power, limit):
        self.kelvins = kelvins
        self.neuron = neuron
        self.voltage = voltage
        self.current = current
        self.t_m_p = theoretical_max_power
        self.limit = limit

    @staticmethod
    def is_criticality_balanced(kelvins, neuron):
        return True if kelvins * neuron < 500000 and kelvins < 800 and neuron > 500 else False

    @staticmethod
    def reactor_efficiency(voltage, current, t_m_p):
        percent_value = (voltage * current / t_m_p) * 100
        if percent_value >= 80:
            return 'Green'
        if percent_value >= 60:
            return 'Orange'
        if percent_value >= 40:
            return 'Red'
        else:
            return 'Black'

    @staticmethod
    def fail_safe(calv, neuron, limit):
        score = (calv * neuron) / limit * 100
        if score < 90:
            print('LOW')
        elif score >= 90:
            print('NORMAL')
