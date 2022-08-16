import tensorflow as tf
from keras.layers import Conv2D, Conv2DTranspose, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import numpy as np
import cv2

# train, test, val 로드
Img_train = np.load('Img_train.npy')
Img_test = np.load('Img_test.npy')
Img_val = np.load("Img_val.npy")

# 데이터 형식 변경
Img_train = np.array(Img_train, dtype='float32')
Img_test = np.array(Img_test, dtype='float32')
Img_val = np.array(Img_val, dtype='float32')

# 정규화 작업(0~ 1)
Img_train /= 255.
Img_test /= 255.
Img_val /= 255.

b, h, w, c = Img_val.shape
    
# 모델 빌드
# 인코더
encoder_input = tf.keras.Input(shape=(h, w, c))

x = Conv2D(128, 3, activation='relu', strides=1, padding='same')(encoder_input)
x = MaxPooling2D((2, 2))(x)

x = Conv2D(64, 3, activation='relu', strides=1, padding='same')(x)
x = MaxPooling2D((2, 2))(x)

x = Conv2D(32, 3, activation='relu', strides=1, padding='same')(x)
x = MaxPooling2D((2, 2))(x)

x = Conv2D(16, 3, activation='relu', strides=1, padding='same')(x)
x = MaxPooling2D((2, 2))(x)

encoder_output = Conv2D(8, 3, activation='relu', strides=1, padding='same')(x)
encoder = Model(encoder_input, encoder_output)
encoder.summary()

# 디코더
decoder_input = tf.keras.Input(shape=(28, 28, 8))

x = Conv2DTranspose(32, 3, activation='relu', strides=1, padding='same')(decoder_input)
x = UpSampling2D((2, 2))(x)

# 112 -> 224
x = Conv2DTranspose(32, 3, activation='relu', strides=1, padding='same')(x)
x = UpSampling2D((2, 2))(x)

x = Conv2DTranspose(64, 3, activation='relu', strides=1, padding='same')(x)
x = UpSampling2D((2, 2))(x)
# 112 -> 224
x = Conv2DTranspose(128, 3, activation='relu', strides=1, padding='same')(x)
x = UpSampling2D((2, 2))(x)

# 224 -> 448
decoder_output = Conv2DTranspose(3, 3, activation='relu', strides=1, padding='same')(x)

decoder = Model(decoder_input, decoder_output)
decoder.summary()

# 모델 학습 
learning_rate = 0.0005
batch_size = 32

encoder_in = tf.keras.Input(shape=(h, w, c))
x = encoder(encoder_in)
decoder_out = decoder(x)

auto_encoder = Model(encoder_in, decoder_out)
auto_encoder.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss=tf.keras.losses.MeanSquaredError())

auto_encoder.fit(Img_train, Img_train, batch_size=batch_size, epochs=100, shuffle=True,
                     validation_data=(Img_val, Img_val)
                     )

# 모델 저장
auto_encoder.save('model')

# 모델 예측
decoded_images = auto_encoder.predict(Img_test)

# 결과값이 0 ~ 1사이임으로 복원
decoded_images *= 255. 
Img_test *= 255.

decoded_images = np.array(decoded_images, dtype = 'uint8')
Img_test = np.array(Img_test, dtype = 'uint8')

for i in range(1):
    cv2.imshow("encoded", Img_test[i, :, :, :])
    cv2.imshow("decoded_images", decoded_images[i, :, :, :])
    cv2.waitKey(0)