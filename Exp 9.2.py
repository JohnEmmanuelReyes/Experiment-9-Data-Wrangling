import pandas as pd

d={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
   'Dimension':['Length','Width','Height','Length','Width','Height'],
   'Value':[6,4,2,5,3,4]}
messy=pd.DataFrame(d)
tidy=messy.pivot(index='Box', columns='Dimension', values='Value')
tidy=tidy[['Length','Width','Height']]
tidy['Volume']=tidy.Length*tidy.Height*tidy.Width