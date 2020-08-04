print("튜터는 잘생겼다.")

a = 10
b = "다람쥐"

if a > 5:
    print("a는 5보다 크다", "안녕")

if b != "호랑이":
    print("호랑이가 아니다")

my_list = ['a', 'b', 'c', 'd']

for l in my_list:
    print(l)

for i in range(len(my_list)):
    print(my_list[i])

my_score = 10
if my_score > 30:
    print("perfect")
elif my_score > 25:
    print("soso")
else:
    print("not good")


def summation(front, back):
    sum = front + back
    return sum


print(summation(100, 200))


def my_list_appender(l, num):
    l.append(num)
    return l


my_list2 = [1, 2, 3, 4]
my_list2 = my_list_appender(my_list2, 9)

print(my_list2)

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0

for tl in test_list:
    if tl % 2 == 0:
        cnt = cnt + 1

print(cnt)

player = [
    {'name': '박지성', 'age': 20},
    {'name': '기성용', 'age': 24}
]

my_player = ['기성용', '박지성']

cnt = 0


def search(player_dict, player_list):
    for pl in player_list:
        for pl_dc in player_dict:
            if pl == pl_dc['name']:
                print(pl_dc)

search(player,my_player)
