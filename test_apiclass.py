import unittest
import apiclass as ac


class Testac(unittest.TestCase):
	def test_getdata(self):
		with self.assertRaises(Bad Request):
			res = ac.getdata('apikey')
			res = res.give_me_data()

		with self.assertRaises(Unauthorized):
			res = ac.getdata('apikey')
			res = res.give_me_data()

		with self.assertRaises(Payment Required):
			res = ac.getdata('apikey')
			res = res.give_me_data()



if __name__ == '__main__':
	unittest.main()