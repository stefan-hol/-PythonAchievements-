import math

trees               = 333             
shadedTrees         = math.ceil(trees * (2/3))  
sunnyTrees          = trees - shadedTrees         

shadeOutputModifier = 0.80            

sunnyTreeOutput     = 146             
shadedTreeOutput    = sunnyTreeOutput * shadeOutputModifier   

sunnyOutput         = sunnyTreeOutput * sunnyTrees        
shadedOutput        = shadedTreeOutput * shadedTrees            
totalOutput         = sunnyOutput + shadedOutput            

owners              = 4           

eatCount            = totalOutput % owners            
sellableOutput      = totalOutput - eatCount         
cut                 = sellableOutput / owners           
print(cut)

