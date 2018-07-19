import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        #no lists needed
        symbols = '!@#$%^&*'
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        password = ''

        for i in range(0, 4):
            password += random.choice(alpha)

        for x in range(0, 3):
            password += str(random.randint(0, 9))

        password += random.choice(symbols)

        return password

    #
    #                       _oo0oo_
    #                      o8888888o
    #                      88" . "88
    #                      (| -_- |)
    #                      0\  =  /0
    #                    ___/`---'\___
    #                  .' \\|     |# '.
    #                 / \\|||  :  |||# \
    #                / _||||| -:- |||||- \
    #               |   | \\\  -  #/ |   |
    #               | \_|  ''\---/''  |_/ |
    #               \  .-\__  '-'  ___/-. /
    #             ___'. .'  /--.--\  `. .'___
    #          ."" '<  `.___\_<|>_/___.' >' "".
    #         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
    #         \  \ `_.   \_ __\ /__ _/   .-` /  /
    #     =====`-.____`.___ \_____/___.-`___.-'=====
    #                       `=---='
    #
    #
    #     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    #               佛祖保佑         永无BUG
    #
    #
