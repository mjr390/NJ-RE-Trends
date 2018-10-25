
# coding: utf-8

# In[ ]:


# ATTOMDATA call
import http.client
# from ib_proj3_config import API_KEY
from jons_config import api_key
from pprint import pprint
import json
import pandas as pd
import time
import pymongo
import ast
import os

 # Create connection variable for Project3 database in MLab
#     mongodb://<dbuser>:<dbpassword>@ds137003.mlab.com:37003/project3
#         connMLAB = 'mongodb://localhost:27017'
# connMLAB = "mongodb://ibaloyan:francis99@ds137003.mlab.com:37003/project3"
connMLAB = "mongodb://jonathan:Biomed#101@ds137003.mlab.com:37003/project3"

# connMLAB = "mongodb://grothjd:Biomed#101@ds137003.mlab.com:37003/"


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(connMLAB)

# Connect to a database. Will create one if not already available.
# db = client.Apple_y_y
# Fix done for Heroku deployment
# db = client.heroku_8nx1c4b9
db = client.project3

# Drops collection if available to remove duplicates
#     db.apple_y_o_y.drop()
# ???    db.zip_community.drop()


# In[ ]:


# Go through zips from the refernce file

# Get Zip codes, etc. from the reference file
# zipCs = pd.read_csv('C:/Users/Inna/Documents/ZIPtoCITYtoCOUNTY.csv')
# zipCs = pd.read_csv('C:/Users/Inna/Desktop/NJ-RE-Trends/data/ZIPtoCITYtoCOUNTY.csv')
# zipCs = pd.read_csv('data/ZIPtoCITYtoCOUNTY.csv')
zipCs = pd.read_csv('data/ZIPtoCITYtoCOUNTY_test.csv')
# #####print ( zipCs)

# Get 0 in front of 4 digit zip code
string_codes = []
for row in zipCs["Zip Code"]:
    new = '0' + str(row)
    string_codes.append(new)
zipCs["Zip Code"] = string_codes   

zipCs = zipCs[["Zip Code", "City", "County"]]
# print (zipCs)
ziptest = zipCs.iloc[1]
ziptest


# In[ ]:


# loop through all zip codes
for zipC in zipCs ["Zip Code"]:

    conn = http.client.HTTPSConnection("search.onboard-apis.com")

    headers = {

       'accept': "application/json",
       'apikey': api_key,

       }
## conn.request("GET", "/propertyapi/v1.0.0/property/detail?address1=4529%20Winona%20Court&address2=Denver%2C%20CO", headers=headers)
# Manalapan county
# conn.request("GET", "/communityapi/v2.0.0/Area/Full/?AreaId=CO34025", headers=headers)
# conn.request("GET", "/communityapi/v2.0.0/Area/Full/?AreaId=ZI07726", headers=headers)
        
