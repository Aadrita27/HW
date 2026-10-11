print('Daily Activity Planner')

hw=(int(input(' How much minutes do u do your hw?')))

if hw>60:
    print('LOOOONG HW SESSION,START YOUR HW.')
else:
    print('U CAN DO IT,FINISH HW QUICKLY')

freetime=input('is there free time after hw?')
if freetime==True:
    print('Do whtever u want to.')
else:
    print('Nevermind! u will get free time tomorrow,probably')