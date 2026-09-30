idades = {'Analice': '16', 'Larissa': '15', 'André': '17'}
print(idades)
print(idades ['Larissa'])
print(idades ['André'])
print(idades ['Analice'])

cidades = {'Analice': 'sjrp', 'Larissa': 'cz', 'André': 'sz'}
print(cidades)

idadesecidades = {'Analice': [ '16', 'sjrp' ], 'Larissa': [ '15', 'cz' ], 'André': [ '17', 'sz' ]}
print('A idade de Analice é:')
print(idadesecidades ['Analice'][0])
print('A idade de Larissa é:')
print(idadesecidades ['Larissa'][0])
print('A idade de André é:')
print(idadesecidades ['André'][0])
print('A cidade de Analice é:')
print(idadesecidades ['Analice'][1])
print('A cidade de Larissa é:')
print(idadesecidades ['Larissa'][1])
print('A cidade de André é:')
print(idadesecidades ['André'][1])