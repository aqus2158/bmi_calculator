# 簡易BMI值計算
height = input('請輸入身高(公尺):')
height = float(height)
weight = input('請輸入體重(公斤):')
weight = float(weight)
bmi = (weight / height ** 2)
print('您的BMI為', bmi)
if bmi < 18.5:
	print('體重過輕')
elif 18.5 <= bmi < 24:
	print('體重適中')
elif 24 <= bmi < 27:
	print('體重過重')
elif 27 <= bmi < 30:
	print('輕度肥胖')
elif 30 <= bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')
