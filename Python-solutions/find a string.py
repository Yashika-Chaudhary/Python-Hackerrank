#using for loop and counter
def count_substring(string, sub_string):
    count = 0
    start_index=0
    for _ in range(0,len(string)):
        i = string.find(sub_string,start_index)
        if(i >= 0):
            start_index = i+1
            count +=1
    return count
  
#using while loop
def count_substring(string, sub_string):
    counting = 0
    while sub_string in string:
        a=string.find(sub_string)
        string=string[a+1:]
        counting += 1
    return counting

  #using for loop
  def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))
  
