import numpy as np

n_samples = 10000
d = 200 # embedding dimensions

attention_weights = np.zeros(n_samples)

for i in range(n_samples):

    q = np.random.normal(0, 1, size=[d])
    k = np.random.normal(0, 1, size=[d])

    attention_weights[i] = q.T @ k
    

attention_weights.shape # (1000,)

attention_weights.mean() # 0.067  # close to zero
attention_weights.var()  # 195.34 # ~ 200 = d
attention_weights.std()  # 13.976 # ~sqrt(d) = 14.14