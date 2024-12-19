from typing import NamedTuple, Self

class Equation(NamedTuple):
    value: int
    operands: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        l, r = line.split(": ")
        return cls(int(l), tuple(map(int, r.split())))
    def valid1(self) -> bool:
        match self.operands:
            case (x,):
                return x == self.value
            case (x, y, *rest):
                a = type(self)(self.value, (x+y, *rest))
                b = type(self)(self.value, (x*y, *rest))
                return a.valid1() or b.valid1()
        return False
    def valid2(self) -> bool:
        match self.operands:
            case (x,):
                return x == self.value
            case (x, y, *rest):
                a = type(self)(self.value, (x+y, *rest))
                b = type(self)(self.value, (x*y, *rest))
                c = type(self)(self.value, (int(f"{x}{y}"), *rest))
                return a.valid2() or b.valid2() or c.valid2()
        return False

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
equations = tuple(map(Equation.from_line, raw.strip().splitlines()))

print(sum(e.value for e in equations if e.valid1()))
print(sum(e.value for e in equations if e.valid2()))
