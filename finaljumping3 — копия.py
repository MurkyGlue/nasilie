import random
import os


x = 1
y = 1
xm = 20
ym = 20
x2 = 6
y2 = 5
s = 5
sc = 0
x3 = x

obj1X = x
obj1Y = y
obj2X = x2
obj2Y = y2
obj3X = x4 = random.randint(1,xm)
obj3Y = y4 = random.randint(4,ym)
fill = '. '
obj1 = '@ '
obj2 = '$ '
obj3 = '# '
check = False

def drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y):
  
            
    
    
    
    minY = min(obj1Y, obj2Y, obj3Y)
    maxY = max(obj1Y, obj2Y, obj3Y)
    if minY == obj1Y:
        if maxY == obj2Y: midY = obj3Y
        elif maxY == obj3Y: midY = obj2Y
    if minY == obj2Y:
        if maxY == obj1Y: midY = obj3Y
        elif maxY == obj3Y: midY = obj1Y            
    if minY == obj3Y:
        if maxY == obj2Y: midY = obj1Y
        elif maxY == obj1Y: midY = obj2Y
    
    for i in range(minY-1):
        print(fill*xm)
    if minY == obj1Y == obj2Y == obj3Y:
        if obj1X<obj2X<obj3X:
            print(fill*(obj1X-1) + obj1 + fill*(obj2X-obj1X-1) + obj2 + fill*(obj3X-obj2X-1) + obj3 + fill*(xm-obj3X))
        elif obj1X<obj3X<obj2X:
            print(fill*(obj1X-1) + obj1 + fill*(obj3X-obj1X-1) + obj3 + fill*(obj2X-obj3X-1) + obj2 + fill*(xm-obj2X))
        elif obj2X<obj1X<obj3X:
            print(fill*(obj2X-1) + obj2 + fill*(obj1X-obj2X-1) + obj1 + fill*(obj3X-obj1X-1) + obj3 + fill*(xm-obj3X))
        elif obj2X<obj3X<obj1X:
            print(fill*(obj2X-1) + obj2 + fill*(obj3X-obj2X-1) + obj3 + fill*(obj1X-obj3X-1) + obj1 + fill*(xm-obj1X))
        elif obj3X<obj1X<obj2X:
            print(fill*(obj3X-1) + obj3 + fill*(obj1X-obj3X-1) + obj1 + fill*(obj2X-obj1X-1) + obj2 + fill*(xm-obj2X))
        elif obj3X<obj2X<obj1X:
            print(fill*(obj3X-1) + obj3 + fill*(obj2X-obj3X-1) + obj2 + fill*(obj1X-obj2X-1) + obj1 + fill*(xm-obj1X))
    elif obj1Y==obj2Y or obj2Y==obj3Y or obj1Y==obj3Y:
        if minY == obj1Y == obj2Y:    
            if obj1X<obj2X:
                print(fill*(obj1X-1) + obj1 + fill*(obj2X-obj1X-1) + obj2 + fill*(xm-obj2X))
            elif obj2X<obj1X:
                print(fill*(obj2X-1) + obj2 + fill*(obj1X-obj2X-1) + obj1 + fill*(xm-obj1X))
        elif minY == obj1Y == obj3Y:
            if obj1X<obj3X:
                print(fill*(obj1X-1) + obj1 + fill*(obj3X-obj1X-1) + obj3 + fill*(xm-obj3X))
            elif obj3X<obj1X:
                print(fill*(obj3X-1) + obj3 + fill*(obj1X-obj3X-1) + obj1 + fill*(xm-obj1X))
        elif minY == obj2Y == obj3Y:
            if obj2X<obj3X:
                print(fill*(obj2X-1) + obj2 + fill*(obj3X-obj2X-1) + obj3 + fill*(xm-obj3X))
            elif obj3X<obj2X:   
                print(fill*(obj3X-1) + obj3 + fill*(obj2X-obj3X-1) + obj2 + fill*(xm-obj2X))
        if  maxY == obj1Y == obj2Y:
            print(fill*(obj3X-1)+ obj3 + fill*(xm-obj3X)) 
        elif  maxY == obj1Y == obj3Y:
            print(fill*(obj2X-1)+ obj2 + fill*(xm-obj2X))     
        elif  maxY == obj3Y == obj2Y:
            print(fill*(obj1X-1)+ obj1 + fill*(xm-obj1X))
              
        for i in range(maxY-minY-1):
            print(fill*xm) 
            
        if minY == obj1Y == obj2Y:    
            print(fill*(obj3X-1) + obj3 + fill*(xm-obj3X))
        elif minY == obj1Y == obj3Y:
            print(fill*(obj2X-1) + obj2 + fill*(xm-obj2X))
        elif minY == obj2Y == obj3Y:
            print(fill*(obj1X-1) + obj1 + fill*(xm-obj1X))
        if maxY == obj1Y == obj2Y:    
            if obj1X<obj2X:
                print(fill*(obj1X-1) + obj1 + fill*(obj2X-obj1X-1) + obj2 + fill*(xm-obj2X))
            elif obj2X<obj1X:
                print(fill*(obj2X-1) + obj2 + fill*(obj1X-obj2X-1) + obj1 + fill*(xm-obj1X))
        elif maxY == obj1Y == obj3Y:
            if obj1X<obj3X:
                print(fill*(obj1X-1) + obj1 + fill*(obj3X-obj1X-1) + obj3 + fill*(xm-obj3X))
            elif obj3X<obj1X:
                print(fill*(obj3X-1) + obj3 + fill*(obj1X-obj3X-1) + obj1 + fill*(xm-obj1X))
        elif maxY == obj2Y == obj3Y:
            if obj2X<obj3X:
                print(fill*(obj2X-1) + obj2 + fill*(obj3X-obj2X-1) + obj3 + fill*(xm-obj3X))
            elif obj3X<obj2X:   
                print(fill*(obj3X-1) + obj3 + fill*(obj2X-obj3X-1) + obj2 + fill*(xm-obj2X))
    elif obj1Y != obj2Y != obj3Y:
        if minY == obj1Y:
            print(fill*(obj1X-1) + obj1 + fill*(xm-obj1X)) 
        elif minY == obj2Y:
            print(fill*(obj2X-1) + obj2 + fill*(xm-obj2X)) 
        elif minY == obj3Y:
            print(fill*(obj3X-1) + obj3 + fill*(xm-obj3X))  
        for i in range(midY-minY-1):
            print(fill*xm)  
        if midY == obj1Y:
            print(fill*(obj1X-1) + obj1 + fill*(xm-obj1X)) 
        elif midY == obj2Y:
            print(fill*(obj2X-1) + obj2 + fill*(xm-obj2X)) 
        elif midY == obj3Y:
            print(fill*(obj3X-1) + obj3 + fill*(xm-obj3X)) 
        for i in range(maxY-midY-1):
            print(fill*xm) 
        if maxY == obj1Y:
            print(fill*(obj1X-1) + obj1 + fill*(xm-obj1X)) 
        elif maxY == obj2Y:
            print(fill*(obj2X-1) + obj2 + fill*(xm-obj2X)) 
        elif maxY == obj3Y:
            print(fill*(obj3X-1) + obj3 + fill*(xm-obj3X))
    for i in range(ym-maxY):
        print(fill*xm)           
            
             


