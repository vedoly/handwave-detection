import pylab as plt
import numpy as np
from preprocess_util import *
X = np.load('Data/hand_waving.npy')
Y = np.load('data/not_hand_waving.npy')


def skeletonPlot(arr):
    body = np.swapaxes(
        np.array([arr[0], arr[1], arr[20], arr[2], arr[3]]), 0, 1)

    l_leg = np.swapaxes(
        np.array([arr[19], arr[18], arr[17], arr[16], arr[0]]), 0, 1)
    r_leg = np.swapaxes(
        np.array([arr[15], arr[14], arr[13], arr[12], arr[0]]), 0, 1)

    l_arm = np.swapaxes(np.array([arr[20], arr[8], arr[9], arr[10]]), 0, 1)
    r_arm = np.swapaxes(np.array([arr[20], arr[4], arr[5], arr[6]]), 0, 1)

    l_arm = np.swapaxes(np.array([arr[20], arr[8], arr[9]]), 0, 1)
    r_arm = np.swapaxes(np.array([arr[20], arr[4], arr[5]]), 0, 1)

    l_hand = np.swapaxes(np.array([arr[7], arr[21], arr[22]]), 0, 1)
    r_hand = np.swapaxes(np.array([arr[11], arr[23], arr[24]]), 0, 1)

    head = np.swapaxes(np.array([arr[3]]), 0, 1)

    fig, ax = plt.subplots()
    ax.axis([-0.6, 0.6, -0.8, 0.8])

    ax.plot(body[0], body[2], '.-')

    ax.plot(l_leg[0], l_leg[2], '.-')
    ax.plot(r_leg[0], r_leg[2], '.-')

    ax.plot(l_arm[0], l_arm[2], '.-')
    ax.plot(r_arm[0], r_arm[2], '.-')

    ax.plot(l_hand[0], l_hand[2], '.')
    ax.plot(r_hand[0], r_hand[2], '.')
    ax.plot(head[0], head[2], 'ro', markersize=15)
    plt.show()


def armPlot(arr):

    r_arm = np.swapaxes(np.array([arr[0], arr[1], arr[2]]), 0, 1)
    l_arm = np.swapaxes(np.array([arr[3], arr[4], arr[5]]), 0, 1)
    link = np.swapaxes(np.array([arr[0], arr[3]]), 0, 1)

    fig, ax = plt.subplots()
    ax.axis([-1, 1, -1, 1])

    ax.plot(l_arm[0], l_arm[1], '.-')
    ax.plot(r_arm[0], r_arm[1], '.-')
    ax.plot(link[0], link[1], '.-')

    plt.show()


def wavePlot(AngleA):

    # f(figsize=(100,100))

    f, axes = plt.subplots(len(AngleA))
    f.subplots_adjust(hspace=1)

    name = ['left elbow', 'left shoulder', 'right shoulder', 'right elbow']

    for i in range(len(AngleA)):
        axes[i].title.set_text(name[i])
        axes[i].plot(AngleA[i])
        axes[i].set_ylim(0, 360)
