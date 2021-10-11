
"""
https://programmers.co.kr/learn/courses/30/lessons/42577

해쉬 문제는 딕셔너리를 써서
key값을 table에 저장한다.

아래 문법이 주요 이용된다.
1. zip(dict.keys(),dict.values())
"""


def solution(genres, plays):
    answer = []
    genres_plays = {}
    genres_num = {}  # (genre,rank)
    for idx, ele in enumerate(genres) :
        if ele in genres_plays:
            genres_plays[ele] += plays[idx]
            if plays[genres_num[(ele,0)]]<plays[idx]:
                genres_num[(ele,1)] = genres_num[(ele,0)]
                genres_num[(ele,0)] = idx
            elif (ele,1) not in genres_num or plays[genres_num[(ele,1)]]<plays[idx]:
                genres_num[(ele,1)] = idx
        else:
            genres_plays[ele] = plays[idx]
            genres_num[(ele,0)] = idx
    li_genres_plays = list(zip(genres_plays.keys(),genres_plays.values()))
    li_genres_plays = sorted(li_genres_plays,reverse = True, key= lambda x: x[1])
    ans = []
    for ele in li_genres_plays:
        g = ele[0]
        ans.append(genres_num[(g,0)])
        if (g,1) in genres_num:
             ans.append(genres_num[(g,1)])
    return ans