
import datetime
'''
 Policy Value calculator for fictional insurance company
 
''' 

class Maturity_value():
    def __init__(self):
        self.Policy_number=''
        self.Policy_start_date=''
        self.Premium=0
        self.Membership=''
        self.Discret_bounus=0
        self.uplift_percentage=0
        self.Policy_type=''
        self.Uplift_value=''
        self.Pol_strt_date_in=''
        self.year=0
        self.month=0
        self.day=0
        self.Maangement_fee=0
        
    def get_input(self):
        self.Policy_number=input('Enter policy number: ')
        self.Pol_strt_date_in=input('Enter policy start date: ')
        self.Premium=int(input('Enter policy premium value: '))
        self.Membership=input('Enter Membership value (Y/N): ')
        self.Discret_bounus=int(input('Enter Discertionay bonus value: '))
        self.uplift_percentage=float(input('Enter uplift percentage value: '))
        self.Policy_type=self.Policy_number[0]
        self.Uplift_value=(100+ self.uplift_percentage)/100
        self.year=int(self.Pol_strt_date_in[6:10])
        self.month=int(self.Pol_strt_date_in[3:5])        
        self.day=int(self.Pol_strt_date_in[0:2])           
        self.Policy_start_date=datetime.date(self.year,self.month,self.day)
        
    def get_management_fee(self):
        if self.Policy_type=='A':
            self.Maangement_fee= (3/100)
        elif self.Policy_type=='B':    
            self.Maangement_fee= (5/100)
        elif self.Policy_type=='C':
            self.Maangement_fee=(7/100)
        else:
            print('Invalid policy type:' + self.Policy_type)
        
        
    def get_discretionary_bonus_flag(self):
       
        if self.Policy_type=='A':
            if self.Policy_start_date < datetime.date(1990,1,1):
               self.discret_bonus_flag='Y'
            else:
               self.discret_bonus_flag='N' 
        elif self.Policy_type=='B':
            if self.Membership=='Y' :
               self.discret_bonus_flag='Y'
            else:               
               self.discret_bonus_flag='N'
        elif self.Policy_type=='C':
            if self.Policy_start_date>=datetime.date(1990,1,1) and self.Membership=='Y' :
               self.discret_bonus_flag='Y'
            else:               
               self.discret_bonus_flag='N'  
        else:
            self.discret_bonus_flag='N'
            
    def calculate_maturity_value(self):
#        print(self.discret_bonus_flag)
        if self.discret_bonus_flag=='Y':
#            self.policy_maturity_value=((self.Premium-(self.Premium*(self.Premium/100))+self.Discret_bounus)*self.Uplift_value)
#             print('I am inside the maturity value')
#             print(self.Premium)
#             print(self.Discret_bounus)
#             print(self.Uplift_value)
             
         
             self.policy_maturity_value=((self.Premium-(self.Premium*self.Maangement_fee))+self.Discret_bounus)*self.Uplift_value

        else:
            self.policy_maturity_value=((self.Premium-(self.Premium*self.Maangement_fee)))*self.Uplift_value
 #           print('I am inside else')
           
    def print_output(self):
        print('Policy number: ' + self.Policy_number)
        print(self.policy_maturity_value)
        
        
obj=Maturity_value() 
obj.get_input()
obj.get_management_fee()
obj.get_discretionary_bonus_flag()
obj.calculate_maturity_value()
obj.print_output()
                