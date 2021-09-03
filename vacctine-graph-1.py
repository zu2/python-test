import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
df = pd.read_csv(sys.argv[1]+'.csv',encoding = 'UTF8', index_col=0)
df['高齢化率'] = df['高齢者人口'] * 100 / df['全人口']
df['type'] = '離島'
df.loc['（全国）':'（沖縄県）','type'] = 'その他'
df.loc['那覇市':'宜野湾市','type'] = '本島市部'
df.loc['浦添市':'うるま市','type'] = '本島市部'
df.loc['南城市':'南城市','type'] = '本島市部'
df.loc['国頭村':'金武町','type'] = '本島町村'
df.loc['読谷村':'南風原町','type'] = '本島町村'
df.loc['八重瀬町':'八重瀬町','type'] = '本島町村'
df_other = df[df.type.isin(['その他'])]
df_city  = df[df.type.isin(['本島市部'])]
df_rural = df[df.type.isin(['本島町村'])]
df_island = df[df.type.isin(['離島'])]
plt.figure(figsize=(10,10))
plt.xlim([15,50])
plt.ylim([10,80])
plt.title("沖縄県自治体別 高齢化率-接種率("+sys.argv[1]+")", fontsize=20)
plt.xlabel("高齢化率")
plt.ylabel("接種率（対全人口）")
#plt.scatter(df['高齢化率'],df['接種率1（全）'],c='black')
plt.scatter(df_other['高齢化率'],df_other['接種率1（全）'],c='black')
plt.scatter(df_city['高齢化率'],df_city['接種率1（全）'],c='red')
plt.scatter(df_rural['高齢化率'],df_rural['接種率1（全）'],c='green')
plt.scatter(df_island['高齢化率'],df_island['接種率1（全）'],c='blue')
for k, v in df.iterrows():
    plt.annotate(k,xy=(v[10],v[3]),size=8)
plt.legend(("その他","本島市部","本島町村","離島"),loc="lower right")
plt.savefig('散布図-高齢化率-1回目接種率-'+sys.argv[1]+'.png')
#plt.show()

sys.exit(0)
