import sys
import re
import os
def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
try : 
	from urllib.request import urlopen
except:
	clear()
	print ('Python 3 Needed ! Good Bye !')
	sys.exit(0)
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
clear()
print (color.RED+color.BOLD+"Created BY SABER SEBRI\nThanks To : TAZ - DS_TN - OJZ")
print (color.RED+color.BOLD+'The author does not hold any responsibility for the bad use of this tool, remember that attacking targets without prior consent is illegal and punished by law.')
if len(sys.argv) != 2 :
	print (color.GREEN+color.BOLD+'Usage : '+sys.argv[0]+" http://site.com")
	sys.exit(0)
vulplugins = {
'revslider': 'Total attacks: 145,626\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/36957/',
'wp-symposium-pro': 'Total attacks: 2,517,975\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/35543/',
'wptf-image-gallery': 'Total attacks: 2,164,9295\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/37751/',
'google-mp3-audio-player': 'Total attacks: 128,622\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/35460/',
'wp-database-backup': 'Total attacks: 148,661\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/35378/',
'woocommerce-store-toolkit': 'Total attacks: 1,011,602\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/39421/',
'wp-ecommerce-shop-styling': 'Total attacks: 2,137,509\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37530/',
'candidate-application-form': 'Total attacks: 2,158,179\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37754/',
'wp-mobile-detector': 'Total attacks: 5,174,567\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/39891/',
'ajax-pagination': 'Total attacks: 276,883\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/32622/',
'plugin-newsletter': 'Total attacks: 124858\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/19018/',
'google-picasa-albums-viewer': 'Total attacks: 136,833\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/19055/',
'dukapress': 'Total attacks: 135,206\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/35346/',
'wp-filemanager': 'Total attacks: 146,480\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/25440/',
'history-collection': 'Total attacks: 142,925\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37254/',
'work-the-flow-file-upload': 'Total attacks: 670,824\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/36640/',
'paypal-currency-converter-basic-for-woocommerce': 'Total attacks: 131,075\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37253/',
'really-simple-guest-post': 'Total attacks: 340,145\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37209/',
'store-locator-le': 'Total attacks: 150,498\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/18989/',
'wp-swimteam': 'Total attacks: 441,445\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37601/',
'zoomsounds': 'Total attacks: 413,237\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/37166//',
'simple-download-button-shortcode': 'Total attacks: 369,066\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/19020/',
'sell-downloads': 'Total attacks: 470,510\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/38868/',
'thecartpress': 'Total attacks: 435,271\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/38869//',
'advanced-uploader': 'Total attacks: 432,619\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/38867/',
'brandfolder': 'Total attacks: 330,113\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/39591/',
'tune-library': 'Total attacks: 211,274\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/36802/',
'advanced-video-embed-embed-videos-or-playlists': 'Total attacks: 204,447\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/19022/',
'wp-user-frontend': 'Total attacks: 203,197\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/39422/',
'formcraft-form-builder': 'Total attacks: 201,984\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/30002/',
'simple-ads-manager': 'Total attacks: 199,230\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/36614/',
'levelfourstorefront': 'Total attacks: 207,554\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/38160//',
'reflex-gallery': 'Total attacks: 137,260\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/36374/',
'acf-frontend-display-by-catsplugins': 'Total attacks: 701,963\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37514/',
'wp-ecommerce-shop-styling': 'Total attacks: 111,546\nType: LFI\nExploit database: https://www.exploit-db.com/exploits/37530/',
'inboundio-marketing': 'Total attacks: 112,696\nType: Shell\nExploit database: https://www.exploit-db.com/exploits/36478/',
'cherry-plugin': 'Total attacks : 102,305\nType: Shell\nDescription: https://www.youtube.com/watch?v=zSva2UPwKvo'
}
url = sys.argv[1]
get = urlopen(url).read().decode('utf8')
version = re.findall('content="WordPress (.*?)"', get)
th = re.findall('\/themes\/(.*?)\/', get)
themes = []
for i in th :
	if i not in themes:
		themes.append(i)
pg = re.findall('\/plugins\/(.*?)\/', get)
plugins = []
for i in pg :
	if i not in plugins:
		plugins.append(i)
usr = url+'/?author=1'
sourcecode = urlopen(url).read().decode('utf8')
enemurate = re.findall('author\/(.*?)\/', sourcecode)
user = []
for i in enemurate:
	if i not in user:
		user.append(i)
print (color.GREEN+color.BOLD+"Site : "+url)
if user == []:
	print (color.GREEN+color.BOLD+"User : Not Found")
else:
	print (color.GREEN+"User enumerated : "+color.RED+'[!] '+''.join(user)+' [!]')
last = '4.9.6'
if last != ''.join(version):
	if version == [] :
		print (color.GREEN+"Version : Not Found")
	else:
		print (color.RED+"Version : "+''.join(version)+" Not Updated !")
else:
	print (color.GREEN+color.BOLD+"Version :",color.RED+''.join(version))
if themes == []:
	print (color.GREEN+"Themes : Not Found")
else: 
	print (color.GREEN+color.BOLD+"Themes Found :",color.RED+'\n'.join(themes))
if plugins == []:
	print (color.GREEN+"Plugins : Not Found")
else:
	print (color.GREEN+color.BOLD+"Plugins Found :",color.RED+'\n'.join(plugins))
if plugins != [] :
	print (color.GREEN+"Do You Need A Report For every vulnerable plugin ? ")
	print ("[1]-Yes")
	print ("[2]-No")
	ch = input("Choice : ")
	if ch == '1':
		for i in plugins:
			if i in vulplugins:
				print (color.RED+i)
				print (color.RED+vulplugins[i])