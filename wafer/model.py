"""모델 정의.

담당: 백찬호
"""

MODEL_NAME = "microsoft/resnet-18"  # 바꿔도 됨


def build_model(num_labels=9):
    """Hugging Face 사전학습 모델을 불러와 출력층을 num_labels개로 바꾼다."""
    # TODO(백찬호): AutoModelForImageClassification.from_pretrained(..., ignore_mismatched_sizes=True)
    raise NotImplementedError
