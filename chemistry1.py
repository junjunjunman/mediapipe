import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False
# 단위 세포의 꼭짓점 좌표 생성
def generate_bcc():
    # 단순 입방 구조의 각 꼭짓점의 좌표
    points = np.array([[0, 0, 0],
                       [0, 0, 1],
                       [0, 1, 0],
                       [0, 1, 1],
                       [1, 0, 0],
                       [1, 0, 1],  
                       [1, 1, 0],
                       [1, 1, 1],
                       ])
    return points
def ggg():
    points1= np.array([[0.5,0.5,0.5]])
    return points1
# 시각화 함수
def plot_scc():
    points = generate_bcc()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    points1 = ggg()
    ax= fig.add_subplot(111,projection='3d')
    # 각 점을 플롯
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='b', s=10000)  # 점의 크기 증가
    ax.scatter(points1[:, 0], points1[:, 1], points1[:, 2], color='r', s=10000) 
    # 각 꼭짓점을 연결하는 선을 그림
    
    # 그래프의 축 레이블 설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 축의 범위 설정
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    
    # 눈금과 격자 표시 제거
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.grid(False)
    
    plt.title("체심입방구조")
    plt.show()

# SCC 구조 시각화
plot_scc()