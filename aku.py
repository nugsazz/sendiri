# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="EmsYB6rB4X9myTIDn4U8.0DEQnvpe1ZLbOU6IqSTPca.3CDVNjkyqtjBpTev4+GCh+jeWYDpIuZIV/BqnA4oF7A=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EmKL3j64LKZSIXdyEtF0.WAyfme1yf6BASHkM/2yRKa.Ys5p2+o/5o80ncdHmX6K5+ZRo2xIIUVxb9B282L7pmk=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EmFvVIkUM7smC5ZqA3R8.sGd5WWqmO7ZOk9A28oPlsa.awY9IX7Bw8cRqz0GKy2Xw1/ki067lJMWZgsS3JOP0R0=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="Emy2dQfzmlO270Sx5mBb./NhWDXfXHs3T5T7YF5IHMW.QzgOnLuHYXCpZ47fqj/S6AjOA31j7j9oeKMhpdyqlx0=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EmrZsO0DEVo32vSp4tp2.uswj2+OcNnhQeebdZ3lRyG.0BzX7dvjU/LSEm7siicnSu8c554D55GjVT4flUHnSSs=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EmrJgbATPWnoZoHyAOzd.GW2pIkpNiRtQdGpi2mzKpq.3haN8/JmV16xv6EEX07BsRTf1Q0J1Gi8IuLw5VGxvqY=")
ki5.loginResult()

print "Iphenk login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" **☬F.A.F PROTECT☬**
↠ Self Command↞
☬ [Bot]                    
☬ [Group id]       
☬ [Ginfo]           
☬ [Mid all]
☬ [Respon]
☬ [Speed]   
☬ [Banlist]
☬ [Gn G.Name]
☬ [Cancel]
☬ [Tag All]
☬ [View]
☬ [Open]
☬ [Close]
☬ [Stafflist]
☬ [Set]  
☬ [Name: 'text']
☬ [All: 'text']
☬ [Add staff]
☬ [Remove staff]
☬ [Setp] [cek]
☬ [/invitemeto:]
☬ [Bc 'text']
☬ [FAF out]
☬ [LG]
☬ [LG2]
☬ [Bc]
☬ [Mid @]
☬ [Bot Like]
☬ [Like]
☬ [/invitemeto:]

