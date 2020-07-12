from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Coroutine, Iterator, List, Optional


class CanNotGoalException(Exception):
    """ゴールできないときに送出する例外"""


@dataclass
class Coordinate:
    x: int
    y: int


class Direction(Enum):
    UPPER_RIGHT = auto()
    LOWER_RIGHT = auto()
    UPPER_LEFT = auto()
    LOWER_LEFT = auto()

    @classmethod
    def from_str(cls, value: str) -> "Direction":
        for direction in cls:
            if direction.name == value:
                return direction
        raise ValueError

    @classmethod
    def get_all_names(cls) -> List[str]:
        return list(map(lambda d: d.name, cls))

    @classmethod
    def get_all_directions(cls) -> List["Direction"]:
        return [
            cls.UPPER_RIGHT,
            cls.LOWER_RIGHT,
            cls.UPPER_LEFT,
            cls.LOWER_LEFT,
        ]

    def get_crosswise_directions(self) -> List["Direction"]:
        if self == self.UPPER_RIGHT:
            return [self.LOWER_RIGHT, self.UPPER_LEFT]
        elif self == self.LOWER_RIGHT:
            return [self.UPPER_RIGHT, self.LOWER_LEFT]
        elif self == self.UPPER_LEFT:
            return [self.LOWER_LEFT, self.UPPER_RIGHT]
        elif self == self.LOWER_LEFT:
            return [self.UPPER_LEFT, self.LOWER_RIGHT]
        else:
            raise ValueError

    def get_reverse_direction(self) -> "Direction":
        if self == self.UPPER_RIGHT:
            return self.LOWER_LEFT
        elif self == self.LOWER_RIGHT:
            return self.UPPER_LEFT
        elif self == self.UPPER_LEFT:
            return self.LOWER_RIGHT
        elif self == self.LOWER_LEFT:
            return self.UPPER_RIGHT
        else:
            raise ValueError

    def get_candidate_directions(self) -> List["Direction"]:
        """候補の方向のリストを取得する"""
        return [self] + self.get_crosswise_directions() + [self.get_reverse_direction()]


@dataclass
class Table:
    x_size: int
    y_size: int

    def __post_init__(self) -> None:
        if self.x_size < 2 or self.y_size < 2:
            # 最小サイズは 2x2
            raise ValueError

    def is_correct_coordinate(self, coordinate: Coordinate) -> bool:
        return 0 < coordinate.x <= self.x_size and 0 < coordinate.y <= self.y_size


@dataclass
class Step:
    coordinate: Coordinate
    direction: Direction
    count: int

    @classmethod
    def generate_first_step(
        cls, coordinate: Coordinate, direction: Direction
    ) -> "Step":
        return cls(coordinate, direction, 1)

    def generate_next_step(
        self, coordinate: Coordinate, direction: Direction
    ) -> "Step":
        return Step(coordinate, direction, self.count + 1)


@dataclass
class Ball:
    table: Table
    start_coordinate: Coordinate
    start_direction: Direction
    goal_coordinate: Coordinate
    current_step: Step = field(init=False)

    def __post_init__(self) -> None:
        first_step = Step.generate_first_step(
            self.start_coordinate, self.start_direction
        )
        self.current_step = first_step

    def simulate_steps(self) -> Iterator[Step]:
        max_step_count = self.table.x_size * self.table.y_size
        while self.current_step.count <= max_step_count:
            yield self.current_step
            if self.current_step.coordinate == self.goal_coordinate:
                return
            if (
                self.current_step.coordinate == self.start_coordinate
                and self.current_step.count > 1
            ):
                raise CanNotGoalException
            self.simulate_next_step()
        raise CanNotGoalException

    def simulate_next_step(self) -> Step:
        next_direction = self._get_next_direction()
        next_coordinate = self._get_next_coordinate(
            self.current_step.coordinate, next_direction
        )
        next_step = self.current_step.generate_next_step(
            next_coordinate, next_direction
        )
        self.current_step = next_step
        return self.current_step

    def _get_next_direction(self) -> Direction:
        current_direction = self.current_step.direction
        current_coordinate = self.current_step.coordinate
        candidate_directions = current_direction.get_candidate_directions()

        for candidate_direction in candidate_directions:
            candidate_next_coordinate = self._get_next_coordinate(
                current_coordinate, candidate_direction
            )
            if self.table.is_correct_coordinate(candidate_next_coordinate):
                return candidate_direction

        raise ValueError

    def _get_next_coordinate(
        self, coordinate: Coordinate, direction: Direction
    ) -> Coordinate:
        if direction == Direction.UPPER_RIGHT:
            return Coordinate(coordinate.x + 1, coordinate.y - 1)
        elif direction == Direction.LOWER_RIGHT:
            return Coordinate(coordinate.x + 1, coordinate.y + 1)
        elif direction == Direction.UPPER_LEFT:
            return Coordinate(coordinate.x - 1, coordinate.y - 1)
        elif direction == Direction.LOWER_LEFT:
            return Coordinate(coordinate.x - 1, coordinate.y + 1)
        else:
            raise ValueError
