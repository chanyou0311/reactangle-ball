from domain.ball import Ball, Coordinate, Direction, Step, Table
import unittest


class TestTable(unittest.TestCase):
    def test_cannot_create_table(self):
        """1x2のときにテーブルが作成できないテスト"""
        # テストの実行
        with self.assertRaises(ValueError):
            Table(1, 2)


class TestBall(unittest.TestCase):
    def test_6x3(self):
        """テーブルが6x3のときの正常系テスト"""
        # データの生成
        start_coordinate = Coordinate(1, 1)
        start_direction = Direction.LOWER_RIGHT
        goal_coordinate = Coordinate(1, 3)
        table = Table(6, 3)
        ball = Ball(table, start_coordinate, start_direction, goal_coordinate)

        expected_steps = [
            Step(Coordinate(1, 1), Direction.LOWER_RIGHT, 1),
            Step(Coordinate(2, 2), Direction.LOWER_RIGHT, 2),
            Step(Coordinate(3, 3), Direction.LOWER_RIGHT, 3),
            Step(Coordinate(4, 2), Direction.UPPER_RIGHT, 4),
            Step(Coordinate(5, 1), Direction.UPPER_RIGHT, 5),
            Step(Coordinate(6, 2), Direction.LOWER_RIGHT, 6),
            Step(Coordinate(5, 3), Direction.LOWER_LEFT, 7),
            Step(Coordinate(4, 2), Direction.UPPER_LEFT, 8),
            Step(Coordinate(3, 1), Direction.UPPER_LEFT, 9),
            Step(Coordinate(2, 2), Direction.LOWER_LEFT, 10),
            Step(Coordinate(1, 3), Direction.LOWER_LEFT, 11),
        ]

        # テストの実行
        for expected_step, actual_step in zip(expected_steps, ball.simulate_steps()):
            with self.subTest("各ステップが正しいこと"):
                self.assertEqual(expected_step, actual_step)

    def test_3x3(self):
        """テーブルが3x3のときの異常系テスト"""
        # データの生成
        start_coordinate = Coordinate(1, 1)
        start_direction = Direction.LOWER_RIGHT
        goal_coordinate = Coordinate(1, 3)
        table = Table(3, 3)
        ball = Ball(table, start_coordinate, start_direction, goal_coordinate)

        expected_steps = [
            Step(Coordinate(1, 1), Direction.LOWER_RIGHT, 1),
            Step(Coordinate(2, 2), Direction.LOWER_RIGHT, 2),
            Step(Coordinate(3, 3), Direction.LOWER_RIGHT, 3),
            Step(Coordinate(2, 2), Direction.UPPER_LEFT, 4),
            Step(Coordinate(1, 1), Direction.UPPER_LEFT, 5),
        ]

        # テストの実行
        for expected_step, actual_step in zip(expected_steps, ball.simulate_steps()):
            with self.subTest("各ステップが正しいこと"):
                self.assertEqual(expected_step, actual_step)


if __name__ == "__main__":
    unittest.main()

