import scipy.linalg

n = 100
A = scipy.linalg.toeplitz(np.hstack([2, -1, np.zeros(n-2)])) * (n+1)**2
t = np.linspace(1/(n+1), 1-1/(n+1),n).T
b = t * (1-t) * np.exp(-t)

def f(x):
    return 0.5 * np.dot(A@x,x) - np.dot(b,x)

def gradf(x):
    return A @ x - b

xstar = np.linalg.solve(A,b)

x0 = np.ones(b.shape)/40 + np.random.random_sample(b.shape)/50
eps = 10**(-4)