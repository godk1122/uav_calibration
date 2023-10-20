import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('acc_thrust.csv')
df = df.drop(0)

# 获取三轴力数据
Fx = df.iloc[:, 0]
Fy = df.iloc[:, 1]
Fz = df.iloc[:, 2]

# 获取三轴力矩数据
Mx = df.iloc[:, 3]
My = df.iloc[:, 4]
Mz = df.iloc[:, 5]

# 获取时间数据
t = df.iloc[:, 6]

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(t, Fx, label='Fx')
plt.plot(t, Fy, label='Fy')
plt.plot(t, Fz, label='Fz')

plt.xlabel('time (s)')
plt.ylabel('force (N)')
plt.legend()

plt.show()
