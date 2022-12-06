import numpy as np
import matplotlib.pyplot as plt


def get_means(ls, chunk_length):
    groups = [ls[x:x+chunk_length] for x in range(0, len(ls), chunk_length)]
    means_list = [sum(group)/len(group) for group in groups]
    return np.asarray(means_list)


def get_STDs(ls, chunk_length):
    groups = [ls[x:x+chunk_length] for x in range(0, len(ls), chunk_length)]
    std_list = [np.std(group) for group in groups]
    return np.asarray(std_list)


def plot_mean_with_std(ls, chunk_length, **kwargs):
    scale = 1
    for key, value in kwargs.items():
        if key=='scale':
            scale = value
    means = get_means(ls, chunk_length)
    stds = get_STDs(ls, chunk_length)
    # plt.plot(means - scale*stds, lw=0.5, c='#396AB1')
    # plt.plot(means + scale*stds, lw=0.5, c='#396AB1')
    plt.fill_between(range(len(means)),means - scale*stds, means + scale*stds, color='#396AB1', alpha=0.2)
    plt.plot(means, lw=1)
    plt.show()


plot_mean_with_std(np.random.uniform(size=1000), 20, scale=.5)
