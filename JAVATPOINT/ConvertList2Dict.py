""" Input : ['Name', 'Abhinay', 'age', 25, 'Marks', 90]  
Output : {'Name', 'Abhinay', 'age', 25, 'Marks', 90}  """
Input = ['Name', 'Abhinay', 'age', 25, 'Marks', 90]

def convert_lst_2_dict(nums):
    itr = iter(nums)
    dictionary = dict(zip(itr,itr))
    return dictionary

# list1 = ['x', 1, 'y', 2, 'z', 3] 
list1 = ['Name', 'Abhinay', 'age', 25, 'Marks', 90]   
print(convert_lst_2_dict(list1))  


student = ["James", "Abhinay", "Peter", "Bicky"]  
  
student_dictionary = { stu : "Passed" for stu in student }  
  
print(student_dictionary)  