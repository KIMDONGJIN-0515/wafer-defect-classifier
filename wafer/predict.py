"""웨이퍼 맵 하나의 불량 패턴을 예측한다.

담당: 김동찬
실행 예: python -m wafer.predict sample.npy
"""

import sys


def predict(wafer_map):
    """예측한 패턴 이름과 확률을 돌려준다."""
    # TODO(김동찬)
    raise NotImplementedError


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python -m wafer.predict <웨이퍼맵 파일>")
        sys.exit(1)
    # TODO(김동찬): 파일을 불러와 predict() 호출 후 결과 출력
