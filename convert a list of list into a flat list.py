list1=[[1,2,3],[4,5,6],[7],[8,9]]
print(list1)
import itertools
flat_list=list(itertools.chain(*list1))
print(flat_list)