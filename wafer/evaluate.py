"""모델 평가.

담당: 김동찬
실행 예: python -m wafer.evaluate
"""


def evaluate(model, X_test, y_test):
    """전체 정확도와 클래스별 정밀도·재현율·F1을 계산한다."""
    # TODO(김동찬): sklearn.metrics.classification_report
    raise NotImplementedError


def plot_confusion_matrix(y_true, y_pred, out_path="assets/confusion_matrix.png"):
    """혼동행렬을 그려 저장한다."""
    # TODO(김동찬)
    raise NotImplementedError


if __name__ == "__main__":
    # TODO(김동찬)
    pass
