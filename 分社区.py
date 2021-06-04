#!/usr/bin/env python
# coding: utf-8

import numpy as np
import copy

#首先构造一个20*20的0矩阵
B=np.zeros((20,20))

#打印一下看看目前矩阵的样子
print(B)

#接下来逐行更新数据，从第0行开始一直更新到第19行
B[[0],[1,6]] = 1
B[[1],[0,2,3,5,6]] = 1
B[[2],[1,4,6,7]] = 1
B[[3],[1,4,6]] = 1
B[[4],[2,3,5,6,13]] = 1
B[[5],[1,4,6]] = 1
B[[6],[1,2,3,4,5,18]] = 1
B[[7],[2,8,9,10]] = 1
B[[8],[7,9,10,11]] = 1
B[[9],[7,8,10]] = 1
B[[10],[7,8,9,11,12]] = 1
B[[11],[8,10,14]] = 1
B[[12],[10,13,14,18,19]] = 1
B[[13],[4,12,18,19]] = 1
B[[14],[11,12,15,17]] = 1
B[[15],[14,16,19]] = 1
B[[16],[15,17,18,19]] = 1
B[[17],[14,16,19]] = 1
B[[18],[6,12,13,16,19]] = 1
B[[19],[12,13,15,16,17,18]] = 1

#再次打印B看一下什么样子
print(B)

#1边聚类系数算法代码
#函数作用：计算各条边的边聚类系数（权重）
def edge_3(A,degree):  # A为邻接矩阵，degree为节点的度
    N = A.shape[0]
    E = np.zeros((N,N))
    for i in range(N):
        for j in range(i+1,N):
            if A[i,j] != 0:
                temp = min(degree[0,i]-1, degree[0,j]-1)
                # temp变量用来记录i和j节点度减1较小的一个
                for k in range(N):
                    E[i,j] = E[i,j] + A[i,k]*A[k,j] # 记录边（i，j）所在的三角形数
                     
                if temp != 0:
                    E[i,j] = E[i,j]/temp 
                    # 本处采用的是边聚类系数的原始定义C_ij=z_ij/min{ki-1,kj-1}
                else:   
                    E[i,j] = 0
                E[j,i] = E[i,j]
                
    return E  #输出边聚类系数矩阵


#2搜索社区分组
# 函数作用：搜索连通分支，得到节点社区划分结果
# 记录节点所在社区标号，从0开始记
def communities(A):
    N = A.shape[0]  # 网络中所有节点，初始时所有节点均未被划分
    flag = -np.ones((1,N))
    lis = -np.ones((1,N))
    c = 0 # 连通分支数目
    lis[0,0] = int(0)# 将0节点加入到查询队列中
    flag[0,0] = c
    f = int(0); e = 0 # 当前查询的队列中前后“游标”
    while e < N:
        if f <= e:
            for i in range(N): # 搜寻f节点的邻居
                if A[int(lis[0,f]),i] == 1 and flag[0,i] == -1: # 邻居节点尚未被划分
                    flag[0,i] = c  #  %划分到社区c中
                    e = e + 1
                    lis[0,e] = i
            f = f+1
        else:
            i = 0
            while i < N: #找到一个未被划分的节点i
                if flag[0,i] == -1:
                    break
                i = i + 1
            if i != N:        
                e = e + 1
                lis[0,e] = i
                c = c + 1
                flag[0,i] = c #新开一个社区组
            else:
                break
    return flag


def modularityQ(M,realA,degree):
    N = realA.shape[0]
    Q = 0.0  # 模块性度量
    m = 0.0  # 网络节点的总度数(对应modularity公式中的2m，m为网络的总边数)
    for i in range(N):
        m = m + degree[0,i]
    for i in range(N):
        for j in range(N):
            if M[i] == M[j]: # 节点在同一个社区
                Q = Q + realA[i,j]-degree[0,i]*degree[0,j]/m
                #Q=1/2m\sum_ij[A_ij-ki*kj/2m]delta(Ci,Cj), Ci,Cj为社区号
    Q = Q/m           
    return Q


