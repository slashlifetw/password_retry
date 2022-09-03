# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 "登入成功!"
# 如果不正確 就印出 "密碼錯誤! 還有_次機會!"

password = 'a123456'
remaining_times = 3
while remaining_times > 0:
    enter_password = input('請輸入密碼')
    if enter_password == password:
        print('登入成功!')
        break
    elif enter_password != password:
        remaining_times = remaining_times - 1
        if remaining_times > 0:
            print('密碼錯誤! 還有', remaining_times, '次機會')
        elif remaining_times == 0:
            print('密碼錯誤! 已輸入3次，請聯繫電腦管理員!')


