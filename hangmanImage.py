class image():
	def img1():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17)  or (col==17 and row<15) or col==34  :
					print('*',end='')
				else:
					print(end=' ')
			print(' ')
		print()
		print()

	def img2():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<15 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)):
					print('*',end='')
				else:
					print(end=' ')
			print(' ')
		print()

	def img3():			
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<15 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('*',end='')
				elif row==9 and (col<18 and  col>9):
					print('*',end='')	
				else:
					print(end=' ')
			print(' ')
		print()
	def img4():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<15 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('*',end='')
				elif row==9 and (col<25 and  col>9):
					print('*',end='')	
				else:
					print(end=' ')
			print(' ')
		print()
	def img5():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<14 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('*',end='')
				elif row==9 and (col<25 and  col>9):
					print('*',end='')	
				elif row==14 and (col<18 and col>9):
					print('*',end='')
					
				else:
					print(end=' ')
			print(' ')

		print()

	def img6():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<14 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('*',end='')
				elif row==9 and (col<25 and  col>9):
					print('*',end='')	
				elif row==14 and (col<25 and col>9):
					print('*',end='')
					
				else:
					print(end=' ')
			print(' ')
		print()


	def img7():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<14 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('*',end='')
				elif row==9 and (col<23 and  col>11):
					print('*',end='')
						
				elif (row==14 and (col==16 or col==18)) or (row==15 and (col==15 or col==19)) or (row==16 and (col==14 or col==20)) :
					print('#',end='')
						
				else:
					print(end=' ')
			print(' ')


	def img8():
		for row in range(20):
			for col in range(35):
				if  row==19 or (row==0 and col>17) or (row==4 and(col==15 or col==19)) or  (col==17 and row<14 and row!=4) or col==34 or ((row==3 or row==6) and (col>13 and col<21)) or ((row==4 or row==5) and (col==13 or col==21)) :
					print('|',end='')
				elif (row==9 and (col==16 or col==18)) or (row==10 and (col==15 or col==19)) or (row==11 and (col==14 or col==20)):
					print('#',end='')
						
				elif (row==14 and (col==16 or col==18)) or (row==15 and (col==15 or col==19)) or (row==16 and (col==14 or col==20)) :
					print('#',end='')
						
				else:
					print(end=' ')
			print(' ')