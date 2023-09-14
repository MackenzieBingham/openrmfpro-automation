# List all users in JSON by the realm you pass in
# to run:  python3 listRolesByRealm.py https://keycloak.mycompany.com/auth/ admin 1wsx2wsx3edc4rfv openrmfpro python-keycloak 8675867tyjhgjghuy5675&JKHLKJH

import sys
import json
from keycloak import KeycloakAdmin
from keycloak import KeycloakOpenIDConnection

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=sys.argv[1],
                        username=sys.argv[2],
                        password=sys.argv[3],
                        realm_name=sys.argv[4],
                        client_id=sys.argv[5],
                        client_secret_key=sys.argv[6],
                        verify=True)

print("debug: getting the admin connection set")
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)

realm_roles = keycloak_admin.get_realm_roles()

# Get Realms
realm_roles = str(realm_roles).replace("'", '"')
realm_roles = str(realm_roles).replace("True", 'true')
realm_roles = str(realm_roles).replace("False", 'false')
json_object = json.loads(realm_roles)
print(json.dumps(json_object, indent=1))