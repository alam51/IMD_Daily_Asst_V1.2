import pandas as pd
dfa = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
dfb = pd.DataFrame([[1, 'a'], [3, 'b'], [5, 'c']], columns=['A', 'B'])
# dfa.join(dfb, on=['A'])
# ValueError: columns overlap but no suffix specified: Index([u'A'], dtype='object')

dfa = pd.concat([dfa, dfb], join='outer')
dfa = dfa[~dfa.index.duplicated(keep='first')]
a = 5
