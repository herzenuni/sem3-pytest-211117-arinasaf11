#Сафиуллина Арина ИВТ 2 курс
def func(list1,list2):
 res={}.fromkeys(list1) #Создает словарь, присваивает ключам значения списка list1, а значениям ключей None
 print('Keys:',t1)
 print('Vals:',t2)
 i=0
 for l in res: #цикл идет по ключам словаря
   if i<len(list2): #меняет значения None в словаре, только если во втором списке есть соотв.значение
    res[l]=list2[i]
    i+=1
 print('New dictionary:',res)
 return res
