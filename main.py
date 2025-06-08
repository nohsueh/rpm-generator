import os
from datetime import datetime

from raven_gen import Matrix, MatrixType

matrix_types = [
    MatrixType.ONE_SHAPE,
    MatrixType.ONE_SHAPE,
    MatrixType.TWO_SHAPE_VERTICAL_SEP,
    MatrixType.TWO_SHAPE_VERTICAL_SEP,
    MatrixType.TWO_SHAPE_HORIZONTAL_SEP,
    MatrixType.TWO_SHAPE_HORIZONTAL_SEP,
    MatrixType.SHAPE_IN_SHAPE,
    MatrixType.SHAPE_IN_SHAPE,
    MatrixType.SHAPE_IN_SHAPE,
    MatrixType.SHAPE_IN_SHAPE,
    MatrixType.FOUR_SHAPE,
    MatrixType.FOUR_SHAPE,
    MatrixType.FOUR_SHAPE,
    MatrixType.FOUR_SHAPE,
    MatrixType.FOUR_SHAPE_IN_SHAPE,
    MatrixType.FOUR_SHAPE_IN_SHAPE,
    MatrixType.FOUR_SHAPE_IN_SHAPE,
    MatrixType.FOUR_SHAPE_IN_SHAPE,
    MatrixType.FIVE_SHAPE,
    MatrixType.FIVE_SHAPE,
    MatrixType.FIVE_SHAPE,
    MatrixType.FIVE_SHAPE,
    MatrixType.NINE_SHAPE,
    MatrixType.NINE_SHAPE,
    MatrixType.NINE_SHAPE,
]

date = datetime.now().strftime("%Y%m%d_%H%M%S")
for index, matrix_type in enumerate(matrix_types):
    try:
        rpm = Matrix.make(matrix_type=matrix_type, n_alternatives=5)
        os.makedirs(f"./output/{date}/rpms/{index}", exist_ok=True)
        rpm.save(path=f"./output/{date}/rpms/{index}", puzzle_name="rpm")
    except Exception as e:
        print(e)
        continue
