#!/usr/bin/env python
# coding: utf-8

# ## Creating a new config file (WCD_postgresql.ini)

# In[12]:


import configparser

config = configparser.ConfigParser()

# Add the structure to the file we will create
config.add_section('postgresql')
config.set('postgresql', 'DB_TYPE', 'postgresql')
config.set('postgresql', 'DB_DRIVER', 'psycopg2')
config.set('postgresql', 'DB_HOST', 'xxxxxxx')
config.set('postgresql', 'DB_USER', 'ameenah_a_202309')
config.set('postgresql', 'DB_PORT', '5432')
config.set('postgresql', 'DB_PASS', 'xxxxxx')
config.set('postgresql', 'DB_NAME', 'xxxxxxxxx')


# Write the new structure to the new file
with open(r"WCD_postgresql.ini", 'w') as configfile:
    config.write(configfile)


# In[ ]:




