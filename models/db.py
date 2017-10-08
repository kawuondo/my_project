# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
db = DAL('sqlite://storage.sqlite')
from gluon.tools import *
from plugin_ckeditor import CKEditor

"""
db = DAL(settings.db_uri)
if settings.db_uri.startswith('gae'):
    session.connect(request, response, db = db)
"""

auth = Auth(db)
auth.define_tables()
crud = Crud(db)
ckeditor = CKEditor(db)

mail = Mail()   #mailer
auth = Auth(db) #authentication/authorization
crud = Crud(db)  #for CRUD helpers using auth
service = Service()  #for json, xml, jsonrpc, xmlrpc, amfrpc
plugins = PluginManager()

db.define_table('page',
    Field('title', length=100),
    Field('body', 'text', widget=ckeditor.widget),
    Field('area'),
#   Field('country'),
    Field('category'),
    Field('language'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(title)s')


db.define_table('post',
    Field('page_id', 'reference page'),
    Field('body', 'text'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id))

db.define_table('category',
    Field('name' ,notnull=True, unique=True),
    format='%(name)s')

db.define_table('language',
    Field('name' ,notnull=True, unique=True),
    format='%(name)s')

auth.settings.extra_fields['auth_user'] = [
    Field('address','text')
]

db.page.title.requires = [
    IS_NOT_EMPTY(),
    IS_NOT_IN_DB(db, 'page.title'),
]

db.page.body.requires = [
    IS_NOT_EMPTY()
]

db.page.category.requires = [
    IS_NOT_EMPTY(),
    IS_IN_DB(db, 'category.name'),
]

db.page.language.requires = [
    IS_NOT_EMPTY(),
    IS_IN_DB(db, 'language.name'),
]

db.page.created_by.readable = db.page.created_by.writable = False
db.page.created_on.readable = db.page.created_on.writable = False

db.post.body.requires = IS_NOT_EMPTY()
db.post.page_id.readable = db.post.page_id.writable = False
db.post.created_by.readable = db.post.created_by.writable = False
db.post.created_on.readable = db.post.created_on.writable = False























# enable generic views for all actions for testing purpose
response.generic_patterns = ['*']
mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login
auth.settings.hmac_key = settings.security_key


# enable generic views for all actions for testing purpose
response.generic_patterns = ['*']
mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login
auth.settings.hmac_key = settings.security_key

# add any extra fields you may want to add to auth_user
auth.settings.extra_fields['auth_user'] = []

# user username as well as email
auth.define_tables(migrate=settings.migrate,username=True)
auth.settings.mailer = mail
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False

auth.messages.verify_email = 'Click on the link http://' \
    + request.env.http_host + URL('default','user',args=['verify_email']) \
    + '/%(key)s to verify your email'

auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://' \
    + request.env.http_host + URL('default','user',
    args=['reset_password']) \
    + '/%(key)s to reset your password'

if settings.login_method=='janrain':
    from gluon.contrib.login_methods.rpx_account import RPXAccount
    auth.settings.actions_disabled=['register', 'change_password',
        'request_reset_password']
    auth.settings.login_form = RPXAccount(request,
        api_key = settings.login_config.split(':')[-1],
        domain = settings.login_config.split(':')[0],
        url = "http://%s/%s/default/user/login" % (request.env.http_host, request.application))
