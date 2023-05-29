from xmindparser import xmind_to_dict
import xlwt


def getXmind(path):

    xmd=xmind_to_dict(path)
    print(xmd)
    case=[]

    for i in xmd[0]["topic"]["topics"]:
        csyl = xmd[0]["topic"]["title"]


        for j in i["topics"]:
            mk=i["title"]
            for k in j["topics"]:
                zc=j["title"]
                case_list=[]
                #print("k is %s"%(k))
                tl=k["title"]
                ca=k["topics"]
                ca_qz=ca[0]["title"]
                ca_bz=ca[0]["topics"][0]["title"]
                ca_zg=ca[0]["topics"][0]["topics"][0]["title"]
                case_list.append(csyl)
                case_list.append(mk)

                case_list.append(zc)
                case_list.append(tl)
                case_list.append(ca_qz)
                case_list.append(ca_bz)
                case_list.append(ca_zg)
                case.append(case_list)
    return case
def updateExecl(workBookPath,data_list):
    book=xlwt.Workbook(encoding="utf-8")
    sheetname=book.add_sheet("测试用例")
    col_title=("功能","模块","场景区分","用例标题","前置条件","操作步骤","逾期结果")
    for i in range(0,7):
        sheetname.write(0,i,col_title[i])
    for i in range(0,len(data_list)):
        data=data_list[i]
        for j in range(0,len(data)):
            sheetname.write(i+1,j,data[j])
    book.save(workBookPath)




if __name__ == '__main__':
   path=r"C:\pythonProject1\com\myproject\file\测试用例.xmind"
   data=getXmind(path)
   print(data)
   updateExecl(r"C:\pythonProject1\com\myproject\file\测试用例.xlsx",data)