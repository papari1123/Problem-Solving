print('01. sort를 이용한 정렬')
a = [5,4,2,1,3,5,7,3,2,3,4,5]
a.sort() #sort 메소드는 정렬한 결과를 객체에 반영한다. 
print(a)
print('02. sorted를 이용한 정렬')
b = [3,2,4,6,8,4,2,1,4,7,6]
c = sorted(b) #b를 소팅하고 정렬된 새로운 리스트를 반환한다.
print('03. 오름차순과 내림차순')
print(sorted(b,reverse=True))  #내림차순
print(sorted(b,reverse=False)) #오름차순 (기본값)
print('04. key 함수를 이용한 정렬')
# key값을 기준으로 정렬한다.
print(sorted("This is a test string from Andrew".split(), key=str.lower))
# 대소문자를 가리지 않는 정렬
print(sorted(['as','was','were','He','tester'],key=len)) #길이를 기준으로 정렬렬rint('04. key 함수를 이용한 정렬')

print('05. 중복을 제거한 리스트')
raw = [1,2,3,4,2,1,2,1,2,3,4,5,6,4,2,1,2,]
unique_list = list(set()) # 중복을 제거, 그러나 정렬은 안됨.
unique_sorted_list = list(dict.fromkeys(raw)) #중복을 제거하면서 정렬됨. python 3.7 dictionary key 넣는 순서를 기억한다.