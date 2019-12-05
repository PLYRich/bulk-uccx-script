import pandas as pd
#Formatter for 2 Skills
df = pd.read_csv('test10skills.csv', delimiter=',')
df2 = df.set_index("userID", drop = False)

x = 0
y = 0

for index, row in df.iterrows():
	convert = df.iloc[x,y]
	str(convert)
	print convert
	with open('%s.json' % convert, "w") as f:
		f.write("{"+"\n")
		f.write("	"+'"userID":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("	"+'"firstName":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("	"+'"lastName":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("	"+'"extension":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("	"+'"alias":"'+'"'+","+"\n")
		f.write("	"+'"skillMap":'+"{"+"\n")
		f.write("		"+'"skillCompetency":'+"["+"\n")
		f.write("			{"+"\n") #START 1
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 2
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 3
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 4
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 5
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 6
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 7
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 8
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 9
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			},"+"\n") #END
		f.write("			{"+"\n") #START 10
		f.write("				"+'"competencelevel":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("				"+'"skillNameUriPair":'+"{"+"\n")
		f.write("					"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("					"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("				}"+"\n")
		f.write("			}"+"\n") #END WITHOUT COMMA
		f.write("		]"+"\n")
		f.write("	},"+"\n")
		f.write("	"+'"autoAvailable":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("	"+'"type":'+str(df.iloc[x,y])+","+"\n")
		y=y+1
		f.write("	"+'"team":'+"{"+"\n")
		f.write("		"+'"@name":"'+str(df.iloc[x,y])+'"'+","+"\n")
		y=y+1
		f.write("		"+'"refURL":"'+str(df.iloc[x,y])+'"'+"\n")
		y=y+1
		f.write("	},"+"\n")
		f.write("	"+'"primarySupervisorOf"'+":{"+"\n")
		f.write("	},"+"\n")
		f.write("	"+'"secondarySupervisorOf"'+":{"+"\n")
		f.write("	}"+"\n")
		f.write("}"+"\n")
		y = 0
		x = x + 1
