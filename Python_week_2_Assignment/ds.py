my_list = [];
my_list.append(10);
my_list.append(20);
my_list.append(30);
my_list.append(40);

print(my_list);
my_list.insert(1, 15);
#The line of code below is another list that should be joined with mylist, The extend method is suitable since it joins two list together.
another_list = [50, 60, 70];
#extend method to join two lists together
my_list.extend(another_list);
#print(my_list);
#Pop method is used to remove the last element in an array and shift the first element.
my_list.pop();
#print(my_list);
#sort the array one can basically use the built in method sort
#just added this to test the sort method my_list.insert(0, 2);
my_list.sort();
print(my_list);
#find and print the index of the value 30 in my_list;
def findThirty(nums):
    for i in range(len(nums)):
        if nums[i] == 30:
            return i;
    return 0;

print(findThirty(my_list));


