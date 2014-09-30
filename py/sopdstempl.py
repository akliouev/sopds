class opdsTemplate():
    def __init__(self, modulepath, charset='utf-8'):
       self.charset=charset
       self.modulepath=modulepath
       self.response_header=('Content-Type','text/xml; charset='+self.charset)
       self.document_header=('<?xml version="1.0" encoding="%(charset)s"?>'
                               '<feed xmlns="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/terms/" xmlns:os="http://a9.com/-/spec/opensearch/1.1/" xmlns:opds="http://opds-spec.org/2010/catalog">'
                               '<id>%%(id)s</id>'
                               '<title>%%(title)s</title>'
                               '<subtitle>%%(subtitle)s</subtitle>'
                               '<updated>%%(updated)s</updated>'
                               '<icon>%%(site_icon)s</icon>'
                               '<author><name>%%(site_author)s</name><uri>%%(site_url)s</uri><email>%%(site_email)s</email></author>'
                               '<link type="application/atom+xml" rel="start" href="%(modulepath)s?id=00"/>'
                               )%{'charset':self.charset,'modulepath':self.modulepath}
       self.document_footer='</feed>'
       self.document_mainmenu_std=('<link href="%(modulepath)s?id=09" rel="search" type="application/opensearchdescription+xml" />'
                               '<link href="%(modulepath)s?searchTerm={searchTerms}" rel="search" type="application/atom+xml" />'
                               '<entry>'
                               '<title>По каталогам</title>'
                               '<content type="text">Каталогов: %%(cat_num)s, книг: %%(book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=01"/>'
                               '<id>id:01</id></entry>'
                               '<entry>'
                               '<title>По авторам</title>'
                               '<content type="text">Авторов: %%(author_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s02"/>'
                               '<id>id:02</id></entry>'
                               '<entry>'
                               '<title>По наименованию</title>'
                               '<content type="text">Книг: %%(book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s03"/>'
                               '<id>id:03</id></entry>'
                               '<entry>'
                               '<title>По Жанрам</title>'
                               '<content type="text">Жанров: %%(genre_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04"/>'
                               '<id>id:04</id></entry>'
                               '<entry>'
                               '<title>По Сериям</title>'
                               '<content type="text">Серий: %%(series_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s06"/>'
                               '<id>id:06</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_mainmenu_new=('<entry>'
                               '<title>Новинки за %%(new_period)s суток</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=05"/>'
                               '<id>id:05</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_mainmenu_shelf=('<entry>'
                               '<title>Книжная полка для %%(user)s</title>'
                               '<content type="text">Книг: %%(shelf_book_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=08"/>'
                               '<id>id:08</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_newmenu=('<entry>'
                               '<title>Все новинки за %%(new_period)s суток</title>'
                               '<content type="text">Новых книг: %%(newbook_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s03&amp;news=1"/>'
                               '<id>id:03:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по авторам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s02&amp;news=1"/>'
                               '<id>id:02:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Жанрам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04&amp;news=1"/>'
                               '<id>id:04:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s06&amp;news=1"/>'
                               '<id>id:06:news</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_authors_submenu=('<entry>'
                               '<title>Книги по сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=31%%(author_id)s"/>'
                               '<id>id:31:authors</id></entry>'
                               '<entry>'
                               '<title>Книги вне серий</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=34%%(author_id)s"/>'
                               '<id>id:32:authors</id></entry>'
                               '<entry>'
                               '<title>Книги по алфавиту</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=33%%(author_id)s"/>'
                               '<id>id:33:authors</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_start='<entry>'
       self.document_entry_finish='</entry>'
       self.document_entry_head=('<title>%(e_title)s</title>'
                               '<updated>%(e_date)s</updated>'
                               '<id>id:%(e_id)s</id>')
       self.document_entry_link_subsection=('<link type="application/atom+xml" rel="alternate" href="%(modulepath)s?id=%%(link_id)s%%(nl)s"/>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="subsection" href="%(modulepath)s?id=%%(link_id)s%%(nl)s"/>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_book_head=''
       self.document_entry_link_book_alternate=('<link type="application/%%(format)s" rel="alternate" href="%(modulepath)s?id=91%%(link_id)s"/>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_link_book=('<link type="application/%%(format)s" href="%(modulepath)s?id=%%(id)s%%(link_id)s" rel="http://opds-spec.org/acquisition" />'
                               )%{'modulepath':self.modulepath}
       self.document_entry_authors=('<author><name>%%(last_name)s %%(first_name)s</name></author>'
                               '<link href="%(modulepath)s?id=22%%(author_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Все книги %%(last_name)s %%(first_name)s" />'
                               )%{'modulepath':self.modulepath}
       self.document_link_authors=self.document_entry_authors
       self.document_entry_doubles=('<link href="%(modulepath)s?id=23%%(book_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Дубликаты книги" />'
                               )%{'modulepath':self.modulepath}
       self.document_entry_genres='<category term="%(genre)s" label="%(genre)s" />'
       self.document_link_genres=self.document_entry_genres
       self.document_entry_series='' 
       self.document_link_series=self.document_entry_series
       self.document_entry_covers=('<link href="%(modulepath)s?id=99%%(book_id)s" rel="http://opds-spec.org/image" type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%%(book_id)s" rel="x-stanza-cover-image" type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%%(book_id)s" rel="http://opds-spec.org/thumbnail"  type="image/jpeg" />'
                               '<link href="%(modulepath)s?id=99%%(book_id)s" rel="x-stanza-cover-image-thumbnail"  type="image/jpeg" />'
                               )%{'modulepath':self.modulepath}
       self.document_entry_content='<content type="text">%(e_content)s</content>'
       self.document_entry_content2_start='<content type="text/html">'
       self.document_entry_content2_title='&lt;b&gt;Название книги:&lt;/b&gt; %(title)s&lt;br/&gt;'
       self.document_entry_content2_authors='&lt;b&gt;Авторы:&lt;/b&gt; %(authors)s&lt;br/&gt;'
       self.document_entry_content2_genres='&lt;b&gt;Жанры:&lt;/b&gt; %(genres)s&lt;br/&gt;'
       self.document_entry_content2_series='&lt;b&gt;Серии:&lt;/b&gt; %(series)s&lt;br/&gt;'
       self.document_entry_content2_filename='&lt;b&gt;Файл:&lt;/b&gt; %(filename)s&lt;br/&gt;'
       self.document_entry_content2_filesize='&lt;b&gt;Размер файла:&lt;/b&gt; %(filesize)sКб.&lt;br/&gt;'
       self.document_entry_content2_docdate='&lt;b&gt;Дата правки:&lt;/b&gt; %(docdate)s&lt;br/&gt;'
       self.document_entry_content2_annotation='&lt;p class=book&gt; %(annotation)s&lt;/p&gt;'
       self.document_entry_content2_finish='</content>'

       self.document_alphabet_menu=('<entry><title>А..Я (РУС)</title><id>alpha:1</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(iid)s&amp;alpha=1%%(nl)s"/></entry>'
                                    '<entry><title>0..9 (Цифры)</title><id>alpha:2</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(iid)s&amp;alpha=2%%(nl)s"/></entry>'
                                    '<entry><title>A..Z (ENG)</title><id>alpha:3</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(iid)s&amp;alpha=3%%(nl)s"/></entry>'
                                    '<entry><title>Другие Символы</title><id>alpha:4</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(iid)s&amp;alpha=4%%(nl)s"/></entry>'
                                    '<entry><title>Показать все</title><id>alpha:5</id><link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(iid)s&amp;alpha=5%%(nl)s"/></entry>'
                                    )%{'modulepath':self.modulepath}

       self.document_page_control_prev=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="prev" title="Previous Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%%(page)s" />'
                               )%{'modulepath':self.modulepath}
       self.document_page_control_next=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="next" title="Next Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%%(page)s" />'
                               )%{'modulepath':self.modulepath}


