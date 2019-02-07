import pandas as pd
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, fbeta_score,
    precision_score, recall_score,
)


def get_metrics(true_labels, predicted_labels, avg='macro'):
    precision = precision_score(true_labels, predicted_labels, average=avg)
    recall = recall_score(true_labels, predicted_labels, average=avg)
    f1 = fbeta_score(true_labels, predicted_labels, 1, average=avg)
    accuracy = accuracy_score(true_labels, predicted_labels)

    metrics = pd.Series(
        {'accuracy': accuracy, 'precision': precision, 'recall': recall,
         'f1': f1})
    return metrics


def eval_summary(true_labels, predicted_labels, avg='macro'):
    summary = get_metrics(true_labels, predicted_labels, avg=avg)
    report = classification_report(true_labels, predicted_labels)
    matrix = confusion_matrix(true_labels, predicted_labels)

    return summary, report, matrix
