from google.colab.output import *
from IPython.display import display, Javascript
from typing import Union

# path that can serve content
nbx = '/usr/local/share/jupyter/nbextensions'

def set_height(h: Union[str, int]):
    eval_js('google.colab.output.setIframeHeight("%s")' % h)

# Usage:
# set_style(fontSize='30px', color='red')
# print("Hello")
def set_style(**kw):
    import json
    display(Javascript('''
    for (rule of document.styleSheets[0].cssRules){
        if (rule.selectorText=='body') {
            Object.assign(rule.style, %s)
            break
        }
    }
    ''' % json.dumps(kw)))


def url_port(port: int):
    """ Convert port number to URL for webapps """
    return eval_js("google.colab.kernel.proxyPort(%d)" % port)


def show_port(port, height=400):
    """ Display webapp at port number in output using iframe """
    display(Javascript("""
    (async ()=>{
        fm = document.createElement('iframe')
        fm.src = await google.colab.kernel.proxyPort(%s)
        fm.width = '95%%'
        fm.height = '%d'
        fm.frameBorder = 0
        document.body.append(fm)
    })();
    """ % (port, height) ))