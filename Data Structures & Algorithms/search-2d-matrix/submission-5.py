class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m,n=len(matrix),len(matrix[0])
        top=0
        bottom=m-1
        l,r=0,n-1
        while top<=bottom:
            row=(top+bottom)//2
            if target>matrix[row][n-1]:
                top=row+1
            elif target<matrix[row][0]:
                bottom=row-1
            else:
                while l<=r:
                    mid=(l+r)//2
                    if matrix[row][mid]==target:
                        return True
                    elif matrix[row][mid]<target:
                        l=mid+1
                    else:
                        r=mid-1
                return False
        return False
