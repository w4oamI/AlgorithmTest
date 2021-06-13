#사전 자료형
#키와 값의 쌍을 데이터로 가지는 자료형
#해시 테이블(Hash Table)을 이용한다.
#데이터 조회및 수정에서 좋다.

# dict()함수를 이용하여 초기화 
# data.[키] = '값'
#-----------------------------------#
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지고 있는 데이터가 존재")
#-----------------------------------#

#다른 방법으로 초기화
#-----------------------------------#
a = dict()
a['최']=910
print(a)
a = {
  '김' : 12,
  '나' : 34,
  '박' : 56,
  '이' : 78
}
print(a)
#-----------------------------------#

#-----------------------------------#
print('--------------------')
b = a.keys()
print(b)

#dict_keys가 없어짐.
b = list(a.keys())
print(b)
print('--------------------')

print(a['박'])
#-----------------------------------#

#사전 자료형 메서드
#-----------------------------------#
#키 데이터만 담은 리스트
print(data.keys())

#값 데이터만 담은 리스트
print(data.values())


#각 키에 따른 값을 하나씩 출력
#키 값을 하나씩 출력 못함. 36번째 data.values() 불가
data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

value = data.keys()
for v in value:
  print(data[v])
#-----------------------------------#