#3计算模块性Q
# 函数作用：对给定的某个社区划分，计算相应的模块性度量标准
# 输入：节点的社区划分结果M，邻接矩阵A，节点的度向量degree
def modify_edge_3(A,E,degree,i0,j0):
    N = A.shape[0]
    flag1 = 0
    for i in range(N):
        if i != i0 and i != j0:
            if A[i,i0]+A[i,j0] == 1: #A[i,i0]=1 or A[i,j0]=1
                if degree[0,i0] == 1:
                    if degree[0,i0] < degree[0,i]:
                        if degree[0,i0] >2.0:
                            E[i0,i] = E[i0,i]*(degree[0,i0]-1.0)/(degree[0,i0]-2.0)
                            E[i,i0] = E[i0,i]
                        else:
                            E[i0,i] = 0.0
                            E[i,i0] = E[i0,i]
                else:
                    if degree[0,j0] < degree[0,i]:
                        if degree[0,j0] > 2.0:
                            E[j0,i] = E[j0,i]*(degree[0,j0]-1.0)/(degree[0,j0]-2.0)
                            E[i,j0] = E[j0,i]
                        else:
                            E[j0,i] = 0.0
                            E[i,j0] = E[j0,i]
            elif A[i,i0]+A[i,j0] == 2: #更新两条边E[i0,i] 和E[j0,i]
                if degree[0,i0] < degree[0,i]:
                    if degree[0,i0] > 2.0:
                        E[i0,i] = (E[i0,i]*(degree[0,i0]-1.0)-1.0)/(degree[0,i0]-2.0)
                        E[i,i0] = E[i0,i]
                    else:
                       E[i0,i] = 0.0
                       E[i,i0] = E[i0,i]
                else:
                    E[i0,i] = E[i0,i]-1.0/degree[0,i]
                    E[i,i0] = E[i0,i]
                if degree[0,j0] < degree[0,i]:
                    if degree[0,j0] > 2.0:
                        E[j0,i] = (E[j0,i]*(degree[0,j0]-1.0)-1.0)/(degree[0,j0]-2.0)
                        E[i,j0] = E[j0,i]
                    else:
                        E[j0,i] = 0.0
                        E[i,j0] = E[j0,i]
                else:
                    E[j0,i] = E[j0,i]-1.0/degree[0,i]
                    E[i,j0] = E[j0,i]
                flag1 = 1 #是否存在三角形
                break
    return flag1, E


#4修改边聚类系数
# 函数作用：修改各条边的边聚类系数（权重）
# 输入：邻接矩阵A，权重矩阵E，节点的度degree，被删去的边i0，j0
def modularityvector(A):
    N = A.shape[0] # 网络的节点数目
    CC = np.zeros((1,N+1)) # 前N维记录最大模块性值对应的模块划分状况，最后第N+1维记录对应的最大模块性值
    degree = np.zeros((1,N)) # 保存原始图的每个节点的度
    #A_degree = np.zeros((1,N)) # 节点度向量的一个副本
    total_edge = int(0) # 总边数
    MM = 10000000.0 # 充分大的数
    flag = 0 # 是否存在三角形
    m = -MM # 记录最大模块性值
    c = np.zeros((2,N)) # 记录节点社区分组结果
    local_A = copy.deepcopy(A) # 由于要去边，所以去边操作是在A的一个副本local_A上进行
    
    for i in range(N):
        for j in range(N):
            degree[0,i] = degree[0,i] + A[i,j] # 计算各个节点的度数
            
    A_degree = copy.deepcopy(degree)# 节点度向量的一个副本
    
    for i in range(N):
        total_edge = total_edge + degree[0,i]
    
    total_edge = int(total_edge/2) # 计算总边数
    
    E = edge_3(local_A,degree) # 计算各边的权重
    
    for k in range(total_edge,1,-1):
        if flag == 0 and np.mod(k,2) == 0: #获得当前的节点社区分组情况
            c[1] = c[0]
            c[0] = communities(local_A)
        else:
            if flag == 0:
                c[0] = c[1]
                c[1] = communities(local_A)
        if flag == 0:
            if  all(c[0] == c[1]): #看是否发生变化
                if np.mod(k,2) == 0:
                    #计算相应分组结果的模块性度量标准值
                    m2 = modularityQ(c[0],A,A_degree)
                    if m <= m2: #寻找最大模块性度量标准值
                        m = m2
                        for i in range(N):
                            CC[0,i] = c[0,i] #计算最大度量标准值对应的社区划分结果
                            CC[0,N] = m #记录最大度量标准值
                else: 
                    #计算相应分组结果的模块性度量标准值
                    m2 = modularityQ(c[1],A,A_degree)
                    if m <= m2: #寻找最大模块性度量标准值
                        m = m2
                        for i in range(N):
                            CC[0,i] = c[1,i] #计算最大度量标准值对应的社区划分结果
                            CC[0,N] = m #记录最大度量标准值
        #找到权重最小的那条边
        i0 = 0
        j0 = 0
        max_e = MM
        for i in range(N):
            for j in range(i+1,N):
                if E[i,j] > 0.0:
                    if E[i,j] <= max_e:
                        max_e = E[i,j]
                        i0 = i
                        j0 = j
                if max_e == 0.0:
                    break
        
        #删去(i0,j0)这条边
        local_A[i0,j0] = 0
        local_A[j0,i0] = 0
        
        #修改边权重矩阵
        E[i0,j0] = MM
        E[j0,i0] = MM
        [flag, E] = modify_edge_3(local_A,E,degree,i0,j0)
        
        #修改节点i0和j0的度数
        degree[0,i0] = degree[0,i0] - 1
        degree[0,j0] = degree[0,j0] - 1

    return CC

result = modularityvector(B)

print(result)