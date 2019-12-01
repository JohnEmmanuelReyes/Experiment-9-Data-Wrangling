import pandas as pd

d1={'Student':["Ice Bear","Panda","Grizzly"],"Math":[80,95,79]}
d2={'Student':["Ice Bear","Panda","Grizzly"],"Electronics":[85,81,83]}
d3={'Student':["Ice Bear","Panda","Grizzly"],"GEAS":[90,79,93]}
d4={'Student':["Ice Bear","Panda","Grizzly"],"ESAT":[93,89,88]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
df3=pd.DataFrame(d3)
df4=pd.DataFrame(d4)
merge=df1.merge(df2).merge(df3).merge(df4)

long=pd.melt(merge,id_vars=['Student'],value_vars=['Math','Electronics','GEAS','ESAT'],var_name='Subject',value_name="Grade")

