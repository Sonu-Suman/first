class Solution:
    def WorldTour(self, petrol, cost):
        l = []

        for i, j in zip(petrol, cost):
            l.append([i, j])

        i = 0
        while i < len(petrol):
            s = 0
            for k in range(len(petrol)):
                s += l[k][0] - l[k][1]
                if s < 0:
                    break
            if s >= 0:
                return i
            l.append(l[0])
            l.remove(l[0])
            i += 1

    def WorldTour1(self, petrol, cost):
        l = []
        for i, j in zip(petrol, cost):
            l.append([i, j])

        for k in range(len(petrol)):
            s = 0
            for j in range(len(petrol)):
                ind = (k + j)
                if ind > len(petrol) - 1:
                    ind -= len(petrol)
                print(k, "INDEX -------------> ", ind)
                s += (l[ind][0] - l[ind][1])
                if s < 0:
                    break
            if s >= 0:
                return k
        return "Not possible"


s = Solution()
petrol = [4, 6, 7, 4]
cost = [6, 5, 3, 5]
print(s.WorldTour(petrol, cost))
print(s.WorldTour1(petrol, cost))