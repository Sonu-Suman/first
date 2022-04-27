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
                # print(k, "INDEX -------------> ", ind)
                s += (l[ind][0] - l[ind][1])
                if s < 0:
                    break
            if s >= 0:
                return k
        return "Not possible"

    # This is the most optimized methode for solving circular Tour problem

    def WorldTour2(self, petrol, cost, n):
        dificit = 0
        balance = 0
        start = 0

        for i in range(n):
            balance += (petrol[i]-cost[i])

            if balance<0:
                dificit += balance
                balance = 0
                start = i+1

        if (balance-dificit)>=0:
            return start
        else:
            return -1

    def WorldTour3(self, petrol, cost):
        for i in range(len(petrol)):
            s = 0
            for k in range(len(petrol)):
                s += (petrol[k]-cost[k])
                if s<0:
                    break
            if s>=0:
                return i

            petrol.append(petrol[0])
            petrol.remove(petrol[0])
            cost.append(cost[0])
            cost.remove(cost[0])


s = Solution()
petrol = [4, 6, 7, 4]
cost = [6, 5, 3, 5]
print(s.WorldTour(petrol, cost))
print(s.WorldTour1(petrol, cost))
print(s.WorldTour2(petrol, cost, 4))
print(s.WorldTour3(petrol, cost))