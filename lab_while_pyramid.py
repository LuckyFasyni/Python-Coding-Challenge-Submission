#Pyramid
#each lower layer contains one block more than the layer above.
#write a program which reads the number of blocks the builders have, and 
#outputs the height of the pyramid that can be built using these blocks.
#if the builders don't have a sufficient number of blocks and cannot complete the next layer, 
#they finish their work immediately.

blocks = int(input("Enter the number of blocks: "))
layer = 1
height = 0

while blocks >= layer:
    height += 1
    blocks -= layer
    layer += 1
    
print("The height of the pyramid:", height)