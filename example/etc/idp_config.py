#!/usr/bin/env python
# -*- coding: utf-8 -*-
from saml2 import BINDING_HTTP_REDIRECT, BINDING_URI
from saml2 import BINDING_HTTP_ARTIFACT
from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_SOAP
from saml2.cert import OpenSSLWrapper
from saml2.saml import NAME_FORMAT_URI
from saml2.saml import NAMEID_FORMAT_TRANSIENT
from saml2.saml import NAMEID_FORMAT_PERSISTENT
import os.path

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None

if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin"])
else:
    xmlsec_path = '/usr/bin/xmlsec1'

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def verify_encrypt_cert(cert_str):
    osw = OpenSSLWrapper()
    ca_cert_str = osw.read_str_from_file(full_path("root_cert/localhost.ca.crt"))
    valid, mess = osw.verify(ca_cert_str, cert_str)
    return valid


def full_path(local_file):
    return os.path.join(BASEDIR, local_file)

#If HTTPS is true you have to assign the server cert, key and certificate chain.
HTTPS = True
SERVER_CERT = "httpsCert/localhost.crt"
SERVER_KEY = "httpsCert/localhost.key"
#CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None


HOST = 'localhost'
PORT = 8088

BASE = "https://%s:%s" % (HOST, PORT)

CONFIG = {
    "entityid": "%s/TestPEFIMIdP.xml" % BASE,
    "description": "Test PEFIM IDP",
    "valid_for": 168,
    "service": {
        "aa": {
            "endpoints": {
                "attribute_service": [
                    ("%s/attr" % BASE, BINDING_SOAP)
                ]
            },
            "name_id_format": [NAMEID_FORMAT_TRANSIENT,
                               NAMEID_FORMAT_PERSISTENT]
        },
        "aq": {
            "endpoints": {
                "authn_query_service": [
                    ("%s/aqs" % BASE, BINDING_SOAP)
                ]
            },
        },
        "idp": {
            "name": "Test PEFIM IdP",
            "want_authn_requests_signed": True,
            "want_authn_requests_only_with_valid_cert": True,
            "sign_response": True,
            "sign_assertion": False,
            "verify_encrypt_cert": verify_encrypt_cert,
            "encrypt_assertion": True,
            "endpoints": {
                "single_sign_on_service": [
                    ("%s/sso/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/sso/post" % BASE, BINDING_HTTP_POST),
                    ("%s/sso/art" % BASE, BINDING_HTTP_ARTIFACT),
                    ("%s/sso/ecp" % BASE, BINDING_SOAP)
                ],
                "single_logout_service": [
                    ("%s/slo/soap" % BASE, BINDING_SOAP),
                    ("%s/slo/post" % BASE, BINDING_HTTP_POST),
                    ("%s/slo/redirect" % BASE, BINDING_HTTP_REDIRECT)
                ],
                "artifact_resolve_service": [
                    ("%s/ars" % BASE, BINDING_SOAP)
                ],
                "assertion_id_request_service": [
                    ("%s/airs" % BASE, BINDING_URI)
                ],
                "manage_name_id_service": [
                    ("%s/mni/soap" % BASE, BINDING_SOAP),
                    ("%s/mni/post" % BASE, BINDING_HTTP_POST),
                    ("%s/mni/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/mni/art" % BASE, BINDING_HTTP_ARTIFACT)
                ],
                "name_id_mapping_service": [
                    ("%s/nim" % BASE, BINDING_SOAP),
                ],
            },
            "policy": {
                "default": {
                    "lifetime": {"minutes": 15},
                    #"attribute_restrictions": None, # means all I have
                    "name_form": NAME_FORMAT_URI,
                    "entity_categories": ["at_egov_pvp2"]
                },
            },
            #"subject_data": "./db/idp.subject",
            "name_id_format": [NAMEID_FORMAT_PERSISTENT]
        },
    },
    "debug": 1,
    "key_file": full_path("pki/mykey.pem"),
    "cert_file": full_path("pki/mycert.pem"),
    "metadata": {
        "local": [full_path("metadata/pefim_proxy_metadata.xml")],
    },
    "organization": {
        "display_name": "Test PEFIM IdP",
        "name": "Test PEFIM IdP",
        "url": "http://localhost:8088",
    },
    "contact_person": [
        {
            "contact_type": "technical",
            "given_name": "Test",
            "sur_name": "Testsson",
            "email_address": "test.testsson@test.com"
        },
    ],
    # This database holds the map between a subjects local identifier and
    # the identifier returned to a SP
    "xmlsec_binary": xmlsec_path,
    #"attribute_map_dir": "../attributemaps",
    "logger": {
        "rotating": {
            "filename": "logs/idp.log",
            "maxBytes": 500000,
            "backupCount": 5,
        },
        "loglevel": "debug",
    }
}

PASSWD = {
    "testuser": "qwerty"
}

USERS = {
    "testuser": {
            "sn": "Testsson",
            "givenName": "Test",
            "eduPersonAffiliation": "student",
            "eduPersonScopedAffiliation": "student@example.com",
            "eduPersonPrincipalName": "test@example.com",
            "uid": "testuser1",
            "eduPersonTargetedID": "one!for!all",
            "c": "SE",
            "o": "Example Co.",
            "ou": "IT",
            "initials": "P",
            "schacHomeOrganization": "example.com",
            "email": "hans@example.com",
            "displayName": "Test Testsson",
            "labeledURL": "http://www.example.com/haho My homepage",
            "norEduPersonNIN": "SE199012315555",
            "PVP-VERSION": "PVP-VERSION",
            "PVP-PRINCIPAL-NAME": "PVP-PRINCIPAL-NAME",
            "PVP-GIVENNAME": "PVP-GIVENNAME",
            "PVP-BIRTHDATE": "PVP-BIRTHDATE",
            "PVP-USERID": "PVP-USERID",
            "PVP-GID": "PVP-GID",
            "PVP-BPK": "PVP-BPK",
            "PVP-MAIL": "PVP-MAIL",
            "PVP-TEL": "PVP-TEL",
            "PVP-PARTICIPANT-ID": "PVP-PARTICIPANT-ID",
            "PVP-PARTICIPANT-OKZ": "PVP-PARTICIPANT-OKZ",
            "PVP-OU-OKZ": "PVP-OU-OKZ",
            "PVP-OU": "PVP-OU",
            "PVP-OU-GV-OU-ID": "PVP-OU-GV-OU-ID",
            "PVP-FUNCTION": "PVP-FUNCTION",
            "PVP-ROLES": "PVP-ROLES",
            "PVP-INVOICE-RECPT-ID": "PVP-INVOICE-RECPT-ID",
            "PVP-COST-CENTER-ID": "PVP-COST-CENTER-ID",
            "PVP-CHARGE-CODE": "PVP-CHARGE-CODE",
    }
}

EXTRA = {
}
