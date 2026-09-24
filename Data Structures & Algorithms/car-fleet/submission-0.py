class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        fleet_time=0

        for p,s in cars:
            time=(target-p)/s

            if time > fleet_time:
                fleet_time=time
                fleet+=1
        return fleet