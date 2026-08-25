class Solution:
    def secondHighest(self, s: str) -> int:
        maxx=-1
        second=-1
        for ch in s:
            if ch.isdigit():
                if int(ch) > maxx:
                    second=maxx
                    maxx=int(ch)
                elif int(ch)>second and int(ch)!= maxx:
                    second=int(ch)
        return second