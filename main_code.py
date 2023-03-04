# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:16:34 2023

@author: Acer
"""

#22028322-Veera Raghunatha Reddy Naguru
#ADS-1 PL 13-02-2023 -Ex-1

import pandas as pd
import matplotlib.pyplot as plt

BCS = pd.read_csv('BCS_ann.csv')
BP = pd.read_csv('BP_ann.csv')
TSCO = pd.read_csv('TSCO_ann.csv')
VOD = pd.read_csv('VOD_ann.csv')

plt.figure()
# fig, ((ax0, ax1), (ax2, ax3))=plt.subplots(2, 2)

#ax0.hist(BCS['ann_return'],bins=20,density=True)
#ax1.hist(BP['ann_return'],bins=20,density=True)
#ax2.hist(TSCO['ann_return'],bins=20,density=True)
#ax3.hist(TSCO['ann_return'],bins=20,density=True)

plt.subplot(2, 2, 1)
plt.hist(BCS['ann_return'], label='Barclays', density=True)
plt.legend()
plt.subplot(2, 2, 2)
plt.hist(BP['ann_return'], density=True, label='BP')
plt.legend()
plt.subplot(2, 2, 3)
plt.hist(TSCO['ann_return'], density=True, label='Tesco')
plt.legend()
plt.subplot(2, 2, 4)
plt.hist(VOD['ann_return'], density=True, label='Vodafone')
plt.legend()
plt.savefig('ADS-1-EX-3-1-a.png')
plt.show()

plt.figure()
plt.hist(BCS['ann_return'], label='Barclays', density=True)
plt.hist(BP['ann_return'], density=True, label='BP', alpha=0.7)
plt.show()


plt.figure()
names = ['Barclays', 'BP', 'Tesco', 'Vodafone']
plt.boxplot([BCS['ann_return'], BP['ann_return'], TSCO['ann_return'],
             VOD['ann_return']], labels=['Barclays', 'BP', 'Tesco', 'Vodafone'])
plt.show()

M_cap = pd.DataFrame()

M_cap['company'] = ['Barclays', 'BP', 'Tesco', 'Vodafone']
M_cap['M_cap_Mill'] = [33367, 68785, 20979, 29741]

plt.figure()
plt.pie(M_cap['M_cap_Mill'], labels=['Barclays', 'BP', 'Tesco', 'Vodafone'],
        autopct='%1.1f%%')
plt.show()

plt.figure()
plt.bar(M_cap['company'], M_cap['M_cap_Mill'], label='Market Capitalisations',
        color='g')
plt.legend(loc='upper right')
plt.show()
