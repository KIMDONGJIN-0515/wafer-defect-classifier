"""데이터 불러오기와 전처리.

담당: 김민재
약속한 형식:
    - 맵 크기 64x64, 값은 0(웨이퍼 바깥) / 1(정상) / 2(불량)
    - 라벨은 wafer.CLASSES 순서대로 0~8
    - load_dataset() -> (X_train, y_train), (X_val, y_val), (X_test, y_test)
"""

MAP_SIZE = 64


def load_raw(path="data/LSWMD.pkl"):
    """원본 pkl 파일을 pandas DataFrame으로 불러온다."""
    # TODO(김민재)
    raise NotImplementedError


def resize_map(wafer_map, size=MAP_SIZE):
    """웨이퍼 맵을 size x size로 맞춘다. 값이 섞이지 않게 cv2.INTER_NEAREST 사용."""
    # TODO(김민재)
    raise NotImplementedError


def preprocess(df):
    """라벨 정리, 크기 맞추기, 학습/검증/테스트 분할, 불균형 처리."""
    # TODO(김민재)
    raise NotImplementedError


def load_dataset(path="data/wafer_data.npz"):
    """전처리된 데이터를 불러온다."""
    # TODO(김민재)
    raise NotImplementedError
