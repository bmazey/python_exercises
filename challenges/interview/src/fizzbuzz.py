class FizzBuzz(object):
    """this is our FizzBuzz class"""

    # test
    # hello!
    @staticmethod
    def fizzbuzz(i):
        # TODO - implement this method!
        if i % 15 == 0:
            string = 'fizzbuzz'
        elif i % 5 == 0:
            string = 'buzz'
        elif i % 3 == 0:
            string = 'fizz'
        else:
            string = ''

        return string

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


