with open(r'C:\Users\Nazneen\git\madlibs-generator\story.txt', "r") as file:
    # content = file.read()
    # print(content)
   collection=[]    


   for line in file.readlines():
          words=line.split()
          for word in words:
             if word.startswith('<'):
                collection.append(word)
   print(collection)
         

   
    
    




        


    
