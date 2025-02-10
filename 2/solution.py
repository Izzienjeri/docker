import pandas as pd

data = {'Company': ['Indian Hotels Co', 'EIH', 'Chalet Hotels', 'Lemon Tree Hotel', 'Juniper Hotels', 'Mahindra Holiday', 'ITC', 'Samhi Hotels', 'Apeejay Surrend.', 'Oriental Hotels', 'EIH Assoc.Hotels', 'Praveg', 'TajGVK Hotels', 'HLV', 'Royal Orch.Hotel'],
        'Market Cap (Crores)': [99790.22, 24121.28, 19540.15, 10335.65, 8654.17, 8575.87, 5927.11, 4622.44, 3710.79, 2961.54, 2605.66, 2198.28, 2040.62, 1289.51, 1030.10]}

df = pd.DataFrame(data)
print(df)
