with open(r'madlibs-generator\story.txt', "r") as file:
   story= file.read()
   collection=[]
  


   words=story.split()
   for word in words:
             if word.startswith('<'):
                collection.append(word)
   
   new=[]
   for i in range(len(collection)):
           new_input=input(f"Enter a word for {collection[i]}:")
           new.append(new_input)
   
   
   for i in range(len(collection)):
         story=story.replace(collection[i],new[i])
         
with open(r'madlibs-generator\story.txt','w') as file:
          file.write(story)
with open(r'madlibs-generator\story.txt', 'r') as file:
    updated_story = file.read()
   
    print(updated_story)
