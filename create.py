from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant
import logging


logging.basicConfig(filename='example.log',level=logging.DEBUG)

apicUrl = 'https://10.23.248.85'
logging.info('Creating a logging session')
loginSession = LoginSession('https://10.23.248.85', 'admin', 'Cisco!123')
logging.info('Acquiring moDir from session')
moDir = MoDirectory(loginSession)
moDir.login()


logging.info('Login Success')

uniMo = moDir.lookupByDn('uni')

logging.info('Passing in tenant information')
tenant1 = str(raw_input('Enter name of first tenant to be created \n'))
print (tenant1, ': has been created \n')
tenant2 = str(raw_input('Enter name of second tenant to be created \n'))

logging.info('Creation of Tenant')
fvTenantMo = Tenant(uniMo, tenant1)
fvTenantMo = Tenant(uniMo, tenant2)

logging.info('Config request of tenants')
configReq = ConfigRequest()
configReq.addMo(uniMo)
moDir.commit(configReq)

logging.info('Config request complete')
print("Yaay")

logging.info('Logout Success')
moDir.logout()

logging.info('Process Completed')
