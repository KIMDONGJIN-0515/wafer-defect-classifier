"""웨이퍼 맵 시각화.

담당: 김동진
"""

# 색상 (OpenCV는 BGR 순서)
COLORS = {
    0: (27, 27, 27),    # 웨이퍼 바깥: 검정
    1: (80, 175, 76),   # 정상 칩: 초록
    2: (53, 57, 229),   # 불량 칩: 빨강
}


def to_color_image(wafer_map, scale=4):
    """0/1/2 웨이퍼 맵을 색 이미지(numpy 배열)로 바꾼다."""
    # TODO(김동진)
    raise NotImplementedError


def save_examples(X, y, out_dir="assets", per_class=1):
    """클래스별 예시 그림을 저장한다 (README용)."""
    # TODO(김동진)
    raise NotImplementedError
