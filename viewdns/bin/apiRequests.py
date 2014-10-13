__author__ = 'MiquelTur'
import urllib2
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

url_header = "http://pro.viewdns.info/"
params = "/?domain=%s&apikey=%s&output=%s"

def abuse_contact_lookup(key,target,output):
    url = url = url_header + "abuselookup"  + params %(target,key,output)
    consulter(output,url)

def asn_lookup(key,target,output):
    not_implemented()


def chinese_firewall_test(key,target,output):
    url = url_header + "chinesefirewall"  + params %(target,key,output)
    consulter(output,url)



def dns_propagation_checker(key,target,output):
    url = url = url_header + "propagation" + params %(target,key,output)
    consulter(output,url)


def dns_record_lookup(key,target,output):
    url = url = url_header + "dnsrecord" + params %(target,key,output)
    consulter(output,url)

def dns_record_lookup(key,target,output):
    url = url = url_header + "dnsrecord" + params %(target,key,output)
    consulter(output,url)

def dns_report(key,target,output):
    not_implemented()

def dnssec_test(key,target,output):
    not_implemented()

def domain_ip_whois(key,target,output):
    url = url = url_header + "whois" + params %(target,key,output)
    consulter(output,url)


def free_email_lookup(key,target,output):
    url = url = url_header + "freeemail" + params %(target,key,output)
    consulter(output,url)


def get_http_headers(key,target,output):
    url = url = url_header + "dnsrecord" + params %(target,key,output)
    consulter(output,url)


def google_pagerank_checker(key,target,output):
    not_implemented()


def ip_history(key,target,output):
    not_implemented()


def ip_location_finder(key,target,output):
    url = url = url_header + "iplocation" + params %(target,key,output)
    consulter(output,url)


def iran_firewall_test(key,target,output):
    url = url = url_header + "iranfirewall" + params %(target,key,output)
    consulter(output,url)


def site_down(key,target,output):
    not_implemented()


def mac_address_lookup(key,target,output):
    url = url = url_header + "maclookup" + params %(target,key,output)
    consulter(output,url)


def ping(key,target,output):
    url = url = url_header + "ping" + params %(target,key,output)
    consulter(output,url)


def port_scanner(key,target,output):
    url = url = url_header + "portscan" + params %(target,key,output)
    consulter(output,url)


def reverse_dns_lookup(key,target,output):
    url = url = url_header + "reversedns" + params %(target,key,output)
    consulter(output,url)


def reverse_ip_lookup(key,target,output):
    url = url = url_header + "reverseip" + params %(target,key,output)
    consulter(output,url)


def spam_Database_Lookup(key,target,output):
    url = url = url_header + "spamdblookup" + params %(target,key,output)
    consulter(output,url)


def traceroute(key,target,output):
    url = url = url_header + "traceroute" + params %(target,key,output)
    consulter(output,url)


def urlL_String_Decode(key,target,output):
    not_implemented()












def not_implemented():
    print "Not implemented method"



def consulter(output,url):
    f = urllib2.urlopen(url)
    resp = f.read()
    if "paid API keys only" in resp:
        print resp
    else:
        try:
            printer(output,resp)
        except Exception, e:
            print "\nSorry, Something went wrong.\n\ntry:\n\t- Check your APIKEY\n\t- Check the target\n"


def printer(output,resp):
    if output == 'json':
        jsonprint(resp)
    else:
        xmlprint(resp)


def jsonprint(resp):
    parsed = json.loads(resp)
    print json.dumps(parsed, indent=4, sort_keys=True)

def xmlprint(resp):
    root = ET.fromstring(resp)
    print prettify(root)

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

