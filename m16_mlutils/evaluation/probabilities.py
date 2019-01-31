import numpy as np
import pandas as pd

def to_labels(predictions, encoder):
    max_probs = np.argmax(predictions, axis=1)
    labels = encoder.inverse_transform(max_probs)
    return labels


def to_dataframe(predictions, encoder):
    labels = encoder.classes_
    return pd.DataFrame(predictions, columns=labels)


def right_wrong(y_true, probabilities, encoder, as_percentage=True):
    labels = to_labels(probabilities, encoder)
    classes = [f'{i}' for i in range(len(encoder.classes_))]
    aligned_dataframe = pd.DataFrame({
        'correct': y_true,
        'assigned': labels,
    })

    for i, clase in enumerate(classes):
        aligned_dataframe[clase] = probabilities[:, i] * (100 if as_percentage else 1)

    right = aligned_dataframe.query('assigned == correct')
    wrong = aligned_dataframe.query('assigned != correct')

    right_max = np.max(right[classes], axis=1)
    wrong_max = np.max(wrong[classes], axis=1)

    return pd.concat([
        pd.DataFrame({
            'Probability': right_max,
            'Result': 'Correct'
        }),

        pd.DataFrame({
            'Probability': wrong_max,
            'Result': 'Wrong'
        })
    ])
