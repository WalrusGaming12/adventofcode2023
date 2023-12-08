string= 'pqr3stu8vwx'
nums=['0','1','2','3','4','5','6','7','8','9']
dict={'one':"1",'two':"2",'three':"3",'four':"4",'five':"5",'six':"6",'seven':"7",'eight':"8",'nine':"9"}
f = open("day1input.txt", "r")
total=[]
full_nums=[]
potentialword=""
sum=0
for line in f:
    full_nums=[]
    potentialword=""
    for i in line:
        if (i in nums):
            potentialword=""
            full_nums.append(i)
        else:
            potentialword=potentialword+i
            print(potentialword)
            for x in dict.keys():
                if(potentialword.find(x)!=-1):
                    full_nums.append(dict[potentialword[potentialword.find(x)::]])
                    potentialword=i
    
    total.append(full_nums[0]+full_nums[-1])
    print(full_nums, line)
for i in total:
    
    sum+=eval(i)
print(sum)