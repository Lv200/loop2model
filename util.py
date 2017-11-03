#-*- coding: utf-8 -*-

#from pandas import DataFrame, Series

def dtypeTransform(data, dtype):
	new_data_lists = []

	for data_list in data:
		data_infos = data_list.split(";")
		new_data_infos = []
		
		for data_info in data_infos:
			if data_info:
				new_data_infos.append(map(dtype, data_info.split("|")))
			else:
				new_data_infos.append([])
		new_data_lists.append(new_data_infos)
	return new_data_lists


if __name__ == "__main__":
	pass
