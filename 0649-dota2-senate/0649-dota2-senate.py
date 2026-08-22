from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant_queue = deque()
        dire_queue = deque()

        #各議員の位置を陣営ごとに保存する
        for index, party in enumerate(senate):
            if party == "R":
                radiant_queue.append(index)
            else:
                dire_queue.append(index)
        
        #どちらかの陣営が全滅するまで続ける
        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()

            if radiant_index < dire_index:
                #Radiantが先に行動し、Direを1人停止する
                #生き残ったRadiantは次のラウンドに参加する
                radiant_queue.append(radiant_index + n)
            
            else:
                #Direが先に行動し、Radiantを1人停止する
                dire_queue.append(dire_index + n)
        
        if radiant_queue:
            return "Radiant"
        else:
            return "Dire"