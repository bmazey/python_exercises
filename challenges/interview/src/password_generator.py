import random
import string


class PasswordGenerator(object):
    """this is a low quality PasswordGenerator"""

    @staticmethod
    def generate_password():
        # TODO - implement this method!

        symbols = {'!', '@', '#', '$', '%', '^', '&', '*'}
        password = ''
        for i in range(0, 4):
            password += str(random.choice(string.letters))

        for x in range(0, 3):
            password += random.randint(0, 9)

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
