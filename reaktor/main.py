from reaktor.modules.reaktor import Reaktor

reaktor1 = Reaktor(100, 600, 10, 100, 1100, 6100)

if reaktor1.is_criticality_balanced(reaktor1.kelvins, reaktor1.neuron):
    print('Jest zrównoważony w stanie krytycznym')
else:
    print('Nie jest zrównoważony w stanie krytycznym')

print(reaktor1.reactor_efficiency(reaktor1.voltage, reaktor1.current, reaktor1.t_m_p))

reaktor1.fail_safe(reaktor1.kelvins, reaktor1.neuron, reaktor1.limit)
