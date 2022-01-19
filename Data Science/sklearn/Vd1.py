import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PoissonRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
n_samples, n_features = 1000, 20
rng = np.random.RandomState(0)
X = rng.randn(n_samples, n_features)
y = rng.poisson(lam = np.exp(X[:,5]) / 2)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)
glm = PoissonRegressor()
gbdt = HistGradientBoostingRegressor(loss = "poisson", learning_rate = 0.01)
glm.fit(X_train, y_train)
gbdt.fit(X_test, y_test)
print(glm.score(X_train, y_train))
print(gbdt.score(X_test, y_test))