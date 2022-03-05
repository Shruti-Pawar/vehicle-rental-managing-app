
print('\t\t\tWELCOME')
print('PLEASE LOGIN')
email=input('Email : ')
password=input('Password : ')
if email=='shrutiepawar@gmail.com' and password=='app@123!':
    print('Welcome to Vehicle Rental Application ')
else:
    print('Please check the email id and password you have entered. ')
class customer:
    def __init__(self,name,Phone_number,Email):
        self.name=name
        self.Phone_number=Phone_number
        self.Email=Email
print('\tMenu')
print('1.Add customer\n2.Add Rental Bookings\n3.View customer list\n4.view rental bookings\n5.view inventory')
menu=input('Select any option : ')
match menu:
    # case '1':
    #     print('Add Customer  : ')
    #     cust_name=input('Enter name : ')
    #     Phone_number=input('enter Phone Number : ')
    #     print('Congratulations !!! you have been selected as a prime customer.')
    case '2':
        Availability_of_Vehicles={'bikes':2, 'cycles':3, 'car':1, 'boat':2}
        print('Availability_of_Vehicles are - ',Availability_of_Vehicles)
        print('\n1.bikes\t\t2.cycles\n3.car\t\t4.boat\n')


        option = input('Select the option of vehicles for rent : ')
        match option:

            case '1':
                print('You have choosed bike for rent.')
                START_DATE = input('Enter the START DATE and TIME(dd/mm/yyyy hh:mm) : ')
                END_DATE = input('Enter the END DATE and TIME(dd/mm/yyyy hh:mm) : ')
                quantity = eval(input('Enter the quantity : '))
                if quantity >2:
                    print('''Out of stock or invalid, Only 2 bikes are available for the selected date.
                                        \n try choosing another date or another type of vehicle''')


            case '2':
                print('You have choosed cycle for rent.')
                START_DATE = input('Enter the START DATE and TIME(dd/mm/yyyy hh:mm) : ')
                END_DATE = input('Enter the END DATE and TIME(dd/mm/yyyy hh:mm) : ')
                quantity = eval(input('Enter the quantity : '))
                if quantity >3:
                    print('''Out of stock, Only 3 cycles are available for the selected date.
                    \n try choosing another date or another type of vehicle''')
                elif quantity<3 and quantity>0:
                    print('Reserve your ride\n ')


            case '3':
                print('You have choosed Car for rent.')
                START_DATE = input('Enter the START DATE and TIME(dd/mm/yyyy hh:mm) : ')
                END_DATE = input('Enter the END DATE and TIME(dd/mm/yyyy hh:mm) : ')
                quantity = eval(input('Enter the quantity : '))
                if quantity > 1:
                    print('''Out of stock, Only 1 car is available for the selected date.
                                        \n try choosing another date or another type of vehicle''')

            case '4':
                print('You have choosed Boats for rent.')
                START_DATE = input('Enter the START DATE and TIME(dd/mm/yyyy hh:mm) : ')
                END_DATE = input('Enter the END DATE and TIME(dd/mm/yyyy hh:mm) : ')
                quantity = eval(input('Enter the quantity : '))
                if quantity > 2:
                    print('''Out of stock, Only 2 boats are available for the selected date.
                                        \n try choosing another date or another type of vehicle''')
    case '3':
        print('Customer list : \n1.Shruti.\n2.Preeti.')
    case '4':
        print('\n\tView Rental Bookings')
    case '5':
        print('View Inventory')

# name=input('Enter Your Name : ')
# Phone_number=input('Enter Phone Number : ')
# Email=input('Enter Email id : ')
# a=customer(name)
# b=customer(Phone_number)
# c=customer(Email)



# class customer:
#     def add_customer(self):
#         for i in range(n):
# class rental(customer):
#     def add_rental(self):
#     def see_rental(self)
#     def inventory_veh_availability(self):
# hr=input('Enter in hours : ')
# bike_rental=350
# print('Cost in Rupees : ',bike_rental*hr)
# cycle_rental=100
# print('Cost in Rupees : ',cycle_rental*hr)
# car_rental=750
# print('Cost in Rupees : ',car_rental*hr)
# boat_rental=1250
# print('Cost in Rupees : ',boat_rental*hr)

