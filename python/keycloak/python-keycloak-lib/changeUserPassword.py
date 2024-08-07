# update a user's password to what is passed in
# fix formatting and return JSON
# to run:  python3 changeUserPassword.py https://keycloak.mycompany.com/auth/ openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH user.name newpassword

import sys
import json
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        realm_name=sys.argv[2],
                        client_id=sys.argv[3],
                        client_secret_key=sys.argv[4],
                        verify=True)

keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

user_id_keycloak = keycloak_admin.get_user_id(sys.argv[5])

if user_id_keycloak is None:
    print("User Id was not found for that Username\n")
else:
    response = keycloak_admin.set_user_password(user_id_keycloak, sys.argv[6], temporary=True)
    print("User successfully\n")