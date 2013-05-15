import ldapom
from functools import wraps
from flask import request, Response

class BasicLDAPAuth:
    def __init__(self, ldap_uri=False, ldap_basedn, ldap_userfilter):
        self.ldap_basedn = ldap_basedn
        self.ldap_userfilter = ldap_userfilter
        self.ldap_uri = ldap_uri


    def init_ldap(self):
        try:
            self.connection = ldapom.LdapConnection(
                uri=self.ldap_uri,
                base=self.ldap_basedn,
                login='uid=%s,%s' % (request.authorization.username, self.ldap_basedn),
                password=request.authorization.password)

        except Exception, e:
            return False

        return True


    def check_auth(self):
        return self.init_ldap() 

    def authenticate(self):
        return Response(
        'Could not verify your access level for that URL.\n'
        'Please log in with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

    def authorization_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth or not self.check_auth():
                return self.authenticate()
            return f(*args, **kwargs)
        return decorated