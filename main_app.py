from coding4fun import PeeringClient


def main():
    print_header()
    search_event_loop()


def print_header():
    print('---------------')
    print('Peering APP')
    print('---------------')


def search_event_loop():
    search = 'once_through_loop'

    while search != 'x':
        search = input('Enter AS number: (x to exit): ')
        if search != 'x':
            client = PeeringClient(search)

            results = client.perform_search()
            n = len(results)
            # print('Found {} Results.'.format(len(results)))
            mb = 0
            for r in results:
                mb += r.speed
                gb = mb / 1000
                print('--------------------------------------------------------------------------------------')
                print('NAME: {} -- SPEED: {} -- ID: {} -- IPv4 Addr: {} -- IPv6 Addr: {}'.format(
                    r.name, r.speed, r.id, r.ipaddr4, r.ipaddr6
                ))
            print('--------------------------------------------------------------------------------------')
            print('Total available bandwidth: {} Gbps at {} internet exchange locations.'.format(gb, n))

    print('exiting...')

if __name__ == '__main__':
    main()