# number = input('Enter any network number: ')
# if number in('0803', '0806', '0810', '0813', '0814', '0816', '0903', '0906', '0913', '0916'):
#     print('The number is belongs to MTN')
# elif number in('0915', '0905', '0815', '0811', '0807','0805'):
#     print('The number is belongs to GLO')
# elif number in('0701', '0708', '0802', '0808', '0812', '0901', '0902', '0904', '0907', '0912'):
#     print('The number is belongs to Airtel')
# elif number in('0909', '0908', '0817', '0818', '0809'):
#     print('The number is belongs to 9mobile')
# else:
#     print('This number does not exist in Nigeria')

list_of_mtn_numbers = ['0803', '0806', '0810', '0813', '0814', '0816', '0903', '0906', '0913', '0916']
list_of_glo_numbers = ['0915', '0905', '0815', '0811', '0807','0805']
list_of_airtel_numbers = ['0701', '0708', '0802', '0808', '0812', '0901', '0902', '0904', '0907', '0912']
list_of_9mobile_numbers = ['0909', '0908', '0817', '0818', '0809']

number = input('Enter any network number: ')
if number in list_of_mtn_numbers:
    print('The number is belongs to MTN')
elif number in list_of_glo_numbers:
    print('The number is belongs to GLO')
elif number in list_of_airtel_numbers:
    print('The number is belongs to Airtel')
elif number in list_of_9mobile_numbers:
    print('The number is belongs to 9mobile')
else:
    print('This number does not exist in Nigeria')

