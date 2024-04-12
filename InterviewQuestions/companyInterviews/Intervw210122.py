# class Article(models.Modle): 1
#     name = models.CharField(max_length=100)


# class Reporter(models.Model):
#     article = models.Foreignkey(Article,on_delete=models.CASCADE)
#     name

# user_id = 1
# queryset = Article.objects.get(id=1)

# queryset.reporter.name


# AAABBCCC => 3A2B3C

# string_input = "AAABBCCC"

# result = {}

# string_result = ""

# for val in string_input:
#     if val in result:
#         result[val] += 1
#     else:
#         result[val] = 1

# for key,val in result.items():
#     string_result += (key + str(val))

# print(string_result)



# Given a list of integers , find 2nd largest element
Arr = [ 5, 1, 8, 3, 4 ]

first_max = max(Arr[0],Arr[1])
# print(first_max)
second_max = min(Arr[0],Arr[1])
# print(second_max)

len_arr = len(Arr)

for i in range(2,len_arr):
    if Arr[i] > first_max:
        second_max = first_max
        first_max = Arr[i]

    elif Arr[i] > second_max and Arr[i] != first_max:
        second_max = Arr[i]

print(second_max)













