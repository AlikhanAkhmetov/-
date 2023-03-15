from Flask import Flask, render_template
from miracles_6-1 import *

miracles_1_6 = Flask (__name__)

@app.route ('/')
@app.route ('/entry')
def entry_page () -> 'html' :
    return render_template ('entry.html' ,
                            the_title = 'Сочини любой текст на арабском'