#     com_url = '/propertyapi/v1.0.0/property/expandedprofile?address1=' + firstPart + "&address2=" + secondPart + "%2C+NJ"
#     conn.request("GET", com_url, headers=headers) 
    conn.request("GET", "/poisearch/v2.0.0/poi/geography?PostalCodeKey=" + zipC + "&SearchDistance=5&RecordLimit=100" + zipC, headers=headers)

    # Get response record in json format
    res = conn.getresponse()
    
    


    # res = { "response": {"inputparameter": {"AreaId": "ZI07726", "package": "Full", "resource": "Area", "service": "Community" }, "result": {"package": {"descr": "",  "item": [ {"age00_04": "2405", "age05_09": "2298", "age10_14": "2695", "age15_19": "3957", "age20_24": "3010", "age25_29": "2535", "age30_34": "1831", "age35_39": "1802", "age40_44": "2434", "age45_49": "3124", "age50_54": "3811", "age55_59": "3951", "age60_64": "3369", "age65_69": "2821", "age70_74": "1856", "age75_79": "1158", "age80_84": "824", "ageavepy_10": "43.48", "ageavepy_5": "42.55", "agegt85": "892", "aimcy25_44": "117427", "aimcy45_64": "129328", "aimcygt_65": "43283", "aimcylt_25": "105625", "airport": "Newark Liberty International", "airportdist": "29", "airx": "0", "ancestamer": "3297", "ancestamind": "15", "ancestasian": "3261", "ancesteuro": "23406", "ancesthawai": "7", "ancesthisp": "2465", "ancestother": "8002", "ancestunclassified": "4322", "avg_prop_tax": "8138", "avg_prop_tax_year": "2015", "avg_prop_tax_year_count": "15605", "avgsaleprice": "368355", "carbmono": "0", "city500_closest_name": "New York city, NY", "cocrmcyasst": "34", "cocrmcyburg": "39", "cocrmcylarc": "54", "cocrmcymurd": "41", "cocrmcymveh": "23", "cocrmcyperc": "36", "cocrmcyproc": "37", "cocrmcyrape": "33", "cocrmcyrobb": "33", "cocrmcytotc": "36", "county3": "025", "county5": "34025", "countyname": "Monmouth County", "crmcyasst": "4", "crmcyburg": "6", "crmcylarc": "5", "crmcymurd": "7", "crmcymveh": "5", "crmcyperc": "5", "crmcyproc": "5", "crmcyrape": "5", "crmcyrobb": "3", "crmcytotc": "5", "daypop": "39388", "dwlowned": "13926", "dwlrent": "1589", "dwltotal": "16072", "dwlvacnt": "556", "eduagelt9_00": "624", "eduagelt9_90": "991", "eduassoc": "2118", "eduassoc_00": "1687", "edubach": "8938", "edubach_00": "5791", "educoll_00": "10875", "educoll_90": "7300", "edudegree_00": "3397", "edugrad": "4922", "eduhsch": "7075", "eduhsch_00": "6281", "eduhsch_90": "5760", "eduindex": "4", "edultgr9": "612", "eduscoll": "5460", "eduscoll_00": "4644", "eduscoll_90": "3387", "edushsch": "1283", "edutotalpop": "30408", "edutotalpop_00": "23680", "edutotalpop_90": "18871", "empadmin": "51", "empagric": "42", "emparts": "563", "empconst": "643", "empedu": "293", "empexec": "0", "empfire": "500", "empfood": "927", "emphcsp": "2917", "emphome": "1211", "empinfo": "197", "empmanuf": "1266", "empmil": "0", "empmil_00": "10", "empmine": "11", "empprof": "1007", "emppubad": "787", "empre": "221", "emprtrad": "2128", "empsrv": "813", "emptotal": "13426", "emptrans": "212", "empuncla": "51", "empunemp": "1044", "emputl": "163", "empwtrad": "190", "enrollcoll_00": "1789", "enrollcoll_90": "1686", "enrollelem_00": "5524", "enrollelem_90": "5760", "enrollhsch_00": "2462", "enrollprek_00": "1835", "enrollprek_90": "912", "enrolltotal_00": "11611", "enrolltotal_90": "8358", "expappar": "157", "expcontrib": "161", "expeduc": "163", "expent": "156", "expfoodbev": "147", "expgift": "160", "exphealth": "161", "exphh": "152", "exphhfurn": "157", "exphhops": "161", "expinsur": "175", "expmisc": "149", "exppers": "153", "expread": "153", "exptob": "121", "exptotal": "65181", "exptransport": "145", "exputil": "144", "famavesz": "3.41", "four_bed_county": "2320", "four_bedindex": "88", "fouryr": "TALMUDICAL ACADEMY-NEW JERSEY", "fouryrdist": "7", "geo_code": "07726", "geo_key": "ZI07726", "geo_type": "Zip Code", "hhd": "15515", "hhd_00": "12496", "hhd_90": "9650", "hhdavesz": "2.89", "hhdavesz_00": "3.06", "hhdch": "5747", "hhdfam": "12359", "hhdhighpy_5": "17369", "hhdlowpy_5": "14821", "hhdnch": "6612", "hhdnfm": "342", "hhdpy_10": "17059", "hhdpy_5": "16434", "hhdsingle": "2815", "hhnwcy1_5": "", "hhnwcy10_25": "", "hhnwcy100_250": "", "hhnwcy25_50": "", "hhnwcy250_500": "", "hhnwcy5_10": "", "hhnwcy50_100": "", "hhnwcygt_500": "", "hhnwcylt_0": "", "hhnwmeancy": "279153", "hhnwmedcy": "", "hhpop_00": "37223", "hhpoppy_10": "47465", "hhpoppy_5": "49250", "hhppy_10": "2.89", "hhppy_5": "2.89", "hincy00_10": "362", "hincy10_15": "274", "hincy100_125": "2048", "hincy125_150": "1361", "hincy15_20": "289", "hincy150_200": "2706", "hincy20_25": "545", "hincy200_250": "939", "hincy25_30": "471", "hincy250_500": "1282", "hincy30_35": "545", "hincy35_40": "391", "hincy40_45": "362", "hincy45_50": "366", "hincy50_60": "588", "hincy60_75": "1078", "hincy75_100": "1794", "hincygt_500": "113", "houmedage": "1985", "idxexptotal": "151", "incavehhpy_5": "146585", "inccyavehh": "133157", "inccymedd": "108455", "inccymeddh": "88844", "inccypcap": "46359", "incdiffbasecy": "35.01", "incdiffcurrcy": "18.51", "incmedpy_5": "117199", "jc": "BROOKDALE COMMUNITY COLLEGE", "jcdist": "11", "langasian": "596", "langasian_00": "414", "langeng": "12051", "langeng_00": "9776", "langeuro": "1988", "langeuro_00": "1382", "langother": "162", "langother_00": "157", "langspan": "718", "langspan_00": "437", "langtotal": "15515", "latitude": "40.296782", "lbf_00": "17772", "lbfaf_00": "10", "lbfciv_00": "17762", "lbfemp_00": "17167", "lbfwf_00": "27029", "lead": "0", "longitude": "-74.333454", "lorturn": "4.32", "mardivor": "2359", "market_id": "", "market_name": "", "marmarr": "22578", "marnever": "9807", "marsep": "336", "martotalpop": "37375", "marwidow": "2295", "medianage": "43.81", "medianagepy_10": "42.99", "medianagepy_5": "44.43", "medsaleprice": "360000", "name": "Englishtown(07726)", "nine_to_12_1990": "1738", "nine_to_12_2000": "1256", "no2": "0", "ob_id": "1975896", "occarts": "285", "occbfin": "441", "occbgmt": "423", "occbluco": "65", "occclero": "2511", "occcomp": "195", "occcons": "532", "occcsrv": "432", "occeduc": "489", "occengr": "226", "occfood": "901", "occhcso": "1007", "occhcsp": "578", "occinstal": "401", "occlegal": "78", "occmilt": "0", "occpcar": "496", "occprim": "25", "occprod": "898", "occprot": "132", "occsalpr": "1736", "occscns": "161", "occtotpop": "13426", "occtran": "688", "occuncl": "61", "occwhtco": "35", "occyexec": "732", "one_bed_county": "1156", "one_bedindex": "88", "ozone": "0", "pm10": "0", "pop_00": "37063", "pop_10": "42593", "pop_90": "29825", "popcorr_00": "126", "popcy": "44774", "popcygqcoll": "0", "popcygqmil": "0", "popdiffbasecy": "20.81", "popdiffcurrcy": "5.12", "popdnsty": "1383.6", "popfemale": "23160", "popfemale_00": "19355", "popfemalepy_10": "25386", "popfemalepy_5": "24477", "popgq_00": "155", "popgq_90": "233", "popgqpy_10": "256", "popgqpy_5": "256", "pophighpy_5": "49716", "popinst_00": "126", "poplowpy_5": "42658", "popmale": "21614", "popmale_00": "17708", "popmalepy_10": "23736", "popmalepy_5": "22872", "popnoninst_00": "29", "popnurshm_00": "0", "popotherinst_00": "0", "popothernoninst_00": "29", "poppy_10": "49122", "poppy_5": "47349", "precipann": "46.77", "raceamerind": "53", "raceamerind_00": "12", "raceasian": "3277", "raceasian_00": "1921", "raceasian_90": "955", "raceasianpy_5": "3490", "raceblack": "1084", "raceblack_00": "676", "raceblack_90": "912", "raceblackpy_5": "1089", "racehawai": "8", "racehawai_00": "42", "racehisp": "2465", "racehisp_90": "761", "racehisppy_5": "2571", "racemulti": "636", "racemulti_00": "461", "racenonhisp": "42309", "raceother": "234", "raceother_00": "255", "raceother_90": "222", "raceotherpy_5": "570", "racetotalpop": "44774", "racewhite": "39482", "racewhite_00": "33696", "racewhite_90": "27736", "racewhitepy_5": "39628", "rskcyhanx": "0", "rskcyhunx": "0", "rskcyquak": "0", "rskcyrisk": "0", "rskcytonx": "0", "rskcywinx": "0", "salavecy": "59214", "salecount": "868", "salestaxrate": "6.88", "salestaxtype": "CO", "salmedcy": "48458", "seasonpop": "249", "state": "34", "statename": "New Jersey", "studio_county": "951", "studioindex": "88", "team": "LAKEWOOD BLUECLAWS (A)", "teamdist": "17", "three_bed_county": "2007", "three_bedindex": "88", "tmpavejan": "30.10", "tmpavejul": "74.70", "tmpmaxjan": "39.30", "tmpmaxjul": "84.90", "tmpminjan": "20.80", "tmpminjul": "64.40", "trw0_5": "297", "trw10_15": "1586", "trw15_20": "1473", "trw20_30": "1937", "trw30_45": "2949", "trw45_60": "1672", "trw5_10": "1256", "trwave": "42", "trwbyc": "14", "trwcpool": "1444", "trwdrive": "12417", "trwgt_60": "5150", "trwhome": "583", "trwmoto": "1", "trwother": "91", "trwpublic": "2216", "trwself": "137", "two_bed_county": "1484", "two_bedindex": "88", "vph1": "21", "vphgt1": "72", "vphnone": "7" } ], "name": "Full", "notice": "", "resource": "Area", "service": "Community", "version": "2.0" }, "xml_record": "1" }, "status": {"code": "0", "long_description": "Your request was successfully processed.", "short_description": "Success" }, "xmlns": "http:\/\/www.ist_prod.obiwebservices.com\/xmlns\/community\/1.0" }}

    data = res.read()
    ###print(data)
    # print(res)

#     import json
#     pprint(json.loads(json.dumps(zip_com_json)))
#     #print(json.dumps(json.loads(zip_com_json)))   

        
    # pprint(data.decode("utf-8")

    zip_com_json = ast.literal_eval(data.decode("utf-8"))
    pprint(zip_com_json)   
    
    
        # Creates a collection in the database and insert document
    for i in range(100):
        db.POI.insert_one(
            zip_com_json["response"]["result"]["package"]["item"][i]
        )

