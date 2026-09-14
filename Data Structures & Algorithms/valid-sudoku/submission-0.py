class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)

                if val == '.':
                    continue

                if val in rows[i] or val in columns[j] or val in boxes[box_index]:
                    return False
                else:
                    rows[i].add(val)
                    columns[j].add(val)
                    boxes[box_index].add(val)

        return True

    


                
                