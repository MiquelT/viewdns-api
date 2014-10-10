# -*- coding: utf-8 -*-
__author__ = 'MiquelTur'

import argparse
from bin.apiRequests import *














def main():
    """
    Main function
    """
    import sys
    # print(sys.version_info)

    parser = argparse.ArgumentParser(description='viewDNS python API')
    parser.add_argument('-ak','--apikey', required=True, help='your api key from viewdns.info')
    parser.add_argument('-t','--target', required=True,  help='target you want to request')


    group0 = parser.add_mutually_exclusive_group()
    group0.add_argument('-al', action="store_true", help='Abuse Contact Lookup')
    group0.add_argument('-asnl', action="store_true", help='ASN Lookup')
    group0.add_argument('-cft', action="store_true", help='Chinese Firewall Test')
    group0.add_argument('-dp', action="store_true", help='DNS Propagation Checker')
    group0.add_argument('-drl', action="store_true", help='DNS Record Lookup')
    group0.add_argument('-dr', action="store_true", help='DNS Report')
    group0.add_argument('-dt', action="store_true", help='DNSSEC Test')
    group0.add_argument('-w', action="store_true", help='Domain/IP Whois')
    group0.add_argument('-el', action="store_true", help='Free Email Lookup')
    group0.add_argument('-hh', action="store_true", help='Get HTTP Headers')
    group0.add_argument('-gp', action="store_true", help='Google Pagerank Checker')
    group0.add_argument('-iph', action="store_true", help='IP History')
    group0.add_argument('-ipl', action="store_true", help='IP Location Finder')
    group0.add_argument('-ift', action="store_true", help='Iran Firewall Test')
    group0.add_argument('-sd', action="store_true", help='Is My Site Down')
    group0.add_argument('-mac', action="store_true", help='MAC Address Lookup')
    group0.add_argument('-p', action="store_true", help='Ping')
    group0.add_argument('-ps', action="store_true", help='Port Scanner')
    group0.add_argument('-rdl', action="store_true", help='Reverse DNS Lookup')
    group0.add_argument('-ril', action="store_true", help='Reverse IP Lookup')
    group0.add_argument('-sdl', action="store_true", help='Spam Database Lookup')
    group0.add_argument('-tr', action="store_true", help='Traceroute')
    group0.add_argument('-dec', action="store_true", help='URL/String Decode')


    # output options
    group2 = parser.add_argument_group('output options')
    group2.add_argument('-o', '--output', dest='output', default="json", choices=['json','xml'],
                        help='output format in json or xml. Default "json"')

    # Parse command line
    args = parser.parse_args()

    key = args.apikey
    output = args.output
    target = args.target

    if args.al:
        abuse_contact_lookup(key,target,output)
    elif args.asnl:
        asn_lookup(key,target,output)
    elif args.cft:
        chinese_firewall_test(key,target,output)
    elif args.dp:
        dns_propagation_checker(key,target,output)
    elif args.drl:
        dns_record_lookup(key,target,output)
    elif args.dr:
        dns_report(key,target,output)
    elif args.dt:
        dnssec_test(key,target,output)
    elif args.w:
        domain_ip_whois(key,target,output)
    elif args.el:
        free_email_lookup(key,target,output)
    elif args.hh:
        get_http_headers(key,target,output)
    elif args.gp:
        google_pagerank_checker(key,target,output)
    elif args.iph:
        ip_history(key,target,output)
    elif args.ipl:
        ip_location_finder(key,target,output)
    elif args.ift:
        iran_firewall_test(key,target,output)
    elif args.sd:
        site_down(key,target,output)
    elif args.mac:
        mac_address_lookup(key,target,output)
    elif args.p:
        ping(key,target,output)
    elif args.ps:
        port_scanner(key,target,output)
    elif args.rdl:
        reverse_dns_lookup(key,target,output)
    elif args.ril:
        reverse_ip_lookup(key,target,output)
    elif args.sdl:
        spam_Database_Lookup(key,target,output)
    elif args.tr:
        traceroute(key,target,output)
    elif args.dec:
        urlL_String_Decode(key,target,output)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()