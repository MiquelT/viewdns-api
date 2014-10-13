viewdns API
=========

API para el portal `viewdns`_ .


Usage
------------

    usage: viewdns.py [-h] -ak APIKEY -t TARGET
                      [-al | -asnl | -cft | -dp | -drl | -dr | -dt | -w | -el | -hh | -gp | -iph | -ipl | -ift | -sd | -mac | -p | -ps | -rdl | -ril | -sdl | -tr | -dec]
                      [-o {json,xml}]
    
    viewDNS python API
    
    optional arguments:
      -ak                   your api key from viewdns.info
      -t                	target you want to request
      -al                   Abuse Contact Lookup
      -asnl                 ASN Lookup
      -cft                  Chinese Firewall Test
      -dp                   DNS Propagation Checker
      -drl                  DNS Record Lookup
      -dr                   DNS Report
      -dt                   DNSSEC Test
      -w                    Domain/IP Whois
      -el                   Free Email Lookup
      -hh                   Get HTTP Headers
      -gp                   Google Pagerank Checker
      -iph                  IP History
      -ipl                  IP Location Finder
      -ift                  Iran Firewall Test
      -sd                   Is My Site Down
      -mac                  MAC Address Lookup
      -p                    Ping
      -ps                   Port Scanner
      -rdl                  Reverse DNS Lookup
      -ril                  Reverse IP Lookup
      -sdl                  Spam Database Lookup
      -tr                   Traceroute
      -dec                  URL/String Decode
    
    output options:
      -o {json,xml}, --output {json,xml}
                        output format in json or xml. Default "json"


Dependencias
------------
* Python 2 (2.7 should be sufficient)

License
-------
Esta obra está sujeta a la licencia `Reconocimiento-NoComercial\ 4.0\ Internacional\ de\ Creative\ Commons`_. Para ver una copia de esta licencia, visite visite `http://creativecommons.org/licenses/by-nc/4.0/`_.


Como puede ayudar
----------------

Si encuentra cualquier error o problema puede contactar conmigo en `Twitter`_  por `email`_.


.. _viewdns: http://viewdns.info
.. _Twitter: https://twitter.com/miqueltur
.. _email: mailto:miquel.tur.m@gmail.com
.. _http\://creativecommons.org/licenses/by-nc/4.0/: http://creativecommons.org/licenses/by-nc/4.0/
.. _Reconocimiento-NoComercial\ 4.0\ Internacional\ de\ Creative\ Commons: http\://creativecommons.org/licenses/by-nc/4.0/
