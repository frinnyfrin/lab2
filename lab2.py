import statistics

def main():
    display_main_menu()
    lst = get_user_input()
    calc_average(lst)
    calc_minmax_temperature(lst)
    find_median(lst)

def display_main_menu():
    print("Enter some numbers separated by commas (eg. 1,2,3,4)")

def get_user_input():
    user = input("Enter a list: ").split(",")
    print (user)
    user = [float(i) for i in user]
    print (user)
    return user    

def calc_average(lst):
    total=sum(lst)
    avg_temp=total/len(lst)
    print("average temperature is:"+str(avg_temp))
    return avg_temp 
def calc_minmax_temperature(num_list):
    max_number= max(num_list)
    min_number = min(num_list)
    mmlist=[min_number,max_number]
    print("Min Temp, Max Temp"+str(mmlist))
    return mmlist

def calc_ascending(lst):
    print("sort temp in ascending order")
    lst.sort()
    print(lst)
    return lst

def find_median(lst):
    lol = calc_ascending(lst)
    median = statistics.median(lol)
    print("the median is " +str(median))
    return median
    

         

if __name__ == "__main__":
    main()