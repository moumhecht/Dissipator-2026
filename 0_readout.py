'''
Functions:
Readout Resonator Spectroscopy
Flux Tuning Spectroscopy

'''

def resonator_spectroscopy(qb,
                           IF_min  = 0.1e6,
                           IF_max = 350e6,
                           df = 0.1e6,
                           atten  10,
                           n_avg = 1000,
                           port_type = 'notch',
                           fit = True,):
    
