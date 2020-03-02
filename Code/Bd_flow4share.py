#-*-encoding:utf-8-*-
"""Bd_flow4share.py:主要用于爬取百度迁徙数据."""
__author__      = "LObsangTashi"
import akshare as ak
import pandas as pd
import io
import os 
import importlib,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
importlib.reload(sys)




def get_data(city,tt,dt):
	migration_area_baidu_df = ak.migration_area_baidu(area=city, indicator=tt, date=dt)
	return migration_area_baidu_df

if __name__ == '__main__':
	###目标日期段设置,如['202002%02d'%i for i in range(1,28)] 为爬取2月1日至27日数据
	lst = ['202001%02d'%i for i in range(1,32)] 
	### 迁徙类型参数设置缺省为迁入： move_in迁入，move_out,迁出
	tt="move_in"
	###读取已提供的全国各地级市名单数据，依自己的需求按照格式删减
	df=pd.read_csv("China_citynamelst.csv",header=0)
	###设置数据保存路径，修改为自己的路径
	path=""
	###按照省份创建文件夹，再依次创建一地级市拼音命名的文件夹，爬取数据将会保存为日期+类型为名的csv，
	###多次爬取无需更改保存路径，程序会判断是否有文件存在，不会复写
	for name,group in df.groupby("Pr"):
		newfolder=path+"\\"+name
		if os.path.exists(newfolder):
			pass
		else:
			os.mkdir(newfolder)
		for j in group.values:
			files=newfolder+"\\"+j[-1]
			if os.path.exists(files):
				pass
			else:
				os.mkdir(files)
			for md in lst:
				try:
					df=get_data(j[1],tt,md)
					output_name=md+"_"+tt".csv"
					outfile=files+"//"+output_name
					df.to_csv(outfile,index=False)
				except:
					continue



		