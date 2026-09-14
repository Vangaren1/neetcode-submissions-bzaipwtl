class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ptr = 0
        count = 0
        if len(flowerbed)==0 and n > 0: 
            return False
        if len(flowerbed)*2 < n:
            return False 
        if len(flowerbed) == 1 and n<= 1 and flowerbed[0]==0:
            return True 
        while ptr < len(flowerbed):
            print(f"{ptr}")
            if count >= n:
                return True
            # check for front end
            if flowerbed[ptr] == 0:

                if (
                    (ptr == 0 and flowerbed[1] == 0)
                    or (ptr == len(flowerbed) - 1 and flowerbed[ptr - 1] == 0)
                    or (
                        0 < ptr < len(flowerbed) - 1
                        and flowerbed[ptr - 1] == 0
                        and flowerbed[ptr + 1] == 0
                    )
                ):
                    count += 1
                    ptr += 2
                    continue
                else:
                    ptr += 1
            else:
                ptr += 1

        return count >= n