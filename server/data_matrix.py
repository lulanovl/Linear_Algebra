

attributes = ['Food', 'Entertainment', 'Cultural & Historical', 'Outdoor Activities', 
                'Trips', 'Get Drunk', 'Student', 'Friends', 'Family', 'Couples', 'Tourists']



matrix = {
    'Bamboo':       [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    'Vanilka':      [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    'Nomad':        [1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    'Khan-Tengri':  [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    'Moldo-Ashu':   [0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    'Kol-Suu lake': [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    'Salkyn-Tor':   [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    'Gurman':       [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    'Museum':       [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    'UCA':          [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    'Izumrud':      [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    'Corona':       [1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    'Madison':      [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
    'Cinema':       [0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    'Theatre':      [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
}


places = {
    'Bamboo':       ['Food', 'Entertainment', 'Get Drunk', 'Friends', 'Family', 'Couples', 'Tourists'],
    'Vanilka':      ['Food', 'Friends', 'Couples'],
    'Nomad':        ['Food', 'Get Drunk', 'Friends','Family'],
    'Khan-Tengri':  ['Food', 'Get Drunk', 'Friends', 'Family','Couples', 'Tourists'],
    'Moldo-Ashu':   ['Cultural & Historical', 'Outdoor Activities', 'Trips', 'Friends', 'Tourists'],
    'Kol-Suu lake': ['Cultural & Historical', 'Outdoor Activities', 'Trips', 'Friends', 'Family', 'Tourists'],
    'Salkyn-Tor':   ['Cultural & Historical', 'Outdoor Activities', 'Trips', 'Friends', 'Family', 'Tourists'],
    'Gurman':       ['Food', 'Student','Friends', 'Family', 'Couples'],
    'Museum':       ['Cultural & History', 'Student', 'Friends', 'Tourists'],
    'UCA':          ['Student', 'Trip', 'Friends', 'Get Drunk'],
    'Izumrud':      ['Food', 'Couples', 'Family', 'Student'],
    'Corona':       ['Food', 'Entertainment', 'Couples', 'Family', 'Student'],
    'Madison':      ['Food', 'Couples', 'Family', 'Student'],
    'Cinema':       ['Entertainment', 'Couples', 'Family', 'Student', 'Friends'],
    'Theatre':      ['Entertainment','Cultural & Historical', 'Family', 'Couples'],
}