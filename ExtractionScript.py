import subprocess 

profile_list_str=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profile_list=list()
password_list=list()
for i in profile_list_str:
    if 'All User Profile' in i:
        z=i.split(': ')
        profile_list.append(z.pop()[:-1])
for i in profile_list:
    retunData=subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    c=True
    for j in retunData:
        if 'Key Content' in j:
            z=j.split(': ')
            password_list.append(z.pop()[:-1])
            c= False
    if c==True:
        password_list.append('No password applied, Open network')
for i,j in zip(profile_list,password_list):
    print('wifi identity:'+i+'\npassword:'+j+'\n')
    
while True:
    pass