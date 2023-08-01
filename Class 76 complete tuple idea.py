def area_volume(length,width,height):
    """
      :return of area and volume of any object
    """
    area = length * width
    volume = length * width * height
    return area,volume,length,width,height
test = area_volume(2,3,4)
print(test)
print(type(test))
print(test[1])
# test[1]=22
print(test)
test_list = list(test)
print(test_list)
test_list[1] = 22
print(test_list)
test_tuple = tuple(test_list)
print(test_tuple)

# unpacking

fruits = ('Mango',"Banana",'Cherry')
x,y,z = fruits
print(z)
