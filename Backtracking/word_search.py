## Explanation:
# 1. We start by iterating over the board and calling the dfs function for each cell.
# 2. The dfs function takes the row, column and the index of the character in the word we are looking for.
# 3. If the index is equal to the length of the word, we have found the word and return True.
# 4. If the row or column is out of bounds or the character in the board does not match the character in the word or the cell has already been visited, we return False.
# 5. We add the cell to the set of visited cells and recursively call the function for all the neighbors.
# 6. If any of the recursive calls return True, we return True.
# 7. We remove the cell from the set of visited cells and return False.
# 8. If we iterate over all the cells and do not find the word, we return False.
# 9. The time complexity is O(4^N) where N is the length of the word. The space complexity is O(N) where N is the length of the word.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])
        seen = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))

            return res
        
        for i in range(R):
            for j in range(C):
                if dfs(i,j,0):
                    return True
        return False
    