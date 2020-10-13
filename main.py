import get_latlng
import latlng_adress_conversion
import json

latlnglist = [[26.116628,127.686533],[26.180929,127.746019],[26.162404,127.792259],[26.146445,127.690376],[26.187708,127.676196],[26.189156,127.709931],[26.187725,127.750234],[26.210561,127.747757],[26.209845,127.707912],[26.210587,127.685650],[26.250964,127.709569],[26.239479,127.755877],[26.287196,127.770549],[26.281918,127.797625],[26.326641,127.778974],[26.323986,127.815225],[26.325780,127.891557],[26.357012,127.968876],[26.337887,127.794341],[26.382367,127.817015],[26.401814,127.757828],[26.433809,127.813333],[26.433809,127.813333],[26.456496,127.845144],[26.493910,127.852644],[26.504675,127.871651],[26.453478,127.926206],[26.470955,127.944510],[26.516568,127.919002],[26.483722,127.970116],[26.522142,128.025441],[26.685696,127.908002],[26.643169,127.922925],[26.625188,127.973932],[26.557787,128.076570],[26.608010,128.132017],[26.630423,128.201123],[26.688942,128.235382],[26.780343,128.234826],[26.837124,128.272233]]
num = len(latlnglist)

convList_comp = []
for i in range(num):
    latlng = latlnglist[i]
    radius = "5000"
    get_latlng_result = get_latlng.makeURL(latlng, radius)
    convList = get_latlng.printResultLog(get_latlng_result)
    convURLList = latlng_adress_conversion.makeConversionURL(convList)
    convlatlngList = latlng_adress_conversion.printConversionLog(convURLList[0], convURLList[1])
    convList_comp.append(convlatlngList)

with open('convenience_store.json', 'w', encoding='utf-8') as f:
    json.dump(convList_comp, f, indent=4, ensure_ascii=False)
    print(f)



