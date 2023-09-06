#import os 
#print(__file__)
#print(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR=os.path.dirname(os.path.abspath(__file__))
#print(BASE_DIR)
#TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
#print(TEMPLATE_DIR)


from faker import Faker
fake=Faker()
print('Name:',fake.name())

