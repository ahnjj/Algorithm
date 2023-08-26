class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        width = len(image[0])

        for i in range(len(image)):
            r = width - 1
            l = 0
            while(l<r):
                #flip
                image[i][r], image[i][l] = image[i][l], image[i][r]
                r -= 1
                l += 1
            for j in range(width):
                #invert
                image[i][j] = abs(image[i][j]-1)


        return image