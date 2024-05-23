




class Permutation:
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789 ,.?!:;'
    def __init__(self, indexes: list[int]):
        self.indexes = indexes
        self.n = len(self.indexes)

    def __str__(self):
        out = []
        if self.n == len(Permutation.chars):
            for i in range(self.n):
                out.append(f"{Permutation.chars[i]} -> {Permutation.chars[self.indexes[i]]}")
        else:
            for i in range(self.n):
                out.append(f"{i} -> {self.indexes[i]}")
        return "\n".join(out)
    
    def __repr__(self) -> str:
        return f"Permutation(n = {self.n})"
    
    def __mul__(self, other: 'Permutation') -> 'Permutation':
        assert self.n == other.n
        return Permutation([self.indexes[other.indexes[i]] for i in range(self.n)])

    def inverse(self) -> 'Permutation':
        out = [0 for i in range(self.n)]
        for i in range(self.n):
            out[self.indexes[i]] = i
        return Permutation(out)
    
    def modify(self, index1: int, index2: int) -> None:
        self.indexes[index1] = index2
        self.indexes[index2] = index1
    
def create_identity(n: int) -> Permutation:
    return Permutation([i for i in range(n)])

