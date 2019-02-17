import pandas as pd
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix, fbeta_score,
    precision_score, recall_score,
)


def get_metrics(true_labels, predicted_labels, avg='macro'):
    """
    Evaluate all the metrics
    :param true_labels:
    :param predicted_labels:
    :param avg:
    :return:
    """
    precision = precision_score(true_labels, predicted_labels, average=avg)
    recall = recall_score(true_labels, predicted_labels, average=avg)
    f1 = fbeta_score(true_labels, predicted_labels, 1, average=avg)
    accuracy = accuracy_score(true_labels, predicted_labels)

    metrics = pd.Series(
        {'accuracy': accuracy, 'precision': precision, 'recall': recall,
         'f1': f1})
    return metrics


def eval_summary(true_labels, predicted_labels, avg='macro', need_matrix=False, summary_as_dict=False):
    """
    Obtain a full classification report, including metrics, a classification report, and optionally, a confusion matrix
    :param true_labels:
    :param predicted_labels:
    :param avg:
    :param need_matrix: If you need the confusion matrix, set this parameter to true.
    :param summary_as_dict: If you want the classification report as a dict, set this parameter to true.
    :return:
    """
    summary = get_metrics(true_labels, predicted_labels, avg=avg)
    report = classification_report(true_labels, predicted_labels, output_dict=summary_as_dict)
    if need_matrix:
        matrix = confusion_matrix(true_labels, predicted_labels)
    else:
        matrix = None

    return summary, report, matrix
