import random


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        symbols = '!@#$%^&*'
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        numbers = '123456789'
        password = ''

        for i in range(5):
            password += random.choice(alpha)

        for x in range(4):
            password += random.choice(numbers)

        for j in range(1):
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
