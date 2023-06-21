#TwoSum por fuerza bruta
def twosum(numeros, objetivo):
    for i in range (len(numeros)):
        for j in range(i+1, len(numeros)):
            if numeros[i] + numeros[j] == objetivo:
                return(i,j)
    raise ValueError ("Sin solucion")

if __name__ == "__main__":
    nums = [3,8,4,7,9,5,1,6]
    target = 14
    print(twosum(nums, target))
#Elfego Adair Juarez Arias