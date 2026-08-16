class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i, row in enumerate(board):
            for j, elt in enumerate(row):
                if elt != ".":
                    #if in the set for row, col, or square
                    #return false    
                    if (elt in rows[i] or elt in columns[j] 
                    or elt in squares[(i//3, j//3)]):
                        return False
                    else:
                        #else add it to each set
                        rows[i].add(elt)
                        columns[j].add(elt)
                        squares[(i//3, j//3)].add(elt)
                
        return True
