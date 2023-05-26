# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    m = int(input())
    arr1 = set(map(int, input().split()))
    n = int(input())
    arr2 = set(map(int,input().split()))
    result = sorted(arr2.difference(arr1) | arr1.difference(arr2))
    for x in result:
        print(x)
        
#Using in built function 
M_int = int(input())
M = set(map(int, input().split())) 
N_int = int(input())
N = set(map(int, input().split()))
print('\n'.join(map(str,sorted(M.symmetric_difference(N)))))
