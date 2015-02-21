# -*- coding: utf-8 -*-
"""
手机里面导出的vcf文件,	去除其中重复的.
名字相同但是号码不同不被视作重复
"""
vcf_f=open("aaa.vcf")

vcfs=vcf_f.readlines()

x=0 # 统计共有单独号码的账户用
vcf_dic={}
for n in range(0,len(vcfs)):
	if vcfs[n].split(":")[0]=="END" and vcfs[(n-6)].split(":")[0]=="BEGIN":
		print "OK"
		x+=1
		number=str(int(vcfs[(n-2)].split(":")[1].strip()))
		print number
		all_name=vcfs[(n-6)]+vcfs[(n-5)]+vcfs[(n-4)]+vcfs[(n-3)]+vcfs[(n-2)]+vcfs[(n-1)]+vcfs[n]
		vcf_dic[number]=all_name
print "共有多少项目:",x
print "合并后项目数目:", len(vcf_dic.keys())


vcf_f.close()
vcf_newf=open("bbb.vcf","w")
for key in vcf_dic.keys():
	vcf_newf.write(vcf_dic[key])
vcf_newf.close()