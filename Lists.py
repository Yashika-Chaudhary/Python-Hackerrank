if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        fcmd = input().split()
        cmd = fcmd[0]
        
        if cmd=='insert':
            list.insert(int(fcmd[1]),int(fcmd[2]))
        
        elif cmd=='print':
            print(list)
        
        elif cmd=='remove':
            list.remove(int(fcmd[1]))
            
        elif cmd=='append':
            list.append(int(fcmd[1]))
        
        elif cmd=='sort':
            list.sort()
            
        elif cmd=='pop':
            list.pop()
            
        else:#reverse
            list.reverse()
