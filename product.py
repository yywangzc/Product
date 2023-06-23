import os # operating system

# 檢查是否有檔案
products = []
if os.path.isfile('products.csv'):
	print('yeah! 找到檔案了')
	# 讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 繼續, 使用在迴圈,指跳到下一迴圈再處理
			#s = line.strip().split(',') # strip把換行和空格去掉, 再用逗點當切割
			#name = s[0] # s清單中的第一欄是名稱
			#price = s[1] # s清單中的第二欄是價錢
			name, price = line.strip().split(',') # 上面三行可結合成一行
			products.append([name, price])
	print(products)
else:
	print('找不到檔案......')




# 讀取檔案
#products = []
#with open('products.csv', 'r', encoding='utf-8') as f:
#	for line in f:
#		if '商品,價格' in line:
#			continue # 繼續, 使用在迴圈,指跳到下一迴圈再處理
#		#s = line.strip().split(',') # strip把換行和空格去掉, 再用逗點當切割
#		#name = s[0] # s清單中的第一欄是名稱
#		#price = s[1] # s清單中的第二欄是價錢
#		name, price = line.strip().split(',') # 上面三行可結合成一行
#		products.append([name, price])
#print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price) # 把價格變成整數
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price] # 可取代前三行
	products.append([name, price]) #可取代前四行
print(products)

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])


#'abc' + '123' = 'abc123' #字串可以相加
#'abd' * 3 = 'abcabcabc' #字串可以相乘

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: # encoding是編碼, utf-8是世界常用編碼
	f.write('商品,價格\n')
	for p in products:
	    f.write(p[0] + ',' + str(p[1]) + '\n') #逗點區隔, excel換不同欄, p[1]是整數需轉乘字串才能同型別相加

