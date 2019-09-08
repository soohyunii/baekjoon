'''
다음 과정을 참고하여 재귀 호출을 사용한 이분 탐색 알고리즘을 만들어 보세요

1. 주어진 탐색 대상이 비어 있다면 탐색할 필요 없음(종료조건)
2. 찾는 값과 주어진 탐색 대상의 중간 위치 값을 비교
3. 찾는 값과 중간 위치 값이 같다면 결괏값으로 중간 위치 값을 돌려줌
4. 찾는 값이 중간 위치 값보다 크면 중간 위치의 오른쪽 부분을 이분탐색 재귀 호출
5. ~~~~~~~~~~~~~~~~~~~~~~~~~~ 작으면 중간 위치 왼쪽을 이분탐색 재귀호출
'''

def recur_bsearch(a,x):
    start = 0
    end = len(a)-1
    mid = (start+end)//2
    print(a[mid])
    if len(a) <= 1 :
        return a
    else :
        if x > a[mid] :
            start = mid+1
            a = a[start:end+1]
            print(a)
            recur_bsearch(a,x)
        elif x < a[mid] :
            end = mid-1
            a = a[start:end+1]
            print(a)
            recur_bsearch(a,x)
        elif x == a[mid] :
            print('here')
            print(mid)
            return
            
        


d = [1,2,3,4,5,6,7,8,9,10]
print(recur_bsearch(d,3))
print(recur_bsearch(d,11))


    
    
