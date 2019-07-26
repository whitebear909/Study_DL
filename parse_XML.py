#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xml.etree.ElementTree as et


# In[1]:


def parse_XML(xml_file, df_cols, root_tag): 
    """Parse the input XML file and store the result in a pandas DataFrame 
    with the given columns. The first element of df_cols is supposed to be 
    the identifier variable, which is an attribute of each node element in 
    the XML data; other features will be parsed from the text content of 
    each sub-element. """    
   
    xroot = et.parse(xml_file).getroot()
    out_df = pd.DataFrame(columns = df_cols)
    links = list(xroot.iter(root_tag))    

    for node in links:
        res = []
        for el in df_cols[:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index=True)
        
    return out_df


def parse_normal_XML(xml_file, df_cols): 
    """Parse the input XML file and store the result in a pandas DataFrame 
    with the given columns. The first element of df_cols is supposed to be 
    the identifier variable, which is an attribute of each node element in 
    the XML data; other features will be parsed from the text content of 
    each sub-element. """    
    
    xroot = et.parse(xml_file).getroot()
    out_df = pd.DataFrame(columns = df_cols)
    
    for node in xroot: 
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index=True)
        
    return out_df


def parse_XML_file(xml_file, df_cols): 
    """Parse the input XML file and store the result in a pandas DataFrame 
    with the given columns. The first element of df_cols is supposed to be 
    the identifier variable, which is an attribute of each node element in 
    the XML data; other features will be parsed from the text content of 
    each sub-element. """
    
    xtree = et.parse(xml_file)
    xroot = xtree.getroot()
    out_df = pd.DataFrame(columns = df_cols)
    
    for node in xroot: 
        res = []
        res.append(node.attrib.get(df_cols[0]))
        for el in df_cols[1:]: 
            if node is not None and node.find(el) is not None:
                res.append(node.find(el).text)
            else: 
                res.append(None)
        out_df = out_df.append(pd.Series(res, index = df_cols), ignore_index=True)
        
    return out_df


# In[ ]:




