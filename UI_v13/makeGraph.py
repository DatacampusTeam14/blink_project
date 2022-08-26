import csv
import matplotlib.pyplot as plt
import os
import glob
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt

path_result = "C:/Users/choi/PycharmProjects/yolo7/blinkResult/"

def makeGraph():
    plt.rcParams['font.family'] ='Malgun Gothic' #한글폰트 깨짐 방지1
    plt.rcParams['axes.unicode_minus'] =False    #한글폰트 깨짐 방지2

    os.chdir(path_result)

    ###### bi 파일=> blink 정수형 초당 체크

    condition2='bi*_*.csv'
    csvfiles2=glob.glob(condition2)
    filename2=csvfiles2[-1]
    total2=0 # 깜빡임 횟수 누적
    idx2=[]
    sec_21=[]
    blink_cnt2=[]
    with open(filename2,"r") as file2:
        fs2=csv.reader(file2)
        fs2.__next__()#헤더 정보 값 한줄 통과
        for i, row in enumerate(fs2):
            idx2.append(row[0])
            sec_21.append(row[1])
            blink_cnt2.append(row[2])

    sec_21=list(map(int,sec_21))
    blink_cnt2=list(map(int,blink_cnt2))

    cum_blink_cnt2=[]
    for i in range(0, len(blink_cnt2)):
        if blink_cnt2[i]!=0:
            total2+=blink_cnt2[i]
            cum_blink_cnt2.append(total2)
        else:
            cum_blink_cnt2.append(total2)

    plt.xlim(0,max(sec_21)) #x축 범위
    plt.ylim(0,5) #y축 범위
    plt.title('눈 깜빡임 횟수', fontsize=15)
    plt.stem(sec_21,blink_cnt2)
    plt.legend(['깜빡임 횟수=%d'%max(cum_blink_cnt2)], fontsize=12)
    plt.savefig(path_result+'blink_count_'+filename2[:-4]+'.png', dpi=100)
    plt.figure() #따로 그리겠다
    #k2=[(0.25*number) for number in idx2]
    k2=[]
    jump=0
    idx2=list(map(int,idx2))
    for i in range (0,len(idx2)):
        if idx2[i]!=0 and idx2[i]%4==0:
            jump+=1
            k2.append(jump)
            
        else:
            k2.append(jump)

    plt.xlim(0,max(sec_21)) #x축 범위
    plt.ylim(0,total2) #y축 범위
    plt.title('눈 깜빡임 누적 횟수', fontsize=15)
    plt.plot(sec_21,cum_blink_cnt2,drawstyle='steps-post')
    plt.plot(sec_21,k2,drawstyle='steps-post')

    plt.legend(['(분당)사용자 눈 깜빡임=%.2f회'%(max(cum_blink_cnt2)*60/max(sec_21)),'(분당)평균 눈 깜빡임=15회'], fontsize=12)
    plt.savefig(path_result + 'blink_total_count_'+filename2[:-4]+'.png', dpi=100)
    plt.figure()

    file2.close()

    ###### bf 파일=> blink 실수형 초당 체크

    condition1='bf*_*.csv'
    csvfiles1=glob.glob(condition1)
    filename1=csvfiles1[-1]
    total1=0
    fps_sec=[]
    idx1=[]
    sec_11=['0']
    blink_cnt1=[]
    with open(filename1,"r") as file1:
        fs1=csv.reader(file1)
        fs1.__next__()#헤더 정보 값 한줄 통과
        for i, row in enumerate(fs1):
            idx1.append(row[0])
            sec_11.append(row[1])
            blink_cnt1.append(row[2])

    sec_11=list(map(float,sec_11))
    sec_12=sec_11[1:]
    for i in range(0,len(sec_11)-1):
        sec_11[i]=sec_11[i+1]-sec_11[i]    
    sec_13=sec_11[1:-1]
    avg_sec=sum(sec_13)/len(sec_13)
    for i in range(0,len(sec_13)):
        fps_sec.append(1/(sec_13[i]))
    avg_fps=sum(fps_sec)/len(fps_sec)

    blink_cnt1=list(map(int,blink_cnt1))
    cum_blink_cnt1=[]
    for i in range(0, len(blink_cnt1)):
        if blink_cnt1[i]==1:
            total1+=1
            cum_blink_cnt1.append(total1/avg_fps)
        else:
            cum_blink_cnt1.append(total1/avg_fps)
    plt.xlim(0,len(sec_13)) #x축 범위 #y축 범위
    plt.title('전체 측정 간격', fontsize=15) #이걸 통해서 평균 측정 간격과 평균 프레임 구하기 가능
    plt.xticks([], [])
    plt.plot(idx1[1:],sec_13)
    plt.plot(idx1[1:],[avg_sec]*len(sec_13))
    plt.legend(['평균 FPS=%.2f'%avg_fps,'평균 측정 시간=%.3fs'%(1/avg_fps)], fontsize=12)
    plt.savefig(path_result + 'total_interval_'+filename1[:-4]+'.png', dpi=100)
    plt.figure() #따로 그리겠다

    plt.xlim(0,max(sec_12)) #x축 범위 #y축 범위
    plt.title('측정 간격', fontsize=15) #이걸 통해서 평균 측정 간격과 평균 프레임 구하기 가능
    plt.scatter(idx1[1:],sec_13)
    plt.plot(idx1[1:],sec_13)
    plt.plot(idx1[1:],[avg_sec]*len(sec_13))
    plt.savefig(path_result + 'interval_'+filename1[:-4]+'.png', dpi=100)
    plt.figure() #따로 그리겠다

    Avarage_closed=[]
    knt=0
    Avcl=0
    for i in range(0,len(sec_12)-1):
        if (int(sec_12[i+1])%4==0)and (int(sec_12[i])!=int(sec_12[i+1])):
            for _ in range(0,4):
                Avcl+=1/avg_fps
                Avarage_closed.append(Avcl)
            knt=3
        else:
            knt-=1
            if 0<=knt<=2: 
                pass
            else:    
                Avarage_closed.append(Avcl)
    Avarage_closed.append(Avcl)
    print(Avarage_closed)

    plt.xlim(0,max(sec_12)) #x축 범위
    plt.ylim(-2,2) #y축 범위
    plt.title('눈 깜빡임 횟수', fontsize=15)
    plt.yticks([], [])
    plt.plot(sec_12,blink_cnt1,drawstyle='steps-post')
    plt.savefig(path_result + 'blink_count_'+filename1[:-4]+'.png', dpi=100)
    plt.figure() #따로 그리겠다
    
    plt.xlim(0,max(sec_12)) #x축 범위
    plt.ylim(0,max(cum_blink_cnt1)) #y축 범위
    plt.title('눈 감은시간', fontsize=15)
    plt.plot(sec_12,cum_blink_cnt1)
    plt.plot(sec_12,Avarage_closed)

    plt.legend(['User closed=%.2fs'%max(cum_blink_cnt1),'Avarage closed=%.2fs'%max(Avarage_closed)], fontsize=12)
    plt.savefig(path_result + 'clt_'+filename1[:-4]+'.png', dpi=100)
    plt.figure()
    file1.close()

    graph_result = [sec_11[-1], avg_fps, cum_blink_cnt2[-1], cum_blink_cnt1[-1]]
    return graph_result
SAVE=makeGraph()