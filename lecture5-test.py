import module

a = '123'
module.func(a)
###
a = '123'
f1 = module.func
f1(a)
###
from module import func
a = '123'
func(a)
### импортируем все 
from module import *

a = '123'
func(a)
### импортируем объект и переименовываем его
from module import func as f1

a = '123'
f1(a)
### 
import sys
#sys.path.append("some/path")
print(dir(sys))



