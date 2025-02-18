import pandas as pd

def avg_in_column(dataset, column):
    file = pd.read_csv(dataset)
    values = file.iloc[column]
    return sum(values) / len(values)


avg_in_column("C:\\Users\\jaspa\\Desktop\\Tagebuch.csv", 0) #points are on index 0