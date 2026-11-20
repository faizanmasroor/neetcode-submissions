class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = []
        for i in range(9):
            cols.append({})

        l, ctr, ri = {}, {}, {}

        for r in range(9):
            if r % 3 == 0:
                l.clear()
                ctr.clear()
                ri.clear()
            row = {}
            for c in range(9):
                val = board[r][c]
                if val.isdigit():
                    row[val] = row.get(val, 0) + 1
                    if row[val] > 1:
                        return False
                    cols[c][val] = cols[c].get(val, 0) + 1
                    if c > 5:
                        ri[val] = ri.get(val, 0) + 1
                    elif c > 2:
                        ctr[val] = ctr.get(val, 0) + 1
                    else:
                        l[val] = l.get(val, 0) + 1
            if r == 2 or r == 5 or r == 8:
                for k, v in l.items():
                    if v > 1:
                        # print('here')
                        return False
                for k, v in ctr.items():
                    # print(f"{k}, {v}")
                    if v > 1:
                        # print('here')
                        return False
                for k, v in ri.items():
                    if v > 1:
                        # print('here')
                        return False

        for col in cols:
            for k, v in col.items():
                if v > 1:
                    return False

        return True

        