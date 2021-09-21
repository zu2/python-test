#!/usr/local/bin/python3

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import japanize_matplotlib
from adjustText import adjust_text

from sklearn.linear_model import LinearRegression
#日付,市区町村,全人口,全人口接種1回目,全人口接種2回目,全人口接種率1回目,全人口接種率2回目,高齢者人口,高齢者接種1回目,高齢者接種2回目,高齢者接種率1回目,高齢者接種率2回目

df_csv = pd.read_csv('all.csv',encoding = 'UTF8' , index_col=0, parse_dates=[0]) # 0-19

df = df_csv[df_csv['市区町村']=='（全国）'][['全人口接種率1回目']]
df.rename(columns={'全人口接種率1回目': '（全国）'},inplace=True)

cities = ['（沖縄県）','那覇市','宜野湾市','浦添市','名護市','糸満市','沖縄市','豊見城市','うるま市','南城市']
for s in cities:
	df_tmp = df_csv[df_csv['市区町村']==s][['全人口接種率1回目']]
	df_tmp.rename(columns={'全人口接種率1回目': s},inplace=True)
	df = pd.concat([df,df_tmp],axis=1)

print(df)
plt.figure(figsize=(10,10))
plt.title("自治体別ワクチン接種率(1回目)", fontsize=20)
plt.ylabel("接種率(接種数/人口）",fontsize=18)
plt.xticks(rotation=20)
for s in ['（全国）']+cities:
	plt.plot(df.index,df[s])
plt.legend(['（全国）']+cities)
plt.rcParams['svg.fonttype'] = 'none'
plt.savefig("自治体別ワクチン接種率(1回目).png")
plt.savefig("自治体別ワクチン接種率(1回目).svg")
plt.show()

sys.exit(0)
