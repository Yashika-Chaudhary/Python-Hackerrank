if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        fullcmd = input().split()
        cmd = fullcmd[0]
        
        if cmd=='insert':
            list.insert(int(fullcmd[1]),int(fullcmd[2]))
        
        elif cmd=='print':
            print(list)
        
        elif cmd=='remove':
            list.remove(int(fullcmd[1]))
            
        elif cmd=='append':
            list.append(int(fullcmd[1]))
        
        elif cmd=='sort':
            list.sort()
            
        elif cmd=='pop':
            list.pop()
            
        else:#reverse
            list.reverse()