while True:
	
	
    
	i = input()
    
	if i == "dd":
		os.system('cls')
		x += 1
		s += 1
		if x2 == x and y2 == y:
			x2 = random.randint(1, xm)
			y2 = random.randint(4, ym)
			check == True
			if y2 == 14 or y2 == 15:
				y2 = random.randint(4, ym)
			sc += 1
            
		if x > xm:
			x = xm
		elif y > ym:
			y = ym
		elif x < 1:
			x = 1
		elif y < 1:
			y = 1
			
		if check:
			check = False
			x4 = random.randint(1, xm)
			y4 = random.randint(4, ym)
			if y4 == 14 or y4 == 15:
				y4 = random.randint(4, ym)
			
		obj1X = x
		obj1Y = y
		obj2X = x2
		obj2Y = y2
		obj3X = x4
		obj3Y = y4  
                
		drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y)
		print('score:', sc)
		
	elif i == "aa":
		os.system('cls')
		x -= 1 
		s -= 1
        
		if x2 == x and y2 == y:
			x2 = random.randint(1, xm)
			y2 = random.randint(4, ym)
			check = True
			if y2 == 14 or y2 == 15:
				y2 = random.randint(4, ym)
			sc += 1
			
		if x > xm:
			x = xm
		elif y > ym:
			y = ym
		elif x < 1:
			x = 1
		elif y < 1:
			y = 1
			
		if check:
			check = False
			x4 = random.randint(1, xm)
			y4 = random.randint(4, ym)
			if y4 == 14 or y4 == 15:
				y4 = random.randint(4, ym)
			
		obj1X = x
		obj1Y = y
		obj2X = x2
		obj2Y = y2
		obj3X = x4
		obj3Y = y4 
		        
		drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y) 
		print('score:', sc)   
    
	elif i == "d":
		s += 8
		for x3 in range(-4, 5):
			os.system('cls')
            
			y = x3**2 + 4
			x = s + x3
			for i in range(ym-x3**2+1):
				if x2 == x and y2 == y:
					x2 = random.randint(1, xm)
					y2 = random.randint(4, ym)
					check = True
					if y2 == 14 or y2 == 15:
						y2 = random.randint(4, ym)
					sc += 1
				y -= 1   
			y = x3**2 +4
            
			if x > xm:
				x = xm
			elif y > ym:
				y = ym
			elif x < 1:
				x = 1
			elif y < 1:
				y = 1
				
			if check:
				check = False
				x4 = random.randint(1, xm)
				y4 = random.randint(4, ym)
				if y4 == 14 or y4 == 15:
					y4 = random.randint(4, ym)	
				
			obj1X = x
			obj1Y = y
			obj2X = x2
			obj2Y = y2
			obj3X = x4
			obj3Y = y4
		   
			drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y)
			
		print('score:', sc)  
	elif i == "a":
        
		for x3 in range(-4, 5):
			os.system('cls')
            
			y = x3**2 + 4
			x = s - x3
            
			for i in range(ym-x3**2+1):
				if x2 == x and y2 == y:
					x2 = random.randint(1, xm)
					y2 = random.randint(4, ym)
					if y2 == 14 or y2 == 15:
						y2 = random.randint(4, ym)
					sc += 1
				y -= 1    
			y = x3**2 +4 
                
			if x > xm:
				x = xm
			elif y > ym:
				y = ym
			elif x < 1:
				x = 1
			elif y < 1:
				y = 1
				
			if check:
				check = False
				x4 = random.randint(1, xm)
				y4 = random.randint(4, ym)
				if y4 == 14 or y4 == 15:
					y4 = random.randint(4, ym)
			
			obj1X = x
			obj1Y = y
			obj2X = x2
			obj2Y = y2
			obj3X = x4
			obj3Y = y4     
			drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y)
			
		print('score:', sc)
			
		s -= 8    
               
	elif i == "w":
		
		for x3 in range(-4, 5):
			os.system('cls')
            
			y = x3**2 + 4
            
			for i in range(ym-x3**2+1):
				if x2 == x and y2 == y:
					x2 = random.randint(1, xm)
					y2 = random.randint(4, ym)
					check = True
					if y2 == 14 or y2 == 15:
						y2 = random.randint(4, ym)
					sc += 1
				y -= 1
            
			y = x3**2 + 4
			
			if check:
				check = False
				x4 = random.randint(1, xm)
				y4 = random.randint(4, ym)
				if y4 == 14 or y4 == 15:
					y4 = random.randint(4, ym)
			
			obj1X = x
			obj1Y = y
			obj2X = x2
			obj2Y = y2
			obj3X = x4
			obj3Y = y4      
			drawing(xm, ym, fill, obj1, obj2, obj3, obj1X, obj1Y, obj2X, obj2Y, obj3X, obj3Y)
			
		print('score:', sc)
            
    
    
