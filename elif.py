'''
name=input("نام داوطلب:")
age=int(input('سن داوطلب:'))
flight_hours=int(input('ساعت پرواز'))
score=int(input('امتیاز شبیه ساز'))
licence=input('گواهینامه پزشکی معتبر دارید؟ بله/خیر')
if age < 25 or licence == "خیر" or flight_hours < 1000 or score <90:
    print('خطا:وضعیت خلبان نامعتبر.پذیرفته نشد')
elif flight_hours>=1000 and score >= 80 :
    print('ذخیره شد')
    print('نام داوطلب',name)
    print('شما به عنوان نامزد ماموریت انتخاب شدید',name)
print(f"fasele ta had nesab emtiaz: {90-score} emtiaz had nesab")
'''
'''
name = input("نام مسئول: ")
people = int(input("تعداد افراد گروه: "))
water = int(input("مقدار آب موجود (لیتر): "))
food = int(input("تعداد بسته های غذا: "))

need_water = people * 3
need_food = people * 1

print("گزارش منابع جزیره")
print(f"مسئول: {name} ")

if people <= 0 or water < 0 or food < 0:
    print("اطلاعات نامعتبر است.")

elif water >= need_water and food >= need_food:
    print("وضعیت آب: کافی است.")
    print("وضعیت غذا: کافی است.")
    print(" گروه می تواند یک روز دیگر در جزیره بماند.")

elif water < need_water and food < need_food:
    print("وضعیت آب: ناکافی است.")
    print("وضعیت غذا: ناکافی است.")
    print(" گروه باید هرچه سریع تر خارج شود.")

elif water < need_water:
    print('آب ناکافی.غذای کافی')
elif food < need_food:
    print('آب اکافی.غذای ناکافی')
'''
'''
nickname=input('nam khod ra vared konid:')
time=int(input('zamane sarf shode baraye peyda kardan asib paziri ha:'))
bug=int(input('tedad asib paziri haye yaft shode:'))
if bug >= 5 and time <= 60:
    print(f"{nickname} barande mosabeghe")
elif bug >= 5 and time >= 61:
    print('natije shoma dar dast barresi ast')
else:
    print('az in marhale pazirofte nashod')
print(f"zamane sabt shode:{time} daghighe")
'''