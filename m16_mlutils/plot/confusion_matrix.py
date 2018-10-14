import matplotlib.pyplot as plt
import numpy as np


def print_cm(cm, labels, **kwargs):
    assert len(cm) == len(labels)
    fig, ax = plt.subplots()

    cmap = kwargs.get('cmap', 'Pastel1')

    ax.matshow(cm, cmap=cmap)

    if 'size' in kwargs:
        size = kwargs['size']
        fig.set_figheight(size)
        fig.set_figwidth(size)

    for (i, j), z in np.ndenumerate(cm):
        ax.text(j, i, '{:0d}'.format(z), ha='center', va='center')

    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    ax.xaxis.set_label_position('top')

    ax.set_xticks(range(len(cm)))
    ax.tick_params(axis='x', rotation=90)
    ax.set_xticklabels(labels)

    ax.set_yticks(range(len(cm)))
    ax.set_yticklabels(labels)
