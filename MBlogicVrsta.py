import random

a = "C:/Users/Maj/Desktop/AnimalsMB/ara.jpg"
b = "C:/Users/Maj/Desktop/AnimalsMB/Dog.jpg"
c = "C:/Users/Maj/Desktop/AnimalsMB/Elephant.jpg"
d = "C:/Users/Maj/Desktop/AnimalsMB/Fish.jpg"
e = "C:/Users/Maj/Desktop/AnimalsMB/Shark.jpg"
f = "C:/Users/Maj/Desktop/AnimalsMB/Snake.jpg"
g = "C:/Users/Maj/Desktop/AnimalsMB/Zebra.jpg"
h = "C:/Users/Maj/Desktop/AnimalsMB/Pig.jpg"
i= "C:/Users/Maj/Desktop/AnimalsMB/Bird.jpg"
j= "C:/Users/Maj/Desktop/AnimalsMB/Giraffe.jpg"
k= "C:/Users/Maj/Desktop/AnimalsMB/BlackPanther.jpg"
l= "C:/Users/Maj/Desktop/AnimalsMB/StarFish.jpg"
m= "C:/Users/Maj/Desktop/AnimalsMB/LadyBug.jpg"
n= "C:/Users/Maj/Desktop/AnimalsMB/Hippo.jpg"
o= "C:/Users/Maj/Desktop/AnimalsMB/Turtle.jpg"



pic_var_list = [a, b, c, d, e, f, g, h, a, b, c, d, e, f, g, h]
pic_var_liststr = ['A','B','C','D','E','F','G','H','A','B','C','D','E','F','G','H']

def pictures_matrix4():
    ran_list4 = pic_var_list
    ran_list4str = pic_var_liststr
    combined = list(zip(ran_list4, ran_list4str))
    random.shuffle(combined)
    ran_list4[:], ran_list4str[:] = zip(*combined)
    return ran_list4str,ran_list4
#
pic_var_list5 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]

def pictures_matrix5():
    ran_list5 = pic_var_list5
    random.shuffle(ran_list5)
    return ran_list5
#