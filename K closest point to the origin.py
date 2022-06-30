class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in points:
            distance = sqrt(i[0]*i[0]+i[1]*i[1])
            i.append(distance)
        points.sort(key=lambda x:x[2])
        distance = []
        i = 0
        while k>0 and i < len(points):
            points[i].pop()
            distance.append(points[i])
            k-=1
            i+=1
        return distance
       