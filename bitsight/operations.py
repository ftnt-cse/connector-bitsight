"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

from datetime import datetime
import logging

from requests import request, exceptions as req_exceptions
from requests_toolbelt.utils import dump
from connectors.core.connector import get_logger, ConnectorError
from .constants import *


logger = get_logger("bitsight")
logger.setLevel(logging.INFO) #Uncomment for debugs

class Bitsight:
    def __init__(self, config, *args, **kwargs):
        server_url = config.get("server_url")
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://"+server_url
        self.url = server_url.strip("/")
        self.username = str(config.get("api_token"))
        self.verify_ssl = config.get("verify_ssl")

    def api_request(self, endpoint, method="GET", params={}, data={}):
        try:
            endpoint = self.url + endpoint
            if params:
                params = self.build_params(params)
            logger.debug(f"\n>>>>>>>> making API request\n{method} {endpoint}\nparams: {params}")
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, auth=(self.username, ""), params=params, verify_ssl=self.verify_ssl)
            except Exception:
                pass
            response = request(method, endpoint, auth=(self.username, ""), params=params, json=data, verify=self.verify_ssl)
            logger.debug('\n{}\n'.format(dump.dump_all(response).decode('utf-8')))

            if 200 <= response.status_code <= 300:
                if response.text != "":
                    return response.json()
                else:
                    return True
            else:
                if response.text != "":
                    err_resp = response.text
                    error_msg = 'Response [{0}:{1} Details: {2}]'.format(response.status_code, response.reason, err_resp)
                else:
                    error_msg = 'Response [{0}:{1}]'.format(response.status_code, response.reason)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            raise ConnectorError(str(err))

    def build_params(self, params):
        new_params = {}
        for key, value in params.items():
            if value is False or value == 0 or value:
                if key in DATE_PARAMS:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').strftime("%Y-%m-%d")
                new_params[key] = value
        return new_params


def check_health_ex(config):
    try:
        return get_alerts(config, {"limit": 10})
    except Exception as err:
        raise ConnectorError(str(err))


def get_alerts(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v2/alerts", params=params)


def get_companies_with_exposed_credentials(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v1/exposed-credentials/affected-companies", params=params)


def get_credentials_leaks(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v1/exposed-credentials/leaks", params=params)


def get_threat_evidence(config, params):
    ob = Bitsight(config)
    threat_guid = params.pop("threat_guid")
    company_guid = params.pop("company_guid")
    for key, value in params.items():
        if key in {"detection_type", "evidence_certainty", "exposure_detection"} and value:
            params[key] = value.lower()
    return ob.api_request(f"/ratings/v1/threats/{threat_guid}/companies/{company_guid}/evidence", params=params)


def get_portfolio_threats(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v1/threats/", params=params)


def get_cataloged_threats(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v1/threats/catalog", params=params)


def get_threat_statistics(config, params):
    ob = Bitsight(config)
    return ob.api_request("/ratings/v1/threats/summaries", params=params)


def get_threat_impact(config, params):
    ob = Bitsight(config)
    threat_guid = params.pop("threat_guid")
    for key, value in params.items():
        if key in {"evidence_certainty", "exposure_detection"} and value:
            params[key] = value.lower()
    return ob.api_request(f"/ratings/v1/threats/{threat_guid}/companies", params=params)


def get_assets(config, params):
    ob = Bitsight(config)
    company_guid = params.pop("company_guid")
    if params.get("tags_contains"):
        tags = params["tags_contains"]
        if isinstance(tags, str):
            tags = tags.split(",")
            params.update({"tags_contains": tags})
    return ob.api_request(f"/ratings/v1/companies/{company_guid}/assets", params=params)


def get_assets_risk_matrix(config, params):
    ob = Bitsight(config)
    company_guid = params.pop("company_guid")
    return ob.api_request(f"/ratings/v1/companies/{company_guid}/assets/statistics", params=params)


def generic_api_call(config, params):
    '''Make a generic API call, user has to build required attributes before making the call'''
    endpoint = params.get("endoint")
    http_method = params.get("method")
    url_params = params.get("url_params")
    body = params.get("body") if http_method != 'GET' else None
    ob = Bitsight(config)
    return ob.api_request(endpoint, method=http_method, params=url_params, data=body)


operations = {
    "get_alerts": get_alerts,
    "get_companies_with_exposed_credentials": get_companies_with_exposed_credentials,
    "get_credentials_leaks": get_credentials_leaks,
    "get_threat_evidence": get_threat_evidence,
    "get_portfolio_threats": get_portfolio_threats,
    "get_cataloged_threats": get_cataloged_threats,
    "get_threat_statistics": get_threat_statistics,
    "get_threat_impact": get_threat_impact,
    "get_assets": get_assets,
    "get_assets_risk_matrix": get_assets_risk_matrix,
    "generic_api_call": generic_api_call
}