import numpy as np


def findAngleR(p0, p1, p2):
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    return np.degrees(angle) % 360


def findAngleL(p0, p1, p2):
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    return 360-np.degrees(angle) % 360


def onlyArm(arr):
    return np.array([arr[8], arr[9], arr[10], arr[4], arr[5], arr[6]]).swapaxes(1, 0)[[0, 2]].swapaxes(1, 0)


def norm(arr):
    maxx = arr.max(axis=0)
    minn = arr.min(axis=0)
    rank = maxx-minn
    return (arr-minn)/rank


def setAxes(arr):
    out = np.swapaxes(arr, 1, 4)
    out = np.swapaxes(out, 1, 0)[0]
    return out


def extractAngles(X):
    X_angle = []
    for A in X:
        AngleA = np.zeros((4, 300))
        for i in range(len(A)):
            c = A[i]
            AngleA[0][i] = (findAngleR(c[3], c[4], c[5]))
            AngleA[1][i] = (findAngleR(c[4], c[3], c[0]))
            AngleA[2][i] = (findAngleL(c[1], c[0], c[3]))
            AngleA[3][i] = (findAngleL(c[0], c[1], c[2]))
        X_angle.append(AngleA)
    X_angle = np.array(X_angle)

    return X_angle


def augment(A):
    out = []
    for i in range(len(A)):
        for j in range(0, 300-120, 50):
            out.append(A[i][:, j:j+120])
            out.append(A[i][:, j:j+120][::-1])
    return out
