import requests
import collections


NextixlanResult = collections.namedtuple(
    'NextixlanResult',
    'name,id,ix_id,speed,ipaddr4,ipaddr6,net_id,notes,created,updated,status,ixlan_id,asn,is_rs_peer'
)

class PeeringClient:
    def __init__(self, search_text):
        self.search_text = search_text

    def perform_search(self):
        url = 'https://www.peeringdb.com/api/netixlan?asn={}'.format(self.search_text)

        r = requests.get(url)
        info = r.json()

        results = info['data']

        nextixlan = [
            NextixlanResult(**m)
            for m in results
            ]
        return nextixlan





# nextixlan = []
# for result in results:
#     p = NextixlanResult(
#         name=result['name'],
#         id=result['id'],
#         ix_id=result['ix_id'],
#         speed=result['speed'],
#         ipaddr4=result['ipaddr4'],
#         ipaddr6=result['ipaddr6']
#     )
#     nextixlan.append(p)
#
# print(nextixlan[0])







