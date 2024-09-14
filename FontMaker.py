from PIL import Image, ImageDraw, ImageFont
import os,glob
import numpy as np
import random
from matplotlib import font_manager

charactersList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

fonts = ["Arial.ttf","Ariali.ttf","Arialbd.ttf","Arialbi.ttf","Ariblk.ttf","Bahnschrift.ttf","Calibril.ttf","Calibrili.ttf","Calibri.ttf","Calibrii.ttf","Calibrib.ttf","Calibriz.ttf","Cambria.ttc","Cambriai.ttf","Cambriab.ttf","Cambriaz.ttf","Cambria.ttc","Candaral.ttf","Candarali.ttf","Candara.ttf","Candarai.ttf","Candarab.ttf","Candaraz.ttf","CascadiaCode.ttf","CascadiaCode Italic.ttf","CascadiaCode.ttf","CascadiaCode.ttf","CascadiaCode Italic.ttf","CascadiaCode.ttf","CascadiaCode Italic.ttf","CascadiaCode.ttf","CascadiaCode Italic.ttf","CascadiaCode.ttf","CascadiaCode Italic.ttf","CascadiaCode.ttf","CascadiaMono.ttf","CascadiaMono Italic.ttf","CascadiaMono.ttf","CascadiaMono.ttf","CascadiaMono Italic.ttf","CascadiaMono.ttf","CascadiaMono Italic.ttf","CascadiaMono.ttf","CascadiaMono Italic.ttf","CascadiaMono.ttf","CascadiaMono Italic.ttf","CascadiaMono.ttf","Comic.ttf","Comici.ttf","Comicbd.ttf","Comicz.ttf","Consola.ttf","Consolai.ttf","Consolab.ttf","Consolaz.ttf","Constan.ttf","Constani.ttf","Constanb.ttf","Constanz.ttf","Corbell.ttf","Corbelli.ttf","Corbel.ttf","Corbeli.ttf","Corbelb.ttf","Corbelz.ttf","Cour.ttf","Couri.ttf","Courbd.ttf","Courbi.ttf","Ebrima.ttf","Ebrimabd.ttf","Framd.ttf","Framdit.ttf","Gabriola.ttf","Gadugi.ttf","Gadugib.ttf","Georgia.ttf","Georgiai.ttf","Georgiab.ttf","Georgiaz.ttf","Holomdl2.ttf","Impact.ttf","Inkfree.ttf","Javatext.ttf","Leelawui.ttf","Leeluisl.ttf","Leelauib.ttf","Lucon.ttf","L_10646.ttf","Malgun.ttf","Malgunbd.ttf","Malgunsl.ttf","Marlett.ttf","Himalaya.ttf","Msjhl.ttc","Msjh.ttc","MSJHBD.ttc","Msjhl.ttc","Msjh.ttc","MSJHBD.ttc","Ntailu.ttf","Ntailub.ttf","Phagspa.ttf","PhagsPaB.ttf","Micross.ttf","Taile.ttf","TaiLeb.ttf","Msyhl.ttc","Msyh.ttc","Msyhbd.ttc","Msyhl.ttc","Msyh.ttc","Msyhbd.ttc","Msyi.ttf","Mingliub.ttc","Mingliub.ttc","Mingliub.ttc","Monbaiti.ttf","Msgothic.ttc","Msgothic.ttc","Msgothic.ttc","Mvboli.ttf","Mmrtext.ttf","Mmrtextb.ttf","Nirmalas.ttf","Nirmala.ttf","Nirmalab.ttf","Pala.ttf","Palai.ttf","Palab.ttf","Palabi.ttf","SegoeIcons.ttf","Segmdl2.ttf","Segoepr.ttf","Segoeprb.ttf","Segoesc.ttf","Segoescb.ttf","Segoeuil.ttf","Seguili.ttf","Segoeuisl.ttf","Seguisli.ttf","Segoeui.ttf","Segoeuii.ttf","Seguisb.ttf","Seguisbi.ttf","Segoeuib.ttf","Segoeuiz.ttf","Seguibl.ttf","Seguibli.ttf","Seguiemj.ttf","Seguihis.ttf","Seguisym.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","SegUIVar.ttf","Simsun.ttc","Simsun.ttc","Simsunb.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","SitkaVF.ttf","SitkaVF-Italic.ttf","Sylfaen.ttf","Symbol.ttf","Tahoma.ttf","Tahomabd.ttf","Times.ttf","Timesi.ttf","Timesbd.ttf","Timesbi.ttf","Trebuc.ttf","Trebucit.ttf","Trebucbd.ttf","Trebucbi.ttf","Verdana.ttf","Verdanai.ttf","Verdanab.ttf","Verdanaz.ttf","Webdings.ttf","Wingding.ttf","YuGothL.ttc","YuGothR.ttc","Yugothm.ttc","YuGothB.ttc","YuGothL.ttc","YuGothR.ttc","Yugothm.ttc","YuGothB.ttc","YuGothB.ttc"]

for y in fonts:
    count = 0
    for x in charactersList:
        try:
            im = Image.new(mode = "RGB", size = (32, 32),
                                   color = (255, 255, 255))

            d = ImageDraw.Draw(im)
            font = ImageFont.truetype(y.lower(), size=24)
            if os.path.exists(f"./fontPics/{y}"):
                pass
            else:
                os.mkdir(f"./fontPics/{y}")

            d.text((15,20),x,align='center',anchor="ms", font=font, fill=(0,0,0))

            im.save(f"./fontPics/{y}/{y+str(count)+x}.jpg")

            count += 1

        except:
            pass
            #print("failed")