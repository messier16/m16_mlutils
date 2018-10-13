import matplotlib.pyplot as plt
import numpy as np


def plot_cm(cm, labels):
    assert len(cm) == len(labels)
    fig, ax = plt.subplots()

    ax.matshow(cm, cmap='Pastel1')

    for (i, j), z in np.ndenumerate(cm):
        ax.text(j, i, '{:0d}'.format(z), ha='center', va='center')

    plt.xlabel("True label")
    plt.ylabel("Predicted label")
    ax.xaxis.set_label_position('top')

    ax.set_xticks(range(len(cm)))
    ax.set_xticklabels(labels)

    ax.set_yticks(range(len(cm)))
    ax.set_yticklabels(labels)
