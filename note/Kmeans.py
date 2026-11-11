"""
@Time ： 2026/10/19 15:40
@Auth ： seven
@File ：Kmeans.py
@IDE ：PyCharm
"""
#核心步骤：
#随机选K个中心→分配样本→更新中心→重复直到收敛
import numpy as np
class KMeans:
    def __init__(self, k = 3, max_iter = 100, tol = 1e-4):
        self.k = k
        self.max_iter = max_iter
        self.tol = tol
        self.centers = None

    def fit(self, X):
        n = X.shape[0]
        # 1. 随机选择 K 个样本作为初始聚类中心
        idx =np.random.choice(n, self.k, replace = False)
        self.centers = X[idx].copy()

        for _ in range(self.max_iter):
            # 2. 计算每个样本到每个聚类中心的距离
            # X: (n, d)
            # centers: (k, d)
            # distances: (n, k)

            distances = np.linalg.norm(
                X[:, None, :] - self.centers[None, :, :],
                axis=2
            )

            # 3. 每个样本归到最近的中心

            labels = np.argmin(distances, axis=1)

            # 4. 更新聚类中心
            new_centers = self.centers.copy()

            for i in range(self.k):
                points = X[labels == i]

                # 防止出现空簇
                if len(points) > 0:
                    new_centers[i] = points.mean(axis = 0)

            # 5. 判断是否收敛
            if np.linalg.norm(new_centers - self.centers) < self.tol:
                break

            self.centers = new_centers
        return self
    def predict(self, X):
        distances = np.linalg.norm(
            X[:, None, :] - self.centers[None, :, :],
            axis=2
        )

        return np.argmin(distances, axis=1)

if __name__ == "__main__":
    X = np.array([
        [1, 1],
        [1.5, 2],
        [3, 4],
        [5, 7],
        [3.5, 5],
        [4.5, 5],
        [3.5, 4.5]
    ])
    model = KMeans(k = 2)
    model.fit(X)
    print("聚类中心：")
    print(model.centers)

    print("类别：")
    print(model.predict(X))

