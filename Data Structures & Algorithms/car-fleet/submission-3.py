class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedByPos = {}
        for i in range(len(position)):
            speedByPos[position[i]] = speed[i]
        sortedPosition = sorted(position)[::-1]
        st = [(target - sortedPosition[0]) / speedByPos[sortedPosition[0]]]
        for pos in sortedPosition:
            timeToArrive = (target - pos) / speedByPos[pos]
            if timeToArrive > st[-1]:
                st.append(timeToArrive)
        return len(st)