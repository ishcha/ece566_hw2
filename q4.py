import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
# np.random.seed(1000)

K = 1000
theta = 1

ns = [6, 100]


for n in ns:
    sample_n_y = np.random.normal(0, theta, n)
    estimation_errors = []
    for k in range(K):
        bootstrap_sample = np.random.choice(sample_n_y, n, replace=True)
        theta_hat = np.mean([bootstrap_sample[i]**2 for i in range(n)])
        estimation_errors.append(np.sqrt(n)*(theta_hat-theta))
        
    print(f"n = {n}:")
    print(f"Mean: {np.mean(estimation_errors)}")
    print(f"Variance: {np.var(estimation_errors)}")
    
    std = np.std(estimation_errors)
    
    estimation_errors = np.sort(estimation_errors)
    
    gaussian_pdf = stats.norm.pdf(estimation_errors, 0, std)
    
    # KDE for the empirical distribution
    kde = stats.gaussian_kde(estimation_errors)
    x_vals = np.linspace(min(estimation_errors), max(estimation_errors), 1000)
    # print(x_vals)
    kde_pdf = kde(x_vals)
    
    l1_error = np.sum(np.abs(gaussian_pdf - kde_pdf))/len(kde_pdf)
    
    print(f"L1 Error: {l1_error}")
    
    plt.plot(x_vals, kde_pdf, label="estimated pdf")
    
    plt.plot(estimation_errors, gaussian_pdf, label="gaussian pdf")
    plt.legend()
    plt.xlabel("Estimation Errors")
    
    
    
    plt.show()