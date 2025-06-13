# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        row = len(image)
        col = len(image[0])

        for i in range(row):
            for j in range(col//2):
                image[i][j], image[i][col-1-j] = image[i][col-1-j], image[i][j]
        
        for i in range(row):
            for j in range(col):
                if (image[i][j] == 1):
                    image[i][j] = 0
                else:
                    image[i][j] = 1

        return image