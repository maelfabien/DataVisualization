import pandas as pd


def preprocessing():

    veh_cols = ['Num_Acc', 'Num_Veh', 'senc', 'catv', 'obs', 'obsm', 'choc']
    usa_cols = ['Num_Acc', 'Num_Veh', 'place', 'catu', 'grav', 'sexe', 'An_nais', 'trajet',
                'secu', 'locp']
    lie_cols = ['Num_Acc', 'catr', 'circ', 'nbv', 'vosp', 'prof', 'plan', 'lartpc', 'larrout',
                'surf', 'infra', 'situ']
    car_cols = ['Num_Acc', 'jour', 'mois', 'an', 'hrmn', 'lum', 'dep', 'com', 'agg', 'atm',
                'col', 'gps', 'lat', 'long']

    veh = pd.read_csv('Accidents/vehicules_2005.csv', usecols=veh_cols)
    usa = pd.read_csv('Accidents/usagers_2005.csv', usecols=usa_cols)
    lie = pd.read_csv('Accidents/lieux_2005.csv', usecols=lie_cols)
    car = pd.read_csv('Accidents/caracteristiques_2005.csv', encoding='latin-1', usecols=car_cols)

    for i in range(2006, 2018, 1):
        lie = pd.concat([lie, pd.read_csv('Accidents/lieux_' + str(i) + '.csv', usecols=veh_cols)], axis=0)
        usa = pd.concat([usa, pd.read_csv('Accidents/usagers_' + str(i) + '.csv', usecols=usa_cols)], axis=0)
        veh = pd.concat([veh, pd.read_csv('Accidents/vehicules_' + str(i) + '.csv', usecols=lie_cols)], axis=0)
        try:
            car = pd.concat([car, pd.read_csv('Accidents/caracteristiques_' + str(i) + '.csv',
                                              encoding='latin-1', usecols=car_cols)], axis=0)
        except:
            car = pd.concat(
                [car, pd.read_csv('Accidents/caracteristiques_' + str(i) + '.csv', usecols=car_cols,
                                  encoding='latin-1', sep='\t')], axis=0)

    return veh, usa, lie, car


def get_city_codes():

    city_codes = pd.read_csv('France2018-city-codes.txt',
                             header=0, sep='\t', error_bad_lines=False,
                             encoding='cp850', usecols=['COM', 'NCC'])

    return city_codes