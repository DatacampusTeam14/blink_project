import random
import numpy as np
import os
import cv2
import glob
from PIL import Image
import PIL.ImageOps    
from helpers import *
import argparse

#다음 변수를 수정하여 새로 만들 이미지 갯수를 정합니다.
num_augmented_images = 10

file_path = 'oe_image\\' # 이미지 경로 설정
labels_path = 'oe_image\\labels\\' #이미지 라벨링 경로 설정
file_names = os.listdir(file_path) #경로에 있는 리스트업


#os.path.isfile(txtname + '.txt')
total_origin_image_num = len(file_names)
augment_cnt = 1

for i in range(1, num_augmented_images):
    change_picture_index = random.randrange(1, total_origin_image_num-1)
    print(change_picture_index)
    print(file_names[change_picture_index][-4:])
    txtname=file_names[change_picture_index][:-4]
    file_name = file_names[change_picture_index] #file_names 인덱스 가져오기
    
    origin_image_path = 'oe_image\\' + file_name
    print(origin_image_path)
    image = Image.open(origin_image_path)
    random_augment = random.randrange(1,4) # 임의로 수정 가능
    
    if(random_augment == 7):
        #이미지 좌우 반전
        print("invert")
        inverted_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        inverted_image.save(file_path + 'change\\inverted_' + str(augment_cnt) + '.png')
        text_file=open(labels_path +txtname+'.txt' ,'r')
        
        bbox=text_file.read()
        # text_file.write(file_path + 'change\\labels\\inverted_' + str(augment_cnt) + '.txt')
        text_file.close()

        origin_file= open('oe_image\\change\\labels\\inverted_' + str(augment_cnt) + '.txt','w')
        origin_file.write(bbox)
        origin_file.close()        
    
    elif(random_augment == 0):
        #이미지 기울이기
        print("rotate")
        
        filename = file_name
        image_ext = image_ext
        angle=random.randrange(-20, 20)     
        image = cv2.imread(filename + image_ext, 1)
        
        
        
        
        
        
        
 
        
        


        rotated_image = image.rotate(angle)
        rotated_image.save(file_path + 'change\\rotated_' + str(augment_cnt) + '.png')
        
        
        
        
        
        
        text_file=open(labels_path +txtname+'.txt' ,'r')
        bbox=text_file.read()
        # text_file.write(file_path + 'change\\labels\\rotated_' + str(augment_cnt) + '.txt')
        text_file.close()

        origin_file= open('oe_image\\change\\labels\\rotated_' + str(augment_cnt) + '.txt','w')
        origin_file.write(bbox)
        origin_file.close()        
    
    elif(random_augment == 8):
        #노이즈 추가하기
        img = cv2.imread(origin_image_path)
        print("noise")
        row,col,ch= img.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy_array = img + gauss
        noisy_image = Image.fromarray(np.uint8(noisy_array)).convert('RGB')
        noisy_image.save(file_path + 'change\\noiseAdded_' + str(augment_cnt) + '.png')
        text_file=open(labels_path +txtname+'.txt' ,'r')
        bbox=text_file.read()
        # text_file.write(file_path + 'change\\labels\\noiseAdded_' + str(augment_cnt) + '.txt')
        text_file.close()

        origin_file= open('oe_image\\change\\labels\\noiseAdded_' + str(augment_cnt) + '.txt','w')
        origin_file.write(bbox)
        origin_file.close()


        #os.path.isfile(txtname + '.txt')



    augment_cnt += 1