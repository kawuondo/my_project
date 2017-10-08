# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

"""
response.logo = A(B('safaritext'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.safaritext.com/",
                  _id="web2py-logo")
"""

response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------


"""
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')
"""


# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------


##########################################################################################################################################
categories = db(db.category).select(orderby=db.category.name,
    cache=(cache.ram, 60))
#-----------------------------------------------------------------------------------------------------------------------------------------
"""
countries = db(db.country).select(orderby=db.country.name,
    cache=(cache.ram, 60))
"""
#-----------------------------------------------------------------------------------------------------------------------------------------
languages = db(db.language).select(orderby=db.language.name,
    cache=(cache.ram, 60))
##########################################################################################################################################

response.menu = [
    ('Recent Pages', URL()==URL('default', 'index'), URL('default', 'index'),[]),
    ('By Category', False, None,
        [
             (c.name, False, URL('default', 'pages_by_category', args=c.id)) for c in categories
        ],
    ),

#    ('By Country', False, None,
#       [
#            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in countries
#       ]
#    )

    ('Create', URL()==URL('default', 'create'), URL('default', 'create'),[]),
    ('Search', URL()==URL('default', 'search'), URL('default', 'search'),[]),
]

#########################################################################################################################################
a_categories = db(db.category.name.like('a%')).select()
b_categories = db(db.category.name.like('b%')).select()
c_categories = db(db.category.name.like('c%')).select()
d_categories = db(db.category.name.like('d%')).select()
e_categories = db(db.category.name.like('e%')).select()
f_categories = db(db.category.name.like('f%')).select()
g_categories = db(db.category.name.like('g%')).select()
h_categories = db(db.category.name.like('h%')).select()
i_categories = db(db.category.name.like('i%')).select()
j_categories = db(db.category.name.like('j%')).select()
k_categories = db(db.category.name.like('k%')).select()
l_categories = db(db.category.name.like('l%')).select()
m_categories = db(db.category.name.like('m%')).select()
n_categories = db(db.category.name.like('n%')).select()
o_categories = db(db.category.name.like('o%')).select()
p_categories = db(db.category.name.like('p%')).select()
q_categories = db(db.category.name.like('q%')).select()
r_categories = db(db.category.name.like('r%')).select()
s_categories = db(db.category.name.like('s%')).select()
t_categories = db(db.category.name.like('t%')).select()
u_categories = db(db.category.name.like('u%')).select()
v_categories = db(db.category.name.like('v%')).select()
w_categories = db(db.category.name.like('w%')).select()
x_categories = db(db.category.name.like('x%')).select()
y_categories = db(db.category.name.like('y%')).select()
z_categories = db(db.category.name.like('z%')).select()


#########################################################################################################################################

category_bar = [
    (T('A'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in a_categories
        ]),
    (T('B'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in b_categories
        ]),
    (T('C'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in c_categories
        ]),
    (T('D'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in d_categories
        ]),
    (T('E'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in e_categories
        ]),
    (T('F'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in f_categories
        ]),
    (T('G'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in g_categories
        ]),
    (T('H'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in h_categories
        ]),
    (T('I'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in i_categories
        ]),
    (T('J'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in j_categories
        ]),
    (T('K'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in k_categories
        ]),
    (T('L'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in l_categories
        ]),
    (T('M'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in m_categories
        ]),
    (T('N'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in n_categories
        ]),
    (T('O'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in o_categories
        ]),
    (T('P'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in p_categories
        ]),
    (T('Q'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in q_categories
        ]),
    (T('R'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in r_categories
        ]),
    (T('S'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in s_categories
        ]),
    (T('T'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in t_categories
        ]),
    (T('U'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in u_categories
        ]),
    (T('V'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in v_categories
        ]),
    (T('W'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in w_categories
        ]),
    (T('X'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in x_categories
        ]),
    (T('Y'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in y_categories
        ]),
     (T('Z'), False, URL('default', 'index'), [
            (c.name, False, URL('default', 'pages_by_language', args=c.id)) for c in z_categories
        ]),
]

#########################################################################################################################################

#########################################################################################################################################
a_languages = db(db.language.name.like('A%')).select()
b_languages = db(db.language.name.like('B%')).select()
c_languages = db(db.language.name.like('C%')).select()
d_languages = db(db.language.name.like('D%')).select()
e_languages = db(db.language.name.like('E%')).select()
f_languages = db(db.language.name.like('F%')).select()
g_languages = db(db.language.name.like('G%')).select()
h_languages = db(db.language.name.like('H%')).select()
i_languages = db(db.language.name.like('I%')).select()
j_languages = db(db.language.name.like('J%')).select()
k_languages = db(db.language.name.like('K%')).select()
l_languages = db(db.language.name.like('L%')).select()
m_languages = db(db.language.name.like('M%')).select()
n_languages = db(db.language.name.like('N%')).select()
o_languages = db(db.language.name.like('O%')).select()
p_languages = db(db.language.name.like('P%')).select()
q_languages = db(db.language.name.like('Q%')).select()
r_languages = db(db.language.name.like('R%')).select()
s_languages = db(db.language.name.like('S%')).select()
t_languages = db(db.language.name.like('T%')).select()
u_languages = db(db.language.name.like('U%')).select()
v_languages = db(db.language.name.like('V%')).select()
w_languages = db(db.language.name.like('W%')).select()
x_languages = db(db.language.name.like('X%')).select()
y_languages = db(db.language.name.like('Y%')).select()
z_languages = db(db.language.name.like('Z%')).select()

#########################################################################################################################################

language_bar = [
    (T('A'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in a_languages
        ]),
    (T('B'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in b_languages
        ]),
    (T('C'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in c_languages
        ]),
    (T('D'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in d_languages
        ]),
    (T('E'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in e_languages
        ]),
    (T('F'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in f_languages
        ]),
    (T('G'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in g_languages
        ]),
    (T('H'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in h_languages
        ]),
    (T('I'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in i_languages
        ]),
    (T('J'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in j_languages
        ]),
    (T('K'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in k_languages
        ]),
    (T('L'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in l_languages
        ]),
    (T('M'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in m_languages
        ]),
    (T('N'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in n_languages
        ]),
    (T('O'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in o_languages
        ]),
    (T('P'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in p_languages
        ]),
    (T('Q'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in q_languages
        ]),
    (T('R'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in r_languages
        ]),
    (T('S'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in s_languages
        ]),
    (T('T'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in t_languages
        ]),
    (T('U'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in u_languages
        ]),
    (T('V'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in v_languages
        ]),
    (T('W'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in w_languages
        ]),
    (T('X'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in x_languages
        ]),
    (T('Y'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in y_languages
        ]),
     (T('Z'), False, URL('default', 'index'), [
            (la.name, False, URL('default', 'pages_by_language', args=la.id)) for la in z_languages
        ]),
]

#########################################################################################################################################






DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [

    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
