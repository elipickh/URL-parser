import re

def url_host(a):
    urlhost = a.replace('https://', '').replace('http://', '').replace('www.', '').split(':')[0].split('/')[0]
    return urlhost.lower()

def url_domain(a):
    if bool(re.search('[\w][ ][\w]', a)) or 'mob.app.' in a or not bool(re.search('([\w][.][\w])', a)):
       urldomain = '__not a valid URL ('+a+')' 
    elif bool(re.search('((co)|(com)|(gov)|(net))[.][\w]', a)):
        domain0 = a.replace('https://', '').replace('http://', '').replace('www.', '').split(':')[0].split('/')[0].split('.')
        urldomain = '.'.join(domain0[-3:])
    else:
        domain0 = a.replace('https://', '').replace('http://', '').replace('www.', '').split(':')[0].split('/')[0].split('.')
        urldomain = '.'.join(domain0[-2:])
    return urldomain.lower()

def url_dir(a):
    urldir0 = a.replace('https://', '').replace('http://', '').split('/', 1)
    if len(urldir0) == 1:
        urldir = None
    else:
        urldir = urldir0[-1].split('/')
        urldir.pop() if "." in urldir[-1] else None
        # Remove empty elements
        urldir = [x for x in urldir if x]
        if len(urldir) > 0:       
	        urldir = ','.join(urldir).lower()
	    else:
	    	urldir = None
    return urldir

def url_page(a):
    urlpage0 = a.replace('https://', '').replace('http://', '').split('/', 1)
    if len(urlpage0) == 1:
        urlpage = None
    else:
    	urlpage = [urlpage0[-1].split('/')[-1].lower()]
    	# Remove empty elements
        urlpage = [x for x in urlpage if x]
        if len(urlpage) == 0:
        	urlpage = None 
        else:
        	urlpage = urlpage[-1]
    return urlpage

