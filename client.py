'''
################################## client.py #############################
# Wallet Client calls a remote GRPC service to encrypt credit/debit cards
# data and decrypt token back to plain text card detail.
################################## client.py #############################
'''
import grpc
import wallet_pb2
import wallet_pb2_grpc
class WalletClient(object):
    '''
    WalletClient encrypts and decrypts card info via GRPC's sub which internally calls
    the remote WalletServicer.
    '''

    def __init__(self, host='0.0.0.0', port=3000):
        '''
        Initializes GRPC channel and stud so that they can be used in encrypt and decrypt functions.
        '''
        # TODO
        channel = grpc.insecure_channel('0.0.0.0:3000')
        self.stub = wallet_pb2_grpc.WalletStub(channel)

    def encrypt(self, plain_text):
        '''
        Encrypts raw card info via stub.
        :param self: the self reference
        :param plain_text: the card details in a dictionary, E.g. plain_text['card_holder_name']
            converts from plain_text => wallet_pb2.Card => wallet_pb2.CardEncryptRequest
        :return: return a protocol buffer card encrypted response.
        :rtype: wallet_pb2.CardEncryptResponse
        '''
        # TODO
        tkn = self.stub.encrypt(wallet_pb2.CardEncryptRequest(card=plain_text))
        return tkn

    def decrypt(self, _token):
        '''
        Decrypts _token via stub.
        :param self: the self reference
        :param _token: the encrypted token
        :return: return a protocol buffer card decrypted response.
        :rtype: wallet_pb2.CardDecryptResponse
        '''
        # TODO
        res = self.stub.decrypt(wallet_pb2.CardDecryptRequest(token=_token))
        return res
if __name__ == '__main__':
    w = WalletClient()
    plain_text = {}
    plain_text['card_holder_name'] = "Foo Bar"
    plain_text['card_number'] = "4012888888881881"
    plain_text['card_expiry_yyyymm'] = 201804
    _token = w.encrypt(plain_text)
    _card = w.decrypt(_token.token)
    print _token.token
    print _card.card_in_plain_text