↠KICKER↞
**Protect F.A.F Group**
☬ [Banned @] 
☬ [Unban @]  
☬ [Kill @]  
☬ [Nk @] 
☬ [Vk @]
☬ [All] 
☬ [Mayhem]
☬ [Clear ban]
"""

Setgroup =""" **F.A.F Protection Key**
☬ [AllProtection]~[Fras on - off]
☬ [3 Protect QR]~[Qr on - off]
☬ [Mid Check]~[Contact On - Off]
☬ [2 Reject Invite]~[Jn on - off]
☬ [4 Protect Cancel]~[Cn on - off]
☬ [1 Member Protect]~[M on - off]
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = ki2.getProfile().mid
Cmid = ki3.getProfile().mid
Dmid = ki4.getProfile().mid
Emid = ki5.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,"ud1d7aa3553c4d73941a2eea242cb6908"]
admin = ["ud1d7aa3553c4d73941a2eea242cb6908"]
staff = ["ud1d7aa3553c4d73941a2eea242cb6908"]
adminMID = "ud1d7aa3553c4d73941a2eea242cb6908"
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"IP ディータ",
    "cName2":"ディータ1つ " , 
    "cName3":"ディータ二人 ",
    "cName4":"ディータ三 ",
    "cName5":"ディータ4人 ",
    "cName6":"ディータ五 ",
    "cName7":"ディータ6 ",
    "cName8":"ディータ7人 ",
    "cName9":"ディータ8人 ",
    "cName10":"ディータ9人 ",
    "cName11":"ディータ10人 ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":True,
    "Protectgr":{},
    "Protectguest":{},
    "Protectcancel":{},
    "protectionOn":{},
    "atjointicket":True,
    "MProtection":{},
    "AllProtection":{},
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        #-------Protect Qr-------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
                        
        #------Finish------#
        # -INV KICK- #
        if op.type == 13:
            if wait["Protectguest"] == True:
                if op.param2 in Bots or staff:
                	pass
                else:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                        wait["blacklist"][op.param2] = True
        #------FINISH------#
        
        #--CANCEL KICK--#
        if op.type == 32:
            if wait["Protectcancel"] == True:
                if op.param2 not in Bots or staff:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
            #------FINISH------#
        if op.type == 15:
            random.choice(KAC).sendText(op.param1, cl.getContact(op.param2).displayName + " Good Bye\n(*´･ω･*)")
            print op.param3 + "has left the group"
        
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                
            if op.param3 in Bmid:
                if op.param2 in Cmid:
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    
            if op.param3 in Cmid:
                if op.param2 in Dmid:
                    X = ki4.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    
            if op.param3 in Dmid:
                if op.param2 in Emid:
                    X = ki5.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki4.updateGroup(X)
                    Ti = ki4.reissueGroupTicket(op.param1)
                    
            if op.param3 in Emid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki5.updateGroup(X)
                    Ti = ki5.reissueGroupTicket(op.param1)            
                    
        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.knviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True
			
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ti = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True
                        
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki4.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki4.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        #if op.param2 in wait["whitelist"]:
                            #pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki4.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki5.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki5.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki4.updateGroup(G)
                    Ticket = ki5.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    #if op.param2 in wait["whitelist"]:
                        #pass
                    else:
                        wait["blacklist"][op.param2] = True                        
                       
        if op.type == 19:
                if op.param3 in Bots:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots and staff:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                if op.param2 in wait["blacklist"]:
                    pass
                #if op.param2 in wait["whitelist"]:
                    #pass
                else:
                    wait["blacklist"][op.param2] = True
                    
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in staff:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
		
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ki.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ki.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ki.sendText(msg.to,"already")
                        #ki.sendText(msg.to,"already")
                        #kk.sendText(msg.to,"already")
                        #kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,"aded")
                        #ki.sendText(msg.to,"aded")
                        #kk.sendText(msg.to,"aded")
                        #kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ki.sendText(msg.to,"deleted")
                        #ki.sendText(msg.to,"deleted")
                        #kk.sendText(msg.to,"deleted")
                        #kc.sendText(msg.to,"deleted")
                        #wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        ki.sendText(msg.to,"It is not in the black list")
                        #ki.sendText(msg.to,"It is not in the black list")
                        #kk.sendText(msg.to,"It is not in the black list")
                        #kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Set"]:
                if msg.from_ in Bots or staff:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,Setgroup)
                    else:
                        cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Cv3 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
            	if msg.from_ in Bots and staff:
                    midd = msg.text.replace("Kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "1 kick " in msg.text:
                midd = msg.text.replace("1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "2 kick " in msg.text:
                midd = msg.text.replace("2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "3 kick " in msg.text:
                midd = msg.text.replace("3 kick ","")
                ki3.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
            	if msg.from_ in Bots or staff:
                    midd = msg.text.replace("Invite ","")
                    ki.findAndAddContactsByMid(midd)
                    ki.inviteIntoGroup(msg.to,[midd])
            elif "1 invite " in msg.text:
                midd = msg.text.replace("Cv1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "2 invite " in msg.text:
                midd = msg.text.replace("Cv2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "3 invite " in msg.text:
                midd = msg.text.replace("Cv3 invite ","")
                ki3.findAndAddContactsByMid(midd)
                ki3.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki2.sendMessage(msg)
            elif msg.text in ["3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                ki3.sendMessage(msg)
            elif msg.text in ["4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ki4.sendMessage(msg)
                
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
     #-----Fungsi List Group------#   
            elif msg.text in ["List group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[~]%s\n" % (cl.getGroup(i).name   +str (len (cl.getGroup(i).members)))
                    cl.sendText(msg.to,"========[List Group]========\n"+ h +"Total Group :" +str(len(gid)))
      #-----Finish--------#
      #-------------Fungsi Creator Start-----------------# 
            elif msg.text in ["Creator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    Creatorbot = "u9e5a757e7b6e466baf87e8f747d96eb5"
                    try:
                        msg.contentMetadata = {'mid': Creatorbot}
                        
                    except:
                        Creatorbot = "Error"
                    cl.sendText(msg.to, "My Creator : IP/nhttp://line.me/ti/p/zuFNPuXyEb")
                    cl.sendMessage(msg)
        #-------------Fungsi Creator Finish-----------------# 
        #-------------Fungsi Kick By Tag---------------------#
            elif ("Bye " in msg.text):
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            random.choice(KAC).sendText(op.param1, cl.getContact(op.param3).displayName + " ~Sorry  (*´･ω･*)")
                        except:
                            pass
        #-------------Fungsi Kick By Tag---------------------#
        #-------------Fungsi Ban By Tag---------------------#  
            elif ("BL " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Blacklist")
                   except:
                      pass
        #-------------Fungsi Ban By Tag Finish---------------------#         
            elif msg.text in ["cancel","Cancel"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        if X.invitee is not None:
                            gInviMids = [contact.mid for contact in X.invitee]
                            ki.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                ki.sendText(msg.to,"No one is inviting")
                            else:
                                ki.sendText(msg.to,"Sorry, nobody absent")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open","Link on"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done")
                        else:
                            ki.sendText(msg.to,"already open")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 open","Cv1 link on"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            
            elif msg.text in ["Close","Link off"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        X = ki.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        ki.updateGroup(X)
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Done")
                        else:
                            ki.sendText(msg.to,"already close")
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"Can not be used outside the group")
                        else:
                            ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 close","Cv1 link off"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done ")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ki.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ki.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "Mid all" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                ki2.sendText(msg.to,Bmid)
                ki3.sendText(msg.to,Cmid)
                ki4.sendText(msg.to,Dmid)
                ki5.sendText(msg.to,Emid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Name: " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("Name: ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"name " + string + "Done")
            elif "1Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("1Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki.updateProfile(profile)
                        ki.sendText(msg.to,"name " + string + "Done")
            elif "2Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("2Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki2.updateProfile(profile)
                        ki2.sendText(msg.to,"name" + string + "Done")
            elif "3Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("3Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki3.updateProfile(profile)
                        ki3.sendText(msg.to,"name" + string + "Done")
            elif "4Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("4Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki4.updateProfile(profile)
                        ki4.sendText(msg.to,"name" + string + "Done")
            elif "5Up n " in msg.text:
            	if msg.from_ in Bots:
                    string = msg.text.replace("5Up n ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        ki5.updateProfile(profile)
                        ki5.sendText(msg.to,"name" + string + "Done")
                    
            elif "All: " in msg.text:
                string = msg.text.replace("All: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki2.updateProfile(profile)
                    ki3.updateProfile(profile)
                    ki4.updateProfile(profile)
                    ki5.updateProfile(profile)
                    ki.sendText(msg.to,"name" + string + "Done")
                    ki2.sendText(msg.to,"name" + string + "Done")
                    ki3.sendText(msg.to,"name" + string + "Done")
                    ki4.sendText(msg.to,"name" + string + "Done")
                    ki5.sendText(msg.to,"name" + string + "Done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #---------------#
            elif msg.text in ["Arie on"]:
            	if msg.from_ in Bots or staff:
            	    if wait["AllProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        wait["Protectguest"] = True
                        wait["Protectgr"] = True
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection On")
                        else:
                            cl.sendText(msg.to,"done")                        
            elif msg.text in ["Arie off"]:
            	if msg.from_ in Bots or staff:
            	    if wait["AllProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        wait["Protectguest"] = False
                        wait["Protectgr"] = False
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"All Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["M on"]:
                if msg.from_ in Bots or staff:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["M off"]:
                if msg.from_ in Bots or staff:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Member Protection Off")
                        else:
                            cl.sendText(msg.to,"done") 
            elif msg.text in ["Blockinvite on","guest on","Jn on"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectguest"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Block Invitation On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Jn off","guest off"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectguest"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectguest"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Blockinvitation Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectgr"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection On")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectgr"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectgr"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"QR Protection Off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Cn on","proc on"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectcancel"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Cn off","proc off"]:
                if msg.from_ in Bots or staff:
                    if wait["Protectcancel"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["Protectcancel"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Protect cancel off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
            	if msg.from_ in admin or staff:
                    if wait["contact"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["contact"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
            	if msg.from_ in admin or staff:
                    if wait["contact"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done ")
                    else:
                        wait["contact"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
            	if msg.from_ in admin or staff:
                    if wait["autoJoin"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
            	if msg.from_ in admin or staff:
                    if wait["autoJoin"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["autoJoin"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
            	if msg.from_ in admin or staff:
                    if wait["leaveRoom"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
            	if msg.from_ in admin or staff:
                    if wait["leaveRoom"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["leaveRoom"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
            	if msg.from_ in admin or staff:
                    if wait["timeline"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already on")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
            	if msg.from_ in admin or staff:
                    if wait["timeline"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"already off")
                        else:
                            cl.sendText(msg.to,"done")
                    else:
                        wait["timeline"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"done")
                        else:
                            cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["View"]:
                md = ""
                if wait["MProtection"] == True: md+=" MProtection : on\n"
                else: md+=" MProtection  : off\n"
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["Protectgr"] == True: md+=" Protectgr      : on\n"
                else: md+=" Protectgr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                else:md+=" Auto Join Group by Ticket : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
                    
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
                
            elif msg.text in ["Cancelall"]:
            	if msg.from_ in admin or staff:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All invitations have been refused")
                    else:
                        cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------                    
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    kk.sendText(msg.to, "Check sider")
                    kc.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["Join","one","One"]:
                if msg.from_ in admin or Bots:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)
                        
            elif msg.text in ["All","."]:
                if msg.from_ in  Bots or staff:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        cl.updateGroup(G)

#-----------------------------------------------
            elif msg.text in ["Bye wm"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)                        
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                            ki6.leaveGroup(msg.to)
                            ki7.leaveGroup(msg.to)                        
			    ki8.leaveGroup(msg.to)
			    ki9.leaveGroup(msg.to)
			    ki10.leaveGroup(msg.to)
			    cl.leaveGroup(msg.to)
                        except:
                            pass
#-----------------------------------------------
            elif msg.text in ["Bye"]:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                            ki2.leaveGroup(msg.to)
                            ki3.leaveGroup(msg.to)                        
			    ki4.leaveGroup(msg.to)
			    ki5.leaveGroup(msg.to)
                        except:
                            pass
#-----------------------------------------------
#-------------Fungsi Tagall User Start---------------#  
            elif msg.text in ["Cipok","Tagall"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in staff:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in staff:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass                      
#-----------------------------------------------
            elif msg.text in ["Kill"]:
            	if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        group = ki.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"Sorry!!")
                            ki2.sendText(msg.to,"（´・ω・｀)")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
      
#---------------kickall started----------------#                   
            elif "Mayhem" in msg.text:
              if msg.from_ in Bots or staff:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n abort to abort♪")
                    ki2.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\nhələbəˈlo͞o hələbəˌlo͞o")
                    ki3.sendText(msg.to,"Good Bye (*´･ω･*)")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki2.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if target not in Bots and staff:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki3.sendText(msg.to,"Mayhem done")
#-----------------------[Cleanse Edited By Toby]------------------------
            elif msg.text in ["Cleanse","cleanse"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Saya bersihkan","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        gs = ki4.getGroup(msg.to)
                        gs = ki5.getGroup(msg.to)
                        ki2.sendText(msg.to,"Group cleansing begin")
                        ki3.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Agar Bot dan Admin Tidak DiKick]----------------
                        targets.remove(adminMID)
                        targets.remove(mid)
                        targets.remove(Amid)
                        targets.remove(Bmid)
                        targets.remove(Cmid)
                        targets.remove(Dmid)
                        targets.remove(Emid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:

                                    klist=[ki,ki2,ki3,ki4,ki5]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"                                   
#----------------kickall finish----------------------#
                                   
            elif "Kickuk" in msg.text:
                if msg.from_ in admin or staff:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Kickuk","")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        #ki.sendText(msg.to,"Just some casual cleansing ô")
                        #ki2.sendText(msg.to,"Group cleansed.")
                        #ki3.sendText(msg.to,"Fuck You All")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                            ki2.sendText(msg.to,"Not found.")
                            ki3.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                            	if target not in Bots and admin:
                                    try:
                                        klist=[ki,ki2,ki3,ki4,ki5]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        ki.sendText(msg.to,"Group cleanse")
                                        ki2.sendText(msg.to,"Group cleanse")
                                        ki3.sendText(msg.to,"Group cleanse")
                                   
            elif "Nk " in msg.text:
                  if msg.from_ in Bots or staff:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,ki2,ki3,ki4,ki5]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Sorry...")
                                    ki3.sendText(msg.to,"（´・ω・｀)")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass                                    
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Succes ")
                                except:
                                    ki.sendText(msg.to,"error")
            elif "Banned @" in msg.text:
                if msg.from_ in Bots or staff:
                    if msg.toType == 2:
                        print "[Banned] Sukses"
                        _name = msg.text.replace("Banned @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        gs = ki3.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Dilarang Banned Bot")
                            #ki.sendText(msg.to,"Dilarang Banned Bot")
                            #ki2.sendText(msg.to,"Dilarang Banned Bot")
                            #ki3.sendText(msg.to,"Dilarang Banned Bot")                        
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Akun telah sukses di banned")
                                except:
                                    ki.sendText(msg.to,"Error")
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #----------------------------------------- 
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                random.choice(KAC).sendText(msg.to,"Clear All Ban Done")            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
            #----------------Fungsi Unbanned User Target Finish-----------------------#
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in staff:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = ki2.getGroupIdsJoined()
                 a = ki3.getGroupIdsJoined()
                 a = ki4.getGroupIdsJoined()
                 a = ki5.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     ki2.sendText(taf, (bctxt))
                     ki3.sendText(taf, (bctxt))
                     ki4.sendText(taf, (bctxt))
                     ki5.sendText(taf, (bctxt))
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
        #------------ Keluar Dari Semua Group------
            elif msg.text in ["FAF out","Op bye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in admin:
                 #gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = ki2.getGroupIdsJoined()
                 gid = ki3.getGroupIdsJoined()
                 gid = ki4.getGroupIdsJoined()
                 gid = ki5.getGroupIdsJoined()
                 for i in gid:
                   ki5.leaveGroup(i)
                   ki4.leaveGroup(i)
                   ki3.leaveGroup(i)
                   ki2.leaveGroup(i)
                   ki.leaveGroup(i)
                   #cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Sayonara")
                 else:
                   cl.sendText(msg.to,"He declined all invitations")        
#-----------------------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki2.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
                ki3.sendText(msg.to,"Ok  􀨁􀄻double thumbs up􏿿")
#-----------------------------------------------
            #elif "Bc " in msg.text:
				#bctxt = msg.text.replace("Bc ","")
				#ki.sendText(msg.to,(bctxt))
				#ki2.sendText(msg.to,(bctxt))
				#ki3.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["say hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki3.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Chivas Family Room")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            
#-----------------------------------------------
            elif msg.text in ["Respon","respon"]:
                ki.sendText(msg.to,"ON BRO")
                ki2.sendText(msg.to,"ON BRO")
                ki3.sendText(msg.to,"ON BRO")
                ki4.sendText(msg.to,"ON BRO")
#-----------------------------------------------
            
            elif "Spam " in msg.text:
              if msg.from_ in Bots or staff:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #Keke cantik <3
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
            
            elif msg.text == "Setp":
                    cl.sendText(msg.to, "Setpoint Telah Dipasang")                    
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print wait2
                
            elif msg.text == "Cek":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "==== Tercyduk ==== %s\n\n==== Tersangka ====\n%s\n\nSetpoint Pada :\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Setpoint Dulu Tolol (Har Har) 「Setp」")
                    pass
                
            elif msg.text in ["Sp","Speedbot","speedbot"]:
            	if msg.from_ in Bots or staff:
                    start = time.time()
                    cl.sendText(msg.to, "Waiting...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    
            elif "Add staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove staff @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Add admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin add executing"
                    _name = msg.text.replace("Add admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the admin list")
                            except:
                                pass
                    print "[Command]admin add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif "Remove admin @" in msg.text:
                if msg.from_ in Bots:
                    print "[Command]admin remove executing"
                    _name = msg.text.replace("Remove admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    #gs = kk.getGroup(msg.to)
                    #gs = kc.getGroup(msg.to)
                    #gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the admin list")
                            except:
                                pass
                    print "[Command]admin remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    
            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
            
            elif msg.text in ["Admin list","admin list"]:
                if admin == []:
                    ki.sendText(msg.to,"The stafflist is empty")
                else:
                    ki.sendText(msg.to,"Admin list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"
                    
            elif msg.text in ["Ip Like", "Ar like"]:
                if msg.from_ in staff:
                    print "[Command]Like executed"
                    cl.sendText(msg.to,"Trying to Like post(s) from staff")
                    try:
                        likePost()
                    except:
                        pass

#------------------------------------------------------------------
            elif msg.text in ["Banned"]:
            	if msg.from_ in admin or staff:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unbanned"]:
            	if msg.from_ in admin or staff:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"send contact")
                    
        #---------Fungsi Banlist With Tag--------#
            elif msg.text in ["Banlist","ip banlist"]:
                if wait["blacklist"] == {}:
                    ki.sendText(msg.to,"No user is Blacklisted")
                else:
                    ki.sendText(msg.to,"Blacklisted user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ki.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
        #---------Fungsi Banlist With Tag Finish--------#
        
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill"]:
            	if msg.from_ in admin or staff:
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ki.sendText(msg.to,"There was no blacklist user")
                        #ki2.sendText(msg.to,"There was no blacklist user")
                        #ki3.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        ki.cancelGroupInvitation(msg.to,[_mid])
                    ki.sendText(msg.to,"I pretended to cancel and canceled.")
            
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
                        
            elif "midb:" in msg.text:
                midd = msg.text.replace("midb:","")
                wait["blacklist"][midd] = True
            
            elif "#終了" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
        
        if op.type == 55:
             print "[NOTIFIED_READ_MESSAGE]"
             try:
                 if op.param1 in wait2['readPoint']:
                     Nama = cl.getContact(op.param2).displayName
                     if Nama in wait2['readMember'][op.param1]:
                           pass
                     else:
                            wait2['readMember'][op.param1] += "\n-> " + Nama
                            wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                 else:
                        cl.sendText
             except:
                 pass
             
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Fras\n\nhttp://line.me/ti/p/~fras88")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by Fras\n\nhttp://line.me/ti/p/~fras88")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
time.sleep(0.60)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by ^F.A.F^\nStatus Boss udah Kami Like\nOwner Kami :\nFras")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like BOS"

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
