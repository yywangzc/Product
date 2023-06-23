products = []
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

for p in products:
	print(p[0], '的價格是', p[1])


#'abc' + '123' = 'abc123' #字串可以相加
#'abd' * 3 = 'abcabcabc' #字串可以相乘

with open('products.csv', 'w', encoding='utf-8') as f: # encoding是編碼, utf-8是世界常用編碼
	f.write('商品,價格\n')
	for p in products:
	    f.write(p[0] + ',' + str(p[1]) + '\n') #逗點區隔, excel換不同欄, p[1]是整數需轉乘字串才能同型別相加

