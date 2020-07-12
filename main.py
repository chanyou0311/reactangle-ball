import argparse
from typing import Coroutine, List

from domain.ball import Ball, CanNotGoalException, Direction, Coordinate, Table


def parse_table(value: str) -> Table:
    return Table(*map(int, value.split(",")))


def parse_coordinate(value: str) -> Coordinate:
    return Coordinate(*map(int, value.split(",")))


def parse_direction(value: str) -> Direction:
    return Direction.from_str(value)


def main():
    parser = argparse.ArgumentParser(description="ビリヤードが跳ね返って穴に落ちるまでのシミュレーション")

    parser.add_argument(
        "-t", "--table", help="テーブルのサイズ", type=parse_table, required=True
    )
    parser.add_argument(
        "-g", "--goal_coordinate", help="終了時の座標", type=parse_coordinate, required=True
    )
    parser.add_argument(
        "-s",
        "--start_coordinate",
        help="開始時の座標",
        type=parse_coordinate,
        default=Coordinate(1, 1),
    )
    parser.add_argument(
        "-sd",
        "--start_direction",
        help="開始時の方向",
        type=parse_direction,
        default=Direction.LOWER_RIGHT,
    )
    args = parser.parse_args()

    ball = Ball(
        args.table, args.start_coordinate, args.start_direction, args.goal_coordinate
    )

    try:
        for step in ball.simulate_steps():
            print(
                f"ステップ数: {step.count}, 座標: ({step.coordinate.x}, {step.coordinate.y})"
            )
    except CanNotGoalException:
        print("ゴールできませんでした。")
    else:
        print("ゴール！")


if __name__ == "__main__":
    main()
