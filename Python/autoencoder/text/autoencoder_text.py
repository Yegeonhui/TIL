import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from keras import layers
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import matplotlib.pyplot as plt

# data load
data = pd.read_csv('기장_inf.csv', encoding='euc-kr')
row, columns = data.shape
data.columns = [i for i in range(columns)]

# 표층 수온값만 사용
alldata = data[2]

# 결측값에 대한 선형보간작업
alldata = alldata.interpolate(method='values')

# 정규화(0~1)
standard = (alldata - alldata.min()) / (alldata.max() - alldata.min())

# 8 : 2 비율로 train, test 데이터 설정 
X_train, X_test = train_test_split(standard, test_size=0.2, random_state=42)

# X_train, X_test를 데이터프레임에서 (n,1)로 바꾸기 2차원배열
r = X_train.shape
X_train = X_train.to_numpy().reshape(r[0], 1)

r  = X_test.shape
X_test = X_test.to_numpy().reshape(r[0], 1)

# 모델 빌드
class AnomalyDetector(Model):
	def __init__(self):
		super().__init__()
		self.encoder = tf.keras.Sequential([
			layers.Dense(32, activation='relu'), 
			layers.Dense(16, activation='relu'), 
			layers.Dense(8, activation='relu')])
		self. decoder = tf.keras.Sequential([
			layers.Dense(16, activation='relu'), 
			layers.Dense(32, activation='relu'), 
			layers.Dense(1, activation='relu')])
	def call(self, x):
		encoded = self.encoder(x)
		decoded = self.decoder(encoded)
		return decoded

autoencoder = AnomalyDetector()
autoencoder.compile(optimizer='adam', loss='mae')

# # checkpointer 
# checkpointer = ModelCheckpoint(filepath='model.h5',
# 											vebose=0,
# 											save_best_only=True)

# 모델 학습
autoencoder.fit(X_train, X_train, 
								 epochs=50, batch_size=512, 
								 validation_data=(X_test, X_test),
								 shuffle=True,
								 verbose=1,
								 #callbacks=[checkpointer]
								 )

# 예측
predictions = autoencoder.predict(X_test)
threshold = 0.00001

# mse 비교 
mse = np.mean(np.power(X_test - predictions, 2), axis=1)
fig, ax = plt.subplots()
arr = []
for i in range(len(mse)):
	ax.plot(i, mse[i], marker='o', ms=3.5, linestyle="")
	#threshold 보다 높은 값 arr에 저장
	if threshold < mse[i]:
		arr.append((X_test[i, 0] * (alldata.max() - alldata.min())) + alldata.min())

print(arr)
#ax.hlines(threshold, ax.get_xlim()[0], ax.get_xlim()[1], colors="r", zorder=100, label='Threshold')
plt.title("Reconstruction error for different classes")
plt.ylabel("Reconstruction error")
plt.xlabel("Data point index")
plt.show()