class webTemplate(opdsTemplate):
    def __init__(self, modulepath, charset='utf-8'):
       self.charset=charset
       self.modulepath=modulepath
       self.response_header=('Content-Type','text/html; charset='+self.charset)
       self.document_style='''
                           <style>
                               body {font-family: Tahoma, Geneva, sans-serif; font-size: 8pt; color: #000; max-width: 840px; margin: 0; padding: 0; }
                               h1 {font-size: 140%%; margin-bottom: 30px; }
                               h2 {font-size: 120%%; }
                               h2 a { color: #000; }
                               a {color: #0F3253;}
                               input, button {vertical-align: middle;border-radius: 2pt;}
                               input {border: 1pt solid #676767;}
                               button {border: 1pt solid #676767; background-color: #EEE; }
                               .page { padding: 0 40px 20px 40px; }
                               .footer {padding-top: 15pt; border-top: 2pt dotted #AAA; margin-top: 20pt; }
                               .navigation_entry {margin-left: 20pt;}
                               .navigation_entry h2 {display: inline-block;margin: 2pt 20pt 6pt -15pt; }
                               .acquisition_entry { width: 100%% }
                               .acq_link { clear: both; width: 100%%; }
                               .acq_cover { float: left; width: 20%%; }
                               .acq_infobook  { float: left; width: 80%%; }
                               .acq_info_container { clear: both; width: 100%%; }
                            </style>
                            '''
       self.document_header=('<html>'
                               '<head>'
                               '<meta charset=%(charset)s>'
                               '<title>%%(subtitle)s</title>'
                               '%(style)s'
                               '</head>'
                               '<body>'
                               '<div class=page>'
                               '<h1>%%(title)s</h1>'
                               )%{'charset':self.charset,'style':self.document_style}
       self.document_footer='</div></body>'
       self.document_mainmenu_std=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=01">По каталогам</a></h2><i>Каталогов: %%(cat_num)s, книг: %%(book_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(alphabet_id)s02">По авторам</a></h2><i>Авторов: %%(author_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(alphabet_id)s03">По наименованию</a></h2><i>Книг: %%(book_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=04">По жанрам</a></h2><i>Жанров: %%(genre_num)s.</i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(alphabet_id)s06">По сериям</a></h2><i>Серий: %%(series_num)s.</i></div>'
                               )%{'modulepath':self.modulepath}
       self.document_mainmenu_new=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=05">Новинки за %%(new_period)s суток.</a></h2><i></i></div>'
                               )%{'modulepath':self.modulepath}
       self.document_mainmenu_shelf=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=08">Книжная полка для %%(user)s.</a></h2><i></i></div>'
                               )%{'modulepath':self.modulepath}
       self.document_newmenu=('<entry>'
                               '<title>Все новинки за %%(new_period)s суток</title>'
                               '<content type="text">Новых книг: %%(newbook_num)s.</content>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s03&amp;news=1"/>'
                               '<id>id:03:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по авторам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s02&amp;news=1"/>'
                               '<id>id:02:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Жанрам</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=04&amp;news=1"/>'
                               '<id>id:04:news</id></entry>'
                               '<entry>'
                               '<title>Новинки по Сериям</title>'
                               '<link type="application/atom+xml;profile=opds-catalog;kind=navigation" href="%(modulepath)s?id=%%(alphabet_id)s06&amp;news=1"/>'
                               '<id>id:06:news</id></entry>'
                               )%{'modulepath':self.modulepath}
       self.document_authors_submenu=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=31%%(author_id)s">Книги по сериям</a></h2><i></i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=34%%(author_id)s">Книги вне серий</a></h2><i></i></div>'
                               '<div class=navigation_entry><h2><a href="%(modulepath)s?id=33%%(author_id)s">Книги по алфавиту</a></h2><i></i></div>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_start='<div class=navigation_entry>'
       self.document_entry_finish='</div>'
       self.document_entry_head=('<!--<title>%(e_title)s</title>'
                               '<updated>%(e_date)s</updated>'
                               '<id>id:%(e_id)s</id>-->')
       self.document_entry_link_subsection=('<h2><a href="%(modulepath)s?id=%%(link_id)s%%(nl)s">%%(e_title)s</a></h2><i></i>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_book_head=('<h2>%(e_title)s</h2> <i>Скачать в формате: </i>')
       self.document_entry_link_book_alternate=''
       self.document_entry_link_book=('<i><a href="%(modulepath)s?id=%%(id)s%%(link_id)s">%%(format)s</a></i>&nbsp;'
                               )%{'modulepath':self.modulepath}
       self.document_entry_authors=('<author><name>%%(last_name)s %%(first_name)s</name></author>'
                               '<link href="%(modulepath)s?id=22%%(author_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Все книги %%(last_name)s %%(first_name)s" />'
                               )%{'modulepath':self.modulepath}
       self.document_link_authors=('<a href="%(modulepath)s?id=22%%(author_id)s">%%(last_name)s %%(first_name)s</a>'
                               )%{'modulepath':self.modulepath}
       self.document_entry_doubles=('<link href="%(modulepath)s?id=23%%(book_id)s" rel="related" type="application/atom+xml;profile=opds-catalog" title="Дубликаты книги" />'
                               )%{'modulepath':self.modulepath}
       self.document_entry_genres=''
       self.document_link_genres=''
       self.document_entry_series=''
       self.document_link_series=''
       self.document_entry_covers=('<br><img src="%(modulepath)s?id=99%%(book_id)s" type="image/jpeg" width="80">'
                               )%{'modulepath':self.modulepath}
       self.document_entry_content='<i>%(e_content)s</i>'
       self.document_entry_content2_start='<div style="content">'
       self.document_entry_content2_title='<b>Название книги:</b> %(title)s<br>'
       self.document_entry_content2_authors='<b>Авторы:</b> %(authors)s<br>'
       self.document_entry_content2_genres='<b>Жанры:</b> %(genres)s<br>'
       self.document_entry_content2_series='<b>Серии:</b> %(series)s<br>'
       self.document_entry_content2_filename='<b>Файл:</b> %(filename)s<br>'
       self.document_entry_content2_filename='<b>Файл:</b> %(filename)s<br>'
       self.document_entry_content2_filesize='<b>Размер файла:</b> %(filesize)sКб.<br>'
       self.document_entry_content2_docdate='<b>Дата правки:</b> %(docdate)s<br>'
       self.document_entry_content2_annotation='<p class="annotation">%(annotation)s</p>'
       self.document_entry_content2_finish='</div>'

       self.document_alphabet_menu=('<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(iid)s&amp;alpha=1%%(nl)s">А..Я (РУС)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(iid)s&amp;alpha=2%%(nl)s">0..9 (Цифры)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(iid)s&amp;alpha=3%%(nl)s">A..Z (ENG)</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(iid)s&amp;alpha=4%%(nl)s">Другие символы</a></h2><i></i></div>'
                                    '<div class=navigation_entry><h2><a href="%(modulepath)s?id=%%(iid)s&amp;alpha=5%%(nl)s">Показать все</a></h2><i></i></div>'
                                    )%{'modulepath':self.modulepath}

       self.document_page_control_prev=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="prev" title="Previous Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%%(page)s" />'
                               )%{'modulepath':self.modulepath}
       self.document_page_control_next=('<link type="application/atom+xml;profile=opds-catalog;kind=acquisition" rel="next" title="Next Page" href="%(modulepath)s?id=%%(link_id)s&amp;page=%%(page)s" />'
                               )%{'modulepath':self.modulepath}


       self.document_entry_acq_start='<br><div class=acquisition_entry>\n'
       self.document_entry_acq_link_start='<div class=acq_link>'
       self.document_entry_acq_book_title=('<h2>%(e_title)s</h2> <i>Скачать в формате: </i>')
       self.document_entry_acq_book_link_alternate=''
       self.document_entry_acq_book_link=('<i><a href="%(modulepath)s?id=%%(id)s%%(link_id)s">%%(format)s</a></i>&nbsp;'
                               )%{'modulepath':self.modulepath}
       self.document_entry_acq_link_finish='</div>'

       self.document_entry_acq_info_start='<div class=acq_info_container>\n'

       self.document_entry_acq_info_cover=('<div class=acq_cover><img src="%(modulepath)s?id=99%%(link_id)s" type="image/jpeg" width="80"></div>'
                               )%{'modulepath':self.modulepath}

       self.document_entry_acq_infobook_start='<div class=acq_infobook>'
       self.document_entry_acq_infobook_title='<b>Название книги:</b> %(e_title)s<br>'
       self.document_entry_acq_infobook_authors='<b>Авторы:</b> %(authors_link)s<br>'
       self.document_entry_acq_infobook_genres='<b>Жанры:</b> %(genres)s<br>'
       self.document_entry_acq_infobook_series='<b>Серии:</b> %(series)s<br>'
       self.document_entry_acq_infobook_filename='<b>Файл:</b> %(filename)s<br>'
       self.document_entry_acq_infobook_filesize='<b>Размер файла:</b> %(filesize)sКб.<br>'
       self.document_entry_acq_infobook_docdate='<b>Дата правки:</b> %(docdate)s<br>'
       self.document_entry_acq_infobook_annotation='<p class="annotation">%(annotation)s</p>'
       self.document_entry_acq_infobook_finish='</div>'

       self.document_entry_acq_info_finish='</div>'

       self.document_entry_acq_finish='</div>'
