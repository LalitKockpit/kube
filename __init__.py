"""
General functions for kube.
"""
import requests

__all__ = ['pushData', 'getSchema','getData']

def initializeApp(client_config):
    """
    client_config = 
    {
        "api_key":"<alpha_numeric string from kube portal>",
        "secret_key":"<alpha_numeric string from kube portal>"
    }
    """
    if client_config=='abc':
        return True
    else:
        return False

def pushData(client,df,table):
    """
    compulsory arguments ->
    df is pandas dataframe, 
    table = <sales,sales_order,ar,hierarchy,customer,product,target>
    ------------------------------------------------------------------
    overwrite -> optional argument -> True/False
    """
    error_message = ''
    if client==True:
        if df==None:
            error_message = 'pandas dataframe as compulsory argument is not provided'
            return error_message
        if table==None:
            error_message = 'table name as a compulsory argument is not provided'
            return error_message
        else:
            return True
    else:
        return False

def getSchema():
    """
    compulsory argument ->
    ------------------------------------------------------------------

    optional argument ->
    table = <sales,sales_order,ar,hierarchy,customer,product,target>
    ------------------------------------------------------------------
    """
    return True

def getData():
    """
    """
    return True