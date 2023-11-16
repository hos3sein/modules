import pandas as pd
import apiclass as ac

class data_maker(ac.getdata):
	def --init--(self):
		ac.getdata.--init--(self , apikey)

	def make_csv(self):
		df = pd.DataFrame(data['data'])
		df.to_csv('data.csv')