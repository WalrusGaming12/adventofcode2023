text = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
final=[]
colors = {"red":0,"blue":0,"green":0}
f=open("input.txt","r")
bre=0
sum=0
for line in f:
    colors = {"red":0,"blue":0,"green":0}
    bre=0
    text=line.split(";")
    final=[]
    final.append((text[0].split(":"))[0].split(" ")[1])
    final.append(text[0].split(":")[1].split(","))
    for split in text[1:]:
        final.append(split.split(","))
    game=final[1:]
    for i in range(len(game)):
        
        #print("game",game)
        for color in game[i]:
            temp = color.split(" ")
            temp = temp[1:]
            #print("temp",temp)
            for num in range(len(temp)):
                if(num%2==1):
                    
                    if((colors[temp[num].replace("\n","")])<=(int(temp[num-1].replace("\n","")))):
                        colors[temp[num].replace("\n","")]=int(temp[num-1].replace("\n",""))
                        next
                    else:
                        #print("GAME IMPOSSIBLE")
                        i+=1
                        bre=1
    print(colors)
    sum+=(colors["blue"]*colors["green"]*colors["red"])


print(sum)