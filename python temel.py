#Bir listeyi düzleştiren (flatten) fonksiyon

l = [1,'a',['cat'],2,[[[3]],'dog'],4,5]

li = []

def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            li.append(i)

flatten(l)
print(li)

#output: [1,'a','cat',2,3,'dog',4,5]

"--------------------------------------------"

#Listenin içindeki elemanları tersine çeviren fonksiyon

l = [[1,2],[3,4],[5,6,7]]
def inverse(n):
 n = n[::-1]
 n = [i[::-1] for i in n]
 return n

list=[[1, 2], [3, 4], [5, 6, 7]]


print(inverse(list))

#output:[[[7, 6, 5], [4, 3], [2, 1]]




