#숫자 뒤집어서 반환
# x: 1234
# return: 4321

# x: -1234
# return: -4321

# x: 1230
# return: 321


def reverse(number):
  # 여기에 코드를 작성해주세요.
  #4번
  flag = 1
  if number < 0:
    flag = -1
    number *= -1
  str_reverse = str(number)[::-1]
  return int(str_reverse) * flag


# x='1234'
# print(x[::-1])->4321


#  3번
  # flag = 1
  # if number < 0:
  #   flag = -1
  #   number *= -1
  # num_str = str(number)
  # result_str = ''  
  # for i in range(len(num_str)):
  #   result_str = num_str[i] + result_str
  # return int(result_str) * flag


  
# 2번
# def reverse(number):
#   # 여기에 코드를 작성해주세요.
#   flag = 1
#   if number < 0:
#     flag = -1
#     number *= -1
#   num_str = str(number)
#   num_list=[]
#   for i in range(len(num_str)):
#     num_list.append(num_str[i])
#   reversed_num_list=list(reversed(num_list))
#   return int(''.join(reversed_num_list))*flag

  
#reverse(-12340)

#print('1234'*(-1))


#1번
  # if number > 0:
  #   num_str=str(number)
  #   text=''
  
  #   for i in range(len(num_str)):
  #     print(num_str[i])
  #     text = num_str[i] + text
  
  #   return int(text)
  # else:
  #   number *= -1
  #   num_str=str(number)
  #   text=''
  
  #   for i in range(len(num_str)):
  #     print(num_str[i])
  #     text = num_str[i] + text
  
  #   return int(text)*(-1)



#print(reverse(1234));
