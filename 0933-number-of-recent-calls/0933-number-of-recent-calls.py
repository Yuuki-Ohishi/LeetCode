from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        #新しいリクエスト時刻を追加する
        self.requests.append(t)

        #t-3000より前のリクエストを削除する
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        #残っているリクエストは全て範囲内
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)