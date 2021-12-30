class PrintHelper:
    @staticmethod
    def PrintBanner(printStr, sep='='):
        bannerStr = sep * len(printStr)
        print(bannerStr)
        print(printStr)
        print(bannerStr)