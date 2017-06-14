from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

consumer_key = 'ma3bBVfGsZc1aJUhpS46tVhd5'
consumer_secret = 'VwZ9iaSR4XJ9JUnk3ZdpJhsUYBPqRZdgzxaHxgdVRlCqYE1g5Y'
access_token = '176382472-XKADJqVNW9ooxNKRfTHad3e9262VX888cX16gbOw'
access_token_secret = 'ATSbGoBMkWWELMsnkNgSeTXGczA4XPGY1EuNJXberr5O4'

auth = OAuthHandler(consumer_key,
                    consumer_secret)

auth.set_access_token(access_token,
                      access_token_secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.author.screen_name,
              status.created_at,
              status.source, '\n')

    def on_error(self, status_code):
        print('Error code {}'.format(status_code))
        return True

    def on_timeout(self):
        print('Listener Timeout\n')
        return True


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    stream.sample()


if __name__ == '__main__':
    print("Hello World!!")
    print_to_terminal()
    print("Hello World!!")
