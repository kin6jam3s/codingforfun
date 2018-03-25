#!/usr/bin/env python3

import requests
import collections
import os
import sys
import pandas as pd


NextixlanResult = collections.namedtuple(
    'NextixlanResult',
    'name,id,ix_id,speed,ipaddr4,ipaddr6,net_id,notes,created,updated,status,ixlan_id,asn,is_rs_peer'
)


def main():
    header()
    search = search_event_loop()
    nextixlan = peering_as_info(search)
    get_bw_and_con_number(nextixlan)
    save_data(nextixlan)
    save_excel(nextixlan)


def header():
    print('-------------------------------------')
    print('---------------AS REPORT-------------')
    print('-------------------------------------')
    print()


# def user_as_input():
#     print('Enter PUBLIC AS Number')
#     while input_as != x:
#         input_as = input('Enter AS Number (x to exit):  ')
#         return input_as

# def search_event_loop(as_num):
#     # Loop for exiting if as_input = x
#     if as_num != 'x':
#         search = as_num
#         return search
#     else:
#         print("Exiting...")


def search_event_loop():
    input_as = 'once_through_loop'

    while input_as != 'x':
        print('Enter PUBLIC AS 1 - 54494')
        input_as = input('Enter AS number: (x to exit): ')
        if input_as != 'x':
            as_num = input_as
            return as_num
        else:
            print("Exiting...")
            exit()


def peering_as_info(search):

    # for Error handling and getting data from url
    print('Searching for information...')
    url = 'https://www.peeringdb.com/api/netixlan?asn={}'.format(search)
    response = requests.get(url)
    while response.status_code == 200:
        try:
            info = response.json()
            results = info['data']

            # creating namedtuples for accessing dictionary data
            nextixlan = [
                NextixlanResult(**m)
                for m in results
                ]
            return nextixlan

        except Exception as e:
            print('Sorry URL is ' + e)


def get_bw_and_con_number(nextixlan):
    # Function for getting Total Band
    n=len(nextixlan)
    mb = 0
    print('         NAME        |       SPEED       |       ID      |       IPv4        |     IPV6 ')
    for r in nextixlan:
        print(' {} | {} | {} | {} | {}'.format(r.name, r.speed, r.id, r.ipaddr4, r.ipaddr6))
        mb += r.speed
        gb = mb / 1000
    print('Total available bandwidth: {} Gbps at {} internet exchange locations.'.format(gb, n))
    cwd = os.getcwd()
    print('CSV data is stored on :' + cwd)


def save_data(nextixlan):
    # Save text format
    name = 'output_as'
    filename = os.path.join(name + '.txt')
    sys.stdout = open(filename, 'wt', encoding='utf8')
    for r in nextixlan:
        print('{} | {} | {} | {} | {}'.format(r.name, r.speed, r.id, r.ipaddr4, r.ipaddr6))
    sys.stdout.close()


def save_excel(nextixlan):
    # Save text to CSV
    name = 'output_as'
    filename = os.path.join(name + '.csv')
    # sys.stdout = open(filename, 'w', encoding='utf8')
    data_columns = ["NAME", "SPEED", "ID", "IPV4", "IPV6"]
    data = pd.read_csv('output_as.txt', delimiter="|", header=None, names=data_columns)
    data.to_csv(filename)


if __name__ == '__main__':
    main()










