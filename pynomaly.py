from PyNomaly import loop
import numpy as np

train_data = np.array([
    [23.3, 50.2, 1020  ],
    [23.9, 51.3, 1020.3],
    [23.2, 50.2, 1020.2],
    [26.6, 51.3, 1020.3],
    [23.1, 52.0, 1020.9],
    [23.5, 52.3, 1020.0]
])

train_set = loop.LocalOutlierProbability(train_data, 
n_neighbors=3).fit()
train_scores = train_set.local_outlier_probabilities

test_scores = []
test_array = np.array([21, 53, 1020])
test_scores.append(train_set.stream(test_array))

print(test_scores)

