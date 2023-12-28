import numpy as np
import pandas as pd

# data = pd.Series([None,1, 2, 3, np.nan , 4, 5])
# print(data)

"""dates = pd.date_range("20220226", periods=6)
col = ["John","Jimbo","Joe",'Jenny']
df = pd.DataFrame(np.random.randn(6,4), index=dates,columns=col)

print(df)"""

df = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20220226'),
    'C': pd.Series(1, index=list(range(4)), dtype="float64"),
    'D': np.array([3] * 4, dtype="int32"),
    'E': pd.Categorical(["test", 'train', 'test', 'train']),
    'F': "foo"
})
print(df)