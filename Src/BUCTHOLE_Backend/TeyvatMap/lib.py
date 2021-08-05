import time
import jieba


###### LIB_FUNC
from TeyvatMap.filter import BasicFliter


def get_local_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def Is_Int(x):
    # 先判断是不是数字，如果是的话判断是不是int
    # Status False 不是Int
    # Status True 是Int
    def Is_Num(x):
        try:
            s = float(x)
            return True
        except ValueError as e:
            return False

    if (Is_Num(x) == True):
        if (type(eval(x)) != int):
            return False
        else:
            return True
    else:
        return False


NLP_Replace_Dict = ["，", "。", ".", ",", "!", "?", "！", "？", "…", " "]


def NLP_JudgeMain(str):
    # BASIC SPLIT
    str_list = jieba.lcut(str)
    str_list = NLP_Remove(str_list)
    # START CALL NLP FUNC
    ## DEBUG
    # NLP_Direct(str_list)
    ## SLANG DETECT
    # NLP_TextFliter(str_list)
    NLP_NaiveTextFliter(str_list)
    NLP_Direct(str_list)
    return str_list


def NLP_Remove(str_list):
    new_str_list = []
    for i in range(len(str_list)):
        temp = str_list[i]
        NLP_Replace(temp)
        if temp != "":
            new_str_list.append(temp)
    str_list = new_str_list
    del new_str_list
    return str_list


def NLP_Replace(temp):
    global NLP_Replace_Dict
    for i in range(len(NLP_Replace_Dict)):
        temp = temp.replace(NLP_Replace_Dict[i], "")
    return temp

def NLP_Replace_Slang(temp):
    NLP_Replace_Dict_Slang = ["习近平", "傻逼", "NMSL", "共产党", "妈", "🐎", "逼", "批", "吊", "屌"]
    for i in range(len(NLP_Replace_Dict_Slang)):
        # print(NLP_Replace_Dict_Slang[i])
        # temp = temp.replace(NLP_Replace_Dict_Slang[i], "*")
        if temp == NLP_Replace_Dict_Slang[i]:
            temp="*"
    print(temp)
    return temp


def NLP_Direct(x):
    print(x)


def NLP_TextFliter(str_list):
    # https://github.com/observerss/textfilter
    BasicFliter()
    for i in range(len(str_list)):
        str_list[i] = filter(str_list[i], "*")
    return str_list
    # with open("slangwords.txt", 'rb') as f:
    #     for x in f.readlines():
    #         for i in range(len(str_list)):
    #             if(str_list[i] == x):
    #                 replace(str_list[i],"*")
    # return str_list

def NLP_NaiveTextFliter(str_list):
    for i in range(len(str_list)):
        # print(str_list[i])
        NLP_Replace_Slang(str_list[i])
    return str_list
