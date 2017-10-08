@auth.requires_login()
def create():
    form = crud.create(db.page,  next = URL(r=request, f='index'))
    return dict(form=form)


def index():
    """ this controller returns a dictionary rendered by the view
    it lists all wiki pages
    >>> index().has_key('pages')
    True
    """
    pages = db().select(
        db.page.id,
        db.page.title,
        db.page.body,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=~db.page.created_on
    )

    return dict(pages=pages)

def profile():
    """ this controller returns a dictionary rendered by the view
    it lists all wiki pages
    >>> index().has_key('pages')
    True
    """
    pages = db(db.page.created_by==auth.user_id).select(
        db.page.id,
        db.page.title,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=db.page.created_on
    )
    return dict(pages=pages)

def show():
    """shows a wiki page"""
    this_page = db.page(request.args(0,cast=int)) or redirect(URL('index'))
    db.post.page_id.default = this_page.id
    form = SQLFORM(db.post).process(formname='post_comment') if auth.user else None
    pagecomments = db(db.post.page_id==this_page.id).select()
    return dict(page=this_page, comments=pagecomments, form=form)

@auth.requires_login()
def edit():
    """edit an existing wiki page"""
    this_page = db.page(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.page, this_page).process(
    next = URL('show',args=request.args))
    return dict(form=form)
#########################################################################################################################################
def pages_by_category():
    category = db.category(request.args(0)) or redirect(URL('index'))
    pages = db(db.page.category==category.name).select(
        db.page.id,
        db.page.title,
        db.page.created_by,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=~db.page.created_on, limitby=(0, 25))
    return locals()
#----------------------------------------------------------------------------------------------------------------------------------------
"""
def pages_by_country():
    country = db.country(request.args(0)) redirect(URL('index'))
    pages = db(db.page.country==country.id).select(
        db.page.id,
        db.page.title,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=~db.page.created_on, limitby=(0, 25))
    return locals()
"""
#----------------------------------------------------------------------------------------------------------------------------------------
def pages_by_language():
    language = db.language(request.args(0)) or redirect(URL('index'))
    pages = db(db.page.language==language.name).select(
        db.page.id,
        db.page.title,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=~db.page.created_on, limitby=(0, 25))
    return locals()
########################################################################################################################################
def pages_by_this_user():
    this_user = db.auth_user(request.args(0)) or redirect(URL('index'))
    pages = db(db.page.created_by==this_user.id).select(
        db.page.id,
        db.page.title,
        db.page.category,
        db.page.language,
        db.page.created_on,
        orderby=~db.page.created_on, limitby=(0, 25))
    return locals()
########################################################################################################################################


def categories():
    categories = db(db.category).select(db.category.name, orderby=db.category.name)
    return locals()
#----------------------------------------------------------------------------------------------------------------------------------------
def languages():
    languages = db(db.language).select(db.category.name, orderby=db.language.name)
    return locals()
#----------------------------------------------------------------------------------------------------------------------------------------
"""
def countries():
    countries = db(db.country).select(orderby=db.country.name)
    return locals()
"""
#########################################################################################################################################
@auth.requires_membership('manager')
def category_create():
    form = crud.create(db.category, next='categories')
    return locals()
#----------------------------------------------------------------------------------------------------------------------------------------
"""
@auth.requires_membership('manager')
def country_create():
    form = crud.create(db.country, next='countries')
    return locals()
"""
#----------------------------------------------------------------------------------------------------------------------------------------
@auth.requires_membership('manager')
def language_create():
    form = crud.create(db.language, next='languages')
    return locals()
#########################################################################################################################################
@auth.requires_membership('manager')
def category_edit():
    category = db.category(request.args(0)) or redirect(URL('categories'))
    form = crud.update(db.category, category, next='categories')
    return locals()
#----------------------------------------------------------------------------------------------------------------------------------------
"""
@auth.requires_membership('manager')
def country_edit():
    country = db.country(request.args(0)) or redirect(URL('country'))
    form = crud.update(db.country, country, next='country')
    return locals()
"""
#----------------------------------------------------------------------------------------------------------------------------------------
@auth.requires_membership('manager')
def language_edit():
    language = db.language(request.args(0)) or redirect(URL('language'))
    form = crud.update(db.language, language, next='language')
    return locals()

#########################################################################################################################################

def user():
    return dict(form=auth())

def download():
    """allows downloading of documents"""
    return response.download(request, db)

def search():
    """an ajax wiki search page"""
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
            _onkeyup="ajax('callback', ['keyword'], 'target');")),
            target_div=DIV(_id='target'))

def callback():
    """an ajax callback that returns a <ul> of links to wiki pages"""
    query = db.page.title.contains(request.vars.keyword)
    pages = db(query).select(orderby=db.page.title)
    links = [A(p.title, _href=URL('show',args=p.id)) for p in pages]
    return UL(*links)

def news():
    """generates rss feed form the wiki pages"""
    response.generic_patterns = ['.rss']
    pages = db().select(db.page.ALL, orderby=db.page.title)
    return dict(
        title = 'mywiki rss feed',
        link = 'http://127.0.0.1:8000/mywiki/default/index',
        description = 'mywiki news',
        created_on = request.now,
        items = [
            dict(title = row.title,
                link = URL('show', args=row.id),
                description = MARKMIN(row.body).xml(),
                created_on = row.created_on
                ) for row in pages])


service = Service()

@service.xmlrpc
def find_by(keyword):
    """finds pages that contain keyword for XML-RPC"""
    return db(db.page.title.contains(keyword)).select().as_list()

def call():
    """exposes all registered services, including XML-RPC"""
    return service()
