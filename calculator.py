print("--Calculator--")
ehnii_too = int(input("Ehnii too:"))
daraagiin_too = int(input("Daraagiin too:"))
nemeh = "nemeh"
print(nemeh)
hasah = "hasah"
print(hasah)
urjih = "urjih"
print(urjih)
huvaah = "huvaah"
print(huvaah)
zeregt_devshuuleh = "zeregt devshuuleh"
print(zeregt_devshuuleh)
kvadrat_yzguur = "kvadrat yzguur"
print(kvadrat_yzguur)
uldegdel = "uldegdel"
print(uldegdel)
garah = "garah"
print(garah)
songoson_uildel = input("uildelee songooroi:")
print("songoson_uildel:" + songoson_uildel)
import math
history = []

if songoson_uildel == "nemeh":
    hariu = ehnii_too + daraagiin_too
elif songoson_uildel == "hasah":
    hariu = ehnii_too - daraagiin_too
elif songoson_uildel == "urjih":
    hariu = ehnii_too * daraagiin_too
elif songoson_uildel == "huvaah":
    if daraagiin_too != 0:
        hariu = ehnii_too // daraagiin_too
    else:
        hariu = "toog 0d huvaaj bolohguiee bro"
elif songoson_uildel == "zeregt devshuuleh":
    hariu = ehnii_too ** daraagiin_too
elif songoson_uildel == "kvadrat yzguur":
    hariu = math.sqrt(ehnii_too), math.sqrt(daraagiin_too)
elif songoson_uildel == "uldegdel":
    hariu = ehnii_too / daraagiin_too
else:
    hariu = "iim uildel bhguie"
print(f"Hariu ni: {hariu}")

