class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """   
        try:
            i= nums.index(target)
            if len(nums)==1:
                return [i,i]
        except:
            return [-1,-1]
        if i ==len(nums)-1:
            return [i,i]
        for j in range(i+1,len(nums)):
            if nums[j]!=target:
                return [i,j-1]
            elif j == len(nums)-1:
                return [i,len(nums)-1]
        """
        
        ###二分查找
        def find_left(nums,target):
            if nums[0]==target:
                return 0
            k1 = 0
            k2 = len(nums)
            while True:
                mid = (k1+k2)//2
                if nums[mid]==target:
                    if nums[mid-1]<target:
                        return mid
                    else:
                        k2 = mid
                else:
                    k1 = mid
        def find_right(nums,target):
            k1 = 0
            k2 = len(nums)
            if nums[-1]==target:
                return k2-1
            while True:
                mid = (k1+k2)//2
                if nums[mid]==target:
                    if nums[mid+1]>target:
                        return mid
                    else:
                        k1 = mid
                else:
                    k2 = mid                    
                
        left = 0
        right = len(nums)-1
        if right==-1:
            return [-1,-1]
        
        find_not = True
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                find_not = False
                break

        if find_not:
            return [-1,-1]    
        else:
            i= left+ find_left(nums[left:mid+1],target)
            j =mid+ find_right(nums[mid:],target)
            return [i,j]

            
        
        